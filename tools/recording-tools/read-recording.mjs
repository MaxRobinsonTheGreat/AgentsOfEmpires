import { readFile } from "node:fs/promises";
import { basename, resolve } from "node:path";
import { parseRecording } from "agelens";

const CIVILIZATIONS = {
  1: "Britons", 2: "Franks", 3: "Goths", 4: "Teutons", 5: "Japanese",
  6: "Chinese", 7: "Byzantines", 8: "Persians", 9: "Saracens", 10: "Turks",
  11: "Vikings", 12: "Mongols", 13: "Celts", 14: "Spanish", 15: "Aztecs",
  16: "Mayans", 17: "Huns", 18: "Koreans", 19: "Italians", 20: "Hindustanis",
  21: "Incas", 22: "Magyars", 23: "Slavs", 24: "Portuguese", 25: "Ethiopians",
  26: "Malians", 27: "Berbers", 28: "Khmer", 29: "Malay", 30: "Burmese",
  31: "Vietnamese", 32: "Bulgarians", 33: "Tatars", 34: "Cumans", 35: "Lithuanians",
  36: "Burgundians", 37: "Sicilians", 38: "Poles", 39: "Bohemians", 40: "Dravidians",
  41: "Bengalis", 42: "Gurjaras", 43: "Romans", 44: "Armenians", 45: "Georgians",
};

const OBJECTS = {
  4: "Archer", 5: "Hand Cannoneer", 7: "Skirmisher", 35: "Battering Ram",
  36: "Bombard Cannon", 38: "Knight", 42: "Trebuchet", 74: "Militia",
  83: "Villager", 93: "Spearman", 125: "Monk", 279: "Scorpion",
  280: "Mangonel", 329: "Camel Rider", 448: "Scout Cavalry", 725: "Jaguar Warrior",
  1258: "Battering Ram",
  751: "Eagle Scout", 331: "Trebuchet", 50: "Farm", 70: "House", 71: "Town Center",
  82: "Castle", 12: "Barracks", 18: "Blacksmith", 103: "Blacksmith",
  30: "Monastery", 104: "Monastery", 49: "Siege Workshop", 150: "Siege Workshop",
  68: "Mill", 84: "Market", 86: "Stable", 101: "Stable", 10: "Archery Range",
  87: "Archery Range", 109: "Town Center", 209: "University",
  562: "Lumber Camp", 584: "Mining Camp",
};

const TECHNOLOGIES = {
  8: "Town Watch", 12: "Crop Rotation", 13: "Heavy Plow", 14: "Horse Collar",
  22: "Loom", 24: "Garland Wars", 47: "Chemistry", 55: "Gold Mining",
  67: "Forging", 68: "Iron Casting", 74: "Scale Mail Armor", 75: "Blast Furnace",
  76: "Chain Mail Armor", 77: "Plate Mail Armor", 80: "Plate Barding Armor",
  81: "Scale Barding Armor", 82: "Chain Barding Armor", 93: "Ballistics",
  98: "Elite Skirmisher", 100: "Crossbowman", 101: "Feudal Age", 102: "Castle Age",
  103: "Imperial Age", 182: "Gold Shaft Mining", 197: "Pikeman", 199: "Fletching",
  200: "Bodkin Arrow", 201: "Bracer", 202: "Double-Bit Axe", 203: "Bow Saw",
  211: "Padded Archer Armor", 212: "Leather Archer Armor", 213: "Wheelbarrow",
  215: "Squires", 230: "Block Printing", 231: "Sanctity", 237: "Arbalester",
  249: "Hand Cart", 252: "Fervor", 278: "Stone Mining", 315: "Conscription",
  316: "Redemption", 322: "Murder Holes", 377: "Siege Engineers", 384: "Eagle Warrior",
  434: "Elite Eagle Warrior", 435: "Bloodlines", 437: "Thumb Ring", 460: "Atlatl",
  602: "Arson",
};

function parseArguments(argv) {
  const options = { format: "summary" };
  for (let index = 0; index < argv.length; index += 1) {
    const argument = argv[index];
    if (argument === "--path") options.path = argv[++index];
    else if (argument === "--format") options.format = argv[++index];
    else throw new Error(`Unknown argument: ${argument}`);
  }
  if (!options.path) throw new Error("--path is required");
  if (!["summary", "json", "raw"].includes(options.format)) {
    throw new Error(`Unsupported format: ${options.format}`);
  }
  return options;
}

function fromHex(hex) {
  return Buffer.from(hex ?? "", "hex");
}

function formatTime(milliseconds) {
  const totalSeconds = Math.max(0, Math.floor(milliseconds / 1000));
  const hours = Math.floor(totalSeconds / 3600);
  const minutes = Math.floor((totalSeconds % 3600) / 60);
  const seconds = totalSeconds % 60;
  return [hours, minutes, seconds].map((value) => String(value).padStart(2, "0")).join(":");
}

function incrementCount(target, id, names, prefix) {
  const name = names[id] ?? `${prefix} ${id}`;
  target[name] = (target[name] ?? 0) + 1;
}

function sortedCounts(counts) {
  return Object.fromEntries(Object.entries(counts).sort((left, right) => right[1] - left[1]));
}

function decodeRuntimeName(bytes) {
  if (bytes.length < 4) return undefined;
  const end = bytes.indexOf(0, 3);
  return bytes.subarray(3, end < 0 ? bytes.length : end).toString("utf8") || undefined;
}

function parseChatMessage(message) {
  try {
    return JSON.parse(message);
  }
  catch {
    return { message };
  }
}

function buildSummary(recording, sourcePath) {
  let elapsed = 0;
  const timeBySequence = new Map();
  for (const operation of recording.operations) {
    if (operation.id === 2) elapsed += operation.payload?.increment ?? 0;
    timeBySequence.set(operation.sequence, elapsed);
  }

  const players = new Map();
  for (const player of recording.players.filter((entry) => entry.number > 0)) {
    players.set(player.number, {
      number: player.number,
      headerName: player.name,
      name: player.name,
      civilizationId: player.civilizationId,
      civilization: CIVILIZATIONS[player.civilizationId] ?? `Civilization ${player.civilizationId}`,
      type: player.type,
      resigned: false,
      resignationTime: null,
      lastActionTime: 0,
      ages: {},
      queueCommands: {},
      buildingPlacementCommands: {},
      researchCommands: [],
      market: { buys: 0, sells: 0 },
    });
  }

  for (const action of recording.actions) {
    const bytes = fromHex(action.payload?.raw?.data);
    if (bytes.length === 0) continue;
    const playerId = bytes[0];
    const player = players.get(playerId);
    if (!player) continue;
    const time = timeBySequence.get(action.sequence) ?? 0;
    player.lastActionTime = Math.max(player.lastActionTime, time);

    if (action.actionId === 11) {
      player.resigned = true;
      player.resignationTime = time;
    }
    else if (action.actionId === 100 && bytes.length >= 15) {
      incrementCount(player.queueCommands, bytes.readUInt32LE(11), OBJECTS, "Object");
    }
    else if (action.actionId === 101 && bytes.length >= 11) {
      const technologyId = bytes.readUInt16LE(9);
      player.researchCommands.push({
        timeMs: time,
        time: formatTime(time),
        technologyId,
        technology: TECHNOLOGIES[technologyId] ?? `Technology ${technologyId}`,
      });
    }
    else if (action.actionId === 102 && bytes.length >= 19) {
      incrementCount(player.buildingPlacementCommands, bytes.readUInt32LE(15), OBJECTS, "Object");
    }
    else if (action.actionId === 122) player.market.sells += 1;
    else if (action.actionId === 123) player.market.buys += 1;
    else if (action.actionId === 135) player.name = decodeRuntimeName(bytes) ?? player.name;
  }

  const chat = [];
  for (const operation of recording.chat) {
    const parsed = parseChatMessage(operation.payload?.message ?? "");
    const time = timeBySequence.get(operation.sequence) ?? 0;
    chat.push({ timeMs: time, time: formatTime(time), ...parsed });
    const ageMatch = parsed.message?.match(/advanced to the (Feudal|Castle|Imperial) Age/i);
    const player = players.get(parsed.player);
    if (player && ageMatch) player.ages[ageMatch[1]] = formatTime(time);
  }

  for (const player of players.values()) {
    player.lastAction = formatTime(player.lastActionTime);
    if (player.resignationTime !== null) player.resignation = formatTime(player.resignationTime);
    player.queueCommands = sortedCounts(player.queueCommands);
    player.buildingPlacementCommands = sortedCounts(player.buildingPlacementCommands);
  }

  const competitors = [...players.values()].filter((player) => player.type === 4);
  const remaining = competitors.filter((player) => !player.resigned);
  const activityOrder = [...remaining].sort((left, right) => right.lastActionTime - left.lastActionTime);
  let inferredWinner = null;
  if (remaining.length === 1) {
    inferredWinner = { player: remaining[0].number, name: remaining[0].name, confidence: "high", reason: "only non-resigned AI" };
  }
  else if (activityOrder.length > 1 &&
           activityOrder[0].lastActionTime >= elapsed - 5000 &&
           activityOrder[1].lastActionTime <= elapsed - 10000) {
    inferredWinner = {
      player: activityOrder[0].number,
      name: activityOrder[0].name,
      confidence: "inferred",
      reason: "only AI issuing commands at the end of the recording",
    };
  }

  const buildMatch = basename(sourcePath).match(/\bv([0-9.]+)/i);
  return {
    source: resolve(sourcePath),
    gameBuild: buildMatch?.[1] ?? null,
    version: recording.header?.gameVersion ?? recording.header?.version ?? null,
    durationMs: elapsed,
    duration: formatTime(elapsed),
    hasPostgameMarker: recording.operations.some((operation) => operation.id === 6),
    hasAchievements: recording.actions.some((action) => action.actionId === 255),
    inferredWinner,
    players: [...players.values()],
    chat,
    warnings: recording.warnings ?? [],
    limitations: [
      "Queue and building-placement commands are attempts, not confirmed completed or surviving objects.",
      "Without an achievements block, exact scores, kills, losses, resources, and population are unavailable.",
      "A winner inferred from command activity is not an official result field.",
    ],
  };
}

function printSummary(summary) {
  console.log(`Recording: ${summary.source}`);
  console.log(`Duration:  ${summary.duration}`);
  if (summary.gameBuild !== null) console.log(`Build:     ${summary.gameBuild}`);
  if (summary.version !== null) console.log(`Format:    ${summary.version}`);
  console.log(`Postgame:  ${summary.hasPostgameMarker ? "present" : "absent"}`);
  if (summary.inferredWinner) {
    console.log(`Winner:    ${summary.inferredWinner.name} (${summary.inferredWinner.confidence}; ${summary.inferredWinner.reason})`);
  }
  else {
    console.log("Winner:    not determinable");
  }
  console.log("");

  for (const player of summary.players) {
    const status = player.resigned ? `resigned ${player.resignation}` : `last action ${player.lastAction}`;
    console.log(`P${player.number} ${player.name} - ${player.civilization} (${status})`);
    const ages = Object.entries(player.ages).map(([age, time]) => `${age} ${time}`).join(", ");
    if (ages) console.log(`  Ages: ${ages}`);
    const queues = Object.entries(player.queueCommands).slice(0, 10).map(([name, count]) => `${name} ${count}`).join(", ");
    if (queues) console.log(`  Queue commands: ${queues}`);
    const buildings = Object.entries(player.buildingPlacementCommands).slice(0, 10).map(([name, count]) => `${name} ${count}`).join(", ");
    if (buildings) console.log(`  Building attempts: ${buildings}`);
    if (player.researchCommands.length > 0) console.log(`  Research commands: ${player.researchCommands.length}`);
    if (player.market.buys || player.market.sells) console.log(`  Market commands: buy ${player.market.buys}, sell ${player.market.sells}`);
  }

  if (!summary.hasAchievements) {
    console.log("\nNote: no achievements block; exact score, kills, losses, resources, and population are unavailable.");
  }
}

const options = parseArguments(process.argv.slice(2));
const bytes = new Uint8Array(await readFile(options.path));
const recording = await parseRecording(bytes);

if (options.format === "raw") {
  console.log(JSON.stringify(recording, null, 2));
}
else {
  const summary = buildSummary(recording, options.path);
  if (options.format === "json") console.log(JSON.stringify(summary, null, 2));
  else printSummary(summary);
}
