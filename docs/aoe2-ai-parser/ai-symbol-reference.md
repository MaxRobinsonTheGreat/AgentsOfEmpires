# AI Symbol Reference

Generated from `extensions/aoe2-ai-parser-extension/data/completions.json`.
Edit the source inventories or completion generator, then run `npm run generate:symbol-docs`.

This file is the formatted local documentation target for Cursor definition navigation.

## Table Of Contents

- [command](#section-command)
- [object](#section-object)
- [strategic-number](#section-strategic-number)
- [tech](#section-tech)
- [value](#section-value)

<a id="section-command"></a>

# command

<a id="symbol-#else"></a>

## `#else`

- Kind: `command`
- Detail: Other - Other

Syntax: `#else`

Loads the following code if the previous #load-if-defined or #load-if-not-defined isn't true. #else is a conditional loading command that can only be used following a #load-if-defined or #load-if-not-defined command. If #else follows a #load-if-defined, then any rules between the #else and a closing #end-if will only be loaded if the system symbol for the #load-if-defined is not defined. Otherwise, the rules between the #else and a closing #end-if will not be read at any point in the game after the debugger is finished checking the AI for errors. Likewise, if #else follows a #load-if-not-defined, then any rules between the #else and a closing #end-if will only be loaded if the system symbol for the #load-if-not-defined is actually defined. All #else commands must have a closing #end-if.

[AIRef](https://airef.github.io/commands/commands-details.html##else)

<a id="symbol-#end-if"></a>

## `#end-if`

- Kind: `command`
- Detail: Other - Other

Syntax: `#end-if`

Ends a conditionally loaded section of code (i.e. a #load-if-defined, #load-if-not-defined, or #else section). Every #load-if-defined or #load-if-not-defined which starts a conditionally loaded section of code must have a matching #end-if that end that section of code, though there may be an #else section before the #end-if. Conditionally loaded sections of code require the use of a pLoadIfSymbol. You can check out the Load-If Symbols page for a complete list of the load-if symbols that you can use.

[AIRef](https://airef.github.io/commands/commands-details.html##end-if)

<a id="symbol-#load-if-defined"></a>

## `#load-if-defined`

- Kind: `command`
- Detail: Other - Other

Syntax: `#load-if-defined <LoadIfSymbol>`

Loads the code following the #load-if-defined if the given load-if symbol is defined for the current game. All code following the #load-if-defined will be conditionally loaded in this manner until an #else command is used, or an #end-if is used to end the load-if block. Using an #else command after a #load-if-defined is optional, but all #load-if-defined commands must eventually have a closing #end-if. load-if symbols are case-sensitive. Technically, any text can be used for the pLoadIfSymbol parameter, such as #load-if-defined TEST, but since "TEST" is not an available load-if symbol, the code following a #load-if-defined TEST will never be loaded. The AI debugger will not generate an error if you accidentally misspelled a load-if symbol. However, you can use this feature intentionally as a way to essentially comment out an entire block of code. Conditional loading commands like #load-if-defined and #load-if-not-defined can be nested up to 50 levels deep. Nesting conditional loading commands means using a conditional loading command inside of a preexisting conditional loading block. In this case, all of the conditional loading commands must be true for the code within the nested conditional loading command to run. See the examples below for details.

[AIRef](https://airef.github.io/commands/commands-details.html##load-if-defined)

Completion insert text:

```text
#load-if-defined ${1:LoadIfSymbol}
```

<a id="symbol-#load-if-not-defined"></a>

## `#load-if-not-defined`

- Kind: `command`
- Detail: Other - Other

Syntax: `#load-if-not-defined <LoadIfSymbol>`

Loads the code following the #load-if-not-defined if the given load-if symbol is NOT defined for the current game. All code following the #load-if-not-defined will be conditionally loaded in this manner until an #else command is used, or an #end-if is used to end the load-if block. Using an #else command after a #load-if-not-defined is optional, but all #load-if-not-defined commands must eventually have a closing #end-if. load-if symbols are case-sensitive. Technically, any text can be used for the pLoadIfSymbol parameter, such as #load-if-not-defined TEST, but since "TEST" is not an available load-if symbol, the code following a #load-if-not-defined TEST will always be loaded. The AI debugger will not generate an error if you accidentally misspelled a load-if symbol. Conditional loading commands like #load-if-not-defined and #load-if-defined can be nested up to 50 levels deep. Nesting conditional loading commands means using a conditional loading command inside of a preexisting conditional loading block. In this case, all of the conditional loading commands must be true for the code within the nested conditional loading command to run. See the examples below for details.

[AIRef](https://airef.github.io/commands/commands-details.html##load-if-not-defined)

Completion insert text:

```text
#load-if-not-defined ${1:LoadIfSymbol}
```

<a id="symbol-acknowledge-event"></a>

## `acknowledge-event`

- Kind: `command`
- Detail: Action - Scenarios

Syntax: `(acknowledge-event <EventType> <EventId>)`

Acknowledges a received event by resetting the associated flag. Scenario triggers that execute an AI Script Goal effect are the only events that AI scripts can detect. This command, along with event-detected, is used to detect an AI Script Goal effect from a scenario trigger, often with the intention of changing the AI behavior after the scenario trigger has fired. The scenario designer chooses an AI Trigger number for the AI Script Goal effect in the scenario editor. Then, the event-detected command in the AI script will detect when this trigger effect happens. The event-detected command will remain true after the AI Script Goal trigger effect fires, so acknowledge-event is used to reset the event-detected flag so that event-detected will no longer be true, similar to how the disable-timer command clears a timer that has triggered or how the acknowledge-taunt" command accepts the taunt message." cAcknowledgeEvent.commandParameters = [ { nameLink: pEventType.getLink(), name: "EventType", type: "Const", dir: "in", range: "trigger", note: "The type of the event. Triggers are the only valid event types." }, { nameLink: pEventId.getLink(), name: "EventId", type: "Const", dir: "in", range: "0 to 255.", note: "The EventId to acknowledge." } ]

[AIRef](https://airef.github.io/commands/commands-details.html#acknowledge-event)

Completion insert text:

```text
(acknowledge-event ${1:EventType} ${2:EventId})
```

<a id="symbol-acknowledge-taunt"></a>

## `acknowledge-taunt`

- Kind: `command`
- Detail: Action - Chat, Debugging, Other Player Info

Syntax: `(acknowledge-taunt <PlayerNumber> <TauntId>)`

Acknowledges the taunt (resets the flag). Like other event systems in the AI, taunt detection requests explicit acknowledgement. In simple terms, whenever an AI receives a taunt message, taunt-detected will remain true for the given taunt until the taunt is acknowledged. If the taunt is not acknowledged, your AI's response to the taunt will happen repeatedly. The action allows "focus-player", "target-player", and "any"/"every" wildcard parameters for pPlayerNumber. It also allows the use of rule variables for pPlayerNumber, such as "this-any-ally" or "this-any-enemy". It also allows for scenario-player-# and lobby-player-#, where # is between 1 and 8. scenario-player-# refers to the player color (where red = scenario-player-2), and lobby-player-# refers to the player slot (where the lobby host or human player playing a single player campaign is always lobby-player-1).

[AIRef](https://airef.github.io/commands/commands-details.html#acknowledge-taunt)

Completion insert text:

```text
(acknowledge-taunt ${1:PlayerNumber} ${2:TauntId})
```

<a id="symbol-and"></a>

## `and`

- Kind: `command`
- Detail: Other - Other

Syntax: `(and)`

Returns true if both of the facts following this command are true. The and command is one of several logical operator commands available, along with nand, nor, not, or, xnor, and xor. See the Logical Operator Commands guide for more information on how to use logical operator commands.

[AIRef](https://airef.github.io/commands/commands-details.html#and)

Completion insert text:

```text
(and)
```

<a id="symbol-attack-now"></a>

## `attack-now`

- Kind: `command`
- Detail: Action - Attack

Syntax: `(attack-now)`

Forces attack with currently available attack units.

[AIRef](https://airef.github.io/commands/commands-details.html#attack-now)

Completion insert text:

```text
(attack-now)
```

<a id="symbol-attack-soldier-count"></a>

## `attack-soldier-count`

- Kind: `command`
- Detail: Fact - Attack, Counting

Syntax: `(attack-soldier-count <compareOp> <Value>)`

Compares the computer player's attack soldier count to pValue using pCompareOp and returns true if the condition is met. Attack soldiers are those attacking with the attack groups method (setting snNumberAttackGroups > 0) or are attacking with the attack-now command. Setting sn-number-attack-groups to 0 and using up-disband-group-type to disband land attack groups when attacking with attack groups will reset the soldiers, and they will no longer be considered attack soldiers. Likewise, using up-reset-attack-now when attacking with attack-now will reset the soldiers, and they will no longer be considered attack soldiers. Monks are included as land attack soldiers when attacking.

[AIRef](https://airef.github.io/commands/commands-details.html#attack-soldier-count)

Completion insert text:

```text
(attack-soldier-count ${1:compareOp} ${2:Value})
```

<a id="symbol-attack-warboat-count"></a>

## `attack-warboat-count`

- Kind: `command`
- Detail: Fact - Attack, Counting

Syntax: `(attack-warboat-count <compareOp> <Value>)`

Compares the computer player's attack warboat count to pValue using pCompareOp and returns true if the condition is met. Attack warboats are those assigned to boat attack groups with the attack-now command, not with the snNumberBoatAttackGroups SN. If you stop calling attack-now then they are immediately no longer attack warboats - even without using up-reset-attack-now.

[AIRef](https://airef.github.io/commands/commands-details.html#attack-warboat-count)

Completion insert text:

```text
(attack-warboat-count ${1:compareOp} ${2:Value})
```

<a id="symbol-build"></a>

## `build`

- Kind: `command`
- Detail: Action - Buildings

Syntax: `(build <BuildingId>)`

Builds the given building if the building is available to the player and the building can be constructed without escrowed resources. If you want to construct walls or gates, use the corresponding build-wall, build-gate, or up-build-line commands instead. The Action allows the use of building line wildcard parameters for pBuildingId. The only wildcard parameter available is watch-tower-line. However, it is better to use watch-tower instead of watch-tower-line, even after Guard Tower or Keep upgrades due to some bugs with watch-tower-line. Simply using (build watch-tower) will work regardless of tower upgrades. Building classes cannot be used with this command. Important Note: Always use a can-build or up-can-build condition in every rule where you use the build command. Without this condition, the building queue for this building may get stuck for the rest of the game. When this command is issued, the AI engine will add the specified building to the building placement queue. If snEnableNewBuildingSystem is set to 0, the engine will only add the building to the placement queue if there isn't already a building of the same type being constructed or waiting to be placed, but if the SN is set to 1 this check is removed, and an unlimited number of buildings of the same type are allowed to be queued for placement or be constructed at once. You can limit the number of buildings added to the placement queue with a up-pending-objects condition. At the end of each script pass, the AI engine checks if the AI has explored the minimum percentage of the map required by snInitialExplorationRequired. If so, it will attempt to place each building that is currently in the placement queue. If the building was added to the queue with the (build) command, the AI will place most buildings at a random location within snMaximumTownSize tiles from the main town center using whatever value sn-maximum-town-size is set to at the end of the script. snMinimumTownSize has no effect on building placement except for towers. However, four tiles around the TC are reserved around every town center for farms, and all buildings are placed at least one tile apart. For a complete list on the min and max distances where each building can be built, see this list here: link. Buildings placed with this command will avoid the following locations:Ally (and self): will avoid placing the building on tiles where an allied building already exists.Enemy: will avoid placing the building on tiles where an enemy building already exists. Will also avoid placing a building within the attack range of a tower, TC, or castle, + 0.5 tiles.There are many other commands that you can use instead of this command that you more precise control over building placement, such as build-forward, up-build, and up-build-line.Placement ExceptionsSeveral buildings have variations on how they are placed that are different from the description above: Town Centers are placed like most buildings when snTownCenterPlacement is set to the default value of 0. However, if sn-town-center-placement is set to the pBuildingId of another building, such as "mill" or "lumber-camp", the town center will follow the placement rules of that building instead. Mills and Folwarks are not placed in a random location within sn-maximum-town-size, but instead are built by a food resource within snMillMaxDistance. The AI engine by default prefers to build mills and folwarks by forage, then by shore fish, then by deer. However, this preference can be changed with snPreferredMillPlacement. Also, mills and folwarks are placed one tile away from food resource piles unless snAllowAdjacentDropsites is set to 1 by the end of the script pass, and they are placed a minimum number of tiles from all dropsites (not just mills and folwarks), as specified by snDropsiteSeparationDistance. Mining Camps are not placed in a random location within sn-maximum-town-size, but instead are built by a gold or stone resource within snMiningCampMaxDistance (or snCampMaxDistance if sn-mining-camp-max-distance is set to 0), and they are placed at least 7 tiles from the main town center. If the closest gold mine distance to a dropoff point is greater than snGoldDropsiteDistance, then it will prefer to place the mining camp near gold mines. Then it checks if the closest stone mine distance to a dropoff point is greater than snStoneDropsiteDistance, and if it is, it will prefer to place the mining camp near stone. If neither condition is met, it prefers neither gold nor stone, and the mining camp placement behavior is undefined. It's possible the mining camp isn't placed, but this is untested. Also, mining camps are placed one tile away from gold and stone resource piles unless snAllowAdjacentDropsites is set to 1 by the end of the script pass, and they are placed a minimum number of tiles from all dropsites (not just mining camps), as specified by snDropsiteSeparationDistance. Lumber Camps are not placed in a random location within sn-maximum-town-size, but instead are built by a tree within snLumberCampMaxDistance (or snCampMaxDistance if sn-lumber-camp-max-distance is set to 0), and they are placed at least 7 tiles from the main town center. Also, lumber camps are placed one tile away from trees unless snAllowAdjacentDropsites is set to 1 by the end of the script pass, though even with the SN set to 1 the AI will sometimes fail to build the lumber camp adjacent to trees, and they are placed a minimum number of tiles from all dropsites (not just lumber camps), as specified by snDropsiteSeparationDistance. Usually the AI favors building lumber camps near forests rather than straggler trees, but the AI will build lumber camps near straggler trees if sn-lumber-camp-max-distance is to small for the AI to find an available forest to build the lumber camp by. Docks are of course only placed on water, and there are several SNs that can affect their placement, such as snDockAvoidanceFactor, snDockPlacementMode, snDockProximityFactor, and snMinimumWaterBodySizeForDock. Farms are automatically placed near town centers, mills, and folwarks. The AI engine prefers to place farms around TCs instead of mills or folwarks, but it will place farms around mills or folwarks if all spaces immediately next to the town center are already filled with farms. Fish Traps should not be placed with the build command. Instead, they should only be placed with up-build-line. It's possible they can be placed with the build command, but they often won't be placed in the right location. Also, make sure to use (up-assign-builders c: fish-trap c: -1) to make sure that villagers aren't sent to contruct them. Outposts, at least according to this info, are placed outside the town, at a distance between sn-maximum-town-size and twice the distance of sn-maximum-town-size. They might also have a preference to be placed on hills like towers do (see the towers section below). If you choose to build outposts, make sure you test to make sure you like their placement location. You can build them in more precise locations or inside the town if you use the place-control or place-point options with up-build, or you can also place them with up-build-line. Towers are the only type of building that uses sn-minimum-town-size as the minimum distance they can be placed from the starting town center. By default they have a preference to be placed on hills, but you can remove this preference by setting snIgnoreTowerElevation to 1. This preference for hills is not used for castles or kreposts. Donjons. Everything from towers applies to donjons. To construct donjons with serjeants, set snAllowSerjeantBuilding to 1. Gates cannot be placed with the build command. Construct them with the build-gate or up-build-line command. To build palisade gates, set snGateTypeForWall to 1 before using the build-gate command. Trebuchets. Yes, (build trebuchet) actually works. Every scripter should try it once in their life. However, soon you'll see why it's considered cheating.

[AIRef](https://airef.github.io/commands/commands-details.html#build)

Completion insert text:

```text
(build ${1:BuildingId})
```

<a id="symbol-build-forward"></a>

## `build-forward`

- Kind: `command`
- Detail: Action - Buildings

Syntax: `(build-forward <BuildingId>)`

Builds the given building close to an enemy if the building is available to the player and the building can be constructed without escrowed resources. The Action allows the use of building line wildcard parameters for pBuildingId. The only wildcard parameter available is watch-tower-line. However, it is better to use watch-tower instead of watch-tower-line, even after Guard Tower or Keep upgrades due to some bugs with watch-tower-line. Simply using (build watch-tower) will work regardless of tower upgrades. Building classes cannot be used with this command. Important Note: Always use a can-build or up-can-build condition in every rule where you use the build-forward command. Without this condition, the building queue for this building may get stuck for the rest of the game. When this command is issued, the AI engine will add the specified building to the building placement queue. If snEnableNewBuildingSystem is set to 0, the engine will only add the building to the placement queue if there isn't already a building of the same type being constructed or waiting to be placed, but if the SN is set to 1 this check is removed, and an unlimited number of buildings of the same type are allowed to be queued for placement or be constructed at once. At the end of each script pass, the AI engine checks if the AI has explored the minimum percentage of the map required by snInitialExplorationRequired. If so, it will attempt to place each building that is currently in the placement queue. If the building was added to the queue with the build-forward command, the AI will place the building near the enemy player specified by snTargetPlayerNumber or the player specified by snAttackWinningPlayer if sn-target-player-number is set to 0. Buildings placed with build-forward will avoid placing the building on tiles where an enemy building already exists, and it will also avoid placing a building within any enemy building's line of sight, + 2 tiles.

[AIRef](https://airef.github.io/commands/commands-details.html#build-forward)

Completion insert text:

```text
(build-forward ${1:BuildingId})
```

<a id="symbol-build-gate"></a>

## `build-gate`

- Kind: `command`
- Detail: Action - Buildings, Walls & Gates

Syntax: `(build-gate <Perimeter>)`

Builds a gate as part of the given perimeter wall if the gate is available to the player and the gate can be constructed without escrowed resources. The given perimeter must first be enabled with enable-wall-placement. Perimeter 1 is usually between 10 and 20 tiles from the starting Town Center. Perimeter 2 is usually between 18 and 30 tiles from the starting Town Center. If wall placement is enabled at a particular perimeter with enable-wall-placement, the AI engine will attempt to plan a roughly circular wall pattern within the given perimeter distances when the build-wall command is issued. Once the AI finds an appropriate location to build a gate within the given perimeter and the build-gate command is issued, the AI will replace four wall segments with a gate foundation. This command cannot be used to build a gate within wall segments that existed at the start of the game, such as the starting walls in Arena or Fortress. In the DE version you can build palisade gates by setting snGateTypeForWall to 1 before using this command.

[AIRef](https://airef.github.io/commands/commands-details.html#build-gate)

Completion insert text:

```text
(build-gate ${1:Perimeter})
```

<a id="symbol-build-wall"></a>

## `build-wall`

- Kind: `command`
- Detail: Action - Buildings, Walls & Gates

Syntax: `(build-wall <Perimeter> <WallId>)`

Builds a wall line of the given wall type at the given perimeter if the wall type is available to the player and the wall can be constructed without escrowed resources. The given perimeter must first be enabled with enable-wall-placement. The Action allows the use of wall line wildcard parameters for pWallId. The only wall line wildcard parameter is stone-wall-line. Perimeter 1 is usually between 10 and 20 tiles from the starting Town Center. Perimeter 2 is usually between 18 and 30 tiles from the starting Town Center. If wall placement is enabled at a particular perimeter with enable-wall-placement, the AI engine will attempt to plan a roughly circular wall pattern within the given perimeter distances and construct the wall according to this pattern. This command cannot be used to rebuild parts of wall segments that existed at the start of the game, such as the starting walls in Arena or Fortress.

[AIRef](https://airef.github.io/commands/commands-details.html#build-wall)

Completion insert text:

```text
(build-wall ${1:Perimeter} ${2:WallId})
```

<a id="symbol-building-available"></a>

## `building-available`

- Kind: `command`
- Detail: Fact - Buildings, Can Do

Syntax: `(building-available <BuildingId>)`

Checks that the building is available to the computer player's civ and that the tech tree prerequisites are met. It does not check that there are enough resources to build the building. It allows the use of building line wildcard parameters for pBuildingId. The only wildcard parameter available is watch-tower-line. However, it is better to use watch-tower instead of watch-tower-line, even after Guard Tower or Keep upgrades due to some bugs with watch-tower-line. Simply using (building-available watch-tower) will work regardless of tower upgrades. You cannot use building classes with this command. When the AI checks the tech tree prerequisites, this includes checking whether the prerequisite age has been researched. There isn't a way at the beginning of the game to check if the building will be available for the civilization in future ages.

[AIRef](https://airef.github.io/commands/commands-details.html#building-available)

Completion insert text:

```text
(building-available ${1:BuildingId})
```

<a id="symbol-building-count"></a>

## `building-count`

- Kind: `command`
- Detail: Fact - Buildings, Counting

Syntax: `(building-count <compareOp> <Value>)`

Checks the computer player's building count. Only existing buildings are included, not buildings under construction. Buildings that existed from the start of the game, such as the starting town center, are not included. Also, farms are included, but walls and gates are not included. To check for the building-count of other players, including buildings under construction, use players-building-count.

[AIRef](https://airef.github.io/commands/commands-details.html#building-count)

Completion insert text:

```text
(building-count ${1:compareOp} ${2:Value})
```

<a id="symbol-building-count-total"></a>

## `building-count-total`

- Kind: `command`
- Detail: Fact - Buildings, Counting

Syntax: `(building-count-total <compareOp> <Value>)`

Checks the computer player's total building count, either existing buildings or buildings under construction. Buildings that existed from the start of the game, such as the starting town center, are not included. Also, farms are included, but walls and gates are not included. To check for the building-count of other players, including buildings under construction, use players-building-count.

[AIRef](https://airef.github.io/commands/commands-details.html#building-count-total)

Completion insert text:

```text
(building-count-total ${1:compareOp} ${2:Value})
```

<a id="symbol-building-type-count"></a>

## `building-type-count`

- Kind: `command`
- Detail: Fact - Buildings, Counting

Syntax: `(building-type-count <BuildingId> <compareOp> <Value>)`

Checks the computer player's building count. Only existing buildings of the given type or class are included, not buildings under construction. To check the number of gates, use gate-count instead. building-type-count allows the use of building line wildcard parameters for pBuildingId. The only wildcard parameter available is watch-tower-line. However, it is better to use watch-tower instead of watch-tower-line, even after Guard Tower or Keep upgrades due to some bugs with watch-tower-line. Simply using (building-type-count watch-tower) will work regardless of tower upgrades. There are four ways you can specify the building "type":Building Name: the name of an individual building, such as house, watch-tower, or town-center.Building Id: the numerical ID assigned to each building, such as 12 (the barracks) or 70 (the house). See the ID column in the Objects Table for a list.Building Line: the building line for the building. The only option here is watch-tower-line, and avoid using it as there are various bugs with it. Simply use watch-tower instead.Building Class: the class of a building, such as building-class, tower-class, or farm-class. Classes group several building types together into a single category. Using a building class will count all buildings of this class. See the Class column in the Objects Table to see each building's class. To check for the building-type-count of other players, including buildings under construction, use players-building-type-count.

[AIRef](https://airef.github.io/commands/commands-details.html#building-type-count)

Completion insert text:

```text
(building-type-count ${1:BuildingId} ${2:compareOp} ${3:Value})
```

<a id="symbol-building-type-count-total"></a>

## `building-type-count-total`

- Kind: `command`
- Detail: Fact - Buildings, Counting

Syntax: `(building-type-count-total <BuildingId> <compareOp> <Value>)`

Checks the computer player's total building count. The total includes buildings of the given type class, both existing buildings and those under construction. To check the number of gates, use gate-count instead. building-type-count-total allows the use of building line wildcard parameters for pBuildingId. The only wildcard parameter available is watch-tower-line. However, it is better to use watch-tower instead of watch-tower-line, even after Guard Tower or Keep upgrades due to some bugs with watch-tower-line. Simply using (building-type-count-total watch-tower) will work regardless of tower upgrades. There are four ways you can specify the building "type":Building Name: the name of an individual building, such as house, watch-tower, or town-center.Building Id: the numerical ID assigned to each building, such as 12 (the barracks) or 70 (the house). See the ID column in the Objects Table for a list.Building Line: the building line for the building. The only option here is watch-tower-line, and avoid using it as there are various bugs with it. Simply use watch-tower instead.Building Class: the class of a building, such as building-class, tower-class, or farm-class. Classes group several building types together into a single category. Using a building class will count all buildings of this class. See the Class column in the Objects Table to see each building's class. To check for the building-type-count of other players, including buildings under construction, use players-building-type-count.

[AIRef](https://airef.github.io/commands/commands-details.html#building-type-count-total)

Completion insert text:

```text
(building-type-count-total ${1:BuildingId} ${2:compareOp} ${3:Value})
```

<a id="symbol-buy-commodity"></a>

## `buy-commodity`

- Kind: `command`
- Detail: Action - Economy, Trading

Syntax: `(buy-commodity <Commodity>)`

Buys one lot of the given commodity. The AI will buy 100 of the given commodity (wood, food, or stone) at the current trading price.

[AIRef](https://airef.github.io/commands/commands-details.html#buy-commodity)

Completion insert text:

```text
(buy-commodity ${1:Commodity})
```

<a id="symbol-can-afford-building"></a>

## `can-afford-building`

- Kind: `command`
- Detail: Fact - Buildings, Can Do

Syntax: `(can-afford-building <BuildingId>)`

Checks whether the computer player has enough resources to build the given building. It does not take into account resources in the escrow stockpiles. It does not check that the tech tree prerequisites are met or if the building is allowed for the civ. It allows the use of building line wildcard parameters for pBuildingId. The only wildcard parameter available is watch-tower-line. However, it is better to use watch-tower instead of watch-tower-line, even after Guard Tower or Keep upgrades due to some bugs with watch-tower-line. Simply using (can-afford-building watch-tower) will work regardless of tower upgrades. You cannot use building classes with this command.

[AIRef](https://airef.github.io/commands/commands-details.html#can-afford-building)

Completion insert text:

```text
(can-afford-building ${1:BuildingId})
```

<a id="symbol-can-afford-complete-wall"></a>

## `can-afford-complete-wall`

- Kind: `command`
- Detail: Fact - Walls & Gates, Can Do

Syntax: `(can-afford-complete-wall <Perimeter> <WallId>)`

Checks whether the computer player has enough resources to finish the given wall type at the pPerimeter. Perimeter 1 is usually between 10 and 20 tiles from the starting Town Center. Perimeter 2 is usually between 18 and 30 tiles from the starting Town Center. If wall placement is enabled at a particular perimeter with enable-wall-placement, the AI engine will attempt to plan a roughly circular wall pattern within the given perimeter distances and construct the wall according to this pattern when the build-wall command is issued. In particular, can-afford-complete-wall checks:The wall type is available to the computer player's civ.The tech tree prerequisites are met.Required resources are available.It does not take into account escrowed resources. It does not check if wall area is explored or if enable-wall-placement has been used. pPerimeter is either: '1' for a 10-20 tile radius aroung home TC or '2' for an 18-30 tile radius.

[AIRef](https://airef.github.io/commands/commands-details.html#can-afford-complete-wall)

Completion insert text:

```text
(can-afford-complete-wall ${1:Perimeter} ${2:WallId})
```

<a id="symbol-can-afford-research"></a>

## `can-afford-research`

- Kind: `command`
- Detail: Fact - Techs, Can Do

Syntax: `(can-afford-research <TechId>)`

Checks whether the computer player has enough resources to perform the given research. Also checks that the research is available for the civ, that its not already researched and that the computer player has reached the required age. Does not check if the required building is built. The fact does not take into account escrowed resources. You can also use my-unique-research, which will usually check the imperial age unique tech for the civilization, and you can also use my-second-unique-research, which will usually check the castle age unique tech for the civilization. The excepts are the Britons, Franks, Goths, and Saracens, whose my-unique-research and my-second-unique-research are switched.

[AIRef](https://airef.github.io/commands/commands-details.html#can-afford-research)

Completion insert text:

```text
(can-afford-research ${1:TechId})
```

<a id="symbol-can-afford-unit"></a>

## `can-afford-unit`

- Kind: `command`
- Detail: Fact - Units, Can Do

Syntax: `(can-afford-unit <UnitId>)`

Checks whether the computer player has enough resources to train the given unit. Does not check anything else. The fact does not take into account escrowed resources. The fact allows the use of unit line wildcard parameters for pUnitId. These wildcard parameters allow you to specify a unit line rather than an individual unit in the unit line. You cannot use unit classes with this command. my-unique-unit, my-elite-unique-unit, and my-unique-unit-line can also be used, which will automatically get the UnitId of the unique unit, elite unique unit, or unique unit line that the AI's civ can train from the castle.

[AIRef](https://airef.github.io/commands/commands-details.html#can-afford-unit)

Completion insert text:

```text
(can-afford-unit ${1:UnitId})
```

<a id="symbol-can-build"></a>

## `can-build`

- Kind: `command`
- Detail: Fact - Buildings, Can Do

Syntax: `(can-build <BuildingId>)`

This fact checks whether the computer player can build the given building. You cannot use building classes with this command. This command does not work with walls or gates. However, you can use can-build-wall, can-build-gate, up-can-build-line, or up-can-build to check if walls or gates can be built. In particular it checks:It's available to the computer player's civ.Tech tree prerequisites are met (also works for the Khmer building prerequisites bonus).Resources needed for the building are available, not counting escrow stockpiles.It does not check whether villagers exist to build it, or if there is adequate space for the building. The fact allows the use of building line wildcard parameters for pBuildingId. The only wildcard parameter available is watch-tower-line. However, it is better to use watch-tower instead of watch-tower-line, even after Guard Tower or Keep upgrades due to some bugs with watch-tower-line. Simply using (can-build watch-tower) will work regardless of tower upgrades. Important Note: Always use a can-build, can-build-with-escrow, or up-can-build condition in every rule where you use the build or up-build command. Without this condition, the building queue for this building may get stuck for the rest of the game.

[AIRef](https://airef.github.io/commands/commands-details.html#can-build)

Completion insert text:

```text
(can-build ${1:BuildingId})
```

<a id="symbol-can-build-gate"></a>

## `can-build-gate`

- Kind: `command`
- Detail: Fact - Buildings, Can Do, Walls & Gates

Syntax: `(can-build-gate <Perimeter>)`

Checks whether construction of a gate as part of the given perimeter wall can start. In non-DE versions, this command will only check if you can build stone gates. In DE, this command will check if you can build the gate type specified by snGateTypeForWall. Perimeter 1 is usually between 10 and 20 tiles from the starting Town Center. Perimeter 2 is usually between 18 and 30 tiles from the starting Town Center. If wall placement is enabled at a particular perimeter with enable-wall-placement, the AI engine will attempt to plan a roughly circular wall pattern within the given perimeter distances and construct the wall according to this pattern when the build-wall command is issued. Once the AI finds an appropriate location to build a gate within the given perimeter and the build-gate command is issued, the AI will replace four wall segments with a gate foundation. can-build-gate checks:It is available to the computer player's civ.Tech tree prerequisites are met.Required resources are available (not counting escrow resources).There is a location in an existing wall to build it.It will return false if it cannot fit a gate 3 tiles away from existing gates. In the DE version, to check if the AI can build palisade gates, set snGateTypeForWall to 1 before using this command.

[AIRef](https://airef.github.io/commands/commands-details.html#can-build-gate)

Completion insert text:

```text
(can-build-gate ${1:Perimeter})
```

<a id="symbol-can-build-gate-with-escrow"></a>

## `can-build-gate-with-escrow`

- Kind: `command`
- Detail: Fact - Buildings, Can Do, Walls & Gates

Syntax: `(can-build-gate-with-escrow <Perimeter>)`

Checks whether construction of a gate as part of the given perimeter wall can start. In non-DE versions, this command will only check if you can build stone gates. In DE, this command will check if you can build the gate type specified by snGateTypeForWall. Perimeter 1 is usually between 10 and 20 tiles from the starting Town Center. Perimeter 2 is usually between 18 and 30 tiles from the starting Town Center. If wall placement is enabled at a particular perimeter with enable-wall-placement, the AI engine will attempt to plan a roughly circular wall pattern within the given perimeter distances and construct the wall according to this pattern when the build-wall command is issued. Once the AI finds an appropriate location to build a gate within the given perimeter and the build-gate command is issued, the AI will replace four wall segments with a gate foundation. can-build-gate-with-escrow checks:It is available to the computer player's civ.Tech tree prerequisites are met.Required resources are available including escrow stockpiles.There is a location in an existing wall to build it.It will return false if it cannot fit a gate 3 tiles away from existing gates. In the DE version, to check if the AI can build palisade gates, set snGateTypeForWall to 1 before using this command.

[AIRef](https://airef.github.io/commands/commands-details.html#can-build-gate-with-escrow)

Completion insert text:

```text
(can-build-gate-with-escrow ${1:Perimeter})
```

<a id="symbol-can-build-wall"></a>

## `can-build-wall`

- Kind: `command`
- Detail: Fact - Buildings, Can Do, Walls & Gates

Syntax: `(can-build-wall <Perimeter> <WallId>)`

Checks whether a given wall type can be built at the given perimeter without escrowed resources. Perimeter 1 is usually between 10 and 20 tiles from the starting Town Center. Perimeter 2 is usually between 18 and 30 tiles from the starting Town Center. If wall placement is enabled at a particular perimeter with enable-wall-placement, the AI engine will attempt to plan a roughly circular wall pattern within the given perimeter distances and construct the wall according to this pattern when the build-wall command is issued. In particular, can-build-wall checks:The wall type is available to the computer player's civ.Tech tree prerequisites are met.There is a location to build a wall.Required resources are available, not counting escrow amounts.This fact checks that there is enough stone for at least 5 wall pieces, whereas can-afford-complete-wall checks if there is enough stone for the entire wall. The fact allows the use of wall line wildcard parameters for pWallId. The only available wall line wildcard parameter is stone-wall-line. Note you are allowed to enable wall placement at both perimeters.

[AIRef](https://airef.github.io/commands/commands-details.html#can-build-wall)

Completion insert text:

```text
(can-build-wall ${1:Perimeter} ${2:WallId})
```

<a id="symbol-can-build-wall-with-escrow"></a>

## `can-build-wall-with-escrow`

- Kind: `command`
- Detail: Fact - Buildings, Can Do, Walls & Gates

Syntax: `(can-build-wall-with-escrow <Perimeter> <WallId>)`

Checks whether a given wall type can be built at the given perimeter, including with escrowed resources.Perimeter 1 is usually between 10 and 20 tiles from the starting Town Center. Perimeter 2 is usually between 18 and 30 tiles from the starting Town Center. If wall placement is enabled at a particular perimeter with enable-wall-placement, the AI engine will attempt to plan a roughly circular wall pattern within the given perimeter distances and construct the wall according to this pattern when the build-wall command is issued. In particular, can-build-wall-with-escrow checks:The wall type is available to the computer player's civ.Tech tree prerequisites are met.There is a location to build a wall.Required resources are available including escrow stockpiles.This fact checks that there is enough stone for at least 5 wall pieces, whereas can-afford-complete-wall checks if there is enough stone for the entire wall. The Fact allows the use of wall line wildcard parameters for pWallId. The only available wall line wildcard parameter is stone-wall-line. Note you are allowed to enable wall placement at both perimeters.

[AIRef](https://airef.github.io/commands/commands-details.html#can-build-wall-with-escrow)

Completion insert text:

```text
(can-build-wall-with-escrow ${1:Perimeter} ${2:WallId})
```

<a id="symbol-can-build-with-escrow"></a>

## `can-build-with-escrow`

- Kind: `command`
- Detail: Fact - Buildings, Can Do

Syntax: `(can-build-with-escrow <BuildingId>)`

This fact checks whether the computer player can build the given building if escrowed resources are included. You cannot use building classes with this command. This command does not work with walls or gates. However, you can use can-build-wall-with-escrow, can-build-gate-with-escrow, up-can-build-line, or up-can-build to check if walls or gates can be built. In particular it checks:It's available to the computer player's civ.Tech tree prerequisites are met (also works for the Khmer building prerequisites bonus).Resources needed for the building are available including escrow stockpiles.It does not check whether villagers exist to build it, or if there is adequate space for the building. The fact allows the use of building line wildcard parameters for pBuildingId. The only wildcard parameter available is watch-tower-line. However, it is better to use watch-tower instead of watch-tower-line, even after Guard Tower or Keep upgrades due to some bugs with watch-tower-line. Simply using (can-build-with-escrow watch-tower) will work regardless of tower upgrades. Important Note: Always use a can-build, can-build-with-escrow, or up-can-build condition in every rule where you use the build or up-build command. Without this condition, the building queue for this building may get stuck for the rest of the game.

[AIRef](https://airef.github.io/commands/commands-details.html#can-build-with-escrow)

Completion insert text:

```text
(can-build-with-escrow ${1:BuildingId})
```

<a id="symbol-can-buy-commodity"></a>

## `can-buy-commodity`

- Kind: `command`
- Detail: Fact - Can Do, Economy, Trading

Syntax: `(can-buy-commodity <Commodity>)`

Checks whether the computer player can buy one lot (100 resources) of the given commodity (food, wood, or stone). The fact does not take into account escrowed resources. In other words, this checks if the AI has a market and enough gold at the current buying price for the specified commodity to be able to buy 100 of the specified commodity.

[AIRef](https://airef.github.io/commands/commands-details.html#can-buy-commodity)

Completion insert text:

```text
(can-buy-commodity ${1:Commodity})
```

<a id="symbol-can-research"></a>

## `can-research`

- Kind: `command`
- Detail: Fact - Can Do, Techs

Syntax: `(can-research <TechId>)`

Checks if the given research can start. In particular it checks:The research item is available to the computer player's civ.Tech tree prerequisites are metRequired resources are available (not including escrow stockpiles).The appropriate building has no items in the queue so that it may start the research.Research names, except for ages, my-unique-research, my-second-unique-research, are prefixed with a "ri-" which might stand for "research item". You can also research by the research ID rather than the research name. You can see all technologies and their research IDs in the Technologies table. You can also use my-unique-research, which will usually (always in DE) check the imperial age unique tech for the civilization, and you can also use my-second-unique-research, which will usually (always in DE) check the castle age unique tech for the civilization. In UP and WK, the exceptions are the Britons (in WK only) and Goths, whose my-unique-research and my-second-unique-research are switched.

[AIRef](https://airef.github.io/commands/commands-details.html#can-research)

Completion insert text:

```text
(can-research ${1:TechId})
```

<a id="symbol-can-research-with-escrow"></a>

## `can-research-with-escrow`

- Kind: `command`
- Detail: Fact - Can Do, Techs

Syntax: `(can-research-with-escrow <TechId>)`

Checks if the given research can start. In particular it checks:The research item is available to the computer player's civ.Tech tree prerequisites are met.Required resources are available, including escrow stockpiles.The appropriate building has no items in the queue so that it may start the research.Research names, except for ages, my-unique-research, my-second-unique-research, are prefixed with a "ri-" which might stand for "research item". You can also research by the research ID rather than the research name. You can see all technologies and their research IDs in the Technologies table. You can also use my-unique-research, which will usually check the imperial age unique tech for the civilization, and you can also use my-second-unique-research, which will usually check the castle age unique tech for the civilization. The excepts are the Britons, Franks, Goths, and Saracens, whose my-unique-research and my-second-unique-research are switched.

[AIRef](https://airef.github.io/commands/commands-details.html#can-research-with-escrow)

Completion insert text:

```text
(can-research-with-escrow ${1:TechId})
```

<a id="symbol-can-sell-commodity"></a>

## `can-sell-commodity`

- Kind: `command`
- Detail: Fact - Can Do, Economy, Trading

Syntax: `(can-sell-commodity <Commodity>)`

Checks whether the computer player can sell one lot (100 resources) of the given commodity (food, wood, or stone). The fact does not take into account escrowed resources. In other words, this checks if the AI has a market and has at least 100 of the specified commodity that it can sell for gold.

[AIRef](https://airef.github.io/commands/commands-details.html#can-sell-commodity)

Completion insert text:

```text
(can-sell-commodity ${1:Commodity})
```

<a id="symbol-can-spy"></a>

## `can-spy`

- Kind: `command`
- Detail: Fact - Can Do, Techs

Syntax: `(can-spy)`

Checks if the AI can research Treason without escrowed resources. Only works in Regicide games. The computer player does see the revealed area around the enemy kings as expected. This command does not check if the AI can research Spies like you might expect.

[AIRef](https://airef.github.io/commands/commands-details.html#can-spy)

Completion insert text:

```text
(can-spy)
```

<a id="symbol-can-spy-with-escrow"></a>

## `can-spy-with-escrow`

- Kind: `command`
- Detail: Fact - Can Do, Techs

Syntax: `(can-spy-with-escrow)`

Checks if the AI can research Treason, including escrowed resources. The computer player does see the revealed area around the enemy kings as expected. This command does not check if the AI can research Spies with escrow like you might expect.

[AIRef](https://airef.github.io/commands/commands-details.html#can-spy-with-escrow)

Completion insert text:

```text
(can-spy-with-escrow)
```

<a id="symbol-can-train"></a>

## `can-train`

- Kind: `command`
- Detail: Fact - Can Do, Units

Syntax: `(can-train <UnitId>)`

Checks that the training of a given unit can start. You cannot use unit classes with this command. my-unique-unit, my-elite-unique-unit, and my-unique-unit-line can also be used, which will automatically get the UnitId of the unique unit, elite unique unit, or unique unit line that the AI's civ can train from the castle. In particular it checks:The unit is available to the computer player's civ.Tech tree prerequisites are met.Required resources are available (not counting escrow stockpiles).There is enough housing headroom for the unit.There is an appropriate building that is ready to queue or start training the unit, where the number of queued units and techs is less than the current snEnableTrainingQueue setting.The fact allows the use of unit line wildcard parameters for pUnitId, which means that you can use (can-train spearman-line), instead of (can-train spearman). Interestingly, you can safely use the base unit of a unit line with this command instead of the unit line version, and it will work regardless of any upgrades that have been researched. For example, you can safely use (can-train archer) even if Crossbowman has been researched. This capability is important if you are scripting for WololoKingdoms (WK) or any other mod where some unit lines aren't defined in the AI engine. Unique units can be trained dynamically by using my-unique-unit or my-unique-unit-line as long as your aren't scripting for a Userpatch modpack like WK. You can also train by the unit ID rather than the unit name. You can see all units and their unit IDs in the Objects table. In WK, there are two units that use a separate placeholder unit ID for training purposes, and you must use it for all can-train, can-train-with-escrow, train, up-can-train, and up-train commands. These units are the condottiero and genitour. Use ID 184 for condottiero-placeholder and use ID 732 for genitour-placeholder. You cannot check for the ability to train units with unit classes (like infantry-class) or with sets (like huskarl-set, which includes castle huskarls and barracks huskarls). To check for units like huskarls or tarkans that can be trained at multiple buildings, you must each each unit type separately, such as (or (can-train huskarl) (can-train barracks-huskarl)). To check if mercenary kipchaks (elite kipchaks that allies can train after Cuman Mercenaries is researched) can be trained, use "mercenary-kipchak" rather than kipchak-line. This fact will return false if the setting of snDockTrainingFilter currently restricts the training of ships.

[AIRef](https://airef.github.io/commands/commands-details.html#can-train)

Completion insert text:

```text
(can-train ${1:UnitId})
```

<a id="symbol-can-train-with-escrow"></a>

## `can-train-with-escrow`

- Kind: `command`
- Detail: Fact - Can Do, Units

Syntax: `(can-train-with-escrow <UnitId>)`

Checks that the training of a given unit can start. You cannot use unit classes with this command. my-unique-unit, my-elite-unique-unit, and my-unique-unit-line can also be used, which will automatically get the UnitId of the unique unit, elite unique unit, or unique unit line that the AI's civ can train from the castle. In particular it checks:The unit is available to the computer player's civ.Tech tree prerequisites are met.Required resources are available including escrow stockpiles.There is enough housing headroom for the unit.There is an appropriate building that is not busy and is ready to start training the unit.The fact allows the use of unit line wildcard parameters for pUnitId, which means that you can use (can-train-with-escrow spearman-line), instead of (can-train-with-escrow spearman). Interestingly, you can safely use the base unit of a unit line with this command instead of the unit line version, and it will work regardless of any upgrades that have been researched. For example, you can safely use (can-train-with-escrow archer) even if Crossbowman has been researched. This capability is important if you are scripting for WololoKingdoms (WK) or any other mod where some unit lines aren't defined in the AI engine. Unique units can be trained dynamically by using my-unique-unit or my-unique-unit-line as long as your aren't scripting for a Userpatch modpack like WK. You can also train by the unit ID rather than the unit name. You can see all units and their unit IDs in the Objects table. In WK, there are two units that use a separate placeholder unit ID for training purposes, and you must use it for all can-train, can-train-with-escrow, train, up-can-train, and up-train commands. These units are the condottiero and genitour. Use ID 184 for condottiero-placeholder and use ID 732 for genitour-placeholder. You cannot check for the ability to train units with unit classes (like infantry-class) or with sets (like huskarl-set, which includes castle huskarls and barracks huskarls). To check for units like huskarls or tarkans that can be trained at multiple buildings, you must each each unit type separately, such as (or (can-train-with-escrow huskarl) (can-train-with-escrow barracks-huskarl)). To check if mercenary kipchaks (elite kipchaks that allies can train after Cuman Mercenaries is researched) can be trained, use "mercenary-kipchak" rather than kipchak-line. This fact will return false if the setting of snDockTrainingFilter currently restricts the training of ships.

[AIRef](https://airef.github.io/commands/commands-details.html#can-train-with-escrow)

Completion insert text:

```text
(can-train-with-escrow ${1:UnitId})
```

<a id="symbol-cc-add-resource"></a>

## `cc-add-resource`

- Kind: `command`
- Detail: Action - Cheat, Economy

Syntax: `(cc-add-resource <Resource> <Value>)`

A cheating action that adds the given resource amount to the computer player. This command works even if cheats are disabled. It is to be used in scenarios to avoid late game oddities such as computer player villagers going all over the map while looking for the last pile of gold. Negative amounts can be used to remove resources from the computer player's stockpile.

[AIRef](https://airef.github.io/commands/commands-details.html#cc-add-resource)

Completion insert text:

```text
(cc-add-resource ${1:Resource} ${2:Value})
```

<a id="symbol-cc-players-building-count"></a>

## `cc-players-building-count`

- Kind: `command`
- Detail: Fact - Buildings, Cheat, Counting, Other Player Info

Syntax: `(cc-players-building-count <PlayerNumber> <compareOp> <Value>)`

A cheating version of players-building-count. This command works even if cheats are disabled. For use in scenarios only. The fact checks the given player's building count. Both existing buildings and buildings under construction are included regardless of whether they have been seen - fog is ignored. Unlike building-count, buildings that existed from the start of the game, such as the starting town center, are included. Also, farms are included, but walls and gates are not included. The Fact allows "focus-player", "target-player", and "any"/"every" wildcard parameters for pPlayerNumber. It also allows for scenario-player-# and lobby-player-#, where # is between 1 and 8. scenario-player-# refers to the player color (where red = scenario-player-2), and lobby-player-# refers to the player slot (where the lobby host or a human player playing a single player campaign is always lobby-player-1).

[AIRef](https://airef.github.io/commands/commands-details.html#cc-players-building-count)

Completion insert text:

```text
(cc-players-building-count ${1:PlayerNumber} ${2:compareOp} ${3:Value})
```

<a id="symbol-cc-players-building-type-count"></a>

## `cc-players-building-type-count`

- Kind: `command`
- Detail: Fact - Buildings, Cheat, Counting, Other Player Info

Syntax: `(cc-players-building-type-count <PlayerNumber> <BuildingId> <compareOp> <Value>)`

A cheating version of players-building-type-count. This command works even if cheats are disabled. For use in scenarios only. This fact checks the given player's building count for the given building. Both existing buildings and buildings under construction of the given type are included regardless of whether they have been seen - fog is ignored. The Fact allows "focus-player", "target-player", "any"/"every" wildcard parameters for pPlayerNumber. It also allows for scenario-player-# and lobby-player-#, where # is between 1 and 8. scenario-player-# refers to the player color (where red = scenario-player-2), and lobby-player-# refers to the player slot (where the lobby host or human player playing a single player campaign is always lobby-player-1). It also allows the use of building line wildcard parameters for pBuildingId. The only wildcard parameter available is watch-tower-line. However, it is better to use watch-tower instead of watch-tower-line, even after Guard Tower or Keep upgrades due to some bugs with watch-tower-line. Simply using (cc-players-building-type-count any-enemy watch-tower > 0) will work regardless of tower upgrades. There are four ways you can specify the building "type":Building Name: the name of an individual building, such as house, watch-tower, or town-center.Building Id: the numerical ID assigned to each building, such as 12 (the barracks) or 70 (the house). See the ID column in the Objects Table for a list.Building Line: the building line for the building. The only option here is watch-tower-line, and avoid using it as there are various bugs with it. Simply use watch-tower instead.Building Class: the class of a building, such as building-class, tower-class, or farm-class. Classes group several building types together into a single category. Using a building class will count all buildings of this class. See the Class column in the Objects Table to see each building's class. Classes don't work for enemy players with players-building-type-count, but they do work with cc-players-building-type-count.

[AIRef](https://airef.github.io/commands/commands-details.html#cc-players-building-type-count)

Completion insert text:

```text
(cc-players-building-type-count ${1:PlayerNumber} ${2:BuildingId} ${3:compareOp} ${4:Value})
```

<a id="symbol-cc-players-unit-count"></a>

## `cc-players-unit-count`

- Kind: `command`
- Detail: Fact - Cheat, Counting, Other Player Info, Units

Syntax: `(cc-players-unit-count <PlayerNumber> <compareOp> <Value>)`

A cheating version of players-unit-count. This command works even if cheats are disabled. For use in scenarios only. This fact checks the given player's unit count. Only trained units are included and fog is ignored. The Fact allows "focus-player", "target-player", and "any"/"every" wildcard parameters for pPlayerNumber. It also allows for scenario-player-# and lobby-player-#, where # is between 1 and 8. scenario-player-# refers to the player color (where red = scenario-player-2), and lobby-player-# refers to the player slot (where the lobby host or human player playing a single player campaign is always lobby-player-1).

[AIRef](https://airef.github.io/commands/commands-details.html#cc-players-unit-count)

Completion insert text:

```text
(cc-players-unit-count ${1:PlayerNumber} ${2:compareOp} ${3:Value})
```

<a id="symbol-cc-players-unit-type-count"></a>

## `cc-players-unit-type-count`

- Kind: `command`
- Detail: Fact - Cheat, Counting, Other Player Info, Units

Syntax: `(cc-players-unit-type-count <PlayerNumber> <UnitId> <compareOp> <Value>)`

A cheating version of players-unit-type-count. This command works even if cheats are disabled. For use in scenarios only, though most AI tournaments allows its use to see if particular Gaia objects are on the map at the beginning of the game, for custom map detection purposes. For example, some scripts will check to see if fish are on the map to detect if the map is a water map. This fact checks the given player's unit count. Only trained units of the given type are included and fog is ignored. The Fact allows "focus-player", "target-player", and "any"/"every" wildcard parameters for pPlayerNumber. It also allows for scenario-player-# and lobby-player-#, where # is between 1 and 8. scenario-player-# refers to the player color (where red = scenario-player-2), and lobby-player-# refers to the player slot (where the lobby host or human player playing a single player campaign is always lobby-player-1). Counting Gaia units (player number 0) is not considered cheating. There are four ways you can specify the unit "type":Unit Name: the name of an individual unit, such as villager, spearman, or monk.Unit Id: the numerical ID assigned to each unit, such as 4 (the archer) or 74 (militiaman). See the ID column in the Objects Table for a list.Unit Line: the unit line for the unit. This includes all units in a unit line. For example, archer-line includes archers, crossbowmen, and arbalests.Unit Class: the class of a unit, such as infantry-class, cavalry-archer-class, or monastery-class. Classes group several unit types together into a single category. Using a unit class will count all units of this class. See the Class column in the Objects Table to see each unit's class. Classes don't work for enemy players with players-unit-type-count, but they do work with cc-players-unit-type-count.

[AIRef](https://airef.github.io/commands/commands-details.html#cc-players-unit-type-count)

Completion insert text:

```text
(cc-players-unit-type-count ${1:PlayerNumber} ${2:UnitId} ${3:compareOp} ${4:Value})
```

<a id="symbol-chat-local"></a>

## `chat-local`

- Kind: `command`
- Detail: Action - Chat, Debugging

Syntax: `(chat-local <String>)`

Displays the given string (a message in quotation marks) as a local chat message to all players. Local chat messages display chat messages in white rather than with the AI's player color, making this command strictly inferior to chat-to-all. If the chat message string starts with numerals, that number will be sent as a taunt to all players and the starting numerals will be removed from the message. For example, "1 TC" will send taunt 1 to all players and send the message " TC" to all players.

[AIRef](https://airef.github.io/commands/commands-details.html#chat-local)

Completion insert text:

```text
(chat-local ${1:String})
```

<a id="symbol-chat-local-to-self"></a>

## `chat-local-to-self`

- Kind: `command`
- Detail: Action - Chat, Debugging

Syntax: `(chat-local-to-self <String>)`

Displays a given string (a message in quotation marks) as local chat message. The message is displayed only if the user is the same player as the computer player sending the message. For debugging purposes only. Local chat messages display chat messages in white rather than with the AI's player color, making this command strictly inferior to chat-to-player with my-player-number as the player Id. If the chat message string starts with numerals, that number will be sent as a taunt to self and the starting numerals will be removed from the message. For example, "1 TC" will send taunt 1 to self and send the message " TC" to self.

[AIRef](https://airef.github.io/commands/commands-details.html#chat-local-to-self)

Completion insert text:

```text
(chat-local-to-self ${1:String})
```

<a id="symbol-chat-local-using-id"></a>

## `chat-local-using-id`

- Kind: `command`
- Detail: Action - Chat

Syntax: `(chat-local-using-id <LanguageId>)`

Displays a string, defined by a string id, as a local chat message to all players. For more info on String ids, see the description of the pLanguageId parameter. For example, string id 22322 in English is "No wonder thou wert victorious! I shalt abdicate." Local chat messages display chat messages in white rather than with the AI's player color, making this command strictly inferior to chat-to-all-using-id.

[AIRef](https://airef.github.io/commands/commands-details.html#chat-local-using-id)

Completion insert text:

```text
(chat-local-using-id ${1:LanguageId})
```

<a id="symbol-chat-local-using-range"></a>

## `chat-local-using-range`

- Kind: `command`
- Detail: Action - Chat

Syntax: `(chat-local-using-range <LanguageId> <Value>)`

Displays a random string from a given range as a local chat message to all players. The random string is defined by a string id randomly picked out of a given string id range. For more info on String ids, see the description of the pLanguageId parameter. For example, string ids from 22300 through 22321 include all of the possible random excuses the default AI can give for why it lost the game. Local chat messages display chat messages in white rather than with the AI's player color, making this command strictly inferior to chat-to-all-using-range.

[AIRef](https://airef.github.io/commands/commands-details.html#chat-local-using-range)

Completion insert text:

```text
(chat-local-using-range ${1:LanguageId} ${2:Value})
```

<a id="symbol-chat-to-all"></a>

## `chat-to-all`

- Kind: `command`
- Detail: Action - Chat, Debugging

Syntax: `(chat-to-all <String>)`

Sends a given string (a message in quotation marks) as a chat message to all players. If the chat message string starts with numerals, that number will be sent as a taunt to all players and the starting numerals will be removed from the message. For example, "1 TC" will send taunt 1 to all players and send the message " TC" to all players.

[AIRef](https://airef.github.io/commands/commands-details.html#chat-to-all)

Completion insert text:

```text
(chat-to-all ${1:String})
```

<a id="symbol-chat-to-all-using-id"></a>

## `chat-to-all-using-id`

- Kind: `command`
- Detail: Action - Chat

Syntax: `(chat-to-all-using-id <LanguageId>)`

Sends a string, defined by a string id, as a chat message to all players. For more info on String ids, see the description of the pLanguageId parameter. For example, string id 22322 in English is "No wonder thou wert victorious! I shalt abdicate."

[AIRef](https://airef.github.io/commands/commands-details.html#chat-to-all-using-id)

Completion insert text:

```text
(chat-to-all-using-id ${1:LanguageId})
```

<a id="symbol-chat-to-all-using-range"></a>

## `chat-to-all-using-range`

- Kind: `command`
- Detail: Action - Chat

Syntax: `(chat-to-all-using-range <LanguageId> <Value>)`

Sends a random string from a given range as a chat message to all players. The random string is defined by a string id randomly picked out of a given string id range. For more info on String ids, see the description of the pLanguageId parameter. For example, string ids from 22300 through 22321 include all of the possible random excuses the default AI can give for why it lost the game.

[AIRef](https://airef.github.io/commands/commands-details.html#chat-to-all-using-range)

Completion insert text:

```text
(chat-to-all-using-range ${1:LanguageId} ${2:Value})
```

<a id="symbol-chat-to-allies"></a>

## `chat-to-allies`

- Kind: `command`
- Detail: Action - Chat

Syntax: `(chat-to-allies <String>)`

Sends a given string as a chat message to allies. If the chat message string starts with numerals, that number will be sent as a taunt to all allies and the starting numerals will be removed from the message. For example, "1 TC" will send taunt 1 to all allies and send the message " TC" to all allies.

[AIRef](https://airef.github.io/commands/commands-details.html#chat-to-allies)

Completion insert text:

```text
(chat-to-allies ${1:String})
```

<a id="symbol-chat-to-allies-using-id"></a>

## `chat-to-allies-using-id`

- Kind: `command`
- Detail: Action - Chat

Syntax: `(chat-to-allies-using-id <LanguageId>)`

Sends a string, defined by a string id, as a chat message to allied players. For more info on String ids, see the description of the pLanguageId parameter. For example, string id 22322 in English is "No wonder thou wert victorious! I shalt abdicate."

[AIRef](https://airef.github.io/commands/commands-details.html#chat-to-allies-using-id)

Completion insert text:

```text
(chat-to-allies-using-id ${1:LanguageId})
```

<a id="symbol-chat-to-allies-using-range"></a>

## `chat-to-allies-using-range`

- Kind: `command`
- Detail: Action - Chat

Syntax: `(chat-to-allies-using-range <LanguageId> <Value>)`

Sends a random string from a given range as a chat message to allies. The random string is defined by a string id randomly picked out of a given string id range. For more info on String ids, see the description of the pLanguageId parameter. For example, string ids from 22300 through 22321 include all of the possible random excuses the default AI can give for why it lost the game.

[AIRef](https://airef.github.io/commands/commands-details.html#chat-to-allies-using-range)

Completion insert text:

```text
(chat-to-allies-using-range ${1:LanguageId} ${2:Value})
```

<a id="symbol-chat-to-enemies"></a>

## `chat-to-enemies`

- Kind: `command`
- Detail: Action - Chat

Syntax: `(chat-to-enemies <String>)`

Sends a given string as a chat message to enemies. If the chat message string starts with numerals, that number will be sent as a taunt to all enemies and the starting numerals will be removed from the message. For example, "1 TC" will send taunt 1 to all enemies and send the message " TC" to all enemies.

[AIRef](https://airef.github.io/commands/commands-details.html#chat-to-enemies)

Completion insert text:

```text
(chat-to-enemies ${1:String})
```

<a id="symbol-chat-to-enemies-using-id"></a>

## `chat-to-enemies-using-id`

- Kind: `command`
- Detail: Action - Chat

Syntax: `(chat-to-enemies-using-id <LanguageId>)`

sends a string, defined by a string id, as a chat message to enemy players. For more info on String ids, see the description of the pLanguageId parameter. For example, string id 22322 in English is "No wonder thou wert victorious! I shalt abdicate."

[AIRef](https://airef.github.io/commands/commands-details.html#chat-to-enemies-using-id)

Completion insert text:

```text
(chat-to-enemies-using-id ${1:LanguageId})
```

<a id="symbol-chat-to-enemies-using-range"></a>

## `chat-to-enemies-using-range`

- Kind: `command`
- Detail: Action - Chat

Syntax: `(chat-to-enemies-using-range <LanguageId> <Value>)`

Sends a random string from a given range as a chat message to enemies. The random string is defined by a string id randomly picked out of a given string id range. For more info on String ids, see the description of the pLanguageId parameter. For example, string ids from 22300 through 22321 include all of the possible random excuses the default AI can give for why it lost the game.

[AIRef](https://airef.github.io/commands/commands-details.html#chat-to-enemies-using-range)

Completion insert text:

```text
(chat-to-enemies-using-range ${1:LanguageId} ${2:Value})
```

<a id="symbol-chat-to-player"></a>

## `chat-to-player`

- Kind: `command`
- Detail: Action - Chat, Debugging

Syntax: `(chat-to-player <PlayerNumber> <String>)`

Sends a given string as a chat message to a given player. If the chat message string starts with numerals, that number will be sent as a taunt to the specified player and the starting numerals will be removed from the message. For example, "1 TC" will send taunt 1 to the specified player and send the message " TC" to the specified player. The fact allows "my-player-number", "focus-player", "target-player", and "any"/"every" wildcard parameters for pPlayerNumber. It also allows for scenario-player-# and lobby-player-#, where # is between 1 and 8. scenario-player-# refers to the player color (where red = scenario-player-2), and lobby-player-# refers to the player slot (where the lobby host or human player playing a single player campaign is always lobby-player-1). It also allows the use of rule variables for pPlayerNumber, such as "this-any-ally" or "this-any-enemy".

[AIRef](https://airef.github.io/commands/commands-details.html#chat-to-player)

Completion insert text:

```text
(chat-to-player ${1:PlayerNumber} ${2:String})
```

<a id="symbol-chat-to-player-using-id"></a>

## `chat-to-player-using-id`

- Kind: `command`
- Detail: Action - Chat

Syntax: `(chat-to-player-using-id <PlayerNumber> <LanguageId>)`

sends a string, defined by a string id, as a chat message to a given player. For more info on String ids, see the description of the pLanguageId parameter. For example, string id 22322 in English is "No wonder thou wert victorious! I shalt abdicate." The action allows "my-player-number", "focus-player", "target-player", and "any"/"every" wildcard parameters for pPlayerNumber. It also allows for scenario-player-# and lobby-player-#, where # is between 1 and 8. scenario-player-# refers to the player color (where red = scenario-player-2), and lobby-player-# refers to the player slot (where the lobby host or human player playing a single player campaign is always lobby-player-1). It also allows the use of rule variables for pPlayerNumber, such as "this-any-ally" or "this-any-enemy".

[AIRef](https://airef.github.io/commands/commands-details.html#chat-to-player-using-id)

Completion insert text:

```text
(chat-to-player-using-id ${1:PlayerNumber} ${2:LanguageId})
```

<a id="symbol-chat-to-player-using-range"></a>

## `chat-to-player-using-range`

- Kind: `command`
- Detail: Action - Chat

Syntax: `(chat-to-player-using-range <PlayerNumber> <LanguageId> <Value>)`

Sends a random string from a given range as a chat message to a given player. The random string is defined by a string id randomly picked out of a given string id range. For more info on String ids, see the description of the pLanguageId parameter. For example, string ids from 22300 through 22321 include all of the possible random excuses the default AI can give for why it lost the game. The Action allows "my-player-number", "focus-player", "target-player", and "any"/"every" wildcard parameters for pPlayerNumber. It also allows the use of rule variables for pPlayerNumber, such as "this-any-ally" or "this-any-enemy". It also allows for scenario-player-# and lobby-player-#, where # is between 1 and 8. scenario-player-# refers to the player color (where red = scenario-player-2), and lobby-player-# refers to the player slot (where the lobby host or human player playing a single player campaign is always lobby-player-1).

[AIRef](https://airef.github.io/commands/commands-details.html#chat-to-player-using-range)

Completion insert text:

```text
(chat-to-player-using-range ${1:PlayerNumber} ${2:LanguageId} ${3:Value})
```

<a id="symbol-chat-trace"></a>

## `chat-trace`

- Kind: `command`
- Detail: Action - Chat, Debugging

Syntax: `(chat-trace <Value>)`

Displays the given value to all players as a chat message, with "Trace " in front. Used purely for testing to check when a rule gets executed.

[AIRef](https://airef.github.io/commands/commands-details.html#chat-trace)

Completion insert text:

```text
(chat-trace ${1:Value})
```

<a id="symbol-cheats-enabled"></a>

## `cheats-enabled`

- Kind: `command`
- Detail: Fact - Cheat

Syntax: `(cheats-enabled)`

Checks whether the cheats have been enabled. Cheating commands that start with "cc-" can be used by AI scripts even if cheats are disabled. This command specifically checks whether players can enter cheat codes in the chat.

[AIRef](https://airef.github.io/commands/commands-details.html#cheats-enabled)

Completion insert text:

```text
(cheats-enabled)
```

<a id="symbol-civ-selected"></a>

## `civ-selected`

- Kind: `command`
- Detail: Fact - Own Player Info

Syntax: `(civ-selected <Civ>)`

Checks the computer player's civilization. You can use "my-civ," which will automatically detect the civilization the AI is playing as. Note that the civilization names used with this command for pre-DE civs are usually different than the civ's display name. They are like the pLoadIfSymbol civ names where they often use the adjective form of the civ name, not the plural name. See pCiv for a list of correct civ names to use with this command. You can also enclose code in a #load-if-defined [CIV-NAME]-CIV block if it should only run when a particular civ is selected. To check for the civilization of other players, use players-civ.

[AIRef](https://airef.github.io/commands/commands-details.html#civ-selected)

Completion insert text:

```text
(civ-selected ${1:Civ})
```

<a id="symbol-civilian-population"></a>

## `civilian-population`

- Kind: `command`
- Detail: Fact - Counting, Units

Syntax: `(civilian-population <compareOp> <Value>)`

Checks the computer player's civilian population. The civilian population is villagers, trade units and fishing ships. To check for the civilian-population of other players, use players-civilian-population.

[AIRef](https://airef.github.io/commands/commands-details.html#civilian-population)

Completion insert text:

```text
(civilian-population ${1:compareOp} ${2:Value})
```

<a id="symbol-clear-tribute-memory"></a>

## `clear-tribute-memory`

- Kind: `command`
- Detail: Action - Diplomacy

Syntax: `(clear-tribute-memory <PlayerNumber> <Resource>)`

Clears the given player's tribute memory, the amount of a given resource received in tribute from the given player since the tribute memory was cleared. Only tribute memory for the given resource type is cleared. This command is used in conjunction with cPlayersTributeMemory, which allows you to check the amount of tribute received from the specified player since clear-tribute-memory was issued. The action allows "focus-player", "target-player", and "any"/"every" wildcard parameters for pPlayerNumber. It also allows the use of rule variables for pPlayerNumber, such as "this-any-ally" or "this-any-enemy". It also allows for scenario-player-# and lobby-player-#, where # is between 1 and 8. scenario-player-# refers to the player color (where red = scenario-player-2), and lobby-player-# refers to the player slot (where the lobby host or human player playing a single player campaign is always lobby-player-1).

[AIRef](https://airef.github.io/commands/commands-details.html#clear-tribute-memory)

Completion insert text:

```text
(clear-tribute-memory ${1:PlayerNumber} ${2:Resource})
```

<a id="symbol-commodity-buying-price"></a>

## `commodity-buying-price`

- Kind: `command`
- Detail: Fact - Economy, Trading

Syntax: `(commodity-buying-price <Commodity> <compareOp> <Value>)`

Checks the current buying price for the given commodity. The current buying price is the amount of gold that will be deducted from the gold stockpile to buy 100 of the specified commodity (wood, food, or stone). This price can range between 26 and infinity without Guilds, between 25 and infinity with Guilds, and between 25 and infinity when playing Saracens.

[AIRef](https://airef.github.io/commands/commands-details.html#commodity-buying-price)

Completion insert text:

```text
(commodity-buying-price ${1:Commodity} ${2:compareOp} ${3:Value})
```

<a id="symbol-commodity-selling-price"></a>

## `commodity-selling-price`

- Kind: `command`
- Detail: Fact - Economy, Trading

Syntax: `(commodity-selling-price <Commodity> <compareOp> <Value>)`

Checks the current selling price for the given commodity. The current selling price is the amount of gold that will be added to the gold stockpile when 100 of the specified commodity (wood, food, or stone) is sold. This price can range between 14 and infinity without Guilds, between 17 and infinity with Guilds, and between 19 and infinity when playing Saracens.

[AIRef](https://airef.github.io/commands/commands-details.html#commodity-selling-price)

Completion insert text:

```text
(commodity-selling-price ${1:Commodity} ${2:compareOp} ${3:Value})
```

<a id="symbol-current-age"></a>

## `current-age`

- Kind: `command`
- Detail: Fact - Own Player Info

Syntax: `(current-age <compareOp> <Age>)`

Checks computer player's current age. In Post-Imperial Age Start games, the current age is imperial-age, not post-imperial-age. To check for Post-Imperial Age Start, use #load-if-defined POST-IMPERIAL-AGE-START or starting-age. To check for the current-age of other players, use players-current-age.

[AIRef](https://airef.github.io/commands/commands-details.html#current-age)

Completion insert text:

```text
(current-age ${1:compareOp} ${2:Age})
```

<a id="symbol-current-age-time"></a>

## `current-age-time`

- Kind: `command`
- Detail: Fact - Own Player Info

Syntax: `(current-age-time <compareOp> <Value>)`

Checks the computer player's current age time (time spent in the current age). This time is measured in seconds. To check for the current-age-time of other players, use players-current-age-time.

[AIRef](https://airef.github.io/commands/commands-details.html#current-age-time)

Completion insert text:

```text
(current-age-time ${1:compareOp} ${2:Value})
```

<a id="symbol-current-score"></a>

## `current-score`

- Kind: `command`
- Detail: Fact - Own Player Info

Syntax: `(current-score <compareOp> <Value>)`

Checks the computer player's current score. To check for the current-score of other players, use players-score.

[AIRef](https://airef.github.io/commands/commands-details.html#current-score)

Completion insert text:

```text
(current-score ${1:compareOp} ${2:Value})
```

<a id="symbol-death-match-game"></a>

## `death-match-game`

- Kind: `command`
- Detail: Fact - Game Info

Syntax: `(death-match-game)`

Checks if the game is a Death Match game. You can also enclose code in a #load-if-defined DEATH-MATCH-GAME block if it should only run in a death match game. In DE, ultra high and infinite resource random map games are considered death match games, and this command will be true in those games.

[AIRef](https://airef.github.io/commands/commands-details.html#death-match-game)

Completion insert text:

```text
(death-match-game)
```

<a id="symbol-defconst"></a>

## `defconst`

- Kind: `command`
- Detail: Other - Other

Syntax: `(defconst <Defconst> <Value>)`

Creates a user-defined constant. The syntax of the AI expert system (the programming language that AoE2 uses for its computer AIs) is entirely based on a dictionary of constants (text variables that are assigned a value that will remain constant) that have an integer or string (text) that are assigned to them. For example, "archer" is a constant that is internally defined with the value 4, which is the archer's ID number in the game's unit list. So, any AI code that uses the constant "archer" will interpret it as the number 4. For example, (unit-type-count archer > 5) will check if the AI has more than 5 units with the Unit ID #4, thus counting the number of archers the AI has. The AoE2 AI engine allows AI scripters to define custom constants with the defconst command. Constants are very handy for naming of goals, goal values, timers, taunts, etc. Without constants all of these would be just nameless numbers. Unlike most commands, the defconst command must be used outside of a rule. During the first initial script pass, the AI engine will compile a list of all loaded defconsts and store their assigned values in memory, and the defconst lines in the code will be ignored for the rest of the game. All uses of that defconst must occur after the defconst line in your code, so the best practice is to include all of your defconsts at the top of your main AI file so that they are easy to find and maintain. If you group all of your defconsts together in one file, it makes it easy to customize your AI by changing the number that the defconst represents without having to change it everywhere in your file. In the example below, if you referred to num-dark-age-villagers in many places in your AI, you could easily change the defconst to be 12 villagers by changing it in just one place. If you want to assign a defconst to a different value depending on the game, you can put the defconst inside of a #load-if-defined or a #load-if-not-defined section. Only defconsts within a #load-if-defined or #load-if-not-defined that matches the current game settings will load and create that defconst. In DE, if you have more than one loaded defconst command with the same defconst name, the value of the last defconst with the same name will be the final value for that defconst. In UP, having multiple loaded defconsts with the same name will cause an error. Also, all defconsts used anywhere in the AI must have a defconst that is loaded for all game settings, even if that defconst is only used inside a #load-if-defined or #load-if-not-defined section of code that isn't loaded for the particular game. For example, if "num-eagle-warriors" is a defconst that is only used in code that is loaded with an American civ, the num-eagle-warriors defconst must be created for every possible game setting. For more information, there is a multi-part article series about defconsts here: Defconsts, Goals, and SNs.

[AIRef](https://airef.github.io/commands/commands-details.html#defconst)

Completion insert text:

```text
(defconst ${1:Defconst} ${2:Value})
```

<a id="symbol-defend-soldier-count"></a>

## `defend-soldier-count`

- Kind: `command`
- Detail: Fact - Counting, Defense, Units

Syntax: `(defend-soldier-count <compareOp> <Value>)`

Checks the computer player's defend soldier count. A defend soldier is a land-based military unit not assigned to attack groups. This includes soldiers attacking with attack-now, with sn-number-attack-groups set > 0, or with TSA. Soldiers don't have to be actively defending the town against attacks to be considered defend soldiers. In other words, the defend-soldier-count is calculated by subtracting the attack-soldier-count from the total soldier-count.

[AIRef](https://airef.github.io/commands/commands-details.html#defend-soldier-count)

Completion insert text:

```text
(defend-soldier-count ${1:compareOp} ${2:Value})
```

<a id="symbol-defend-warboat-count"></a>

## `defend-warboat-count`

- Kind: `command`
- Detail: Fact - Counting, Defense, Units

Syntax: `(defend-warboat-count <compareOp> <Value>)`

Checks the computer player's defend warboat count. A defend warboat is a boat capable of attacking that is not assigned to boat attack groups. This includes warboats attacking with attack-now or with sn-number-boat-attack-groups set > 0. Warboats don't have to be actively defending against enemy warship attacks to be considered defend warboats. In other words, the defend-warboat-count is calculated by subtracting the attack-warboat-count from the total warboat-count.

[AIRef](https://airef.github.io/commands/commands-details.html#defend-warboat-count)

Completion insert text:

```text
(defend-warboat-count ${1:compareOp} ${2:Value})
```

<a id="symbol-defrule"></a>

## `defrule`

- Kind: `command`
- Detail: Other - Other

Syntax: `(defrule)`

Defines the start of a new rule. "defrule" is short for "define rule." Rules are the basis for the Expert System, the AI scripting language for AoE2. There is a list of things we know about the game world, the other players, and so on. These are called facts. We check the facts with rules until a set of conditions exists that we need the computer player to act upon. Actions are what we call those commands that cause things to happen in the game. Examples might be training a unit, researching a technology, or sending a chat message. Rules are defined in the script with the defrule instruction. Each defined rule is given a rule ID. If the conditions (facts) for the rule are met (i.e. true), the instructions in that rule (actions) are followed. If the conditions for the rule are not met (False), the rule is passed by. The facts section of the rule is separated from the following actions section with a "=>" forward arrow. Note that the parentheses around the rule are required, though the white-space formatting (spaces, tabs, etc.) is not important. Rules continue to be evaluated in order each pass unless they are disabled. This is done with the disable-self command. Disabled rules cannot be enabled later, but their rule ID is still valid, so the rule will still be counted for rule jump commands like up-jump-rule. Each rule must have at least one fact and at least one action. Each rule is limited to 32 commands, including facts, actions, and logical operators, such as and or not. In UP and the original versions of the game, rules were limited to 16 commands. AIs are limited to loading 10,000 rules. This limit does not include rules that aren't loaded for the particular game, such as rules within a #load-if-defined or a #load-if-not-defined block.

[AIRef](https://airef.github.io/commands/commands-details.html#defrule)

Completion insert text:

```text
(defrule)
```

<a id="symbol-delete-building"></a>

## `delete-building`

- Kind: `command`
- Detail: Action - Buildings

Syntax: `(delete-building <BuildingId>)`

Deletes exactly one building of a given type. You cannot use building classes with this command. There are several other commands available to delete objects: delete-unit: delete exactly one unit of a given typeup-delete-distant-farms: delete farms that are beyond a specified distance from a dropsiteup-delete-idle-units: delete all idle units of the specified typeup-delete-objects: delete all objects of the specified type that have less than the specified hitpointsup-target-objects or up-target-point: when used with the action-delete action, this command will delete all objects in the local search list

[AIRef](https://airef.github.io/commands/commands-details.html#delete-building)

Completion insert text:

```text
(delete-building ${1:BuildingId})
```

<a id="symbol-delete-unit"></a>

## `delete-unit`

- Kind: `command`
- Detail: Action - Units

Syntax: `(delete-unit <UnitId>)`

Deletes exactly one unit of a given type. You cannot use unit classes with this command. my-unique-unit, my-elite-unique-unit, and my-unique-unit-line can also be used, which will automatically get the UnitId of the unique unit, elite unique unit, or unique unit line that the AI's civ can train from the castle. There are several other commands available to delete objects: delete-building: delete exactly one building of a given typeup-delete-distant-farms: delete farms that are beyond a specified distance from a dropsiteup-delete-idle-units: delete all idle units of the specified typeup-delete-objects: delete all objects of the given type that have less than the specified hitpointsup-target-objects or up-target-point: when used with the action-delete action, this command will delete all objects in the local search list

[AIRef](https://airef.github.io/commands/commands-details.html#delete-unit)

Completion insert text:

```text
(delete-unit ${1:UnitId})
```

<a id="symbol-difficulty"></a>

## `difficulty`

- Kind: `command`
- Detail: Fact - Game Info

Syntax: `(difficulty <compareOp> <Difficulty>)`

Checks the difficulty setting. The ordering of difficulty settings is the opposite of what one would expect! Make sure that this is taken in account when using facts to compare difficulties. easiest &gt; easy &gt; moderate &gt; hard &gt; hardest (ie; treat easiest as a difficulty value of 4, easy as 3, moderate as 2, hard as 1, hardest as 0, and extreme as -1). For testing certain difficulty levels see the code examples. It is counter intuitive!(difficulty == easiest)True if the difficulty is easiest(difficulty &gt; easiest)WRONG: This will never be true, Easiest is the &quot;highest&quot; number!(difficulty &lt; hardest)WRONG: This will never be true, Hardest is the &quot;lowest&quot; number (Extreme is the lowest number in DE)!(difficulty &lt;= moderate)This is true if the difficulty is Moderate, Hard, Hardest, or Extreme.(difficulty &gt;= easy)This is true if the difficulty is Easy or Easiest.(difficulty &gt; hard)Counter-intuitive - avoid (you probably want the opposite in fact, see below), this is true if the difficulty is Moderate, Easy or Easiest.(difficulty &lt;= hard)This is true if the difficulty is Hard, Hardest, or Extreme.(difficulty &gt; hardest)This is true if the difficulty is Hard, Moderate, Easy or EasiestBecause of the counter-intuitive ordering of difficulties, you may find it helpful to use #load-if-defined or #load-if-not-defined to check difficulty settings instead, such as #load-if-defined DIFFICULTY-HARD or #load-if-not-defined DIFFICULTY-HARDEST.Full information on difficulty affecting aspectsRemember that easy is referred to as Standard in the game. This information about difficulty is from the CPSB about the hardcoded changes. Automatic changes to some sn values can be stopped with snDoNotScaleForDifficultyLevel; see this SN for more information.Distance an enemy unit must be within when the computer player unit looks for a new target:easiest: LOS (can be modified by snEasiestReactionPercentage)easy: LOS (can be modified by snEasierReactionPercentage)moderate: LOS * 2hard: LOS * 2hardest: LOS * 2Computer players ignore relics on the easiest level.Computer players do not attack villagers on the easiest and easy difficulty levels.If a non-exploring computer unit gets attacked, the computer player's attack delay for attack-group settings is modified:easiest: allow attacking one minute earliereasy: allow attacking two minutes earliermoderate: allow attacking immediatelyhard: allow attacking immediatelyhardest: allow attacking immediatelyAfter a wolf kills a unit, have it gorge itself (not attack again) for:easiest: 35 secondseasy: 30 secondsmoderate: 25 secondshard: 20 secondshardest: 15 secondsDistance a unit must be within when a wolf looks for a new target (UP only):DE removed the reaction distance modifier for predator animals (like Wolves, Snow Leopards) depending on difficulty and made it so that predator animals always find villagers within 6 tiles and other units within 4 tiles. Easiest difficulty on scenarios and campaigns will still use 4 tiles.easiest: LOS * 0.5easy: LOS * 0.75moderate: LOS * 2hard: LOS * 2hardest: LOS * 2Unit build (using villager for example) and research time (including age advancement):easiest: 200% (0:25 to 0:50)easy/standard: 133% (0:25 to 0:33)moderate: 100% (for DE it's 114% (0:25 to 0:28))hard: 100% (for DE it's 105% (0:25 to 0:26))hardest: 100%Building construction appears to be unaffected. For non-DE game versions, Hardest difficulty adds a hardcoded 500 of each resource at the beginning of the game and on reaching each new age. This cannot be disabled, but you can remove these resources with a negative cc-add-resource or up-cc-add-resource command. Also note that starting the game in later ages adds these bonuses incrementally (so up to 2000 for starting in the Imperial Age or Post-Imperial Age). Each difficulty level will change certain SN values automatically (including when set manually) unless sn-do-not-scale-for-difficulty-level is set to 1. See snDoNotScaleForDifficultyLevel for these values. Small additional note is that Hard also still makes SN changes, so it is recommended for a non-cheating AI to use sn-do-not-scale-for-difficulty-level so it can perform well on Hard.

[AIRef](https://airef.github.io/commands/commands-details.html#difficulty)

Completion insert text:

```text
(difficulty ${1:compareOp} ${2:Difficulty})
```

<a id="symbol-disable-rule"></a>

## `disable-rule`

- Kind: `command`
- Detail: Action - Don't Use

Syntax: `(disable-rule <Value>)`

Disables the given rule id. (Not Fully Implemented! Do Not Use!)

[AIRef](https://airef.github.io/commands/commands-details.html#disable-rule)

Completion insert text:

```text
(disable-rule ${1:Value})
```

<a id="symbol-disable-self"></a>

## `disable-self`

- Kind: `command`
- Detail: Action - Other

Syntax: `(disable-self)`

Disables the rule that it is part of so that the rule is never run again. Since disabling takes effect in the next execution pass, other actions in the same rule are still executed once. Use this whenever you only want the rule to run once and never again. Rules disabled with a disable-self command are never read again, but they are still counted as rules by commands that jump over rules like up-jump-rule or up-jump-dynamic.

[AIRef](https://airef.github.io/commands/commands-details.html#disable-self)

Completion insert text:

```text
(disable-self)
```

<a id="symbol-disable-timer"></a>

## `disable-timer`

- Kind: `command`
- Detail: Action - Timers

Syntax: `(disable-timer <TimerId>)`

Disables the given timer. The given timer can be any valid timer number, which can range from 1 to 50. You can also substitute a defconst that is defined with a value between 1 and 50 if you want to give the timer a name. Timers have three possible states, and they cannot have multiple states at once: timer-running, timer-triggered, and timer-disabled. disable-timer or up-set-timer with a -1 timer length puts the timer in the timer-disabled state. enable-timer or up-set-timer with a timer length > 0 puts the timer in the timer-running state. disable-timer doesn't have to be used before using an enable-timer command.

[AIRef](https://airef.github.io/commands/commands-details.html#disable-timer)

Completion insert text:

```text
(disable-timer ${1:TimerId})
```

<a id="symbol-do-nothing"></a>

## `do-nothing`

- Kind: `command`
- Detail: Action - Other

Syntax: `(do-nothing)`

Does nothing. Used as a placeholder action if you don't want a rule to have any actions. Every rule must have at least one fact and one action. In rare cases where you don't want to include any actions in your rule, use do-nothing as a placeholder to fulfill the one action requirement. One of these rare cases is when you want to temporarily comment out all the actions in your rule for testing purposes but you want to keep the facts section of your rule. Unlike disable-self do-nothing will not stop the rule from being checked each pass.

[AIRef](https://airef.github.io/commands/commands-details.html#do-nothing)

Completion insert text:

```text
(do-nothing)
```

<a id="symbol-doctrine"></a>

## `doctrine`

- Kind: `command`
- Detail: Fact - Goals

Syntax: `(doctrine <Value>)`

Checks what the current doctrine is, similar to checking the value of a goal. The doctrine is always an integer value which is set with the set-doctrine command, and the doctrine command simply checks if the doctrine is currently equal to the given value. Unlike goals, there is only one doctrine that you can set, and you can only use the doctrine command to check if the doctrine is currently equal to the given value, not less than, or greater than, or any other type of comparison. In all cases, using goals instead of the doctrine will give you more flexibility, but if you run out of available goals then you can use the doctrine like an extra goal if you need it. The doctrine starts with the value of -1 at the beginning of the game, and it only changes if you use the set-doctrine command.

[AIRef](https://airef.github.io/commands/commands-details.html#doctrine)

Completion insert text:

```text
(doctrine ${1:Value})
```

<a id="symbol-dropsite-min-distance"></a>

## `dropsite-min-distance`

- Kind: `command`
- Detail: Fact - Economy

Syntax: `(dropsite-min-distance <Resource> <compareOp> <Value>)`

Checks computer player's minimum dropsite walking distance for a given resource type. The distance is the tile distance between the tile the resource is on and the center tile of the nearest dropsite. For example, if the dropsite is adjacent to the given resource, then dropsite-min-distance will be 1. Long walking distances indicate a need for a new dropsite. It is not recommended to use this fact for building of first dropsites necessary for age advancement. If, at the beginning, the resources happen to be close enough to the Town Center, building of the first dropsites will be delayed, resulting in slower age progression.If no resources of the given type have been found, then dropsite-min-distance will be -1 for that resource. If resources of the given type have been found but are unaccessible because they are on a different island, then dropsite-min-distance will be 255 for that resource. However, hunting, boar-hunting, deer-hunting, and live-boar drop distances are 255 instead when those hunting resources haven't been found, at least on UP. There are eight different types of resource dropsite distances you can check for: food: all food sources, including farms, except boar and fish for fishing ships. Some specially generated objects, like the Incan starting llama, aren't counted.wood: all trees.stone: all stone mines.gold: all gold mines.Hunting: all boar and deer (and their geographical variants), both live and dead.boar-hunting: all boar (and their geographical variants), both live and dead, excludes all types of deer.deer-hunting: all deer (and their geographical variants), both live and dead, excludes all types of boar.live-boar: all boar (and their geographical variants) that have not yet been killed.

[AIRef](https://airef.github.io/commands/commands-details.html#dropsite-min-distance)

Completion insert text:

```text
(dropsite-min-distance ${1:Resource} ${2:compareOp} ${3:Value})
```

<a id="symbol-enable-rule"></a>

## `enable-rule`

- Kind: `command`
- Detail: Action - Don't Use

Syntax: `(enable-rule <Value>)`

Enables the given rule id. (Not Fully Implemented! Do Not Use!)

[AIRef](https://airef.github.io/commands/commands-details.html#enable-rule)

Completion insert text:

```text
(enable-rule ${1:Value})
```

<a id="symbol-enable-timer"></a>

## `enable-timer`

- Kind: `command`
- Detail: Action - Timers

Syntax: `(enable-timer <TimerId> <Value>)`

Enables the given timer and sets it to the given time interval. The given timer can be any valid timer number, which can range from 1 to 50. You can also substitute a defconst that is defined with a value between 1 and 50 if you want to give the timer a name. Time intervals are measured in game time seconds, so enabling a timer for 240 seconds would start a 4 minute timer. If played on 2.0 speed (Fast speed), this 4 minute timer would last 2 minutes in real time. Timers have three possible states, and they cannot have multiple states at once: timer-running, timer-triggered, and timer-disabled. disable-timer or up-set-timer with a -1 timer length puts the timer in the timer-disabled state. enable-timer or up-set-timer with a timer length > 0 puts the timer in the timer-running state. disable-timer doesn't have to be used before using an enable-timer command.

[AIRef](https://airef.github.io/commands/commands-details.html#enable-timer)

Completion insert text:

```text
(enable-timer ${1:TimerId} ${2:Value})
```

<a id="symbol-enable-wall-placement"></a>

## `enable-wall-placement`

- Kind: `command`
- Detail: Action - Buildings, Walls & Gates

Syntax: `(enable-wall-placement <Perimeter>)`

Enables wall placement for the given perimeter, either perimeter 1 or perimeter 2. Walls cannot be built with the build-wall command at the given perimeter unless this command is used. Enabled wall placement causes the rest of the placement code to do some planning and place all structures at least one tile away from the future wall lines. If you are planning to build a wall, you have to explicitly define which perimeter wall you plan to use when the game starts. This is a one-time action and should be used during the initial setup. Perimeter 1 is usually between 10 and 20 tiles from the starting Town Center. Perimeter 2 is usually between 18 and 30 tiles from the starting Town Center.

[AIRef](https://airef.github.io/commands/commands-details.html#enable-wall-placement)

Completion insert text:

```text
(enable-wall-placement ${1:Perimeter})
```

<a id="symbol-enemy-buildings-in-town"></a>

## `enemy-buildings-in-town`

- Kind: `command`
- Detail: Fact - Buildings, Defense

Syntax: `(enemy-buildings-in-town)`

Returns true if there are sighted enemy buildings less than snMaximumTownSize tiles of the computer player's home TC. For this fact, sn-maximum-town-size is a circle of sn-maximum-town-size tiles in a diagonal direction and sn-maximum-town-size * sqrt(2) tiles in any straight direction (it appears a perfect circle on the map rather than a square as for the building commands). Works with all buildings (including walls). Updates every few AOC seconds.

[AIRef](https://airef.github.io/commands/commands-details.html#enemy-buildings-in-town)

Completion insert text:

```text
(enemy-buildings-in-town)
```

<a id="symbol-enemy-captured-relics"></a>

## `enemy-captured-relics`

- Kind: `command`
- Detail: Fact - Game Info

Syntax: `(enemy-captured-relics)`

Checks if the enemy team has captured all relics. When this happens, tactical AI automatically starts targeting monasteries and monks. Use this fact to intensify attacks and combine it with the attack-now action to force attacks. You can also add snSpecialAttackType1 to 1, snSpecialAttackInfluence1 > 0, and up-set-offense-priority for monasteries to a high number to increase the likelyhood to target monasteries.

[AIRef](https://airef.github.io/commands/commands-details.html#enemy-captured-relics)

Completion insert text:

```text
(enemy-captured-relics)
```

<a id="symbol-escrow-amount"></a>

## `escrow-amount`

- Kind: `command`
- Detail: Fact - Economy

Syntax: `(escrow-amount <Resource> <compareOp> <Value>)`

Checks a computer player's escrow stockpile amount for a given resource type. AIs can store each of their four resource stockpiles in one of two stockpile types: normal and escrow. Resources in the normal stockpiles are free for the AI to use, while resources in the escrow stockpiles can only be used with up-build, up-train, or up-research when the EscrowGoalId parameter in these commands is a goal set to the value "with-escrow". The user interface shows the sum of both the normal and escrow stockpile resources added together for each resource. By default, all resources are stored in the normal stockpiles. However, set-escrow-percentage and up-modify-escrow can be used to store some or all of the AI's resources in the escrow stockpiles instead. Resources in the escrow stockpiles can transferred back into the normal stockpiles by using release-escrow, up-release-escrow, or up-modify-escrow. Resources are usually placed in escrow stockpiles in order to save up for expensive technologies or important buildings or units, so that it isn't spent on lower priority things.

[AIRef](https://airef.github.io/commands/commands-details.html#escrow-amount)

Completion insert text:

```text
(escrow-amount ${1:Resource} ${2:compareOp} ${3:Value})
```

<a id="symbol-event-detected"></a>

## `event-detected`

- Kind: `command`
- Detail: Fact - Scenarios

Syntax: `(event-detected <EventType> <EventId>)`

Checks if the given event has been detected. Scenario triggers that execute an AI Script Goal effect are the only events that AI scripts can detect. The event-detected fact stays true until the event is explicitly disabled by the acknowledge-event action. This command, along with acknowledge-event, is used to detect an AI Script Goal effect from a scenario trigger, often with the intention of changing the AI behavior after the scenario trigger has fired. The scenario designer chooses an AI Trigger number for the AI Script Goal effect in the scenario editor. Then, the event-detected command in the AI script will detect when this trigger effect happens. The event-detected command will remain true after the AI Script Goal trigger effect fires, so acknowledge-event is used to reset the event-detected flag so that event-detected will no longer be true, similar to how the disable-timer command clears a timer that has triggered or how the acknowledge-taunt command accepts the taunt message. Trigger events are essentially the inverse of signals. To allow an AI script to send a signal which the AI Signal trigger condition can detect, use set-signal.

[AIRef](https://airef.github.io/commands/commands-details.html#event-detected)

Completion insert text:

```text
(event-detected ${1:EventType} ${2:EventId})
```

<a id="symbol-false"></a>

## `false`

- Kind: `command`
- Detail: Fact - Other

Syntax: `(false)`

A Fact that is always false. A rule with this fact will never execute its actions. This command was likely added to the AI engine by Ensemble Studios early on to test logical operators, such as "or," "and," or "not." This command's usefulness is pretty limited, but scripters might be able to use it creatively. If you want to stop a rule from running, a more effective strategy is to comment out each of the lines in the rule with a semi-colon (;).

[AIRef](https://airef.github.io/commands/commands-details.html#false)

Completion insert text:

```text
(false)
```

<a id="symbol-fe-break-point"></a>

## `fe-break-point`

- Kind: `command`
- Detail: Action - Debugging

Syntax: `(fe-break-point <Value> <compareOp> <Value> <OptionGoalId>)`

DE only. Add a break point to force the AI debugger interface to display if the break point conditions are met. The break point conditions are met if the comparison between the first and second values is true and either the last parameter is -1 or the goal specified in the last parameter is set to a value >= 1. The debugger shows you various information about the AI's current state, such as the current value of each goal and the object IDs stored in the local and remote lists. Once the debugger is opened, you'll be able to step through your rules. To enable the debugger you must first enable AI debugging for the game in the Steam launch options. Before launching the game, go to Steam => Right click game => Properties => in bottom box type AIDEBUGGING.

[AIRef](https://airef.github.io/commands/commands-details.html#fe-break-point)

Completion insert text:

```text
(fe-break-point ${1:Value} ${2:compareOp} ${3:Value} ${4:OptionGoalId})
```

<a id="symbol-fe-cc-effect-amount"></a>

## `fe-cc-effect-amount`

- Kind: `command`
- Detail: Action - Cheat, Scenarios

Syntax: `(fe-cc-effect-amount <EffectId> <ItemId> <AttrId> <Value>)`

DE only. Apply a research-style effect with an integer value for the AI player. This is considered a cheat command, but cheats do not have to be enabled. When modifying objects, you may need to target ALL hidden variations, one-by-one, as well. Please consider in-game object upgrades, so that an upgrade will not push a unit's max hitpoints over 32768 or the object will be destroyed. If you disable an object with this command, in-game techs/ages (unless disabled) may re-enable them. The civ tech tree may also override changes. This command can only use integer values. If you need to make an effect with a decimal value, use fe-cc-effect-percent.

[AIRef](https://airef.github.io/commands/commands-details.html#fe-cc-effect-amount)

Completion insert text:

```text
(fe-cc-effect-amount ${1:EffectId} ${2:ItemId} ${3:AttrId} ${4:Value})
```

<a id="symbol-fe-cc-effect-percent"></a>

## `fe-cc-effect-percent`

- Kind: `command`
- Detail: Action - Cheat, Scenarios

Syntax: `(fe-cc-effect-percent <EffectId> <ItemId> <AttrId> <Percent>)`

DE only. Apply a research-style effect as a percentage for the AI player. This command is identical to fe-cc-effect-amount, except the value is divided by 100 to provide decimal precision. This is considered a cheat command, but cheats do not have to be enabled. When modifying objects, you may need to target ALL hidden variations, one-by-one, as well. Please consider in-game object upgrades, so that an upgrade will not push a unit's max hitpoints over 32768 or the object will be destroyed. If you disable an object with this command, in-game techs/ages (unless disabled) may re-enable them. The civ tech tree may also override changes. This command can only use integer values.

[AIRef](https://airef.github.io/commands/commands-details.html#fe-cc-effect-percent)

Completion insert text:

```text
(fe-cc-effect-percent ${1:EffectId} ${2:ItemId} ${3:AttrId} ${4:Percent})
```

<a id="symbol-fe-exclude-from-attack-group"></a>

## `fe-exclude-from-attack-group`

- Kind: `command`
- Detail: Action - Attack

Syntax: `(fe-exclude-from-attack-group <typeOp> <UnitId>)`

DE only. Removes the given unit type from attack-now and attack-groups attacks. To reset the list of units excluded from attack-now and attack-group attacks, use fe-reset-attack-group-exclusion-list.

[AIRef](https://airef.github.io/commands/commands-details.html#fe-exclude-from-attack-group)

Completion insert text:

```text
(fe-exclude-from-attack-group ${1:typeOp} ${2:UnitId})
```

<a id="symbol-fe-filter-garrisoned"></a>

## `fe-filter-garrisoned`

- Kind: `command`
- Detail: Action - DUC

Syntax: `(fe-filter-garrisoned <typeOp> <Option>)`

DE only. Filters whether garrisoned and/or ungarrisoned units are found in DUC searches. Set to 0 before a DUC search to exclude objects that are garrisoned in a building, ram, or transport ship from future DUC searches, but allow units that aren't garrisoned to be found (the default setting). Set to 1 before a DUC search to allow both garrisoned and ungarrisoned units to be found. Set to 2 before a DUC search to exclude ungarrisoned units. Using up-full-reset-search or up-reset-filters will reset the filter back to its default setting (0).

[AIRef](https://airef.github.io/commands/commands-details.html#fe-filter-garrisoned)

Completion insert text:

```text
(fe-filter-garrisoned ${1:typeOp} ${2:Option})
```

<a id="symbol-fe-idle-pasture-count"></a>

## `fe-idle-pasture-count`

- Kind: `command`
- Detail: Fact - Counting, Economy

Syntax: `(fe-idle-pasture-count <compareOp> <Value>)`

DE only. Checks the number of pastures with zero herders gathering from it. It can be used before a new pasture is built to make sure it is needed. To check the number of idle farms, use idle-farm-count.

[AIRef](https://airef.github.io/commands/commands-details.html#fe-idle-pasture-count)

Completion insert text:

```text
(fe-idle-pasture-count ${1:compareOp} ${2:Value})
```

<a id="symbol-fe-reset-attack-group-exclusion-list"></a>

## `fe-reset-attack-group-exclusion-list`

- Kind: `command`
- Detail: Action - Attack

Syntax: `(fe-reset-attack-group-exclusion-list)`

DE only. Clears the list of unit types excluded from attack-now and attack-groups attacks. To add unit types that should be excluded from attack-now and attack-group attacks, use fe-exclude-from-attack-group.

[AIRef](https://airef.github.io/commands/commands-details.html#fe-reset-attack-group-exclusion-list)

Completion insert text:

```text
(fe-reset-attack-group-exclusion-list)
```

<a id="symbol-fe-set-signal"></a>

## `fe-set-signal`

- Kind: `command`
- Detail: Action - Scenarios

Syntax: `(fe-set-signal <typeOp> <SignalId> <typeOp> <Value>)`

DE only. Set the value of a multiplayer scenario trigger signal. This action only works with a "Multiplayer AI Signal" trigger condition in a single and multiplayer scenario. For the "AI Signal" condition use up-set-signal (only works in a single player scenario).

[AIRef](https://airef.github.io/commands/commands-details.html#fe-set-signal)

Completion insert text:

```text
(fe-set-signal ${1:typeOp} ${2:SignalId} ${3:typeOp} ${4:Value})
```

<a id="symbol-fe-sub-game-type"></a>

## `fe-sub-game-type`

- Kind: `command`
- Detail: Fact - Game Info

Syntax: `(fe-sub-game-type <compareOp> <SubGameType>)`

DE only. Checks if game matches the specified sub-game type. There are four sub-game types: sub-game-type-empire-wars, sub-game-type-sudden-death, sub-game-type-regicide, and sub-game-type-king-of-the-hill. Sub-games are loaded whenever the checkbox for these sub-game modes are checked in the lobby screen, rather than being selected from the game type dropdown. Multiple sub-games modes can be true at once in a game.

[AIRef](https://airef.github.io/commands/commands-details.html#fe-sub-game-type)

Completion insert text:

```text
(fe-sub-game-type ${1:compareOp} ${2:SubGameType})
```

<a id="symbol-food-amount"></a>

## `food-amount`

- Kind: `command`
- Detail: Fact - Economy

Syntax: `(food-amount <compareOp> <Value>)`

Checks a computer player's food amount. This amount includes escrowed food.

[AIRef](https://airef.github.io/commands/commands-details.html#food-amount)

Completion insert text:

```text
(food-amount ${1:compareOp} ${2:Value})
```

<a id="symbol-game-time"></a>

## `game-time`

- Kind: `command`
- Detail: Fact - Game Info

Syntax: `(game-time <compareOp> <Value>)`

Checks the game time, the amount of time elapsed since the start of the game, measured in game seconds. The fact can be used to make rules time-specific. For example, the computer can become more aggressive after 15 minutes of game time. game-time measures the game time in game seconds. The current game time can be found by using F11. Unless the game is being played on Slow speed (1.0 speed), the game time moves faster that real time. Casual speed (Normal speed in single player games in UP) is 1.5 times faster than real time, Normal speed (Normal speed in multiplayer games in UP) is 1.7 times faster than real time, and Fast speed is 2.0 times faster than real time. Even faster speeds are possible with DE launch options (see this video or with the speedhack option in Cheat Engine, though AI behavior can diminish at faster game speeds.

[AIRef](https://airef.github.io/commands/commands-details.html#game-time)

Completion insert text:

```text
(game-time ${1:compareOp} ${2:Value})
```

<a id="symbol-game-type"></a>

## `game-type`

- Kind: `command`
- Detail: Fact - Game Info

Syntax: `(game-type <compareOp> <GameType>)`

Checks the game type. Game types include settings like random-map, regicide, king-of-the-hill, or turbo-random-map. See pGameType for the list of game types. Game types are not defined, so you must defconst them before using them.

[AIRef](https://airef.github.io/commands/commands-details.html#game-type)

Completion insert text:

```text
(game-type ${1:compareOp} ${2:GameType})
```

<a id="symbol-gate-count"></a>

## `gate-count`

- Kind: `command`
- Detail: Fact - Buildings, Counting

Syntax: `(gate-count <Perimeter> <compareOp> <Value>)`

Checks for the number of gates that are either being built or are completed at the given perimeter. Perimeter 1 is usually between 10 and 20 tiles from the starting Town Center. Perimeter 2 is usually between 18 and 30 tiles from the starting Town Center. This command likely only counts stone gates, but it is possible that you can count only palisade gates instead by setting snGateTypeForWall to 1 before using gate-count.

[AIRef](https://airef.github.io/commands/commands-details.html#gate-count)

Completion insert text:

```text
(gate-count ${1:Perimeter} ${2:compareOp} ${3:Value})
```

<a id="symbol-generate-random-number"></a>

## `generate-random-number`

- Kind: `command`
- Detail: Action - Other

Syntax: `(generate-random-number <Value>)`

Generates a player-specific integer random number within given range (1 to pValue). The number is stored internally and its value can be tested with random-number. Subsequent executions of this action generate new random numbers that replace existing ones. If you want to store the random number in a goal, use up-get-fact. Unfortunately, the numbers generated by this command are not truly random, and restarting the game can sometimes result in the same random numbers being generated. It's best to avoid generating random numbers in the first few seconds of the game since the results can be less reliable. If you want to generate a number that is more random, consider using up-get-precise-time to get a timestamp into a goal (such as gl-random-number) and then use (up-modify-goal gl-random-number c:mod X) where X is the range of values you want your random number to use. The mod operator (c:mod) divides the goal by the given value (X) and stores the remainder left over from the division. Thus, if X is 100, gl-random-number will range somewhere between 0 and 99. In addition to using up-get-precise-time, you can also do the same c:mod calculation with another number that is fairly random, like a player's score. Unfortunately, these alternative methods can only generate one random number per pass because game state information like up-get-precise-time and player scores are only updated between passes.

[AIRef](https://airef.github.io/commands/commands-details.html#generate-random-number)

Completion insert text:

```text
(generate-random-number ${1:Value})
```

<a id="symbol-goal"></a>

## `goal`

- Kind: `command`
- Detail: Fact - Goals

Syntax: `(goal <GoalId> <Value>)`

Checks the current value of the given goal to see if it is equal to the given value. To do any other comparisons, including comparisons with goal or strategic number values, use up-compare-goal. While their purpose may be unclear based on their name, goals are variables which can store an integer value which can be checked with this command or with up-compare-goal. Each goal is given an ID, and AIs have 16000 goals available (only 512 in UP and only 40 in AoC) that they can use to store different values, and they all store the value -1 at the beginning of the game. Goals are one of the most important concepts of AI scripting, so it's good to learn how to use them. In programming speak, goals are a 16000-length one-indexed 32-bit integer array, pre-initialized to -1, and a GoalId refers to a particular index of that array. The goal command checks if the value of the given GoalId is equal to the given value. New goals or variables cannot be defined, only constants (called defconsts by the AI engine), so AI scripters are limited to these 16000 goals, though unused strategic numbers can also be used like goals in a pinch. If the paragraph above makes absolutely no sense to you, you can imagine goals like a bank which holds 16000 bank accounts, numbered with IDs from 1 to 16000. These accounts can hold whole amounts (no cents or decimal amounts of money), and they can store either positive or negative amounts of money. These bank accounts are restricted to holding between -2,147,483,648 and 2,147,483,647 dollars, and they all start with -$1 (negative 1 dollars) stored inside them until they are used by a customer (the AI scripter). The set-goal and up-modify-goal commands can modify how much money is stored in a particular account. Following this bank metaphor, the goal command checks if the given bank account number holds the given amount of money. For example, (goal 5 13) checks if goal ID #5 holds the value 13 (i.e. bank account #5 holds $13), and (goal 415 -3274) checks if goal ID #415 holds the value -3,274 (i.e. bank account #415 holds -$3,274). You can also use up-compare-goal" to check the current value of a goal ID in a more powerful manner, such as checking if the goal stores greater or less than the given value. It is pretty common to use a defconst to refer to a goal ID number to make the AI more readable. See the second example below on what this looks like." cGoal.commandParameters = [ { nameLink: pGoalId.getLink(), name: "GoalId", type: "Const", dir: "in", range: "A valid GoalId, from 1 to 16000.", note: "The goal to compare the Value to." }, { nameLink: pValue.getLink(), name: "Value", type: "Const", dir: "in", range: "-2,147,483,648 to 2,147,483,647.", note: "A number for comparison." } ]

[AIRef](https://airef.github.io/commands/commands-details.html#goal)

Completion insert text:

```text
(goal ${1:GoalId} ${2:Value})
```

<a id="symbol-gold-amount"></a>

## `gold-amount`

- Kind: `command`
- Detail: Fact - Economy

Syntax: `(gold-amount <compareOp> <Value>)`

Checks a computer player's gold amount. This amount includes escrowed gold.

[AIRef](https://airef.github.io/commands/commands-details.html#gold-amount)

Completion insert text:

```text
(gold-amount ${1:compareOp} ${2:Value})
```

<a id="symbol-hold-koh-ruin"></a>

## `hold-koh-ruin`

- Kind: `command`
- Detail: Fact - Game Info, Own Player Info

Syntax: `(hold-koh-ruin)`

Undocumented command that checks whether or not it (or its team) currently holds the monument in King of the Hill games. Koh stands for King of the Kill.

[AIRef](https://airef.github.io/commands/commands-details.html#hold-koh-ruin)

Completion insert text:

```text
(hold-koh-ruin)
```

<a id="symbol-hold-relics"></a>

## `hold-relics`

- Kind: `command`
- Detail: Fact - Game Info, Own Player Info

Syntax: `(hold-relics)`

Undocumented command that checks whether or not it (or its team) has all of the relics.

[AIRef](https://airef.github.io/commands/commands-details.html#hold-relics)

Completion insert text:

```text
(hold-relics)
```

<a id="symbol-housing-headroom"></a>

## `housing-headroom`

- Kind: `command`
- Detail: Fact - Own Player Info

Syntax: `(housing-headroom <compareOp> <Value>)`

Checks computer player's housing headroom. Housing headroom is the difference between current housing capacity and trained unit capacity. For example, a computer player has a Town Center (capacity 5), a House (capacity 5) and 6 villagers. In this case, housing headroom is 4.

[AIRef](https://airef.github.io/commands/commands-details.html#housing-headroom)

Completion insert text:

```text
(housing-headroom ${1:compareOp} ${2:Value})
```

<a id="symbol-idle-farm-count"></a>

## `idle-farm-count`

- Kind: `command`
- Detail: Fact - Counting, Economy

Syntax: `(idle-farm-count <compareOp> <Value>)`

Checks a computer player's idle farm count - the number of farms with no farmers assigned to gather from it. It can be used before a new farm is built to make sure it is needed. To check the number of idle pastures, use fe-idle-pasture-count.

[AIRef](https://airef.github.io/commands/commands-details.html#idle-farm-count)

Completion insert text:

```text
(idle-farm-count ${1:compareOp} ${2:Value})
```

<a id="symbol-include"></a>

## `include`

- Kind: `command`
- Detail: Other - Other

Syntax: `(include <String>)`

DE only. Loads an XS file. For more info on XS scripting, see this exhaustive guide: link. Unlike the load command, the filetype (.xs) must be included in the include command. The filepath must be inside quotes. By default, .xs files must be placed in the game's xs folder, located at: "C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\resources\_common\xs", but you can also load .xs files with a relative filepath name, using "../" to go up a filepath level from the xs folder and then follow the rest of the filepath to get to your .xs file. For example, to include a .xs file stored in your "My AI" folder within the default AI installation directory, you can use (include "../ai/My AI/Example XS File.xs"). Once you have included your .xs file, you can use xs-script-call to call any function from that file that doesn't have any parameters. See the xs-script-call page for more details. Unfortunately, as of this writing, including XS scripts seems to be bugged because it seems to still use the xs folder within the installation directory as the default folder, rather than the xs folder inside the mods folder, making it impossible to specify the correct directory. Additionally, if there are any load or load-random commands that appear later in your AI script, any include commands will not work. In summary, place all load and load-random commands at the top of your AI, and then add your include commands. The include command can be inserted anywhere between rules. Include commands cannot be included inside a rule. Once an .xs file is included, all .xs code that isn't within a function will start running immediately, and any rules within the .xs file will start running periodically if enabled. To call functions from the AI script, use xs-script-call.

[AIRef](https://airef.github.io/commands/commands-details.html#include)

Completion insert text:

```text
(include ${1:String})
```

<a id="symbol-load"></a>

## `load`

- Kind: `command`
- Detail: Other - Other

Syntax: `(load <String>)`

Loads the code from a separate .per AI file with the given filename. Notice that the filename does not have path or an extension. The script interpreter automatically adds a path and an extension. By default, the load command will look for a file with a matching filename within the main AI directory. If you want to load a .per file from a folder within the AI directory, enter the name of the folder, followed by a slash, and then followed by the filename without a file extension. Here are the default AI directories per game version:CD Version/UP: C:\Program Files (x86)\Microsoft Games\Age of Empires II\AIWK: C:\Program Files (x86)\Microsoft Games\Age of Empires II\Games\WololoKingdoms\Script.AiDE: C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\resources\_common\aiDE Mods: C:\Users\%USERNAME%\Games\Age of Empires 2 DE\[Your Unique Game ID]\mods\local\[The Mod's Name]\resources\_common\ai (if you want to edit a mod you downloaded, use the subscribed folder instead of the local folder) Using the load command makes it easier to organize and re-use parts of your scripts in new ways. Loaded files are in every aspect the same as original script files, so any script file can be loaded by any other script file. The load command can be inserted anywhere between rules. Load commands cannot be used inside a rule, so if you want to load your AI code according to a certain condition, use #load-if-defined or #load-if-not-defined. If you want to randomly select a file to load from a list of files, use load-random. The AI Expert system that AoE2 uses loads all AI files at runtime, so you cannot tell the AI to load a file after a game has started. It is important to mention that the load command executes immediately. This means that when a load command is encountered, parsing of the current file is suspended until the load command finishes. At that point parsing resumes, starting with a rule immediately following the load command. Essentially, you can think of the load command as copying the code from the external .per file and pasting it into the original .per file that has the load command. Or, more accurately, if you have programming experience, you can think of the load command as a function call. Load commands can be nested (a script that loads another script) up to 10 levels deep. Loading multiple script files from a top-level script file makes computer players' knowledge modular. This approach has a benefit only if the script files loaded do not have overlapping areas of expertise.

[AIRef](https://airef.github.io/commands/commands-details.html#load)

Completion insert text:

```text
(load ${1:String})
```

<a id="symbol-load-random"></a>

## `load-random`

- Kind: `command`
- Detail: Other - Other

Syntax: `(load-random <Value> <String>)`

Randomly loads the code from one AI file out of a list of files. This command provides an option of randomizing AI strategies on the level higher than the rule level. Notice that the filenames do not have path or an extension. The script interpreter automatically adds a path and an extension. By default, the load-random command will look for a file with a matching filename within the main AI directory. If you want to load a .per file from a folder within the AI directory, enter the name of the folder, followed by a slash, and then followed by the filename without a file extension. Here are the default AI directories per game version:CD Version/UP: C:\Program Files (x86)\Microsoft Games\Age of Empires II\AIWK: C:\Program Files (x86)\Microsoft Games\Age of Empires II\Games\WololoKingdoms\Script.AiDE: C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\resources\_common\aiDE Mods: C:\Users\%USERNAME%\Games\Age of Empires 2 DE\[Your Unique Game ID]\mods\local\[The Mod's Name]\resources\_common\ai (if you want to edit a mod you downloaded, use the subscribed folder instead of the local folder) Using the load-random command makes it easier to organize and re-use parts of your scripts in new ways and to provide variation between games. Loaded files are in every aspect the same as original script files, so any script file can be loaded by any other script file. The load-random command can be inserted anywhere between rules. load-random commands cannot be used inside a rule, so if you want to load your AI code according to a certain condition, use #load-if-defined or #load-if-not-defined. Each file within the load-random is given a percent chance from 1 to 100 for that file to be selected. If a percentage is not provided, this file is regarded as the default file which will be picked if the other files with percentages are not chosen. Only one of the possible files within the load-random command will be selected. If the percentages don't add up to 100 and there is no default file given, then there is a chance that the load-random command will not load any files. If only the default file is given, that file will load 100% of the time, but this version of the load-random command is slower than the load command, so specifying only a default file is not recommended. Userpatch added some additional options for load-random. Instead of a literal numeric percent, you can use a + followed by a defconst which specifies the percent, without spaces. This allows the scripter to randomly load files according to defconsts. You can also use a + to load files with 100% probability. In either case, the + is ignored by the CD version (version AoC) AI parser, so load-random commands using a + will ensure that thes files are only loaded if the player is using Userpatch. As of this writing, the options in this paragraph are bugged in DE. The AI Expert system that AoE2 uses loads all AI files at runtime, so you cannot tell the AI to load a file after a game has started. Once a load-random command has determined which file to randomly load, this selected file will be used throughout the rest of the game. When a load-random command is encountered, parsing of the current file is suspended until the load-random command finishes. At that point parsing resumes, starting with a rule immediately following the load-random command. Essentially, you can think of the load-random command as copying the code from the external .per file and pasting it into the original .per file that has the load-random command. Or, more accurately, if you have programming experience, you can think of the load-random command as a function call. Load commands can be nested (a script that loads another script) up to 10 levels deep. Loading multiple script files from a top-level script file makes computer players' knowledge modular. This approach has a benefit only if the script files loaded do not have overlapping areas of expertise.

[AIRef](https://airef.github.io/commands/commands-details.html#load-random)

Completion insert text:

```text
(load-random ${1:Value} ${2:String})
```

<a id="symbol-log"></a>

## `log`

- Kind: `command`
- Detail: Action - Debugging

Syntax: `(log <String>)`

Writes the given string to a log file. Used purely for testing purposes. Works only if logging is enabled. Logging is disabled in AoC (the old CD version of the game) and Userpatch. Use up-log-data instead. However, logging can be enabled in DE. To do this, you need to launch the game with the parameters LOGSYSTEMS=AIScript and VERBOSELOGGING (case sensitive). To do this with the Steam version, open your Steam games library with the Steam client, right click on Age of Empires II: Definitive Edition in the left sidebar that lists the games you own, and click Properties. In the Properties window, under the General tab, type the parameters above separated by spaces. Then, when you launch the game these parameters will be active. The log produced in DE will be found in the Steam user folder, usually something like "C:\Users\[user ID]\Games\Age of Empires 2 DE\logs" but note that this log isn't just used by the AI (it would be best to log something identifying the AI log at the start of the game), some of these logs with VERBOSELOGGING can get quite large so it might be a good idea to periodically clean out the folder.

[AIRef](https://airef.github.io/commands/commands-details.html#log)

Completion insert text:

```text
(log ${1:String})
```

<a id="symbol-log-trace"></a>

## `log-trace`

- Kind: `command`
- Detail: Action - Debugging

Syntax: `(log-trace <Value>)`

Writes the given value to a log file. Used purely for testing to check when a rule gets executed. Works only if logging is enabled (which it isn't). Use up-log-data instead. You can also use log to log a text string if you are scripting for DE.

[AIRef](https://airef.github.io/commands/commands-details.html#log-trace)

Completion insert text:

```text
(log-trace ${1:Value})
```

<a id="symbol-map-size"></a>

## `map-size`

- Kind: `command`
- Detail: Fact - Game Info

Syntax: `(map-size <MapSize>)`

Checks the map size. The map sizes can be tiny, small, medium, normal, large, giant, or ludikris (DE only). To get the actual dimensions of the map, you can use up-get-point with position-map-size, which will store the coordinates of the rightmost point on the map.

[AIRef](https://airef.github.io/commands/commands-details.html#map-size)

Completion insert text:

```text
(map-size ${1:MapSize})
```

<a id="symbol-map-type"></a>

## `map-type`

- Kind: `command`
- Detail: Fact - Game Info

Syntax: `(map-type <MapType>)`

Checks the map type. The map type is the map's name. See pMapType for a complete list of maps.For custom random maps, the map type is "custom_map" (yes, with the underscore). The exception is if the custom random map script uses ai_info_map_type. For example, if the random map script has ai_info_map_type ARABIA 0 0 0, then (map-type arabia) will be true instead of (map-type custom_map).

[AIRef](https://airef.github.io/commands/commands-details.html#map-type)

Completion insert text:

```text
(map-type ${1:MapType})
```

<a id="symbol-military-population"></a>

## `military-population`

- Kind: `command`
- Detail: Fact - Counting, Units

Syntax: `(military-population <compareOp> <Value>)`

Check's the player's military population. Military population includes any units that aren't civilian population (not villagers, trade units and fishing ships). It includes transport ships, but it does not count kings. To check for the military-population of other players, use players-military-population. This command counts Karambit Warriors as 1 population, rather than 0.5 population.

[AIRef](https://airef.github.io/commands/commands-details.html#military-population)

Completion insert text:

```text
(military-population ${1:compareOp} ${2:Value})
```

<a id="symbol-nand"></a>

## `nand`

- Kind: `command`
- Detail: Other - Other

Syntax: `(nand)`

Returns true if at least one of the facts following this command is false. The nand command is one of several logical operator commands available, along with and, nor, not, or, xnor, and xor. See the Logical Operator Commands guide for more information on how to use logical operator commands.

[AIRef](https://airef.github.io/commands/commands-details.html#nand)

Completion insert text:

```text
(nand)
```

<a id="symbol-nor"></a>

## `nor`

- Kind: `command`
- Detail: Other - Other

Syntax: `(nor)`

Returns true if both of the facts following this command are false. The nor command is one of several logical operator commands available, along with and, nand, not, or, xnor, and xor. See the Logical Operator Commands guide for more information on how to use logical operator commands.

[AIRef](https://airef.github.io/commands/commands-details.html#nor)

Completion insert text:

```text
(nor)
```

<a id="symbol-not"></a>

## `not`

- Kind: `command`
- Detail: Other - Other

Syntax: `(not)`

Returns true if the fact following this command is false. The not command is one of several logical operator commands available, along with and, nand, nor, or, xnor, and xor. See the Logical Operator Commands guide for more information on how to use logical operator commands.

[AIRef](https://airef.github.io/commands/commands-details.html#not)

Completion insert text:

```text
(not)
```

<a id="symbol-or"></a>

## `or`

- Kind: `command`
- Detail: Other - Other

Syntax: `(or)`

Returns true if at least one of the facts following this command is true. The or command is one of several logical operator commands available, along with and, nand, nor, not, xnor, and xor. See the Logical Operator Commands guide for more information on how to use logical operator commands.

[AIRef](https://airef.github.io/commands/commands-details.html#or)

Completion insert text:

```text
(or)
```

<a id="symbol-player-computer"></a>

## `player-computer`

- Kind: `command`
- Detail: Fact - Other Player Info

Syntax: `(player-computer <PlayerNumber>)`

Checks if the given player is a computer player. The fact allows "my-player-number", "focus-player", "target-player", and "any"/"every" wildcard parameters for pPlayerNumber. It also allows for scenario-player-# and lobby-player-#, where # is between 1 and 8. scenario-player-# refers to the player color (where red = scenario-player-2), and lobby-player-# refers to the player slot (where the lobby host or human player playing a single player campaign is always lobby-player-1).

[AIRef](https://airef.github.io/commands/commands-details.html#player-computer)

Completion insert text:

```text
(player-computer ${1:PlayerNumber})
```

<a id="symbol-player-human"></a>

## `player-human`

- Kind: `command`
- Detail: Fact - Other Player Info

Syntax: `(player-human <PlayerNumber>)`

Checks if the given player is a human player. The fact allows "my-player-number", "focus-player", "target-player", and "any"/"every" wildcard parameters for pPlayerNumber. It also allows for scenario-player-# and lobby-player-#, where # is between 1 and 8. scenario-player-# refers to the player color (where red = scenario-player-2), and lobby-player-# refers to the player slot (where the lobby host or human player playing a single player campaign is always lobby-player-1).

[AIRef](https://airef.github.io/commands/commands-details.html#player-human)

Completion insert text:

```text
(player-human ${1:PlayerNumber})
```

<a id="symbol-player-in-game"></a>

## `player-in-game`

- Kind: `command`
- Detail: Fact - Other Player Info

Syntax: `(player-in-game <PlayerNumber>)`

Checks if the given player is a valid player and still playing (hasn't resigned or been defeated). The fact allows "my-player-number", "focus-player", "target-player", and "any"/"every" wildcard parameters for pPlayerNumber. It also allows for scenario-player-# and lobby-player-#, where # is between 1 and 8. scenario-player-# refers to the player color (where red = scenario-player-2), and lobby-player-# refers to the player slot (where the lobby host or human player playing a single player campaign is always lobby-player-1).

[AIRef](https://airef.github.io/commands/commands-details.html#player-in-game)

Completion insert text:

```text
(player-in-game ${1:PlayerNumber})
```

<a id="symbol-player-number"></a>

## `player-number`

- Kind: `command`
- Detail: Fact - Other Player Info

Syntax: `(player-number <PlayerNumber>)`

Checks computer player's player number. The player number is the player's slot order, not the number associated with the AI's player color. Only a number between 1 to 8 can be used. It also allows for scenario-player-# and lobby-player-#, where # is between 1 and 8. scenario-player-# refers to the player color (where red = scenario-player-2), and lobby-player-# refers to the player slot (where the lobby host or human player playing a single player campaign is always lobby-player-1).

[AIRef](https://airef.github.io/commands/commands-details.html#player-number)

Completion insert text:

```text
(player-number ${1:PlayerNumber})
```

<a id="symbol-player-resigned"></a>

## `player-resigned`

- Kind: `command`
- Detail: Fact - Other Player Info

Syntax: `(player-resigned <PlayerNumber>)`

Checks if the given player has lost by resigning. Note that a player can lose without resigning, so this fact should not be used to check whether a player has lost a game. To check whether a player has lost a game (such as player 3) use:(not (player-in-game 3))The fact allows "focus-player", "target-player", and "any"/"every" wildcard parameters for pPlayerNumber. It also allows for scenario-player-# and lobby-player-#, where # is between 1 and 8. scenario-player-# refers to the player color (where red = scenario-player-2), and lobby-player-# refers to the player slot (where the lobby host or human player playing a single player campaign is always lobby-player-1).

[AIRef](https://airef.github.io/commands/commands-details.html#player-resigned)

Completion insert text:

```text
(player-resigned ${1:PlayerNumber})
```

<a id="symbol-player-valid"></a>

## `player-valid`

- Kind: `command`
- Detail: Fact - Other Player Info

Syntax: `(player-valid <PlayerNumber>)`

Checks if the given player is a valid player, meaning the player slot was used during the game. In games with more than 2 players, players that lost before the game is over are still considered to be valid players. This is because although the player is not in the game, their units/buildings can still be in the game. To check whether the given player is still in the game use the player-in-game fact. The fact allows "focus-player", "target-player", and "any"/"every" wildcard parameters for pPlayerNumber. It also allows for scenario-player-# and lobby-player-#, where # is between 1 and 8. scenario-player-# refers to the player color (where red = scenario-player-2), and lobby-player-# refers to the player slot (where the lobby host or human player playing a single player campaign is always lobby-player-1).

[AIRef](https://airef.github.io/commands/commands-details.html#player-valid)

Completion insert text:

```text
(player-valid ${1:PlayerNumber})
```

<a id="symbol-players-building-count"></a>

## `players-building-count`

- Kind: `command`
- Detail: Fact - Buildings, Cheat, Counting, Other Player Info

Syntax: `(players-building-count <PlayerNumber> <compareOp> <Value>)`

A cheating version of players-building-count. This command works even if cheats are disabled. For use in scenarios only. The fact checks the given player's building count. Both existing buildings and buildings under construction are included regardless of whether they have been seen - fog is ignored. Unlike building-count, buildings that existed from the start of the game, such as the starting town center, are included. Also, farms are included, but walls and gates are not included. The Fact allows "focus-player", "target-player", and "any"/"every" wildcard parameters for pPlayerNumber. It also allows for scenario-player-# and lobby-player-#, where # is between 1 and 8. scenario-player-# refers to the player color (where red = scenario-player-2), and lobby-player-# refers to the player slot (where the lobby host or a human player playing a single player campaign is always lobby-player-1).

[AIRef](https://airef.github.io/commands/commands-details.html#players-building-count)

Completion insert text:

```text
(players-building-count ${1:PlayerNumber} ${2:compareOp} ${3:Value})
```

<a id="symbol-players-building-type-count"></a>

## `players-building-type-count`

- Kind: `command`
- Detail: Fact - Buildings, Cheat, Counting, Other Player Info

Syntax: `(players-building-type-count <PlayerNumber> <BuildingId> <compareOp> <Value>)`

A cheating version of players-building-type-count. This command works even if cheats are disabled. For use in scenarios only. This fact checks the given player's building count for the given building. Both existing buildings and buildings under construction of the given type are included regardless of whether they have been seen - fog is ignored. The Fact allows "focus-player", "target-player", "any"/"every" wildcard parameters for pPlayerNumber. It also allows for scenario-player-# and lobby-player-#, where # is between 1 and 8. scenario-player-# refers to the player color (where red = scenario-player-2), and lobby-player-# refers to the player slot (where the lobby host or human player playing a single player campaign is always lobby-player-1). It also allows the use of building line wildcard parameters for pBuildingId. The only wildcard parameter available is watch-tower-line. However, it is better to use watch-tower instead of watch-tower-line, even after Guard Tower or Keep upgrades due to some bugs with watch-tower-line. Simply using (cc-players-building-type-count any-enemy watch-tower > 0) will work regardless of tower upgrades. There are four ways you can specify the building "type":Building Name: the name of an individual building, such as house, watch-tower, or town-center.Building Id: the numerical ID assigned to each building, such as 12 (the barracks) or 70 (the house). See the ID column in the Objects Table for a list.Building Line: the building line for the building. The only option here is watch-tower-line, and avoid using it as there are various bugs with it. Simply use watch-tower instead.Building Class: the class of a building, such as building-class, tower-class, or farm-class. Classes group several building types together into a single category. Using a building class will count all buildings of this class. See the Class column in the Objects Table to see each building's class. Classes don't work for enemy players with players-building-type-count, but they do work with cc-players-building-type-count.

[AIRef](https://airef.github.io/commands/commands-details.html#players-building-type-count)

Completion insert text:

```text
(players-building-type-count ${1:PlayerNumber} ${2:BuildingId} ${3:compareOp} ${4:Value})
```

<a id="symbol-players-civ"></a>

## `players-civ`

- Kind: `command`
- Detail: Fact - Other Player Info

Syntax: `(players-civ <PlayerNumber> <Civ>)`

Checks the given player's civilization. Note that the civilization names used with this command for pre-DE civs are usually different than the civ's display name. They are like the pLoadIfSymbol civ names where they often use the adjective form of the civ name, not the plural name. See pCiv for a list of correct civ names to use with this command. The fact allows "focus-player", "target-player", and "any"/"every" wildcard parameters for pPlayerNumber. It also allows for scenario-player-# and lobby-player-#, where # is between 1 and 8. scenario-player-# refers to the player color (where red = scenario-player-2), and lobby-player-# refers to the player slot (where the lobby host or human player playing a single player campaign is always lobby-player-1). You can use "my-civ" for the Civ parameter, which will automatically detect the civilization the AI is playing as.

[AIRef](https://airef.github.io/commands/commands-details.html#players-civ)

Completion insert text:

```text
(players-civ ${1:PlayerNumber} ${2:Civ})
```

<a id="symbol-players-civilian-population"></a>

## `players-civilian-population`

- Kind: `command`
- Detail: Fact - Counting, Other Player Info, Units

Syntax: `(players-civilian-population <PlayerNumber> <compareOp> <Value>)`

Checks a given player's civilian population, which includes villagers, fishing ships, and trade units. This fact includes seen and unseen civilians for the given player. The CPSB notes that this is equivalent to a human player checking the timeline, which was possible in-game in AoE1, and it was probably also possible during AoE2 development when the CPSB was written, hence why this isn't regarded as a cc- cheating command. However, since this command includes unseen civilian units, some consider this command to be cheating when it's used to check enemy civilian population, but the AI scripting community permits this command in AI tournaments for historical reasons. The fact allows "focus-player", "target-player", and "any"/"every" wildcard parameters for pPlayerNumber. It also allows for scenario-player-# and lobby-player-#, where # is between 1 and 8. scenario-player-# refers to the player color (where red = scenario-player-2), and lobby-player-# refers to the player slot (where the lobby host or human player playing a single player campaign is always lobby-player-1).

[AIRef](https://airef.github.io/commands/commands-details.html#players-civilian-population)

Completion insert text:

```text
(players-civilian-population ${1:PlayerNumber} ${2:compareOp} ${3:Value})
```

<a id="symbol-players-current-age"></a>

## `players-current-age`

- Kind: `command`
- Detail: Fact - Other Player Info

Syntax: `(players-current-age <PlayerNumber> <compareOp> <Age>)`

Checks the given player's current age. The CPSB notes that this is equivalent to a human player checking the timeline, which was possible in-game in AoE1, and it was probably also possible during AoE2 development when the CPSB was written. Of course, this information is available to all players in-game, even without the timeline. The fact allows "focus-player", "target-player", and "any"/"every" wildcard parameters for pPlayerNumber. It also allows for scenario-player-# and lobby-player-#, where # is between 1 and 8. scenario-player-# refers to the player color (where red = scenario-player-2), and lobby-player-# refers to the player slot (where the lobby host or human player playing a single player campaign is always lobby-player-1).

[AIRef](https://airef.github.io/commands/commands-details.html#players-current-age)

Completion insert text:

```text
(players-current-age ${1:PlayerNumber} ${2:compareOp} ${3:Age})
```

<a id="symbol-players-current-age-time"></a>

## `players-current-age-time`

- Kind: `command`
- Detail: Fact - Other Player Info

Syntax: `(players-current-age-time <PlayerNumber> <compareOp> <Value>)`

Checks the given player's current age time -- time spent in the current age. The CPSB notes that this is equivalent to a human player checking the timeline, which was possible in-game in AoE1, and it was probably also possible during AoE2 development when the CPSB was written. Of course, this information could be calculated in-game even without using the timeline. The fact allows "focus-player", "target-player", and "any"/"every" wildcard parameters for pPlayerNumber. It also allows for scenario-player-# and lobby-player-#, where # is between 1 and 8. scenario-player-# refers to the player color (where red = scenario-player-2), and lobby-player-# refers to the player slot (where the lobby host or human player playing a single player campaign is always lobby-player-1).

[AIRef](https://airef.github.io/commands/commands-details.html#players-current-age-time)

Completion insert text:

```text
(players-current-age-time ${1:PlayerNumber} ${2:compareOp} ${3:Value})
```

<a id="symbol-players-military-population"></a>

## `players-military-population`

- Kind: `command`
- Detail: Fact - Counting, Other Player Info, Units

Syntax: `(players-military-population <PlayerNumber> <compareOp> <Value>)`

Checks the given player's military population, which includes all units except for villagers, fishing ships, trade units, and kings. This fact includes seen and unseen military units for the given player. This command counts Karambit Warriors as 1 population, rather than 0.5 population. The CPSB notes that this is equivalent to a human player checking the timeline, which was possible in-game in AoE1, and it was probably also possible during AoE2 development when the CPSB was written, hence why this isn't regarded as a cc- cheating command. However, since this command includes unseen military units, some consider this command to be cheating when it's used to check enemy military population, but the AI scripting community permits this command in AI tournaments for historical reasons. The fact allows "focus-player", "target-player", and "any"/"every" wildcard parameters for pPlayerNumber. It also allows for scenario-player-# and lobby-player-#, where # is between 1 and 8. scenario-player-# refers to the player color (where red = scenario-player-2), and lobby-player-# refers to the player slot (where the lobby host or human player playing a single player campaign is always lobby-player-1).

[AIRef](https://airef.github.io/commands/commands-details.html#players-military-population)

Completion insert text:

```text
(players-military-population ${1:PlayerNumber} ${2:compareOp} ${3:Value})
```

<a id="symbol-players-population"></a>

## `players-population`

- Kind: `command`
- Detail: Fact - Counting, Other Player Info

Syntax: `(players-population <PlayerNumber> <compareOp> <Value>)`

Checks the given player's population. This fact includes seen and unseen units for the given player. This command counts Karambit Warriors as 1 population, rather than 0.5 population. The CPSB notes that this is equivalent to a human player checking the timeline, which was possible in-game in AoE1, and it was probably also possible during AoE2 development when the CPSB was written, hence why this isn't regarded as a cc- cheating command. However, since this command includes unseen units, some consider this command to be cheating when it's used to check enemy population, but the AI scripting community permits this command in AI tournaments for historical reasons. When checking for the population of an enemy player, consider using players-unit-count. players-unit-count can overestimate enemy unit counts, but it doesn't count unseen units. The fact allows "focus-player", "target-player", and "any"/"every" wildcard parameters for pPlayerNumber. It also allows for scenario-player-# and lobby-player-#, where # is between 1 and 8. scenario-player-# refers to the player color (where red = scenario-player-2), and lobby-player-# refers to the player slot (where the lobby host or human player playing a single player campaign is always lobby-player-1).

[AIRef](https://airef.github.io/commands/commands-details.html#players-population)

Completion insert text:

```text
(players-population ${1:PlayerNumber} ${2:compareOp} ${3:Value})
```

<a id="symbol-players-score"></a>

## `players-score`

- Kind: `command`
- Detail: Fact - Other Player Info

Syntax: `(players-score <PlayerNumber> <compareOp> <Value>)`

Checks the given player's current score. The fact allows "focus-player", "target-player", and "any"/"every" wildcard parameters for pPlayerNumber. It also allows for scenario-player-# and lobby-player-#, where # is between 1 and 8. scenario-player-# refers to the player color (where red = scenario-player-2), and lobby-player-# refers to the player slot (where the lobby host or human player playing a single player campaign is always lobby-player-1).

[AIRef](https://airef.github.io/commands/commands-details.html#players-score)

Completion insert text:

```text
(players-score ${1:PlayerNumber} ${2:compareOp} ${3:Value})
```

<a id="symbol-players-stance"></a>

## `players-stance`

- Kind: `command`
- Detail: Fact - Diplomacy, Other Player Info

Syntax: `(players-stance <PlayerNumber> <PlayerStance>)`

Checks if the given player's diplomatic stance toward the computer player matches the give stance, either ally, neutral, or enemy. To check our stance toward another player, use stance-toward. The fact allows "focus-player", "target-player", and "any"/"every" wildcard parameters for pPlayerNumber. It also allows for scenario-player-# and lobby-player-#, where # is between 1 and 8. scenario-player-# refers to the player color (where red = scenario-player-2), and lobby-player-# refers to the player slot (where the lobby host or human player playing a single player campaign is always lobby-player-1).

[AIRef](https://airef.github.io/commands/commands-details.html#players-stance)

Completion insert text:

```text
(players-stance ${1:PlayerNumber} ${2:PlayerStance})
```

<a id="symbol-players-tribute"></a>

## `players-tribute`

- Kind: `command`
- Detail: Fact - Diplomacy, Other Player Info

Syntax: `(players-tribute <PlayerNumber> <Resource> <compareOp> <Value>)`

Checks the player's tribute given throughout the game. Only tribute for the given resource type is checked. The fact allows "focus-player", "target-player", and "any"/"every" wildcard parameters for pPlayerNumber. It also allows for scenario-player-# and lobby-player-#, where # is between 1 and 8. scenario-player-# refers to the player color (where red = scenario-player-2), and lobby-player-# refers to the player slot (where the lobby host or human player playing a single player campaign is always lobby-player-1).

[AIRef](https://airef.github.io/commands/commands-details.html#players-tribute)

Completion insert text:

```text
(players-tribute ${1:PlayerNumber} ${2:Resource} ${3:compareOp} ${4:Value})
```

<a id="symbol-players-unit-count"></a>

## `players-unit-count`

- Kind: `command`
- Detail: Fact - Cheat, Counting, Other Player Info, Units

Syntax: `(players-unit-count <PlayerNumber> <compareOp> <Value>)`

A cheating version of players-unit-count. This command works even if cheats are disabled. For use in scenarios only. This fact checks the given player's unit count. Only trained units are included and fog is ignored. The Fact allows "focus-player", "target-player", and "any"/"every" wildcard parameters for pPlayerNumber. It also allows for scenario-player-# and lobby-player-#, where # is between 1 and 8. scenario-player-# refers to the player color (where red = scenario-player-2), and lobby-player-# refers to the player slot (where the lobby host or human player playing a single player campaign is always lobby-player-1).

[AIRef](https://airef.github.io/commands/commands-details.html#players-unit-count)

Completion insert text:

```text
(players-unit-count ${1:PlayerNumber} ${2:compareOp} ${3:Value})
```

<a id="symbol-players-unit-type-count"></a>

## `players-unit-type-count`

- Kind: `command`
- Detail: Fact - Cheat, Counting, Other Player Info, Units

Syntax: `(players-unit-type-count <PlayerNumber> <UnitId> <compareOp> <Value>)`

A cheating version of players-unit-type-count. This command works even if cheats are disabled. For use in scenarios only, though most AI tournaments allows its use to see if particular Gaia objects are on the map at the beginning of the game, for custom map detection purposes. For example, some scripts will check to see if fish are on the map to detect if the map is a water map. This fact checks the given player's unit count. Only trained units of the given type are included and fog is ignored. The Fact allows "focus-player", "target-player", and "any"/"every" wildcard parameters for pPlayerNumber. It also allows for scenario-player-# and lobby-player-#, where # is between 1 and 8. scenario-player-# refers to the player color (where red = scenario-player-2), and lobby-player-# refers to the player slot (where the lobby host or human player playing a single player campaign is always lobby-player-1). Counting Gaia units (player number 0) is not considered cheating. There are four ways you can specify the unit "type":Unit Name: the name of an individual unit, such as villager, spearman, or monk.Unit Id: the numerical ID assigned to each unit, such as 4 (the archer) or 74 (militiaman). See the ID column in the Objects Table for a list.Unit Line: the unit line for the unit. This includes all units in a unit line. For example, archer-line includes archers, crossbowmen, and arbalests.Unit Class: the class of a unit, such as infantry-class, cavalry-archer-class, or monastery-class. Classes group several unit types together into a single category. Using a unit class will count all units of this class. See the Class column in the Objects Table to see each unit's class. Classes don't work for enemy players with players-unit-type-count, but they do work with cc-players-unit-type-count.

[AIRef](https://airef.github.io/commands/commands-details.html#players-unit-type-count)

Completion insert text:

```text
(players-unit-type-count ${1:PlayerNumber} ${2:UnitId} ${3:compareOp} ${4:Value})
```

<a id="symbol-population"></a>

## `population`

- Kind: `command`
- Detail: Fact - Counting, Own Player Info, Units

Syntax: `(population <compareOp> <Value>)`

Checks the computer player's population. To check for the population of other players, use players-population. This command counts Karambit Warriors as 1 population, rather than 0.5 population.

[AIRef](https://airef.github.io/commands/commands-details.html#population)

Completion insert text:

```text
(population ${1:compareOp} ${2:Value})
```

<a id="symbol-population-cap"></a>

## `population-cap`

- Kind: `command`
- Detail: Fact - Game Info

Syntax: `(population-cap <compareOp> <Value>)`

Checks the population cap setting.

[AIRef](https://airef.github.io/commands/commands-details.html#population-cap)

Completion insert text:

```text
(population-cap ${1:compareOp} ${2:Value})
```

<a id="symbol-population-headroom"></a>

## `population-headroom`

- Kind: `command`
- Detail: Fact - Counting, Own Player Info

Syntax: `(population-headroom <compareOp> <Value>)`

Checks the computer player's population headroom. Population headroom is the difference between the game's population cap and current housing capacity. For example, in a game with a population cap of 75, if the computer player has a town center (capacity 5) and a house (capacity 5), then the population headroom is 65.

[AIRef](https://airef.github.io/commands/commands-details.html#population-headroom)

Completion insert text:

```text
(population-headroom ${1:compareOp} ${2:Value})
```

<a id="symbol-random-number"></a>

## `random-number`

- Kind: `command`
- Detail: Fact - Other

Syntax: `(random-number <compareOp> <Value>)`

Checks the value of the most recent random number value generated by generate-random-number. To store the random number in a goal, use up-get-fact with random-number as the pFactId.

[AIRef](https://airef.github.io/commands/commands-details.html#random-number)

Completion insert text:

```text
(random-number ${1:compareOp} ${2:Value})
```

<a id="symbol-regicide-game"></a>

## `regicide-game`

- Kind: `command`
- Detail: Fact - Game Info

Syntax: `(regicide-game)`

Checks if the game is a regicide game. You can also enclose code in a #load-if-defined REGICIDE block if it should only run in a regicide game. In DE, to check if the Regicide secondary game mode is active you can use fe-sub-game-type.

[AIRef](https://airef.github.io/commands/commands-details.html#regicide-game)

Completion insert text:

```text
(regicide-game)
```

<a id="symbol-release-escrow"></a>

## `release-escrow`

- Kind: `command`
- Detail: Action - Economy

Syntax: `(release-escrow <Resource>)`

Releases the computer player's escrow for a given resource type (transfers all of the given resource type from its escrow stockpile into its normal stockpile, setting the amount stored in that resource's escrow stockpile to 0). AIs can store each of their four resource stockpiles in one of two stockpile types: normal and escrow. Resources in the normal stockpiles are free for the AI to use, while resources in the escrow stockpiles can only be used with up-build, up-train, or up-research if the EscrowGoalId parameter in these commands is a goal set to the value "with-escrow". The user interface shows the sum of both the normal and escrow stockpile resources added together for each resource. By default, all resources are stored in the normal stockpiles. However, set-escrow-percentage and up-modify-escrow can be used to store some or all of the AI's resources in the escrow stockpiles instead. Resources in the escrow stockpiles can transferred back into the normal stockpiles by using release-escrow, up-release-escrow, or up-modify-escrow". Resources are usually placed in escrow stockpiles in order to save up for expensive technologies or important buildings or units, so that it isn't spent on lower priority things." cReleaseEscrow.commandParameters = [ { nameLink: pResource.getLink(), name: "Resource", type: "Const", dir: "in", range: "food, wood, stone, or gold.", note: "The escrow resource stockpile." } ]

[AIRef](https://airef.github.io/commands/commands-details.html#release-escrow)

Completion insert text:

```text
(release-escrow ${1:Resource})
```

<a id="symbol-research"></a>

## `research`

- Kind: `command`
- Detail: Action - Techs

Syntax: `(research <TechId>)`

Researches the given item if the technology is available to the player and the technology can be researched without escrowed resources. Please use can-research, can-research-with-escrow, or up-can-research in any rule where you use the research command, in order to prevent possible crashes. To prevent cheating, this action will fail if the item currently cannot be researched (i.e. the tech prerequisites are not met, there is no available building, or the player cannot afford the item). Research names, except for ages, my-unique-research, my-second-unique-research, are prefixed with a "ri-" which might stand for "research item". You can also research by the research ID rather than the research name. You can see all technologies and their research IDs in the Technologies table. You can also use my-unique-research, which will usually (always in DE) research the imperial age unique tech for the civilization, and you can also use my-second-unique-research, which will usually (always in DE) research the castle age unique tech for the civilization. In UP and WK, the exceptions are the Britons (in WK only) and Goths, whose my-unique-research and my-second-unique-research are switched.

[AIRef](https://airef.github.io/commands/commands-details.html#research)

Completion insert text:

```text
(research ${1:TechId})
```

<a id="symbol-research-available"></a>

## `research-available`

- Kind: `command`
- Detail: Fact - Can Do, Techs

Syntax: `(research-available <TechId>)`

Checks that the given research is available to the computer player's civ, and that the research is available at this time (technology and tech tree prerequisites are met). The fact does not check that there are enough resources to start researching or if the player has built the building needed to research the technology. Unfortunately, because most technologies have an age as a prerequisite tech, research-available cannot be used at the beginning of the game to check if a technology is available in the civ's tech tree. There currently isn't a command that simply checks whether a technology is available in a civ's tech tree. Using this command is equivalent to using up-research-status to check if the technology's research status is equal to research-available.

[AIRef](https://airef.github.io/commands/commands-details.html#research-available)

Completion insert text:

```text
(research-available ${1:TechId})
```

<a id="symbol-research-completed"></a>

## `research-completed`

- Kind: `command`
- Detail: Fact - Can Do, Techs

Syntax: `(research-completed <TechId>)`

Checks that the given research is completed. Using this command is equivalent to using up-research-status to check if the technology's research status is equal to research-complete.

[AIRef](https://airef.github.io/commands/commands-details.html#research-completed)

Completion insert text:

```text
(research-completed ${1:TechId})
```

<a id="symbol-resign"></a>

## `resign`

- Kind: `command`
- Detail: Action - Other

Syntax: `(resign)`

Causes the computer player to resign.

[AIRef](https://airef.github.io/commands/commands-details.html#resign)

Completion insert text:

```text
(resign)
```

<a id="symbol-resource-found"></a>

## `resource-found`

- Kind: `command`
- Detail: Fact - Economy

Syntax: `(resource-found <Resource>)`

Checks whether the computer player has found the given resource. For food, gold, and stone (not wood), the given resource must be within the dropsite's max distance for this command to be true (snMillMaxDistance for food and snMiningCampMaxDistance or snCampMaxDistance for gold and stone). The fact should be used at the beginning period of the game. Once it becomes true for a certain resource it stays true for that resource. Only forests, not straggler trees, will make resource-found true for wood. Also, only forage bushes will make resource-found true for food. Using up-gaia-type-count, up-gaia-type-count-total, or dropsite-min-distance are often better commands to use than resource-found because they can count how many of the given resource have been found or determine how far away the resources are.

[AIRef](https://airef.github.io/commands/commands-details.html#resource-found)

Completion insert text:

```text
(resource-found ${1:Resource})
```

<a id="symbol-sell-commodity"></a>

## `sell-commodity`

- Kind: `command`
- Detail: Action - Economy, Trading

Syntax: `(sell-commodity <Commodity>)`

Sells one lot of a given commodity. The AI will sell 100 of the given commodity (wood, food, or stone) in return for gold at the current commodity-selling-price. The commodity selling price is the amount of gold that will be added to the gold stockpile when 100 of the specified commodity (wood, food, or stone) is sold. This price can range between 14 and infinity without Guilds, between 17 and infinity with Guilds, and between 19 and infinity when playing Saracens.

[AIRef](https://airef.github.io/commands/commands-details.html#sell-commodity)

Completion insert text:

```text
(sell-commodity ${1:Commodity})
```

<a id="symbol-set-author-email"></a>

## `set-author-email`

- Kind: `command`
- Detail: Action - Don't Use

Syntax: `(set-author-email)`

The game does not use it for anything.

[AIRef](https://airef.github.io/commands/commands-details.html#set-author-email)

Completion insert text:

```text
(set-author-email)
```

<a id="symbol-set-author-name"></a>

## `set-author-name`

- Kind: `command`
- Detail: Action - Don't Use

Syntax: `(set-author-name)`

The game does not use it for anything.

[AIRef](https://airef.github.io/commands/commands-details.html#set-author-name)

Completion insert text:

```text
(set-author-name)
```

<a id="symbol-set-author-version"></a>

## `set-author-version`

- Kind: `command`
- Detail: Action - Don't Use

Syntax: `(set-author-version)`

The game does not use it for anything.

[AIRef](https://airef.github.io/commands/commands-details.html#set-author-version)

Completion insert text:

```text
(set-author-version)
```

<a id="symbol-set-difficulty-parameter"></a>

## `set-difficulty-parameter`

- Kind: `command`
- Detail: Action - SNs

Syntax: `(set-difficulty-parameter <DiffParameterId> <Value>)`

Sets a given difficulty parameter to a given value. Difficulty parameters are similar to strategic numbers. There are two difficulty parameters that can be set: ability-to-maintain-distance or ability-to-dodge-missiles. Both have a range from 0 to 100, and the values have the opposite effect from what you'd expect! Setting a difficulty parameter to 0 completely enables the difficulty parameter behavior, and setting a difficulty parameter to 100 disables it. It isn't possible to check the current value of each difficulty parameter. Descriptions of each difficulty parameter:ability-to-maintain-distance: Chance that a computer player's ranged unit will maintain the distance. Range is 0-100, and the values are opposite from what you'd expect! When set to 0, ranged units will frequently move back to maintain distance. When set to 100, ranged units will not move back. However, this behavior only works on units are not following a move, patrol, or attack move command and are simply using their automatic attacking behavior. Setting snEnablePatrolAttack may also disable this behavior.ability-to-dodge-missiles: Chance of a computer player's unit dodging a missile. Range is 0-100, and the values are opposite from what you'd expect! When set to 0, units will try to dodge immediately upon seeing a projectile in the air. When set to 100, they have to hit first to react. Projectiles from siege-weapon-class and unpacked-trebuchet-class (913 and 954, not including scorpions) are always dodged, no matter what this parameter is set to. Note that while setting this to 0 might seem obvious, it may prove better to experiment especially depending on what enemy units you are facing and what units you are producing. For example, navy units have turn rates and so can suffer.

[AIRef](https://airef.github.io/commands/commands-details.html#set-difficulty-parameter)

Completion insert text:

```text
(set-difficulty-parameter ${1:DiffParameterId} ${2:Value})
```

<a id="symbol-set-doctrine"></a>

## `set-doctrine`

- Kind: `command`
- Detail: Action - Goals

Syntax: `(set-doctrine <Value>)`

Sets the doctrine to the given value, similar to setting the value of a goal. The doctrine is always an integer value and you can check if the doctrine is set to a given value with the doctrine" command. Unlike goals, there is only one doctrine that you can set, and you can only use the set-doctrine command to set the doctrine to a specific value. You can't dynamically set the doctrine to equal the value of a goal or strategic number, like you can with goals. In all cases, using goals instead of the doctrine will give you more flexibility, but if you run out of available goals then you can use the doctrine like an extra goal if you need it. The doctrine starts with the value of -1 at the beginning of the game, and it only changes if you use the set-doctrine command." cSetDoctrine.commandParameters = [ { nameLink: pValue.getLink(), name: "Value", type: "Const", dir: "in", range: "-2,147,483,648 to 2,147,483,647.", note: "The value to set the doctrine to." } ]

[AIRef](https://airef.github.io/commands/commands-details.html#set-doctrine)

Completion insert text:

```text
(set-doctrine ${1:Value})
```

<a id="symbol-set-escrow-percentage"></a>

## `set-escrow-percentage`

- Kind: `command`
- Detail: Action - Economy

Syntax: `(set-escrow-percentage <Resource> <Value>)`

Sets the computer player's escrow percentage for a given resource type. Given values have to be in the range 0-100. AIs can store each of their four resource stockpiles in one of two stockpile types: normal and escrow. Resources in the normal stockpiles are free for the AI to use, while resources in the escrow stockpiles can only be used with up-build, up-train, or up-research if the EscrowGoalId parameter in these commands is a goal set to the value "with-escrow". The user interface shows the sum of both the normal and escrow stockpile resources added together for each resource. By default, all resources are stored in the normal stockpiles. However, set-escrow-percentage and up-modify-escrow can be used to store some or all of the AI's resources in the escrow stockpiles instead. set-escrow-percentage sets the percentage of the resources a villager or fishing ship is carrying that will be stored in the escrow stockpile instead of the normal stockpile every time the villager or fishing ship drops off the resources they are carrying. For example, if a villager is dropping off 10 wood at the lumber camp and the wood escrow percentage is set to 30, then 3 of the 10 wood that is dropped off is stored in the wood escrow stockpile, while the remaining 7 wood is stored in the normal wood stockpile. set-escrow-percentage only applies to resources as they are dropped off. It does not immediately force a certain percentage of the total stockpile to be stored in escrow. For example, if the AI has 1000 gold, setting the gold escrow percentage to 20 does not mean that the AI will reallocate its gold stockpiles so that 200 gold will be in the gold escrow stockpile and 800 gold will be in the normal gold stockpile. If you want this behavior, you can use up-modify-escrow instead (see the examples section on the up-modify-escrow page on how to do this). Resources in the escrow stockpiles can transferred back into the normal stockpiles by using release-escrow, up-release-escrow, or up-modify-escrow. Resources are usually placed in escrow stockpiles in order to save up for expensive technologies or important buildings or units, so that it isn't spent on lower priority things. There is no command that can check the current escrow percentage, so if you want to check the current escrow percentage, you'll need to store this percentage in a goal or an unused strategic number when you use set-escrow-percentage.

[AIRef](https://airef.github.io/commands/commands-details.html#set-escrow-percentage)

Completion insert text:

```text
(set-escrow-percentage ${1:Resource} ${2:Value})
```

<a id="symbol-set-goal"></a>

## `set-goal`

- Kind: `command`
- Detail: Action - Goals

Syntax: `(set-goal <GoalId> <Value>)`

Sets a given goal to a given value. While their purpose may be unclear based on their name, goals are variables which can store an integer value which can be checked with this command or with up-compare-goal. Each goal is given an ID, and AIs have 16000 goals available (only 512 in UP and only 40 in AoC) that they can use to store different values, and they all store the value -1 at the beginning of the game. Goals are one of the most important concepts of AI scripting, so it's good to learn how to use them. In programming speak, goals are a 16000-length one-indexed 32-bit integer array, pre-initialized to -1, and a GoalId refers to a particular index of that array. The set-goal command sets the value the given GoalId to the given integer value. New goals or variables cannot be defined, only constants (called defconsts by the AI engine), so AI scripters are limited to these 16000 goals, though unused strategic numbers can also be used like goals in a pinch. If the paragraph above makes absolutely no sense to you, you can imagine goals like a bank which holds 16000 bank accounts, numbered with IDs from 1 to 16000. These accounts can hold whole amounts (no cents or decimal amounts of money), and they can store either positive or negative amounts of money. These bank accounts are restricted to holding between -2,147,483,648 and 2,147,483,647 dollars, and they all start with -$1 (negative 1 dollars) stored inside them until they are used by a customer (the AI scripter). The set-goal and up-modify-goal commands can modify how much money is stored in a particular account. Following this bank metaphor, the goal command checks if the given bank account number holds the given amount of money. For example, (goal 5 13) checks if goal ID #5 holds the value 13 (i.e. bank account #5 holds $13), and (goal 415 -3274) checks if goal ID #415 holds the value -3,274 (i.e. bank account #415 holds -$3,274). You can also use up-compare-goal" to check the current value of a goal ID in a more powerful manner, such as checking if the goal stores greater or less than the given value. It is pretty common to use a defconst to refer to a goal ID number to make the AI more readable. See the second example below on what this looks like." cSetGoal.commandParameters = [ { nameLink: pGoalId.getLink(), name: "GoalId", type: "Const", dir: "in", range: "A valid GoalId, from 1 to 16000.", note: "The goal to set." }, { nameLink: pValue.getLink(), name: "Value", type: "Const", dir: "in", range: "-2,147,483,648 to 2,147,483,647.", note: "The value to set the goal to." } ]

[AIRef](https://airef.github.io/commands/commands-details.html#set-goal)

Completion insert text:

```text
(set-goal ${1:GoalId} ${2:Value})
```

<a id="symbol-set-shared-goal"></a>

## `set-shared-goal`

- Kind: `command`
- Detail: Action - Goals, Other Player Info

Syntax: `(set-shared-goal <SharedGoalId> <Value>)`

Sets a given shared goal (a goal that is shared among all computer players) to a given value. To be used only when all computer players are on the same team. Shared goals are a separate set of 256 goals, in addition to the regular 16000 normal goals, which are shared between all AIs in the game, even between AIs that are enemies. Any AI can modify them at any time with set-shared-goal or up-set-shared-goal, and all AIs can check their values with shared-goal or up-get-shared-goal. Otherwise, shared goals share the same characteristics of normal goals, which you can read about in the set-goal description. Because shared goals can change without the AI's knowledge and the fact than enemy AIs can check their values, it's often better to use up-allied-goal, which allows you to check the value of one of an allied AI's normal 16000 goals.

[AIRef](https://airef.github.io/commands/commands-details.html#set-shared-goal)

Completion insert text:

```text
(set-shared-goal ${1:SharedGoalId} ${2:Value})
```

<a id="symbol-set-signal"></a>

## `set-signal`

- Kind: `command`
- Detail: Action - Scenarios

Syntax: `(set-signal <SignalId>)`

Sets a given signal value that can be checked by the AI Signal trigger condition in the scenario editor. To set a signal dynamically, use up-set-signal. To check if a signal was already set, use up-get-signal. There are 256 different signals that an AI can send to the scenario editor, from 0 to 255, which can trigger various events in the scenario. Signals are essentially on/off flags which are set to "off" at the beginning of the game, and are set to "on" whenever the set-signal action is used. This AI Signal trigger condition can be very useful to detect events that AIs can detect, but scenario triggers cannot easily detect, such as receiving tribute. Once the given signal is set, the scenario designer can create a trigger with the condition "AI Signal", and select the corresponding AI Signal value in the dropdown list. Once the signal is set in the AI script, the AI Signal condition for the given signal value will become true for the rest of the game, even after a trigger with an AI Signal condition is executed, unless you use the up-set-signal AI command to turn the signal off by setting the signal ID to the value 0, or the scenario designer uses the Acknowledge AI Signal trigger effect to turn the signal off (this trigger effect is only available in DE). Signals are essentially the inverse of AI Script Goal trigger effects. To allow an AI script to detect an AI Script Goal trigger effect from a scenario trigger, use event-detected. This action only works with a single player scenario and "AI Signal" trigger condition. For a multiplayer scenario, use "Multiplayer AI Signal" and fe-set-signal.

[AIRef](https://airef.github.io/commands/commands-details.html#set-signal)

Completion insert text:

```text
(set-signal ${1:SignalId})
```

<a id="symbol-set-stance"></a>

## `set-stance`

- Kind: `command`
- Detail: Action - Diplomacy

Syntax: `(set-stance <PlayerNumber> <PlayerStance>)`

Sets the diplomatic stance toward a given player to the specified stance, either ally, neutral, or enemy. To check our stance toward a given player, use stance-toward. To check the stance another player has toward us, use players-stance. The action allows "focus-player", "target-player", and "any"/"every" wildcard parameters for pPlayerNumber. It also allows the use of rule variables for Player, such as "this-any-ally" or "this-any-enemy". It also allows for scenario-player-# and lobby-player-#, where # is between 1 and 8. scenario-player-# refers to the player color (where red = scenario-player-2), and lobby-player-# refers to the player slot (where the lobby host or human player playing a single player campaign is always lobby-player-1).

[AIRef](https://airef.github.io/commands/commands-details.html#set-stance)

Completion insert text:

```text
(set-stance ${1:PlayerNumber} ${2:PlayerStance})
```

<a id="symbol-set-strategic-number"></a>

## `set-strategic-number`

- Kind: `command`
- Detail: Action - SNs

Syntax: `(set-strategic-number <SnId> <Value>)`

Sets a given strategic number to a given value. See the Strategic Numbers section for more info on each strategic number. Each strategic number has a different default value, which you can also check on the SN Index page. Each SN is given an ID between 0 and 511. Currently, the SNs in the 313-511 range don't appear in the SN index and don't modify the behavior of your AI, but they are available for your AI to use. So, you can modify these SNs however you like, similar to goals, without changing the behavior of your AI. However, if you want to use a strategic number in this way like an extra custom goal, always check the SN index to make sure that the SN ID you are using is actually currently unused. A good practice is to start with using SN 510 (SN 511 might have some bugs in DE) and work your way backwards toward SNs in the 300 range.

[AIRef](https://airef.github.io/commands/commands-details.html#set-strategic-number)

Completion insert text:

```text
(set-strategic-number ${1:SnId} ${2:Value})
```

<a id="symbol-shared-goal"></a>

## `shared-goal`

- Kind: `command`
- Detail: Fact - Goals, Other Player Info

Syntax: `(shared-goal <SharedGoalId> <Value>)`

Checks a given shared goal (a goal that is shared among all computer players). It is to be used only when all computer players are on the same team. Shared goals are a separate set of 256 goals, in addition to the regular 16000 normal goals, which are shared between all AIs in the game, even between AIs that are enemies. Any AI can modify them at any time with set-shared-goal or up-set-shared-goal, and all AIs can check their values with shared-goal or up-get-shared-goal. Otherwise, shared goals share the same characteristics of normal goals, which you can read about in the set-goal description. Because shared goals can change without the AI's knowledge and the fact than enemy AIs can check their values, it's often better to use up-allied-goal, which allows you to check the value of one of an allied AI's normal 16000 goals.

[AIRef](https://airef.github.io/commands/commands-details.html#shared-goal)

Completion insert text:

```text
(shared-goal ${1:SharedGoalId} ${2:Value})
```

<a id="symbol-sheep-and-forage-too-far"></a>

## `sheep-and-forage-too-far`

- Kind: `command`
- Detail: Fact - Economy

Syntax: `(sheep-and-forage-too-far)`

Checks whether the computer player has any forage site(s) and/or sheep within 8 tiles of the drop-off location (Mill or Town Center). If not, this fact is true. To check if any resource is within a certain distance of a dropsite, you can use dropsite-min-distance instead, which is usually more flexible. You can check if the AI can currently see any particular resource with up-gaia-type-count.

[AIRef](https://airef.github.io/commands/commands-details.html#sheep-and-forage-too-far)

Completion insert text:

```text
(sheep-and-forage-too-far)
```

<a id="symbol-soldier-count"></a>

## `soldier-count`

- Kind: `command`
- Detail: Fact - Counting, Units

Syntax: `(soldier-count <compareOp> <Value>)`

Checks the computer player's soldier count. A soldier is a land-based military unit. Monks and siege weapons are included. attack-soldier-count + defend-soldier-count should equal soldier-count.

[AIRef](https://airef.github.io/commands/commands-details.html#soldier-count)

Completion insert text:

```text
(soldier-count ${1:compareOp} ${2:Value})
```

<a id="symbol-spy"></a>

## `spy`

- Kind: `command`
- Detail: Action - Techs

Syntax: `(spy)`

Executes a spy command. Only works in Regicide games to research the Treason effect. The computer player does see the revealed area around the enemy kings as expected. This command does not research Spies like you might expect.

[AIRef](https://airef.github.io/commands/commands-details.html#spy)

Completion insert text:

```text
(spy)
```

<a id="symbol-stance-toward"></a>

## `stance-toward`

- Kind: `command`
- Detail: Fact - Diplomacy, Own Player Info

Syntax: `(stance-toward <PlayerNumber> <PlayerStance>)`

Checks if the computer player's diplomatic stance toward a given player matches the given stance, either ally, neutral, or enemy. To check another player's diplomatic stance toward the computer player, use players-stance. The fact allows "focus-player", "target-player", and "any"/"every" wildcard parameters for pPlayerNumber. It also allows for scenario-player-# and lobby-player-#, where # is between 1 and 8. scenario-player-# refers to the player color (where red = scenario-player-2), and lobby-player-# refers to the player slot (where the lobby host or human player playing a single player campaign is always lobby-player-1).

[AIRef](https://airef.github.io/commands/commands-details.html#stance-toward)

Completion insert text:

```text
(stance-toward ${1:PlayerNumber} ${2:PlayerStance})
```

<a id="symbol-starting-age"></a>

## `starting-age`

- Kind: `command`
- Detail: Fact - Game Info

Syntax: `(starting-age <compareOp> <Age>)`

Checks the game's starting age. In addition to the regular age parameters, post-imperial-age can be used.

[AIRef](https://airef.github.io/commands/commands-details.html#starting-age)

Completion insert text:

```text
(starting-age ${1:compareOp} ${2:Age})
```

<a id="symbol-starting-resources"></a>

## `starting-resources`

- Kind: `command`
- Detail: Fact - Game Info

Syntax: `(starting-resources <compareOp> <StartingResources>)`

Checks the starting resources level. The standard setting is Low resources. In games without a Starting Resources option, like Death Match, starting-resources will be equal to 1 (low resources), probably because 1 is the standard resource setting in random map games. DE added the option for Ultra High, Infinite, and Random resource starts. Before DE, AIs on hardest difficulty would get 500 of each resource at the beginning of each age, including at the beginning of the game, but DE no longer does this. Starting resources can be modified by snAddStartingResourceWood, snAddStartingResourceFood, snAddStartingResourceGold, or snAddStartingResourceStone, though using these strategic numbers is considered cheating in AI tournaments. Starting resource amounts:Low Resources: start with 200W, 200F, 100G, and 200S.Medium Resources: start with 500W, 500F, 300G, and 400S.High Resources: start with 1000W, 1000F, 700G, and 800S.Ultra High Resources (DE only): start with 20,000W, 20,000F, 10,000G, and 5000S (same as Death Match).Infinite Resources (DE only): infinite amounts of each resource.Random Resources (DE only): start with random amounts of each resource.

[AIRef](https://airef.github.io/commands/commands-details.html#starting-resources)

Completion insert text:

```text
(starting-resources ${1:compareOp} ${2:StartingResources})
```

<a id="symbol-stone-amount"></a>

## `stone-amount`

- Kind: `command`
- Detail: Fact - Economy

Syntax: `(stone-amount <compareOp> <Value>)`

Checks a computer player's stone amount. This amount includes escrowed stone.

[AIRef](https://airef.github.io/commands/commands-details.html#stone-amount)

Completion insert text:

```text
(stone-amount ${1:compareOp} ${2:Value})
```

<a id="symbol-strategic-number"></a>

## `strategic-number`

- Kind: `command`
- Detail: Fact - SNs

Syntax: `(strategic-number <SnId> <compareOp> <Value>)`

Checks a strategic number's value. Strategic numbers modify various built-in behaviors and settings that can modify the automatic behaviors of your AI. See the SN Index for details on what each strategic number does. Each strategic number has a different default value, which you can also check on the SN Index page. Each SN is given an ID between 0 and 511. Currently, the SNs in the 313-511 range don't appear in the SN index and don't modify the behavior of your AI, but they are available for your AI to use. So, you can modify these SNs however you like, similar to goals, without changing the behavior of your AI. However, if you want to use a strategic number in this way like an extra custom goal, always check the SN index to make sure that the SN ID you are using is actually currently unused. A good practice is to start with using SN 510 (SN 511 might have some bugs in DE) and work your way backwards toward SNs in the 300 range.

[AIRef](https://airef.github.io/commands/commands-details.html#strategic-number)

Completion insert text:

```text
(strategic-number ${1:SnId} ${2:compareOp} ${3:Value})
```

<a id="symbol-taunt"></a>

## `taunt`

- Kind: `command`
- Detail: Action - Chat, Debugging, Other Player Info

Syntax: `(taunt <TauntId>)`

Triggers the taunt associated with the given value. This taunt will only be sent to allies, and other AIs can detect this taunt with the taunt-detected command. To send a randomized taunt to allies between a range of taunt values, you can use taunt-using-range. You can also use any of the chat commands, like chat-to-player, to send a taunt along with a chat message. To do this, put the taunt number at the very beginning of the message, followed by the rest of the chat message, like (chat-to-allies "/3Please send food!"). In DE, the forward slash "/" is currently required, but in UP it is not. This example will send taunt 3 to all allies, and they will see the message without the taunt number at the beginning, just like when a human player starts a chat message with a taunt number.

[AIRef](https://airef.github.io/commands/commands-details.html#taunt)

Completion insert text:

```text
(taunt ${1:TauntId})
```

<a id="symbol-taunt-detected"></a>

## `taunt-detected`

- Kind: `command`
- Detail: Fact - Chat, Debugging, Other Player Info

Syntax: `(taunt-detected <PlayerNumber> <TauntId>)`

Detects a given taunt from the given player. The check can be performed any number of times until the taunt is explicitly acknowledged, meaning that if the given taunt is received from the given player, this fact with remain true until the AI uses the acknowledge-taunt command to acknowledge the taunt from that player. taunt-detected will detect taunts sent to the AI from another AI that uses the taunt command, and it will also detect taunts sent in a chat message if the message starts with a number between 1 and 255. The fact allows "focus-player", "target-player", and "any"/"every" wildcard parameters for pPlayerNumber. It also allows for scenario-player-# and lobby-player-#, where # is between 1 and 8. scenario-player-# refers to the player color (where red = scenario-player-2), and lobby-player-# refers to the player slot (where the lobby host or human player playing a single player campaign is always lobby-player-1).

[AIRef](https://airef.github.io/commands/commands-details.html#taunt-detected)

Completion insert text:

```text
(taunt-detected ${1:PlayerNumber} ${2:TauntId})
```

<a id="symbol-taunt-using-range"></a>

## `taunt-using-range`

- Kind: `command`
- Detail: Action - Chat, Other Player Info

Syntax: `(taunt-using-range <TauntId> <Value>)`

Triggers a random taunt that is picked from a given taunt range. This taunt will only be sent to allies, and other AIs can detect this taunt with the taunt-detected command.

[AIRef](https://airef.github.io/commands/commands-details.html#taunt-using-range)

Completion insert text:

```text
(taunt-using-range ${1:TauntId} ${2:Value})
```

<a id="symbol-timer-triggered"></a>

## `timer-triggered`

- Kind: `command`
- Detail: Fact - Timers

Syntax: `(timer-triggered <TimerId>)`

Checks whether a given timer has triggered (the time on the timer has run out). For disabled or running timers this fact is always false. The check can be performed any number of times until the timer is explicitly disabled or enabled again (restarted). The given timer ID can be any valid timer ID, which can range from 1 to 50. You can also substitute a defconst that is defined with a value between 1 and 50 if you want to give the timer a name. Timers have three possible states, and they cannot have multiple states at once: timer-running, timer-triggered, and timer-disabled. All 50 timers start in the timer-disabled state, and timer-triggered command is only true when the timer is in the timer-triggered state. To disable a timer, use disable-timer or use up-set-timer with a -1 timer length. To enable a timer, use enable-timer or use up-set-timer with a timer length > 0.

[AIRef](https://airef.github.io/commands/commands-details.html#timer-triggered)

Completion insert text:

```text
(timer-triggered ${1:TimerId})
```

<a id="symbol-town-under-attack"></a>

## `town-under-attack`

- Kind: `command`
- Detail: Fact - Defense

Syntax: `(town-under-attack)`

town-under-attack is triggered (i.e. returns true) if any unit/building belonging to the computer player that is inside snMaximumTownSize gets attacked. It lasts 1 to 10 in-game seconds after the attack. It is not triggered by attacks to buildings or villagers that are outside sn-maximum-town-size. This command detects ally attackers. Because town-under-attack detects any attack events within sn-maximum-town-size, it can sometimes trigger town-under-attack in conditions when a human player wouldn't consider the town under attack, such as if a wolf attacks a villager or an enemy scout attacks a villager while exploring. Most importantly, town-under-attack can trigger when the AI is using TSA to attack the enemy, since sn-maximum-town-size is large enough to detect attack events that occur in the enemy's town, so use town-under-attack with care.

[AIRef](https://airef.github.io/commands/commands-details.html#town-under-attack)

Completion insert text:

```text
(town-under-attack)
```

<a id="symbol-trace-fact"></a>

## `trace-fact`

- Kind: `command`
- Detail: Action - Don't Use

Syntax: `(trace-fact)`

Undocumented action that doesn't work. Probably only for debugging purposes originally.

[AIRef](https://airef.github.io/commands/commands-details.html#trace-fact)

Completion insert text:

```text
(trace-fact)
```

<a id="symbol-train"></a>

## `train`

- Kind: `command`
- Detail: Action - Units

Syntax: `(train <UnitId>)`

Trains the given unit if the unit is available to the player and the unit can be trained without escrowed resources. In order to use escrow resources, they must be released with release-escrow, up-release-escrow, or up-modify-escrow. To prevent cheating, this action uses the same criteria as the can-train fact to make sure the unit can be trained. It also checks When possible, use unit lines with this command. my-unique-unit, my-elite-unique-unit, and my-unique-unit-line can also be used, which will automatically get the UnitId of the unique unit, elite unique unit, or unique unit line that the AI's civ can train from the castle. You can also train by the unit ID rather than the unit name. You can see all units and their unit IDs in the Objects table. You cannot use unit classes or unit sets, like huskarl-set. To train units which can be trained at multiple buildings, like huskarls, tarkans, konniks, and serjeants, you must use a separate unit type or unit line to train them from their non-castle building. Look up these units in the Objects Table for more information. To train mercenary kipchaks (elite kipchaks that allies can train after Cuman Mercenaries is researched), use "mercenary-kipchak" rather than kipchak-line. In WK, there are two units that use a separate placeholder unit ID for training purposes, and you must use it for all train, can-train-with-escrow, train, up-can-train, and up-train commands. These units are the condottiero and genitour. Use ID 184 for condottiero-placeholder and use ID 732 for genitour-placeholder.The AI engine will automatically pick the building with the least number of queued units and techs to train the unit, and if there are multiple equally available buildings, the AI will pick one of those buildings at random. To pick a particular building or buildings on the map to train the unit, use a DUC search to put those buildings in the local list and use the up-target-point command with the action-train action to order the buildings to train the unit. See the up-target-point page for an example. Interestingly, you can safely use the base unit of a unit line with this command instead of the unit line version, and it will work regardless of any upgrades that have been researched. For example, you can safely use (train archer) even if Crossbowman has been researched. This capability is important if you are scripting for WololoKingdoms (WK) or any other mod where some unit lines aren't defined in the AI engine. The setting of snDockTrainingFilter affects the ability for docks to train warships with this command. The fact allows the use of unit line wildcard parameters for pUnitId.

[AIRef](https://airef.github.io/commands/commands-details.html#train)

Completion insert text:

```text
(train ${1:UnitId})
```

<a id="symbol-tribute-to-player"></a>

## `tribute-to-player`

- Kind: `command`
- Detail: Action - Diplomacy

Syntax: `(tribute-to-player <PlayerNumber> <Resource> <Value>)`

Tributes the given amount of the given resource type to the player defined by the PlayerNumber parameter. If the computer player does not have a Market, no tribute is given. In the case when the value parameter specifies an amount larger than available, only the available resources of the given type are tributed. If, for example, there is only 60 food and the tribute action specifies 100 food, only 60 food will be tributed. The tribute action is ignored when there are no resources of the given type. Tribute fees are paid and deducted from the tribute amount (if applicable). The action allows "focus-player", "target-player", and "any"/"every" wildcard parameters for pPlayerNumber. It also allows the use of rule variables for Player, such as "this-any-ally" or "this-any-enemy". It also allows for scenario-player-# and lobby-player-#, where # is between 1 and 8. scenario-player-# refers to the player color (where red = scenario-player-2), and lobby-player-# refers to the player slot (where the lobby host or human player playing a single player campaign is always lobby-player-1).

[AIRef](https://airef.github.io/commands/commands-details.html#tribute-to-player)

Completion insert text:

```text
(tribute-to-player ${1:PlayerNumber} ${2:Resource} ${3:Value})
```

<a id="symbol-true"></a>

## `true`

- Kind: `command`
- Detail: Fact - Other

Syntax: `(true)`

A Fact that is always true. Each rule has to have at least one fact/condition, so this command is often used as a placeholder for rules that should execute its actions without conditions.

[AIRef](https://airef.github.io/commands/commands-details.html#true)

Completion insert text:

```text
(true)
```

<a id="symbol-unit-available"></a>

## `unit-available`

- Kind: `command`
- Detail: Fact - Can Do, Units

Syntax: `(unit-available <UnitId>)`

Checks that the unit is available to the computer player's civ, and that the tech tree prerequisites for training the unit are met. The fact does not check whether the unit training can start, meaning this command does not check resource availability, housing headroom, or whether the building needed for training is currently used for research/training of another unit. The fact allows the use of unit line wildcard parameters for pUnitId. my-unique-unit, my-elite-unique-unit, and my-unique-unit-line can also be used, which will automatically get the UnitId of the unique unit, elite unique unit, or unique unit line that the AI's civ can train from the castle. When the AI checks the tech tree prerequisites, this includes checking whether the prerequisite age has been researched. There isn't a way at the beginning of the game to check if the unit will be available for the civilization in future ages.

[AIRef](https://airef.github.io/commands/commands-details.html#unit-available)

Completion insert text:

```text
(unit-available ${1:UnitId})
```

<a id="symbol-unit-count"></a>

## `unit-count`

- Kind: `command`
- Detail: Fact - Counting, Units

Syntax: `(unit-count <compareOp> <Value>)`

Checks the computer player's unit count. Only trained units are included. To check for the unit-count of other players, use players-unit-count.

[AIRef](https://airef.github.io/commands/commands-details.html#unit-count)

Completion insert text:

```text
(unit-count ${1:compareOp} ${2:Value})
```

<a id="symbol-unit-count-total"></a>

## `unit-count-total`

- Kind: `command`
- Detail: Fact - Counting, Units

Syntax: `(unit-count-total <compareOp> <Value>)`

Checks the computer player's total unit count. The total includes trained and queued units. To check for the unit-count of other players (not including queued units), use players-unit-type-count.

[AIRef](https://airef.github.io/commands/commands-details.html#unit-count-total)

Completion insert text:

```text
(unit-count-total ${1:compareOp} ${2:Value})
```

<a id="symbol-unit-type-count"></a>

## `unit-type-count`

- Kind: `command`
- Detail: Fact - Counting, Units

Syntax: `(unit-type-count <UnitId> <compareOp> <Value>)`

Checks the computer player's unit count of the given type. Only trained units of the given type are included. The fact allows the use of unit line wildcard parameters for pUnitId. my-unique-unit, my-elite-unique-unit, and my-unique-unit-line can also be used, which will automatically get the UnitId of the unique unit, elite unique unit, or unique unit line that the AI's civ can train from the castle. There are four ways you can specify the unit "type":Unit Name: the name of an individual unit, such as villager, knight, or cavalry-archer.Unit Id: the numerical ID assigned to each unit, such as 4 (the archer) or 74 (the militia). See the ID column in the Objects Table for a list.Unit Line: the unit line for the unit, such as spearman-line or militiaman-line. Unit lines include each upgrade type of each type of unit. For example, spearman-line includes spearmen, pikemen, and halberdiers.Unit Class: the class of a unit, such as infantry-class, cavalry-class, or scorpion-class. Classes group several unit types together into a single category. Using a unit class will count all units that belong to this class. See the Class column in the Objects Table to see each units's class. To check for the unit-type-count of other players, use players-unit-type-count.

[AIRef](https://airef.github.io/commands/commands-details.html#unit-type-count)

Completion insert text:

```text
(unit-type-count ${1:UnitId} ${2:compareOp} ${3:Value})
```

<a id="symbol-unit-type-count-total"></a>

## `unit-type-count-total`

- Kind: `command`
- Detail: Fact - Counting, Units

Syntax: `(unit-type-count-total <UnitId> <compareOp> <Value>)`

Checks the computer player's unit count of the given type, including queued units. The fact allows the use of unit line wildcard parameters for pUnitId. my-unique-unit, my-elite-unique-unit, and my-unique-unit-line can also be used, which will automatically get the UnitId of the unique unit, elite unique unit, or unique unit line that the AI's civ can train from the castle. There are four ways you can specify the unit "type":Unit Name: the name of an individual unit, such as villager, knight, or cavalry-archer.Unit Id: the numerical ID assigned to each unit, such as 4 (the archer) or 74 (the militia). See the ID column in the Objects Table for a list.Unit Line: the unit line for the unit, such as spearman-line or militiaman-line. Unit lines include each upgrade type of each type of unit. For example, spearman-line includes spearmen, pikemen, and halberdiers.Unit Class: the class of a unit, such as infantry-class, cavalry-class, or scorpion-class. Classes group several unit types together into a single category. Using a unit class will count all units that belong to this class. See the Class column in the Objects Table to see each units's class. To check for the unit-type-count of other players, use players-unit-type-count.

[AIRef](https://airef.github.io/commands/commands-details.html#unit-type-count-total)

Completion insert text:

```text
(unit-type-count-total ${1:UnitId} ${2:compareOp} ${3:Value})
```

<a id="symbol-up-add-cost-data"></a>

## `up-add-cost-data`

- Kind: `command`
- Detail: Action - Cost Data

Syntax: `(up-add-cost-data <GoalId> <typeOp> <Value>)`

Add or subtract another set of cost data to the current cost data.

[AIRef](https://airef.github.io/commands/commands-details.html#up-add-cost-data)

Completion insert text:

```text
(up-add-cost-data ${1:GoalId} ${2:typeOp} ${3:Value})
```

<a id="symbol-up-add-object-by-id"></a>

## `up-add-object-by-id`

- Kind: `command`
- Detail: Fact/Action - DUC

Syntax: `(up-add-object-by-id <SearchSource> <typeOp> <Id>)`

Add an object to the search results by id. This command can be used as either a Fact or an Action.

[AIRef](https://airef.github.io/commands/commands-details.html#up-add-object-by-id)

Completion insert text:

```text
(up-add-object-by-id ${1:SearchSource} ${2:typeOp} ${3:Id})
```

<a id="symbol-up-add-object-cost"></a>

## `up-add-object-cost`

- Kind: `command`
- Detail: Action - Cost Data

Syntax: `(up-add-object-cost <typeOp> <ObjectId> <typeOp> <Value>)`

Add or subtract objects of a specific type to the current cost data. Note the special exception for town centers below. Gates likely also need to use foundation IDs instead. It's recommended to use the base unit or building, rather than a unit or building line. This command does not work with unit or building lines if the unit or building is not yet available to the civ because of incomplete techs or not being in the prerequisite age for the object. For example, "mangonel-line" only works once the AI is in the castle or imperial age, but "mangonel" works from the start of the game.

[AIRef](https://airef.github.io/commands/commands-details.html#up-add-object-cost)

Completion insert text:

```text
(up-add-object-cost ${1:typeOp} ${2:ObjectId} ${3:typeOp} ${4:Value})
```

<a id="symbol-up-add-point"></a>

## `up-add-point`

- Kind: `command`
- Detail: Action - Points

Syntax: `(up-add-point <Point> <Point> <typeOp> <Value>)`

Add or subtract two point goal pairs together and store the result in Point1. The Value parameter indicates how many instances of Point2 to add to Point1. A negative Value will result in subtracting this number of instances of Point2 from Point1. Set Point2 to 0 to use the point that is stored by up-set-target-point.

[AIRef](https://airef.github.io/commands/commands-details.html#up-add-point)

Completion insert text:

```text
(up-add-point ${1:Point} ${2:Point} ${3:typeOp} ${4:Value})
```

<a id="symbol-up-add-research-cost"></a>

## `up-add-research-cost`

- Kind: `command`
- Detail: Action - Cost Data

Syntax: `(up-add-research-cost <typeOp> <TechId> <typeOp> <Value>)`

Add or subtract techs of a specific type to the current cost data.

[AIRef](https://airef.github.io/commands/commands-details.html#up-add-research-cost)

Completion insert text:

```text
(up-add-research-cost ${1:typeOp} ${2:TechId} ${3:typeOp} ${4:Value})
```

<a id="symbol-up-allied-goal"></a>

## `up-allied-goal`

- Kind: `command`
- Detail: Fact - Goals, Other Player Info

Syntax: `(up-allied-goal <PlayerNumber> <GoalId> <compareOp> <Value>)`

Perform a comparison with an allied AI's goal variable. The command cannot be used to check human players or computer players who are not allies.

[AIRef](https://airef.github.io/commands/commands-details.html#up-allied-goal)

Completion insert text:

```text
(up-allied-goal ${1:PlayerNumber} ${2:GoalId} ${3:compareOp} ${4:Value})
```

<a id="symbol-up-allied-resource-amount"></a>

## `up-allied-resource-amount`

- Kind: `command`
- Detail: Fact - Economy, Other Player Info

Syntax: `(up-allied-resource-amount <PlayerNumber> <ResourceType> <compareOp> <Value>)`

Perform a comparison with an ally's internal resource value. The command cannot be used to check the resources of players who are not allies.

[AIRef](https://airef.github.io/commands/commands-details.html#up-allied-resource-amount)

Completion insert text:

```text
(up-allied-resource-amount ${1:PlayerNumber} ${2:ResourceType} ${3:compareOp} ${4:Value})
```

<a id="symbol-up-allied-resource-percent"></a>

## `up-allied-resource-percent`

- Kind: `command`
- Detail: Fact - Economy, Other Player Info

Syntax: `(up-allied-resource-percent <PlayerNumber> <ResourceType> <compareOp> <Value>)`

Perform a comparison with an ally's internal resource value * 100. This command cannot be used with players who are not allies.

[AIRef](https://airef.github.io/commands/commands-details.html#up-allied-resource-percent)

Completion insert text:

```text
(up-allied-resource-percent ${1:PlayerNumber} ${2:ResourceType} ${3:compareOp} ${4:Value})
```

<a id="symbol-up-allied-sn"></a>

## `up-allied-sn`

- Kind: `command`
- Detail: Fact - Other Player Info, SNs

Syntax: `(up-allied-sn <PlayerNumber> <SnId> <compareOp> <Value>)`

Perform a comparison with an allied AI's strategic number. This command cannot be used on human players or players who aren't allies.

[AIRef](https://airef.github.io/commands/commands-details.html#up-allied-sn)

Completion insert text:

```text
(up-allied-sn ${1:PlayerNumber} ${2:SnId} ${3:compareOp} ${4:Value})
```

<a id="symbol-up-assign-builders"></a>

## `up-assign-builders`

- Kind: `command`
- Detail: Action - Buildings, Economy

Syntax: `(up-assign-builders <typeOp> <BuildingId> <typeOp> <Value>)`

Assign a specific number of builders to a building type or class. This assignment lasts for all future buildings of the specified building type or class until a new up-assign-builders command is issued. If the current number of builders for the building type or class is less than the amount of villagers specified by up-assign-builders, the additional builders are immediately sent to help construct the building. If you want a certain number of assign builders to only last for the construction of one building, you must set up-assign-builders again after the building is constructed. Additionally, if you want to stop sending any builders to construct a building type or class, you must set up-assign-builders to -1, not 0. When using any build command besides up-build-line, the game will automatically assign one builder to construct the building, regardless of what you have up-assign-builders set to. However, if the original builder is killed or restasked and up-assign-builders is set to -1 for the building, the AI will not send a replacement builder to finish the building. Assigning the number of builders by class is best for walls and gates. By default, like AoC, wonders have 250 (max) builders, and the wall class has 2.

[AIRef](https://airef.github.io/commands/commands-details.html#up-assign-builders)

Completion insert text:

```text
(up-assign-builders ${1:typeOp} ${2:BuildingId} ${3:typeOp} ${4:Value})
```

<a id="symbol-up-attacker-class"></a>

## `up-attacker-class`

- Kind: `command`
- Detail: Fact - Defense

Syntax: `(up-attacker-class <compareOp> <ClassId>)`

Check the class of the last enemy object to trigger town-under-attack.

[AIRef](https://airef.github.io/commands/commands-details.html#up-attacker-class)

Completion insert text:

```text
(up-attacker-class ${1:compareOp} ${2:ClassId})
```

<a id="symbol-up-bound-point"></a>

## `up-bound-point`

- Kind: `command`
- Detail: Action - Points

Syntax: `(up-bound-point <Point> <Point>)`

Copy a point goal pair (Point2), shift it into the map bounds, and store the bounded point in Point1.

[AIRef](https://airef.github.io/commands/commands-details.html#up-bound-point)

Completion insert text:

```text
(up-bound-point ${1:Point} ${2:Point})
```

<a id="symbol-up-bound-precise-point"></a>

## `up-bound-precise-point`

- Kind: `command`
- Detail: Action - Points

Syntax: `(up-bound-precise-point <Point> <Option> <typeOp> <Value>)`

Bound a point goal pair, either a normal point or a precise point, inside the map according to the number of tiles specified by the Value parameter, effectively acting as if the map has been shrunk on all sides by the number of tiles specified by the Value parameter. For example, the point (0,3) will be bounded to the point (5,5) if the Value parameter is 5. Please ensure that Value is a valid value and will not cause an overflow for the map size. If Option is set to 1, the command will treat the point goal pair as precise point and multiply the map size by 100 before bounding to account for the precise point coordinates, so the Value parameter should be adjusted accordingly by multiplying by 100. The bounded point will be stored back into the original point goal pair.

[AIRef](https://airef.github.io/commands/commands-details.html#up-bound-precise-point)

Completion insert text:

```text
(up-bound-precise-point ${1:Point} ${2:Option} ${3:typeOp} ${4:Value})
```

<a id="symbol-up-build"></a>

## `up-build`

- Kind: `command`
- Detail: Action - Buildings

Syntax: `(up-build <PlacementType> <EscrowGoalId> <typeOp> <BuildingId>)`

Add a building to the construction queue with dynamic values. The AI will avoid placing the building in the following locations according to the placement type: System 1 (used by place-normal, place-control, and place-point):Ally (and self): will avoid placing the building on tiles where an allied building already exists.Enemy: will avoid placing the building on tiles where an enemy building already exists. Will also avoid placing a building within the attack range of a tower, TC, or castle, + 0.5 tiles.System 2 (used by place-forward):Ally (and self): will avoid placing the building on tiles where an allied building already exists.Enemy: will avoid placing the building on tiles where an enemy building already exists. Will also avoid placing a building within any enemy building's line of sight, + 2 tiles.

[AIRef](https://airef.github.io/commands/commands-details.html#up-build)

Completion insert text:

```text
(up-build ${1:PlacementType} ${2:EscrowGoalId} ${3:typeOp} ${4:BuildingId})
```

<a id="symbol-up-build-line"></a>

## `up-build-line`

- Kind: `command`
- Detail: Action - Buildings, Walls & Gates

Syntax: `(up-build-line <Point> <Point> <typeOp> <BuildingId>)`

Place a line of buildings between two point goal pairs. For town centers and gates, please use a FoundationId, such as town-center-foundation or gate-ascending. Do not use town-center or gate with this command.

[AIRef](https://airef.github.io/commands/commands-details.html#up-build-line)

Completion insert text:

```text
(up-build-line ${1:Point} ${2:Point} ${3:typeOp} ${4:BuildingId})
```

<a id="symbol-up-building-type-in-town"></a>

## `up-building-type-in-town`

- Kind: `command`
- Detail: Fact - Buildings, Counting, Defense

Syntax: `(up-building-type-in-town <typeOp> <BuildingId> <compareOp> <Value>)`

Check the number of a specific enemy building type in town.

[AIRef](https://airef.github.io/commands/commands-details.html#up-building-type-in-town)

Completion insert text:

```text
(up-building-type-in-town ${1:typeOp} ${2:BuildingId} ${3:compareOp} ${4:Value})
```

<a id="symbol-up-buy-commodity"></a>

## `up-buy-commodity`

- Kind: `command`
- Detail: Action - Economy, Trading

Syntax: `(up-buy-commodity <typeOp> <ResourceType> <typeOp> <Value>)`

Buy a variable amount of resources at the market. The actual amount you receive depends on available gold.

[AIRef](https://airef.github.io/commands/commands-details.html#up-buy-commodity)

Completion insert text:

```text
(up-buy-commodity ${1:typeOp} ${2:ResourceType} ${3:typeOp} ${4:Value})
```

<a id="symbol-up-can-build"></a>

## `up-can-build`

- Kind: `command`
- Detail: Fact - Buildings, Can Do

Syntax: `(up-can-build <EscrowGoalId> <typeOp> <BuildingId>)`

Check if a building can be constructed with dynamic values.

[AIRef](https://airef.github.io/commands/commands-details.html#up-can-build)

Completion insert text:

```text
(up-can-build ${1:EscrowGoalId} ${2:typeOp} ${3:BuildingId})
```

<a id="symbol-up-can-build-line"></a>

## `up-can-build-line`

- Kind: `command`
- Detail: Fact - Buildings, Can Do, Walls & Gates

Syntax: `(up-can-build-line <EscrowGoalId> <Point> <typeOp> <BuildingId>)`

Check if a building can be constructed at a point goal pair. For town centers and gates, please use a FoundationId, such as town-center-foundation or gate-ascending. Do not use town-center or gate with this command.

[AIRef](https://airef.github.io/commands/commands-details.html#up-can-build-line)

Completion insert text:

```text
(up-can-build-line ${1:EscrowGoalId} ${2:Point} ${3:typeOp} ${4:BuildingId})
```

<a id="symbol-up-can-research"></a>

## `up-can-research`

- Kind: `command`
- Detail: Fact - Can Do, Techs

Syntax: `(up-can-research <EscrowGoalId> <typeOp> <TechId>)`

Check if a technology can be researched with dynamic values.

[AIRef](https://airef.github.io/commands/commands-details.html#up-can-research)

Completion insert text:

```text
(up-can-research ${1:EscrowGoalId} ${2:typeOp} ${3:TechId})
```

<a id="symbol-up-can-search"></a>

## `up-can-search`

- Kind: `command`
- Detail: Fact - Can Do, DUC

Syntax: `(up-can-search <SearchSource>)`

Check the status for either the local or remote search. If the result list is full or the index offset is at the end of the player object list, this will return false.

[AIRef](https://airef.github.io/commands/commands-details.html#up-can-search)

Completion insert text:

```text
(up-can-search ${1:SearchSource})
```

<a id="symbol-up-can-train"></a>

## `up-can-train`

- Kind: `command`
- Detail: Fact - Can Do, Units

Syntax: `(up-can-train <EscrowGoalId> <typeOp> <UnitId>)`

Check if a unit can be trained with dynamic values. my-unique-unit, my-elite-unique-unit, and my-unique-unit-line can also be used for the Unit ID to check, which will automatically get the UnitId of the unique unit, elite unique unit, or unique unit line that the AI's civ can train from the castle. This fact will return false if nhe setting of snDockTrainingFilter currently restricts the training of ships.

[AIRef](https://airef.github.io/commands/commands-details.html#up-can-train)

Completion insert text:

```text
(up-can-train ${1:EscrowGoalId} ${2:typeOp} ${3:UnitId})
```

<a id="symbol-up-cc-add-resource"></a>

## `up-cc-add-resource`

- Kind: `command`
- Detail: Action - Cheat, Economy

Syntax: `(up-cc-add-resource <typeOp> <ResourceType> <typeOp> <Value>)`

Add resources dynamically to the player stockpile. This is considered a cheat command, but cheats do not have to be enabled.

[AIRef](https://airef.github.io/commands/commands-details.html#up-cc-add-resource)

Completion insert text:

```text
(up-cc-add-resource ${1:typeOp} ${2:ResourceType} ${3:typeOp} ${4:Value})
```

<a id="symbol-up-cc-send-cheat"></a>

## `up-cc-send-cheat`

- Kind: `command`
- Detail: Action - Chat, Cheat

Syntax: `(up-cc-send-cheat <String>)`

Send a message in order to execute a cheat code. Cheats must be enabled for this to take effect.

[AIRef](https://airef.github.io/commands/commands-details.html#up-cc-send-cheat)

Completion insert text:

```text
(up-cc-send-cheat ${1:String})
```

<a id="symbol-up-change-name"></a>

## `up-change-name`

- Kind: `command`
- Detail: Action - Other

Syntax: `(up-change-name <String>)`

Change the name of the AI during gameplay. When you use (up-change-name -1), the AI's name will be set to one of that civilization's first 8 built-in historical names in an semi-random manner, same as the names used in the default AI. The name is guaranteed to be unique among other AIs that use this command, but not necessarily with Petersen's selection.

[AIRef](https://airef.github.io/commands/commands-details.html#up-change-name)

Completion insert text:

```text
(up-change-name ${1:String})
```

<a id="symbol-up-chat-data-to-all"></a>

## `up-chat-data-to-all`

- Kind: `command`
- Detail: Action - Chat, Debugging, Goals

Syntax: `(up-chat-data-to-all <String> <typeOp> <Value>)`

Send a chat message with a formatted value to everyone.

[AIRef](https://airef.github.io/commands/commands-details.html#up-chat-data-to-all)

Completion insert text:

```text
(up-chat-data-to-all ${1:String} ${2:typeOp} ${3:Value})
```

<a id="symbol-up-chat-data-to-player"></a>

## `up-chat-data-to-player`

- Kind: `command`
- Detail: Action - Chat, Debugging, Goals

Syntax: `(up-chat-data-to-player <PlayerNumber> <String> <typeOp> <Value>)`

Send a chat message with a formatted value to a player. The Action allows "my-player-number", "focus-player", "target-player", and "any"/"every" wildcard parameters for pPlayerNumber. It also allows the use of rule variables for pPlayerNumber, such as "this-any-ally" or "this-any-enemy". It also allows for scenario-player-# and lobby-player-#, where # is between 1 and 8. scenario-player-# refers to the player color (where red = scenario-player-2), and lobby-player-# refers to the player slot (where the lobby host or human player playing a single player campaign is always lobby-player-1).

[AIRef](https://airef.github.io/commands/commands-details.html#up-chat-data-to-player)

Completion insert text:

```text
(up-chat-data-to-player ${1:PlayerNumber} ${2:String} ${3:typeOp} ${4:Value})
```

<a id="symbol-up-chat-data-to-self"></a>

## `up-chat-data-to-self`

- Kind: `command`
- Detail: Action - Chat, Debugging, Goals

Syntax: `(up-chat-data-to-self <String> <typeOp> <Value>)`

Send a chat message with a formatted value locally.

[AIRef](https://airef.github.io/commands/commands-details.html#up-chat-data-to-self)

Completion insert text:

```text
(up-chat-data-to-self ${1:String} ${2:typeOp} ${3:Value})
```

<a id="symbol-up-clean-search"></a>

## `up-clean-search`

- Kind: `command`
- Detail: Action - DUC

Syntax: `(up-clean-search <SearchSource> <ObjectData> <SearchOrder>)`

Removes duplicate ids or sorts the search results. If ObjectData is set to -1, this will attempt to remove duplicates, lowering the result total. When removing duplicates, using search-order-none to preserve the existing order may perform slower than with asc/desc. If you wish to sort by ObjectData, it's best to remove duplicates first. Depending on the number of objects in the list, this command may be expensive, so please take care.

[AIRef](https://airef.github.io/commands/commands-details.html#up-clean-search)

Completion insert text:

```text
(up-clean-search ${1:SearchSource} ${2:ObjectData} ${3:SearchOrder})
```

<a id="symbol-up-compare-const"></a>

## `up-compare-const`

- Kind: `command`
- Detail: Fact - Other

Syntax: `(up-compare-const <Defconst> <compareOp> <Value>)`

Perform a comparison with a constant value. A defconst that defines a string (quoted text) stores a string table index where the string is stored. Therefore, up-compare-const will compare against the string index of such a defconst, rather than the text itself.

[AIRef](https://airef.github.io/commands/commands-details.html#up-compare-const)

Completion insert text:

```text
(up-compare-const ${1:Defconst} ${2:compareOp} ${3:Value})
```

<a id="symbol-up-compare-flag"></a>

## `up-compare-flag`

- Kind: `command`
- Detail: Fact - Goals

Syntax: `(up-compare-flag <GoalId> <compareOp> <Flag>)`

Perform a bitwise flag test with a goal variable. Flags allow multiple states to be stored in a single value by using powers of 2 (1, 2, 4, 8, 16, etc.). You can use [cgs]:== to see if a flag is stored or [cgs]:!= to see if it isn't stored.

[AIRef](https://airef.github.io/commands/commands-details.html#up-compare-flag)

Completion insert text:

```text
(up-compare-flag ${1:GoalId} ${2:compareOp} ${3:Flag})
```

<a id="symbol-up-compare-goal"></a>

## `up-compare-goal`

- Kind: `command`
- Detail: Fact - Goals

Syntax: `(up-compare-goal <GoalId> <compareOp> <Value>)`

Perform a comparison with a goal variable.

[AIRef](https://airef.github.io/commands/commands-details.html#up-compare-goal)

Completion insert text:

```text
(up-compare-goal ${1:GoalId} ${2:compareOp} ${3:Value})
```

<a id="symbol-up-compare-sn"></a>

## `up-compare-sn`

- Kind: `command`
- Detail: Fact - SNs

Syntax: `(up-compare-sn <GoalId> <compareOp> <Value>)`

Perform a comparison with a strategic number.

[AIRef](https://airef.github.io/commands/commands-details.html#up-compare-sn)

Completion insert text:

```text
(up-compare-sn ${1:GoalId} ${2:compareOp} ${3:Value})
```

<a id="symbol-up-compare-text"></a>

## `up-compare-text`

- Kind: `command`
- Detail: Fact - Text Data

Syntax: `(up-compare-text <typeOp> <Defconst> <compareOp> <Value>)`

Perform a string comparison with the stored text. You must store text before using this command and the provided Defconst must be a text defconst. If the provided string cannot be found anywhere in the stored text, the value will be -1. Otherwise, the value will be the index of the match.

[AIRef](https://airef.github.io/commands/commands-details.html#up-compare-text)

Completion insert text:

```text
(up-compare-text ${1:typeOp} ${2:Defconst} ${3:compareOp} ${4:Value})
```

<a id="symbol-up-copy-point"></a>

## `up-copy-point`

- Kind: `command`
- Detail: Action - Points

Syntax: `(up-copy-point <Point> <Point>)`

Copy one point goal pair (Point2) into another pair of extended goals (Point1).

[AIRef](https://airef.github.io/commands/commands-details.html#up-copy-point)

Completion insert text:

```text
(up-copy-point ${1:Point} ${2:Point})
```

<a id="symbol-up-create-group"></a>

## `up-create-group`

- Kind: `command`
- Detail: Action - DUC, DUC Groups

Syntax: `(up-create-group <GoalId> <GoalId> <typeOp> <GroupId>)`

Reset the group and create a search group from the local search results. The number of units put into the group will be capped by the number stored in CountGoalId. If 0 is used for the CountGoalId parameter, up to 40 objects will be put into the group instead (the highest amount). If there are no units available in the results list to create the specified group, the group will be cleared in the same way as up-reset-group.

[AIRef](https://airef.github.io/commands/commands-details.html#up-create-group)

Completion insert text:

```text
(up-create-group ${1:GoalId} ${2:GoalId} ${3:typeOp} ${4:GroupId})
```

<a id="symbol-up-cross-tiles"></a>

## `up-cross-tiles`

- Kind: `command`
- Detail: Action - Points

Syntax: `(up-cross-tiles <Point> <Point> <typeOp> <Value>)`

Get a point perpendicular to two point goal pairs. The Value parameter specifies how many tiles away the new point will be from Point1, perpendicularly away in reference to Point2. A negative Value will result in the new point being located perpendicularly away in opposite direction. Set Point2 to 0 to use the point that is stored by up-set-target-point. The new point will be stored in Point1.

[AIRef](https://airef.github.io/commands/commands-details.html#up-cross-tiles)

Completion insert text:

```text
(up-cross-tiles ${1:Point} ${2:Point} ${3:typeOp} ${4:Value})
```

<a id="symbol-up-defender-count"></a>

## `up-defender-count`

- Kind: `command`
- Detail: Fact - Counting, Defense, Units

Syntax: `(up-defender-count <compareOp> <Value>)`

Check the number of units actively defending in town. With this command you can check to see if your TSA attack is actually actively targeting anything or if it's just idling. If, after expecting your new town-size to initiate a defensive attack, the response from this command is far less than expected for several consecutive turns, your target may be unreachable by the defensive targeting system (target has been walled for protection by one of their allies, etc.) and you may need to switch targets.

[AIRef](https://airef.github.io/commands/commands-details.html#up-defender-count)

Completion insert text:

```text
(up-defender-count ${1:compareOp} ${2:Value})
```

<a id="symbol-up-delete-distant-farms"></a>

## `up-delete-distant-farms`

- Kind: `command`
- Detail: Action - Buildings, Economy

Syntax: `(up-delete-distant-farms <typeOp> <Value>)`

Delete all farms that exist outside the specified drop distance.

[AIRef](https://airef.github.io/commands/commands-details.html#up-delete-distant-farms)

Completion insert text:

```text
(up-delete-distant-farms ${1:typeOp} ${2:Value})
```

<a id="symbol-up-delete-idle-units"></a>

## `up-delete-idle-units`

- Kind: `command`
- Detail: Action - Units

Syntax: `(up-delete-idle-units <IdleType>)`

Delete all idle units of the specified type.

[AIRef](https://airef.github.io/commands/commands-details.html#up-delete-idle-units)

Completion insert text:

```text
(up-delete-idle-units ${1:IdleType})
```

<a id="symbol-up-delete-objects"></a>

## `up-delete-objects`

- Kind: `command`
- Detail: Action - Units

Syntax: `(up-delete-objects <typeOp> <UnitId> <typeOp> <Value>)`

Delete all objects with less hitpoints than the specified Value.

[AIRef](https://airef.github.io/commands/commands-details.html#up-delete-objects)

Completion insert text:

```text
(up-delete-objects ${1:typeOp} ${2:UnitId} ${3:typeOp} ${4:Value})
```

<a id="symbol-up-disband-group-type"></a>

## `up-disband-group-type`

- Kind: `command`
- Detail: Action - Units

Syntax: `(up-disband-group-type <GroupType>)`

Disband all internal groups of the specified type. To attack with groups with TSA, it is possible to collect units into large groups, disband with up-disband-group-type, and then send them with TSA.

[AIRef](https://airef.github.io/commands/commands-details.html#up-disband-group-type)

Completion insert text:

```text
(up-disband-group-type ${1:GroupType})
```

<a id="symbol-up-drop-resources"></a>

## `up-drop-resources`

- Kind: `command`
- Detail: Action - Economy

Syntax: `(up-drop-resources <Resource> <typeOp> <Value>)`

Request a drop by gatherers carrying a specific number of a resource. This command works for both villagers and fishing ships.

[AIRef](https://airef.github.io/commands/commands-details.html#up-drop-resources)

Completion insert text:

```text
(up-drop-resources ${1:Resource} ${2:typeOp} ${3:Value})
```

<a id="symbol-up-enemy-buildings-in-town"></a>

## `up-enemy-buildings-in-town`

- Kind: `command`
- Detail: Fact - Buildings, Counting, Defense

Syntax: `(up-enemy-buildings-in-town <compareOp> <Value>)`

Check the number of targetable enemy buildings in town.

[AIRef](https://airef.github.io/commands/commands-details.html#up-enemy-buildings-in-town)

Completion insert text:

```text
(up-enemy-buildings-in-town ${1:compareOp} ${2:Value})
```

<a id="symbol-up-enemy-units-in-town"></a>

## `up-enemy-units-in-town`

- Kind: `command`
- Detail: Fact - Counting, Defense

Syntax: `(up-enemy-units-in-town <compareOp> <Value>)`

Check the number of targetable enemy units in town.

[AIRef](https://airef.github.io/commands/commands-details.html#up-enemy-units-in-town)

Completion insert text:

```text
(up-enemy-units-in-town ${1:compareOp} ${2:Value})
```

<a id="symbol-up-enemy-villagers-in-town"></a>

## `up-enemy-villagers-in-town`

- Kind: `command`
- Detail: Fact - Counting, Defense, Units

Syntax: `(up-enemy-villagers-in-town <compareOp> <Value>)`

Check the number of targetable enemy villagers in town.

[AIRef](https://airef.github.io/commands/commands-details.html#up-enemy-villagers-in-town)

Completion insert text:

```text
(up-enemy-villagers-in-town ${1:compareOp} ${2:Value})
```

<a id="symbol-up-filter-distance"></a>

## `up-filter-distance`

- Kind: `command`
- Detail: Action - DUC

Syntax: `(up-filter-distance <typeOp> <MinDistance> <typeOp> <MaxDistance>)`

Set distance parameters for the direct targeting system. If any of these parameters is set to -1, then the associated condition will be ignored during search filtering.

[AIRef](https://airef.github.io/commands/commands-details.html#up-filter-distance)

Completion insert text:

```text
(up-filter-distance ${1:typeOp} ${2:MinDistance} ${3:typeOp} ${4:MaxDistance})
```

<a id="symbol-up-filter-exclude"></a>

## `up-filter-exclude`

- Kind: `command`
- Detail: Action - DUC

Syntax: `(up-filter-exclude <CmdId> <ActionId> <OrderId> <ClassId>)`

Set exclude parameters for the direct targeting system. If any of these parameters is set to -1, then the associated condition will be ignored during search filtering.

[AIRef](https://airef.github.io/commands/commands-details.html#up-filter-exclude)

Completion insert text:

```text
(up-filter-exclude ${1:CmdId} ${2:ActionId} ${3:OrderId} ${4:ClassId})
```

<a id="symbol-up-filter-garrison"></a>

## `up-filter-garrison`

- Kind: `command`
- Detail: Action - DUC

Syntax: `(up-filter-garrison <typeOp> <MinGarrison> <typeOp> <MaxGarrison>)`

Set garrison parameters for the direct targeting system. If any of these parameters is set to -1, then the associated condition will be ignored during search filtering.

[AIRef](https://airef.github.io/commands/commands-details.html#up-filter-garrison)

Completion insert text:

```text
(up-filter-garrison ${1:typeOp} ${2:MinGarrison} ${3:typeOp} ${4:MaxGarrison})
```

<a id="symbol-up-filter-include"></a>

## `up-filter-include`

- Kind: `command`
- Detail: Action - DUC

Syntax: `(up-filter-include <CmdId> <ActionId> <OrderId> <OnMainland>)`

Set include parameters for the direct targeting system. If any of these parameters is set to -1, then the associated condition will be ignored during search filtering.

[AIRef](https://airef.github.io/commands/commands-details.html#up-filter-include)

Completion insert text:

```text
(up-filter-include ${1:CmdId} ${2:ActionId} ${3:OrderId} ${4:OnMainland})
```

<a id="symbol-up-filter-range"></a>

## `up-filter-range`

- Kind: `command`
- Detail: Action - DUC

Syntax: `(up-filter-range <MinGarrison> <MaxGarrison> <MinDistance> <MaxDistance>)`

Set range parameters for the direct targeting system. If any of these parameters is set to -1, then the associated condition will be ignored during search filtering.

[AIRef](https://airef.github.io/commands/commands-details.html#up-filter-range)

Completion insert text:

```text
(up-filter-range ${1:MinGarrison} ${2:MaxGarrison} ${3:MinDistance} ${4:MaxDistance})
```

<a id="symbol-up-filter-status"></a>

## `up-filter-status`

- Kind: `command`
- Detail: Action - DUC

Syntax: `(up-filter-status <typeOp> <ObjectStatus> <typeOp> <ObjectList>)`

Set the object status value for use with up-find-status. The default (after up-reset-filters) is 2, which should match most active objects. Buildings that are incomplete have a status of 0, while certain resources have a status of 3. For remote search, up-find-remote can find objects with object status values 0 to 3 (status-pending, status-ready, and status-resource) if you search by object type id instead of class id.

[AIRef](https://airef.github.io/commands/commands-details.html#up-filter-status)

Completion insert text:

```text
(up-filter-status ${1:typeOp} ${2:ObjectStatus} ${3:typeOp} ${4:ObjectList})
```

<a id="symbol-up-find-flare"></a>

## `up-find-flare`

- Kind: `command`
- Detail: Action - Other Player Info, Points

Syntax: `(up-find-flare <Point>)`

Read the (x,y) position of an allied flare into an extended goal pair. This command writes to 2 consecutive goals and requires an extended goal pair between 41 and 15998. If it fails to get a valid position, it will return (-1,-1). This command is equivalent to up-find-player-flare with any-ally.

[AIRef](https://airef.github.io/commands/commands-details.html#up-find-flare)

Completion insert text:

```text
(up-find-flare ${1:Point})
```

<a id="symbol-up-find-local"></a>

## `up-find-local`

- Kind: `command`
- Detail: Fact/Action - DUC

Syntax: `(up-find-local <typeOp> <UnitId> <typeOp> <Value>)`

Find objects owned by the local player for direct targeting. If UnitId changes, the search index offset will be reset. Otherwise, it will continue from where it left off. This command can be used as either a Fact or an Action.

[AIRef](https://airef.github.io/commands/commands-details.html#up-find-local)

Completion insert text:

```text
(up-find-local ${1:typeOp} ${2:UnitId} ${3:typeOp} ${4:Value})
```

<a id="symbol-up-find-next-player"></a>

## `up-find-next-player`

- Kind: `command`
- Detail: Action - Other Player Info

Syntax: `(up-find-next-player <PlayerStance> <FindPlayerMethod> <OutputGoalId>)`

Find the next active player based on the provided information.

[AIRef](https://airef.github.io/commands/commands-details.html#up-find-next-player)

Completion insert text:

```text
(up-find-next-player ${1:PlayerStance} ${2:FindPlayerMethod} ${3:OutputGoalId})
```

<a id="symbol-up-find-player"></a>

## `up-find-player`

- Kind: `command`
- Detail: Action - Other Player Info

Syntax: `(up-find-player <PlayerStance> <FindPlayerMethod> <OutputGoalId>)`

Find the first active player based on the provided information.

[AIRef](https://airef.github.io/commands/commands-details.html#up-find-player)

Completion insert text:

```text
(up-find-player ${1:PlayerStance} ${2:FindPlayerMethod} ${3:OutputGoalId})
```

<a id="symbol-up-find-player-flare"></a>

## `up-find-player-flare`

- Kind: `command`
- Detail: Action - Other Player Info, Points

Syntax: `(up-find-player-flare <PlayerNumber> <Point>)`

Read the (x,y) position of any visible flare into an extended goal pair. This command writes to 2 consecutive goals and requires an extended goal pair between 41 and 15998. If it fails to get a valid position, it will return (-1,-1). Please note that it has never been designed to work with this-any-* or every-* wildcards, as flares belong to all recipient players, even when they aren't owned by them, so the stored player from this-* would not necessarily be the actual sender of the flare. If you search for players-unit-type-count any-* flare, do not expect this-* to be the sender player for any action commands (not limited to just the flare stuff). If you need to know the specific player number of the sender, you'll need to loop with focus-player checks. The action allows "my-player-number", "focus-player", "target-player", and "any"/"every" wildcard parameters for pPlayerNumber. It also allows for scenario-player-# and lobby-player-#, where # is between 1 and 8. scenario-player-# refers to the player color (where red = scenario-player-2), and lobby-player-# refers to the player slot (where the lobby host or human player playing a single player campaign is always lobby-player-1).

[AIRef](https://airef.github.io/commands/commands-details.html#up-find-player-flare)

Completion insert text:

```text
(up-find-player-flare ${1:PlayerNumber} ${2:Point})
```

<a id="symbol-up-find-remote"></a>

## `up-find-remote`

- Kind: `command`
- Detail: Fact/Action - DUC

Syntax: `(up-find-remote <typeOp> <UnitId> <typeOp> <Value>)`

Find objects owned by the focus player for direct targeting. Set sn-focus-player-number before using this command. If the focus or UnitId changes, the search index offset will be reset. Otherwise, it will continue from where it left off. This command can be used as either a Fact or an Action. Normally, up-find-remote will only find status-ready objects, but up-find-remote can also find objects with object status values 0 to 3 (status-pending, status-ready, and status-resource) if you search by object type id instead of class id. For self/ally objects, it can find them directly at all times. For non-ally objects, if the object has been sighted and is either a building or has been seen/reseen within the past 5 seconds, it can be found. This should allow the AI to target units that are clearly visible without cheating, and target sighted enemy buildings in the fog. One other note: although the new targeting and find commands aren't as heavy as attack-now, like any command that directly manipulates units like retreat-now, guard-unit, etc., please try not to flood them.

[AIRef](https://airef.github.io/commands/commands-details.html#up-find-remote)

Completion insert text:

```text
(up-find-remote ${1:typeOp} ${2:UnitId} ${3:typeOp} ${4:Value})
```

<a id="symbol-up-find-resource"></a>

## `up-find-resource`

- Kind: `command`
- Detail: Fact/Action - DUC

Syntax: `(up-find-resource <typeOp> <Resource> <typeOp> <Value>)`

Find gatherable resource objects for direct targeting. This command stores data in the remote list and it will consider the status value set by up-filter-status. To find stone, gold, fallen trees, and other directly gatherable resources, status-resource is required. For standing trees and living objects, status-ready is required. Please ensure the proper status is set before searching. The remote index will reset automatically when switching between this command and other remote search commands like up-find-remote. If Resource changes, the search index offset will be reset. Otherwise, it will continue from where it left off. This command can be used as either a Fact or an Action. When searching with boar-class (class 910), this command will not include wolves in the search.

[AIRef](https://airef.github.io/commands/commands-details.html#up-find-resource)

Completion insert text:

```text
(up-find-resource ${1:typeOp} ${2:Resource} ${3:typeOp} ${4:Value})
```

<a id="symbol-up-find-status-local"></a>

## `up-find-status-local`

- Kind: `command`
- Detail: Fact/Action - DUC

Syntax: `(up-find-status-local <typeOp> <UnitId> <typeOp> <Value>)`

Find objects owned by the local player filtered by status. This is identical to up-find-local, except it will consider the status value set by up-filter-status. If UnitId changes, the search index offset will be reset. Otherwise, it will continue from where it left off. This command can be used as either a Fact or an Action.

[AIRef](https://airef.github.io/commands/commands-details.html#up-find-status-local)

Completion insert text:

```text
(up-find-status-local ${1:typeOp} ${2:UnitId} ${3:typeOp} ${4:Value})
```

<a id="symbol-up-find-status-remote"></a>

## `up-find-status-remote`

- Kind: `command`
- Detail: Fact/Action - DUC

Syntax: `(up-find-status-remote <typeOp> <UnitId> <typeOp> <Value>)`

Find objects owned by the focus player for direct targeting. Set sn-focus-player-number before using this command. This is identical to up-find-remote, except it will consider the status value set by up-filter-status. If the focus or UnitId changes, the search index offset will be reset. Otherwise, it will continue from where it left off. This command can be used as either a Fact or an Action.

[AIRef](https://airef.github.io/commands/commands-details.html#up-find-status-remote)

Completion insert text:

```text
(up-find-status-remote ${1:typeOp} ${2:UnitId} ${3:typeOp} ${4:Value})
```

<a id="symbol-up-full-reset-search"></a>

## `up-full-reset-search`

- Kind: `command`
- Detail: Action - DUC

Syntax: `(up-full-reset-search)`

Reset all search and filter states for direct unit targeting. This command simply combines (up-reset-search 1 1 1 1) and (up-reset-filters) for rule size optimization.

[AIRef](https://airef.github.io/commands/commands-details.html#up-full-reset-search)

Completion insert text:

```text
(up-full-reset-search)
```

<a id="symbol-up-gaia-type-count"></a>

## `up-gaia-type-count`

- Kind: `command`
- Detail: Fact - Counting, Economy

Syntax: `(up-gaia-type-count <typeOp> <Resource> <compareOp> <Value>)`

Check the current sighted resource count from gaia. This command may be relatively slow, since it must check the status of all discovered resources within the requested subset (food, wood, stone, or gold). This command does not work with relics.

[AIRef](https://airef.github.io/commands/commands-details.html#up-gaia-type-count)

Completion insert text:

```text
(up-gaia-type-count ${1:typeOp} ${2:Resource} ${3:compareOp} ${4:Value})
```

<a id="symbol-up-gaia-type-count-total"></a>

## `up-gaia-type-count-total`

- Kind: `command`
- Detail: Fact - Counting, Economy

Syntax: `(up-gaia-type-count-total <typeOp> <Resource> <compareOp> <Value>)`

Check the total sighted resource count from gaia. When checking food, wood, stone, or gold, this command operates very quickly. However, the required data does not exist for specific food types, including deer and sheep. As a fallback, it will redirect to the slower up-gaia-type-count, and the result will only reflect resources that still exist. This command does not work with relics.

[AIRef](https://airef.github.io/commands/commands-details.html#up-gaia-type-count-total)

Completion insert text:

```text
(up-gaia-type-count-total ${1:typeOp} ${2:Resource} ${3:compareOp} ${4:Value})
```

<a id="symbol-up-garrison"></a>

## `up-garrison`

- Kind: `command`
- Detail: Action - Buildings

Syntax: `(up-garrison <ObjectId> <typeOp> <UnitId>)`

Garrison all units of the specified type into another object. The first parameter cannot be a class or a unit-line. my-unique-unit and my-elite-unique-unit can be used though, which will automatically get the UnitId of the unique unit or elite unique unit that the AI's civ can train from the castle. It must be a valid root object type id that can accept a garrison (battering-ram instead of battering-ram-line). DE requires "feudal-battering-ram" (ID 1258) instead of battering-ram. Objects tasked to garrison are prioritized in the order from newest to oldest trained/built.

[AIRef](https://airef.github.io/commands/commands-details.html#up-garrison)

Completion insert text:

```text
(up-garrison ${1:ObjectId} ${2:typeOp} ${3:UnitId})
```

<a id="symbol-up-gather-inside"></a>

## `up-gather-inside`

- Kind: `command`
- Detail: Action - Buildings

Syntax: `(up-gather-inside <typeOp> <BuildingId> <typeOp> <Option>)`

Set all existing buildings of a specific type to hold units inside. If the Option parameter is set to 1, both trained and garrisoned units will be held inside the building. If set to -1, only garrisoned units will be held inside. Otherwise, if set to 0, all units will be released as usual.

[AIRef](https://airef.github.io/commands/commands-details.html#up-gather-inside)

Completion insert text:

```text
(up-gather-inside ${1:typeOp} ${2:BuildingId} ${3:typeOp} ${4:Option})
```

<a id="symbol-up-get-attacker-class"></a>

## `up-get-attacker-class`

- Kind: `command`
- Detail: Action - Defense

Syntax: `(up-get-attacker-class <ThreatSource>)`

Get the class of the last enemy object to trigger town-under-attack.

[AIRef](https://airef.github.io/commands/commands-details.html#up-get-attacker-class)

Completion insert text:

```text
(up-get-attacker-class ${1:ThreatSource})
```

<a id="symbol-up-get-cost-delta"></a>

## `up-get-cost-delta`

- Kind: `command`
- Detail: Action - Cost Data

Syntax: `(up-get-cost-delta <OutputGoalId>)`

Get the difference between player resources and the current cost data, and store this difference in four consecutive goals in the order of food, wood, stone, and gold. The calculation is the current stockpile minus the current amount stored in the four cost goals from the most recent up-setup-cost-data command.

[AIRef](https://airef.github.io/commands/commands-details.html#up-get-cost-delta)

Completion insert text:

```text
(up-get-cost-delta ${1:OutputGoalId})
```

<a id="symbol-up-get-event"></a>

## `up-get-event`

- Kind: `command`
- Detail: Action - Scenarios

Syntax: `(up-get-event <typeOp> <EventId> <Value>)`

Get the value of a scenario trigger event.

[AIRef](https://airef.github.io/commands/commands-details.html#up-get-event)

Completion insert text:

```text
(up-get-event ${1:typeOp} ${2:EventId} ${3:Value})
```

<a id="symbol-up-get-fact"></a>

## `up-get-fact`

- Kind: `command`
- Detail: Fact/Action - Player Facts, Own Player Info

Syntax: `(up-get-fact <FactId> <FactParameter> <OutputGoalId>)`

Read a fact for my-player-number into a goal. This command can be used as either a fact or an action.

[AIRef](https://airef.github.io/commands/commands-details.html#up-get-fact)

Completion insert text:

```text
(up-get-fact ${1:FactId} ${2:FactParameter} ${3:OutputGoalId})
```

<a id="symbol-up-get-fact-max"></a>

## `up-get-fact-max`

- Kind: `command`
- Detail: Fact/Action - Other Player Info, Player Facts

Syntax: `(up-get-fact-max <PlayerNumber> <FactId> <FactParameter> <OutputGoalId>)`

Read the maximum value of the facts for specific players into a goal. This command can be used as either a fact or an action. The matching player will be set to the this-any-* rule variable for use in the action section of the rule, even if up-get-fact-max is used as an action. The Action allows only the "any" wildcard parameters for pPlayerNumber, such as any-ally or any-enemy. It also allows for scenario-player-# and lobby-player-#, where # is between 1 and 8. scenario-player-# refers to the player color (where red = scenario-player-2), and lobby-player-# refers to the player slot (where the lobby host or human player playing a single player campaign is always lobby-player-1).

[AIRef](https://airef.github.io/commands/commands-details.html#up-get-fact-max)

Completion insert text:

```text
(up-get-fact-max ${1:PlayerNumber} ${2:FactId} ${3:FactParameter} ${4:OutputGoalId})
```

<a id="symbol-up-get-fact-min"></a>

## `up-get-fact-min`

- Kind: `command`
- Detail: Fact/Action - Other Player Info, Player Facts

Syntax: `(up-get-fact-min <PlayerNumber> <FactId> <FactParameter> <OutputGoalId>)`

Read the minimum value of the facts for specific players into a goal. This command can be used as either a fact or an action. The matching player will be set to the this-any-* wildcard player id for use in the action section of the rule, even if up-get-fact-min is used as an action. The Action allows only the "any" wildcard parameters for pPlayerNumber, such as any-ally or any-enemy. It also allows for scenario-player-# and lobby-player-#, where # is between 1 and 8. scenario-player-# refers to the player color (where red = scenario-player-2), and lobby-player-# refers to the player slot (where the lobby host or human player playing a single player campaign is always lobby-player-1).

[AIRef](https://airef.github.io/commands/commands-details.html#up-get-fact-min)

Completion insert text:

```text
(up-get-fact-min ${1:PlayerNumber} ${2:FactId} ${3:FactParameter} ${4:OutputGoalId})
```

<a id="symbol-up-get-fact-sum"></a>

## `up-get-fact-sum`

- Kind: `command`
- Detail: Fact/Action - Other Player Info, Player Facts

Syntax: `(up-get-fact-sum <PlayerNumber> <FactId> <FactParameter> <OutputGoalId>)`

Read the sum of facts for specific players into a goal. This command can be used as either a fact or an action. The action only allows the "any" wildcard parameters for pPlayerNumber, such as any-ally or any-enemy. It also allows for scenario-player-# and lobby-player-#, where # is between 1 and 8. scenario-player-# refers to the player color (where red = scenario-player-2), and lobby-player-# refers to the player slot (where the lobby host or human player playing a single player campaign is always lobby-player-1).

[AIRef](https://airef.github.io/commands/commands-details.html#up-get-fact-sum)

Completion insert text:

```text
(up-get-fact-sum ${1:PlayerNumber} ${2:FactId} ${3:FactParameter} ${4:OutputGoalId})
```

<a id="symbol-up-get-focus-fact"></a>

## `up-get-focus-fact`

- Kind: `command`
- Detail: Fact/Action - Other Player Info, Player Facts

Syntax: `(up-get-focus-fact <FactId> <FactParameter> <OutputGoalId>)`

Read a fact for the focus-player into a goal. This command can be used as either a fact or an action.

[AIRef](https://airef.github.io/commands/commands-details.html#up-get-focus-fact)

Completion insert text:

```text
(up-get-focus-fact ${1:FactId} ${2:FactParameter} ${3:OutputGoalId})
```

<a id="symbol-up-get-group-size"></a>

## `up-get-group-size`

- Kind: `command`
- Detail: Action - DUC, DUC Groups

Syntax: `(up-get-group-size <typeOp> <GroupId> <OutputGoalId>)`

Get the current number of units in a search group.

[AIRef](https://airef.github.io/commands/commands-details.html#up-get-group-size)

Completion insert text:

```text
(up-get-group-size ${1:typeOp} ${2:GroupId} ${3:OutputGoalId})
```

<a id="symbol-up-get-guard-state"></a>

## `up-get-guard-state`

- Kind: `command`
- Detail: Action - Game Info

Syntax: `(up-get-guard-state <OutputGoalId>)`

Get the guard state into 4 consecutive extended goals. The guard state is defined in custom random maps using the guard_state command, which enables a resource trickle and/or a defeat condition depending on whether a certain unit type is killed. The goals will be filled with data in the following order: TypeId, ResourceType, ResourceDelta, GuardFlags. Please use up-compare-flag to check the guard flags (see pGuardFlag for a list of guard flags). If guard-flag-resource is set in GuardFlags, then ResourceDelta/100 will slowly be added to ResourceType as long as TypeId objects remain. If both guard-flag-resource and guard-flag-inverse are set, then the resources will be added only when there are no TypeId objects left. If the guard-flag-victory condition is set, the AI will be defeated if no TypeId objects remain.

[AIRef](https://airef.github.io/commands/commands-details.html#up-get-guard-state)

Completion insert text:

```text
(up-get-guard-state ${1:OutputGoalId})
```

<a id="symbol-up-get-indirect-goal"></a>

## `up-get-indirect-goal`

- Kind: `command`
- Detail: Action - Goals

Syntax: `(up-get-indirect-goal <typeOp> <GoalId> <OutputGoalId>)`

Get the value of a goal indirectly by reference.

[AIRef](https://airef.github.io/commands/commands-details.html#up-get-indirect-goal)

Completion insert text:

```text
(up-get-indirect-goal ${1:typeOp} ${2:GoalId} ${3:OutputGoalId})
```

<a id="symbol-up-get-object-data"></a>

## `up-get-object-data`

- Kind: `command`
- Detail: Fact/Action - DUC

Syntax: `(up-get-object-data <ObjectData> <OutputGoalId>)`

Get specific information about the selected target object. This command can be used as either a Fact or an Action.

[AIRef](https://airef.github.io/commands/commands-details.html#up-get-object-data)

Completion insert text:

```text
(up-get-object-data ${1:ObjectData} ${2:OutputGoalId})
```

<a id="symbol-up-get-object-target-data"></a>

## `up-get-object-target-data`

- Kind: `command`
- Detail: Fact/Action - DUC

Syntax: `(up-get-object-target-data <ObjectData> <OutputGoalId>)`

Get specific information about the target object's target. This command can be used as either a Fact or an Action.

[AIRef](https://airef.github.io/commands/commands-details.html#up-get-object-target-data)

Completion insert text:

```text
(up-get-object-target-data ${1:ObjectData} ${2:OutputGoalId})
```

<a id="symbol-up-get-object-type-data"></a>

## `up-get-object-type-data`

- Kind: `command`
- Detail: Action - DUC, Game Info

Syntax: `(up-get-object-type-data <typeOp> <TypeId> <ObjectData> <OutputGoalId>)`

Get generic information about an object type. This can be expensive, so please consider performance.

[AIRef](https://airef.github.io/commands/commands-details.html#up-get-object-type-data)

Completion insert text:

```text
(up-get-object-type-data ${1:typeOp} ${2:TypeId} ${3:ObjectData} ${4:OutputGoalId})
```

<a id="symbol-up-get-path-distance"></a>

## `up-get-path-distance`

- Kind: `command`
- Detail: Action - DUC, Points

Syntax: `(up-get-path-distance <Point> <Option> <OutputGoalId>)`

Get the distance from the target object to a specified point goal pair. This will return 65535 if the point is unreachable. Set the Option parameter to 1 to require an open destination tile to find the path distance toward or 0 to allow for a few tiles of separation to find a reachable open tile.

[AIRef](https://airef.github.io/commands/commands-details.html#up-get-path-distance)

Completion insert text:

```text
(up-get-path-distance ${1:Point} ${2:Option} ${3:OutputGoalId})
```

<a id="symbol-up-get-player-color"></a>

## `up-get-player-color`

- Kind: `command`
- Detail: Action - Other Player Info, Player Facts, Text Data

Syntax: `(up-get-player-color <PlayerNumber> <ColorId>)`

Get the color id and store the name in the internal butter. ColorId will range from 1 to 8. The buffer can be referenced by the chat-data commands using %s instead of %d with c: 7031232 (7031232 cannot be stored in a defconst). This buffer is shared by all AIs, so please store data before using it in a rule pass. The action only allows for exact player numbers, "my-player-number", or "this-any" rule variables for pPlayerNumber, such as this-any-ally or this-any-enemy. It does not allow "any"/"every" wildcard parameters for pPlayerNumber. It also allows for scenario-player-# and lobby-player-#, where # is between 1 and 8. scenario-player-# refers to the player color (where red = scenario-player-2), and lobby-player-# refers to the player slot (where the lobby host or human player playing a single player campaign is always lobby-player-1).

[AIRef](https://airef.github.io/commands/commands-details.html#up-get-player-color)

Completion insert text:

```text
(up-get-player-color ${1:PlayerNumber} ${2:ColorId})
```

<a id="symbol-up-get-player-fact"></a>

## `up-get-player-fact`

- Kind: `command`
- Detail: Fact/Action - Other Player Info, Player Facts

Syntax: `(up-get-player-fact <PlayerNumber> <FactId> <FactParameter> <OutputGoalId>)`

Read a fact for a specific player into a goal. This command can be used as either a fact or an action. For better performance, please use one of the more direct commands from the up-get-fact series whenever possible. The action only allows for exact player numbers, "my-player-number", or "this-any" rule variables for pPlayerNumber, such as this-any-ally or this-any-enemy. It does not allow "any"/"every" wildcard parameters for pPlayerNumber. It also allows for scenario-player-# and lobby-player-#, where # is between 1 and 8. scenario-player-# refers to the player color (where red = scenario-player-2), and lobby-player-# refers to the player slot (where the lobby host or human player playing a single player campaign is always lobby-player-1).

[AIRef](https://airef.github.io/commands/commands-details.html#up-get-player-fact)

Completion insert text:

```text
(up-get-player-fact ${1:PlayerNumber} ${2:FactId} ${3:FactParameter} ${4:OutputGoalId})
```

<a id="symbol-up-get-point"></a>

## `up-get-point`

- Kind: `command`
- Detail: Action - Points

Syntax: `(up-get-point <PositionType> <Point>)`

Read a specific (x,y) position into an extended goal pair. This command writes to 2 consecutive goals and requires an extended goal pair between 41 and 15998. If it fails to get a valid position, it will return (-1,-1).

[AIRef](https://airef.github.io/commands/commands-details.html#up-get-point)

Completion insert text:

```text
(up-get-point ${1:PositionType} ${2:Point})
```

<a id="symbol-up-get-point-contains"></a>

## `up-get-point-contains`

- Kind: `command`
- Detail: Fact/Action - Points

Syntax: `(up-get-point-contains <Point> <OutputGoalId> <typeOp> <ObjectId>)`

Get the id if an object exists at a point goal pair position. Set Point to 0 to use the point that is stored by up-set-target-point. Please note that when used with all-units-class (-1), this may capture unexpected objects like birds flying over a tile, terrain plants, etc. This command can be used as either a Fact or an Action. Also, this action will work whether the point has been explored or not. Therefore, in AI tournaments up-point-explored must be used as a condition in every rule where this command is used.

[AIRef](https://airef.github.io/commands/commands-details.html#up-get-point-contains)

Completion insert text:

```text
(up-get-point-contains ${1:Point} ${2:OutputGoalId} ${3:typeOp} ${4:ObjectId})
```

<a id="symbol-up-get-point-distance"></a>

## `up-get-point-distance`

- Kind: `command`
- Detail: Action - Points

Syntax: `(up-get-point-distance <Point> <Point> <OutputGoalId>)`

Get the distance between two point goal pairs. Set Point2 to 0 to use the point that is stored by up-set-target-point. This command does not bound the points to the map, meaning you can use it for more general calculations. It simply calculates the distance formula. When calculating the distance between two precise points, it will calculate a precise distance, where the distance is 100 times larger than the actual distance.

[AIRef](https://airef.github.io/commands/commands-details.html#up-get-point-distance)

Completion insert text:

```text
(up-get-point-distance ${1:Point} ${2:Point} ${3:OutputGoalId})
```

<a id="symbol-up-get-point-elevation"></a>

## `up-get-point-elevation`

- Kind: `command`
- Detail: Action - Points

Syntax: `(up-get-point-elevation <Point> <OutputGoalId>)`

Get the elevation for a tile with a point goal pair.

[AIRef](https://airef.github.io/commands/commands-details.html#up-get-point-elevation)

Completion insert text:

```text
(up-get-point-elevation ${1:Point} ${2:OutputGoalId})
```

<a id="symbol-up-get-point-terrain"></a>

## `up-get-point-terrain`

- Kind: `command`
- Detail: Action - Points

Syntax: `(up-get-point-terrain <Point> <Terrain>)`

Get the terrain id at a specific point goal pair position. Set Point to 0 to use the point that is stored by up-set-target-point.

[AIRef](https://airef.github.io/commands/commands-details.html#up-get-point-terrain)

Completion insert text:

```text
(up-get-point-terrain ${1:Point} ${2:Terrain})
```

<a id="symbol-up-get-point-zone"></a>

## `up-get-point-zone`

- Kind: `command`
- Detail: Action - Points

Syntax: `(up-get-point-zone <Point> <OutputGoalId>)`

Get the zone for a tile with a point goal pair. Zone ids may differ if you have no villagers.

[AIRef](https://airef.github.io/commands/commands-details.html#up-get-point-zone)

Completion insert text:

```text
(up-get-point-zone ${1:Point} ${2:OutputGoalId})
```

<a id="symbol-up-get-precise-time"></a>

## `up-get-precise-time`

- Kind: `command`
- Detail: Action - Game Info

Syntax: `(up-get-precise-time <OptionGoalId> <OutputGoalId>)`

Get a system timestamp or the elapsed time into a goal. The OptionGoalId parameter determines whether a system timestamp is retrieved or the elapsed time since a previous system timestamp is retrieved. To get a system timestamp, use 0 for the OptionGoalId parameter. To get the elapsed time since a timestamp, use a pGoalId that is currently storing a system timestamp for the OptionGoalId parameter. The system timestamp or elapsed time will be stored in the OutputGoal.

[AIRef](https://airef.github.io/commands/commands-details.html#up-get-precise-time)

Completion insert text:

```text
(up-get-precise-time ${1:OptionGoalId} ${2:OutputGoalId})
```

<a id="symbol-up-get-projectile-player"></a>

## `up-get-projectile-player`

- Kind: `command`
- Detail: Action - Defense

Syntax: `(up-get-projectile-player <ProjectileType> <OutputGoalId>)`

Get the enemy player that last attacked with a specific type of projectile.

[AIRef](https://airef.github.io/commands/commands-details.html#up-get-projectile-player)

Completion insert text:

```text
(up-get-projectile-player ${1:ProjectileType} ${2:OutputGoalId})
```

<a id="symbol-up-get-rule-id"></a>

## `up-get-rule-id`

- Kind: `command`
- Detail: Action - Rule Jumps

Syntax: `(up-get-rule-id <GoalId>)`

Get the zero-based id for the current rule within the rule set. This id can be used with up-jump-direct to precisely control jump destinations.

[AIRef](https://airef.github.io/commands/commands-details.html#up-get-rule-id)

Completion insert text:

```text
(up-get-rule-id ${1:GoalId})
```

<a id="symbol-up-get-search-state"></a>

## `up-get-search-state`

- Kind: `command`
- Detail: Action - DUC

Syntax: `(up-get-search-state <OutputGoalId>)`

Get the search state into 4 consecutive extended goals. The goals will be filled with data in the following order: current local search total, last local search count, current remote search total, last remote search count.

[AIRef](https://airef.github.io/commands/commands-details.html#up-get-search-state)

Completion insert text:

```text
(up-get-search-state ${1:OutputGoalId})
```

<a id="symbol-up-get-shared-goal"></a>

## `up-get-shared-goal`

- Kind: `command`
- Detail: Action - Goals, Other Player Info

Syntax: `(up-get-shared-goal <typeOp> <SharedGoalId> <Value>)`

Get the value of a shared goal.

[AIRef](https://airef.github.io/commands/commands-details.html#up-get-shared-goal)

Completion insert text:

```text
(up-get-shared-goal ${1:typeOp} ${2:SharedGoalId} ${3:Value})
```

<a id="symbol-up-get-signal"></a>

## `up-get-signal`

- Kind: `command`
- Detail: Action - Scenarios

Syntax: `(up-get-signal <typeOp> <SignalId> <Value>)`

Get the value of a scenario trigger signal.

[AIRef](https://airef.github.io/commands/commands-details.html#up-get-signal)

Completion insert text:

```text
(up-get-signal ${1:typeOp} ${2:SignalId} ${3:Value})
```

<a id="symbol-up-get-target-fact"></a>

## `up-get-target-fact`

- Kind: `command`
- Detail: Fact/Action - Other Player Info, Player Facts

Syntax: `(up-get-target-fact <FactId> <FactParameter> <OutputGoalId>)`

Read a fact for the target-player into a goal. This command can be used as either a fact or an action.

[AIRef](https://airef.github.io/commands/commands-details.html#up-get-target-fact)

Completion insert text:

```text
(up-get-target-fact ${1:FactId} ${2:FactParameter} ${3:OutputGoalId})
```

<a id="symbol-up-get-threat-data"></a>

## `up-get-threat-data`

- Kind: `command`
- Detail: Action - Defense

Syntax: `(up-get-threat-data <ThreatTime> <ThreatPlayer> <ThreatSource> <ThreatTarget>)`

Get the elapsed time, player, source, and target of the last threat and store them in the four specified goals. This command returns the absolute, most recent attack information before the rule pass begins. If the last attack event was from a p2 archer against one of your villagers, you'll get "time, 2, 900, 904" in return (900 = archery-class, 904 = villager-class). In an epic battle, it would become relatively useless in determining what is going on.

[AIRef](https://airef.github.io/commands/commands-details.html#up-get-threat-data)

Completion insert text:

```text
(up-get-threat-data ${1:ThreatTime} ${2:ThreatPlayer} ${3:ThreatSource} ${4:ThreatTarget})
```

<a id="symbol-up-get-timer"></a>

## `up-get-timer`

- Kind: `command`
- Detail: Action - Timers

Syntax: `(up-get-timer <typeOp> <TimerId> <OutputGoalId>)`

Get the trigger time for a timer in milliseconds.

[AIRef](https://airef.github.io/commands/commands-details.html#up-get-timer)

Completion insert text:

```text
(up-get-timer ${1:typeOp} ${2:TimerId} ${3:OutputGoalId})
```

<a id="symbol-up-get-treaty-data"></a>

## `up-get-treaty-data`

- Kind: `command`
- Detail: Action - Diplomacy, Game Info

Syntax: `(up-get-treaty-data <OutputGoalId>)`

DE only. Stores the remaining treaty time in seconds into a goal. Treaty time is the amount of time left in treaty games where players cannot attack each other.

[AIRef](https://airef.github.io/commands/commands-details.html#up-get-treaty-data)

Completion insert text:

```text
(up-get-treaty-data ${1:OutputGoalId})
```

<a id="symbol-up-get-upgrade-id"></a>

## `up-get-upgrade-id`

- Kind: `command`
- Detail: Action - DUC, Game Info

Syntax: `(up-get-upgrade-id <PlayerNumber> <Option> <GoalId> <OutputGoalId>)`

Get the upgrade type id for an object into a goal. Set the Option parameter to 1 to get the current type id for counting, otherwise 0. The action only allows for exact player numbers, "my-player-number", or "this-any" rule variables for pPlayerNumber, such as this-any-ally or this-any-enemy. It does not allow "any"/"every" wildcard parameters for pPlayerNumber. It also allows for scenario-player-# and lobby-player-#, where # is between 1 and 8. scenario-player-# refers to the player color (where red = scenario-player-2), and lobby-player-# refers to the player slot (where the lobby host or human player playing a single player campaign is always lobby-player-1).

[AIRef](https://airef.github.io/commands/commands-details.html#up-get-upgrade-id)

Completion insert text:

```text
(up-get-upgrade-id ${1:PlayerNumber} ${2:Option} ${3:GoalId} ${4:OutputGoalId})
```

<a id="symbol-up-get-victory-data"></a>

## `up-get-victory-data`

- Kind: `command`
- Detail: Action - Game Info

Syntax: `(up-get-victory-data <VictoryPlayer> <VictoryType> <VictoryTime>)`

Get standard victory status information into the provided goals.

[AIRef](https://airef.github.io/commands/commands-details.html#up-get-victory-data)

Completion insert text:

```text
(up-get-victory-data ${1:VictoryPlayer} ${2:VictoryType} ${3:VictoryTime})
```

<a id="symbol-up-get-victory-limit"></a>

## `up-get-victory-limit`

- Kind: `command`
- Detail: Action - Game Info

Syntax: `(up-get-victory-limit <OutputGoalId>)`

Get the time or score victory limit into the provided goal.

[AIRef](https://airef.github.io/commands/commands-details.html#up-get-victory-limit)

Completion insert text:

```text
(up-get-victory-limit ${1:OutputGoalId})
```

<a id="symbol-up-group-size"></a>

## `up-group-size`

- Kind: `command`
- Detail: Fact - DUC, DUC Groups

Syntax: `(up-group-size <typeOp> <GroupId> <compareOp> <Value>)`

Check the current number of units in a search group.

[AIRef](https://airef.github.io/commands/commands-details.html#up-group-size)

Completion insert text:

```text
(up-group-size ${1:typeOp} ${2:GroupId} ${3:compareOp} ${4:Value})
```

<a id="symbol-up-guard-unit"></a>

## `up-guard-unit`

- Kind: `command`
- Detail: Action - Units

Syntax: `(up-guard-unit <ObjectId> <typeOp> <UnitId>)`

Set a single unit of a specific type to protect a random instance of another, as long as they are on the same continent. my-unique-unit, my-elite-unique-unit, and my-unique-unit-line can be used for the UnitId, which will automatically get the UnitId of the unique unit, elite unique unit, or unique unit line that the AI's civ can train from the castle.

[AIRef](https://airef.github.io/commands/commands-details.html#up-guard-unit)

Completion insert text:

```text
(up-guard-unit ${1:ObjectId} ${2:typeOp} ${3:UnitId})
```

<a id="symbol-up-idle-unit-count"></a>

## `up-idle-unit-count`

- Kind: `command`
- Detail: Fact - Counting, Economy, Units

Syntax: `(up-idle-unit-count <IdleType> <compareOp> <Value>)`

Check the number of idle units for the specified type.

[AIRef](https://airef.github.io/commands/commands-details.html#up-idle-unit-count)

Completion insert text:

```text
(up-idle-unit-count ${1:IdleType} ${2:compareOp} ${3:Value})
```

<a id="symbol-up-jump-direct"></a>

## `up-jump-direct`

- Kind: `command`
- Detail: Action - Rule Jumps

Syntax: `(up-jump-direct <typeOp> <RuleId>)`

Jump directly within the current rule set. Please ensure that the rule you are jumping to actually exists. You can use up-get-rule-id to get a valid rule id to jump to. With this action, you can either decrease rules per pass with intelligent skips, or greatly increase it with loops. Please consider game performance.

[AIRef](https://airef.github.io/commands/commands-details.html#up-jump-direct)

Completion insert text:

```text
(up-jump-direct ${1:typeOp} ${2:RuleId})
```

<a id="symbol-up-jump-dynamic"></a>

## `up-jump-dynamic`

- Kind: `command`
- Detail: Action - Rule Jumps

Syntax: `(up-jump-dynamic <typeOp> <RuleDelta>)`

Jump dynamically within the current rule set. Never use this command where #load-if-defined or #load-if-not-defined blocks may make your jump target unreliable. Please ensure that the rule you are jumping to actually exists. With this action, you can either decrease rules per pass with intelligent skips, or greatly increase it with loops. Please consider game performance.

[AIRef](https://airef.github.io/commands/commands-details.html#up-jump-dynamic)

Completion insert text:

```text
(up-jump-dynamic ${1:typeOp} ${2:RuleDelta})
```

<a id="symbol-up-jump-rule"></a>

## `up-jump-rule`

- Kind: `command`
- Detail: Action - Rule Jumps

Syntax: `(up-jump-rule <RuleDelta>)`

Jump forward or backward within the current rule set. Never use this command where #load-if-defined or #load-if-not-defined blocks may make your jump target unreliable. Please ensure that the rule you are jumping to actually exists. With this action, you can either decrease rules per pass with intelligent skips, or greatly increase it with loops. Please consider game performance.

[AIRef](https://airef.github.io/commands/commands-details.html#up-jump-rule)

Completion insert text:

```text
(up-jump-rule ${1:RuleDelta})
```

<a id="symbol-up-lerp-percent"></a>

## `up-lerp-percent`

- Kind: `command`
- Detail: Action - Points

Syntax: `(up-lerp-percent <Point> <Point> <typeOp> <Percent>)`

Interpolate a point by percentage between two point goal pairs and store the new point in Point1. The Percent parameter specifies the percentage of the distance between the two points that the new point will move toward or away from Point1 to Point2. If Value is positive, the new point will move closer to Point2. If Value is negative, the new point will move further away from Point2. Set Point2 to 0 to use the point that is stored by up-set-target-point.

[AIRef](https://airef.github.io/commands/commands-details.html#up-lerp-percent)

Completion insert text:

```text
(up-lerp-percent ${1:Point} ${2:Point} ${3:typeOp} ${4:Percent})
```

<a id="symbol-up-lerp-tiles"></a>

## `up-lerp-tiles`

- Kind: `command`
- Detail: Action - Points

Syntax: `(up-lerp-tiles <Point> <Point> <typeOp> <Value>)`

Interpolate a point by tiles between two point goal pairs and store the new point in Point1. The Value parameter specifies how many tiles the new point will move toward or away from Point1 to Point2. If Value is positive, the new point will move closer to Point2. If Value is negative, the new point will move further away from Point2. Set Point2 to 0 to use the point that is stored by up-set-target-point. Note: It is possible for the new point to be outside the bounds of the map which can cause several issues. Therefore, it is wise to use up-bound-point afterward to ensure that you always have a valid point location.

[AIRef](https://airef.github.io/commands/commands-details.html#up-lerp-tiles)

Completion insert text:

```text
(up-lerp-tiles ${1:Point} ${2:Point} ${3:typeOp} ${4:Value})
```

<a id="symbol-up-log-data"></a>

## `up-log-data`

- Kind: `command`
- Detail: Action - Debugging

Syntax: `(up-log-data <Option> <String> <typeOp> <Value>)`

Write a formatted text line to aoelog.txt. Set Option to 1 in order to write plain text. You must close the game in order to open aoelog.txt, which is located in the game folder, usually at "C:\Program Files (x86)\Microsoft Games\Age of Empires II". Please consider game performance when writing data. To log a message without referencing any data, simply leave the %d out of the chat message and use 'c: 0' as the last two parameters. In DE, this command does not write the data to an aoelog.txt file. Instead, you need to launch the game with the parameters 'LOGSYSTEMS=AIScript' and 'VERBOSELOGGING' (case sensitive)To do this with the Steam version, open your Steam games library with the Steam client, right click on Age of Empires II: Definitive Edition in the left sidebar that lists the games you own, and click Properties. In the Properties window, under the General tab, type the parameters above separated by spaces. Then, when you launch the game these parameters will be active. Unless you use the launch parameter CONSTANTLOGGING, DE will not create the log file until the game has closed. The log produced in DE will be found in the Steam user folder, usually something like "C:\Users\[user ID]\Games\Age of Empires 2 DE\logs" but note that this log isn't just used by the AI (it would be best to log something identifying the AI log at the start of the game), some of these logs with VERBOSELOGGING can get quite large so it might be a good idea to periodically clean out the folder. Here's a full list of recommended Steam launch parameters: SKIPINTRO DEBUGSPEEDS AIDEBUGGING LOGSYSTEMS=AIScript VERBOSELOGGING CONSTANTLOGGING. This allows you to skip the intro cinematic, increase the game speed up to 8.0 speed (beware that AI performance suffers noticeably past 2.0 speed and especially at 8.0 speed), allows for AI scripting logs, and writes to the log file continuously, rather than only when exiting the game.

[AIRef](https://airef.github.io/commands/commands-details.html#up-log-data)

Completion insert text:

```text
(up-log-data ${1:Option} ${2:String} ${3:typeOp} ${4:Value})
```

<a id="symbol-up-modify-escrow"></a>

## `up-modify-escrow`

- Kind: `command`
- Detail: Action - Economy

Syntax: `(up-modify-escrow <Resource> <mathOp> <Value>)`

Perform math operations to adjust escrowed resources.

[AIRef](https://airef.github.io/commands/commands-details.html#up-modify-escrow)

Completion insert text:

```text
(up-modify-escrow ${1:Resource} ${2:mathOp} ${3:Value})
```

<a id="symbol-up-modify-flag"></a>

## `up-modify-flag`

- Kind: `command`
- Detail: Action - Goals

Syntax: `(up-modify-flag <GoalId> <mathOp> <Flag>)`

Modify a bitwise flag on the value stored in a goal variable. Flags allow multiple states to be stored in a single value by using powers of 2 (1, 2, 4, 8, 16, etc.). The only ops allowed are [cgs]:+ to append a flag and [cgs]:- to remove a flag.

[AIRef](https://airef.github.io/commands/commands-details.html#up-modify-flag)

Completion insert text:

```text
(up-modify-flag ${1:GoalId} ${2:mathOp} ${3:Flag})
```

<a id="symbol-up-modify-goal"></a>

## `up-modify-goal`

- Kind: `command`
- Detail: Fact/Action - Goals

Syntax: `(up-modify-goal <GoalId> <mathOp> <Value>)`

Perform math operations on the value stored in a goal variable. This command can be used as either a Fact or an Action, meaning the command can appear before the "=>" in the rule or after it. The behavior of the command is identical, regardless of whether it is used as a Fact or as an Action. This command is a much more flexible version of the set-goal command, which only allows you to set a goal to a specific value. up-modify-goal allows you to add, subtract, multiply, divide, find remainders, find percentages, find min and max values, and do other mathematical operations, either with specific numbers or with the values currently stored in a goal or strategic number. See the pMathOp page for a full list of all the operations available, along with in-depth examples of each operation.

[AIRef](https://airef.github.io/commands/commands-details.html#up-modify-goal)

Completion insert text:

```text
(up-modify-goal ${1:GoalId} ${2:mathOp} ${3:Value})
```

<a id="symbol-up-modify-group-flag"></a>

## `up-modify-group-flag`

- Kind: `command`
- Detail: Action - DUC, DUC Groups

Syntax: `(up-modify-group-flag <Option> <typeOp> <GroupId>)`

Modify the control group flag for units in a search group. You must manage the group flag carefully in order to avoid unexpected situations. Please remove the group flag before modifying a flagged search group. You can find units from a flagged search group using object-data-group-flag, which is set to the group id. Because this command modifies the object-data-group-flag of the units themselves, AI scripters must ensure that objects owned by other players are not stored in the AI's search group before using this command. This can occur if a unit in search group is converted and now belongs to another player, and the AI scripter doesn't include code to remove converted units from the AI's search groups during each script pass. Changing the control group flag of other players' units, even accidentally, is considered cheating in AI tournaments.

[AIRef](https://airef.github.io/commands/commands-details.html#up-modify-group-flag)

Completion insert text:

```text
(up-modify-group-flag ${1:Option} ${2:typeOp} ${3:GroupId})
```

<a id="symbol-up-modify-sn"></a>

## `up-modify-sn`

- Kind: `command`
- Detail: Fact/Action - SNs

Syntax: `(up-modify-sn <SnId> <mathOp> <Value>)`

Perform math operations on a strategic number. In DE, this command can be used as either a fact or an action, but it can only be used as an action in UP and WK. When used as a fact, it will modify the strategic number just like it would if it was used in the actions section of the rule. The only difference when up-modify-sn is used as a fact is that if it to modify the strategic number (because of an invalid strategic number ID or an invalid value), then the rest of the rule won't execute.

[AIRef](https://airef.github.io/commands/commands-details.html#up-modify-sn)

Completion insert text:

```text
(up-modify-sn ${1:SnId} ${2:mathOp} ${3:Value})
```

<a id="symbol-up-object-data"></a>

## `up-object-data`

- Kind: `command`
- Detail: Fact - DUC

Syntax: `(up-object-data <ObjectData> <compareOp> <Value>)`

Check specific information about the selected target object.

[AIRef](https://airef.github.io/commands/commands-details.html#up-object-data)

Completion insert text:

```text
(up-object-data ${1:ObjectData} ${2:compareOp} ${3:Value})
```

<a id="symbol-up-object-target-data"></a>

## `up-object-target-data`

- Kind: `command`
- Detail: Fact - DUC

Syntax: `(up-object-target-data <ObjectData> <compareOp> <Value>)`

Check specific information about the target object's target.

[AIRef](https://airef.github.io/commands/commands-details.html#up-object-target-data)

Completion insert text:

```text
(up-object-target-data ${1:ObjectData} ${2:compareOp} ${3:Value})
```

<a id="symbol-up-object-type-count"></a>

## `up-object-type-count`

- Kind: `command`
- Detail: Fact - Buildings, Counting, Units

Syntax: `(up-object-type-count <typeOp> <ObjectId> <compareOp> <Value>)`

Combine unit-type-count and building-type-count checks.

[AIRef](https://airef.github.io/commands/commands-details.html#up-object-type-count)

Completion insert text:

```text
(up-object-type-count ${1:typeOp} ${2:ObjectId} ${3:compareOp} ${4:Value})
```

<a id="symbol-up-object-type-count-total"></a>

## `up-object-type-count-total`

- Kind: `command`
- Detail: Fact - Buildings, Counting, Units

Syntax: `(up-object-type-count-total <typeOp> <ObjectId> <compareOp> <Value>)`

Combine unit-type-count-total and building-type-count-total checks.

[AIRef](https://airef.github.io/commands/commands-details.html#up-object-type-count-total)

Completion insert text:

```text
(up-object-type-count-total ${1:typeOp} ${2:ObjectId} ${3:compareOp} ${4:Value})
```

<a id="symbol-up-path-distance"></a>

## `up-path-distance`

- Kind: `command`
- Detail: Fact - DUC, Points

Syntax: `(up-path-distance <Point> <Option> <compareOp> <Value>)`

Check the distance from the target object to a specified point goal pair. The distance will be 65535 if the point is unreachable. Set the Option parameter to 1 to require an open destination tile to find the path distance toward or 0 to allow for a few tiles of separation to find a reachable open tile.

[AIRef](https://airef.github.io/commands/commands-details.html#up-path-distance)

Completion insert text:

```text
(up-path-distance ${1:Point} ${2:Option} ${3:compareOp} ${4:Value})
```

<a id="symbol-up-pending-objects"></a>

## `up-pending-objects`

- Kind: `command`
- Detail: Fact - Counting, Units

Syntax: `(up-pending-objects <typeOp> <ObjectId> <compareOp> <Value>)`

Perform a comparison with the pending count of an object.

[AIRef](https://airef.github.io/commands/commands-details.html#up-pending-objects)

Completion insert text:

```text
(up-pending-objects ${1:typeOp} ${2:ObjectId} ${3:compareOp} ${4:Value})
```

<a id="symbol-up-pending-placement"></a>

## `up-pending-placement`

- Kind: `command`
- Detail: Fact - Buildings, Can Do

Syntax: `(up-pending-placement <typeOp> <BuildingId>)`

Check if a specific type of building is waiting for placement.

[AIRef](https://airef.github.io/commands/commands-details.html#up-pending-placement)

Completion insert text:

```text
(up-pending-placement ${1:typeOp} ${2:BuildingId})
```

<a id="symbol-up-player-distance"></a>

## `up-player-distance`

- Kind: `command`
- Detail: Fact - Other Player Info

Syntax: `(up-player-distance <PlayerNumber> <compareOp> <Value>)`

Check the distance in tiles to the nearest building of another player. The action allows "focus-player", "target-player", and "any"/"every" wildcard parameters for pPlayerNumber. It cannot be used with players who aren't allies. It also allows for scenario-player-# and lobby-player-#, where # is between 1 and 8. scenario-player-# refers to the player color (where red = scenario-player-2), and lobby-player-# refers to the player slot (where the lobby host or human player playing a single player campaign is always lobby-player-1).

[AIRef](https://airef.github.io/commands/commands-details.html#up-player-distance)

Completion insert text:

```text
(up-player-distance ${1:PlayerNumber} ${2:compareOp} ${3:Value})
```

<a id="symbol-up-players-in-game"></a>

## `up-players-in-game`

- Kind: `command`
- Detail: Fact - Diplomacy, Other Player Info

Syntax: `(up-players-in-game <PlayerStance> <compareOp> <Value>)`

Check the number of active players in the game of the specified stance. Players are considered allied with themselves, so "ally" will include the AI player itself.

[AIRef](https://airef.github.io/commands/commands-details.html#up-players-in-game)

Completion insert text:

```text
(up-players-in-game ${1:PlayerStance} ${2:compareOp} ${3:Value})
```

<a id="symbol-up-point-contains"></a>

## `up-point-contains`

- Kind: `command`
- Detail: Fact - Buildings, Points, Units

Syntax: `(up-point-contains <Point> <typeOp> <ObjectId>)`

Check if an object exists at a point goal pair position. Set Point to 0 to use the point that is stored by up-set-target-point. Please note that when used with all-units-class (-1), this may capture unexpected objects like birds flying over a tile, terrain plants, etc. Also, this action will work whether the point has been explored or not. Therefore, in AI tournaments up-point-explored must be used as a condition in every rule where this command is used.

[AIRef](https://airef.github.io/commands/commands-details.html#up-point-contains)

Completion insert text:

```text
(up-point-contains ${1:Point} ${2:typeOp} ${3:ObjectId})
```

<a id="symbol-up-point-distance"></a>

## `up-point-distance`

- Kind: `command`
- Detail: Fact - Points

Syntax: `(up-point-distance <Point> <Point> <compareOp> <Value>)`

Perform a distance check between two point goal pairs. Set Point2 to 0 to use the point that is stored by up-set-target-point.

[AIRef](https://airef.github.io/commands/commands-details.html#up-point-distance)

Completion insert text:

```text
(up-point-distance ${1:Point} ${2:Point} ${3:compareOp} ${4:Value})
```

<a id="symbol-up-point-elevation"></a>

## `up-point-elevation`

- Kind: `command`
- Detail: Fact - Points

Syntax: `(up-point-elevation <Point> <compareOp> <Value>)`

Check the elevation for a tile with a point goal pair.

[AIRef](https://airef.github.io/commands/commands-details.html#up-point-elevation)

Completion insert text:

```text
(up-point-elevation ${1:Point} ${2:compareOp} ${3:Value})
```

<a id="symbol-up-point-explored"></a>

## `up-point-explored`

- Kind: `command`
- Detail: Fact - Points

Syntax: `(up-point-explored <Point> <compareOp> <ExploredState>)`

Check if a point on the map has been explored. Set Point to 0 to use the point that is stored by up-set-target-point.

[AIRef](https://airef.github.io/commands/commands-details.html#up-point-explored)

Completion insert text:

```text
(up-point-explored ${1:Point} ${2:compareOp} ${3:ExploredState})
```

<a id="symbol-up-point-terrain"></a>

## `up-point-terrain`

- Kind: `command`
- Detail: Fact - Points

Syntax: `(up-point-terrain <Point> <compareOp> <Terrain>)`

Perform a terrain id at a point goal pair position. Set Point to 0 to use the point that is stored by up-set-target-point.

[AIRef](https://airef.github.io/commands/commands-details.html#up-point-terrain)

Completion insert text:

```text
(up-point-terrain ${1:Point} ${2:compareOp} ${3:Terrain})
```

<a id="symbol-up-point-zone"></a>

## `up-point-zone`

- Kind: `command`
- Detail: Fact - Points

Syntax: `(up-point-zone <Point> <compareOp> <Value>)`

Check the zone for a tile with a point goal pair. Zone ids may differ if you have no villagers.

[AIRef](https://airef.github.io/commands/commands-details.html#up-point-zone)

Completion insert text:

```text
(up-point-zone ${1:Point} ${2:compareOp} ${3:Value})
```

<a id="symbol-up-projectile-detected"></a>

## `up-projectile-detected`

- Kind: `command`
- Detail: Fact - Defense

Syntax: `(up-projectile-detected <ProjectileType> <compareOp> <Value>)`

Check the elapsed time in milliseconds since a type of projectile was fired at the AI.

[AIRef](https://airef.github.io/commands/commands-details.html#up-projectile-detected)

Completion insert text:

```text
(up-projectile-detected ${1:ProjectileType} ${2:compareOp} ${3:Value})
```

<a id="symbol-up-projectile-target"></a>

## `up-projectile-target`

- Kind: `command`
- Detail: Fact - Defense

Syntax: `(up-projectile-target <ProjectileType> <compareOp> <ClassId>)`

Check the class of the target of a projectile that was fired at the AI.

[AIRef](https://airef.github.io/commands/commands-details.html#up-projectile-target)

Completion insert text:

```text
(up-projectile-target ${1:ProjectileType} ${2:compareOp} ${3:ClassId})
```

<a id="symbol-up-release-escrow"></a>

## `up-release-escrow`

- Kind: `command`
- Detail: Action - Economy

Syntax: `(up-release-escrow)`

Set all escrow amounts to 0 with a single command.

[AIRef](https://airef.github.io/commands/commands-details.html#up-release-escrow)

Completion insert text:

```text
(up-release-escrow)
```

<a id="symbol-up-remaining-boar-amount"></a>

## `up-remaining-boar-amount`

- Kind: `command`
- Detail: Fact - Economy

Syntax: `(up-remaining-boar-amount <compareOp> <Value>)`

Check the amount of food remaining on the current boar. This data is only valid if the boar is lured with strategic numbers (not Direct Unit Control), while another boar is targetable and available to hunt. If this is not the case, it remains invalid (65535) to signify that this is the final boar.

[AIRef](https://airef.github.io/commands/commands-details.html#up-remaining-boar-amount)

Completion insert text:

```text
(up-remaining-boar-amount ${1:compareOp} ${2:Value})
```

<a id="symbol-up-remove-objects"></a>

## `up-remove-objects`

- Kind: `command`
- Detail: Action - DUC

Syntax: `(up-remove-objects <SearchSource> <ObjectData> <compareOp> <Value>)`

Removes objects from the search results based on specific data. If ObjectData is set to -1, the object index in the search results will be used for data comparison when performing removal.

[AIRef](https://airef.github.io/commands/commands-details.html#up-remove-objects)

Completion insert text:

```text
(up-remove-objects ${1:SearchSource} ${2:ObjectData} ${3:compareOp} ${4:Value})
```

<a id="symbol-up-request-hunters"></a>

## `up-request-hunters`

- Kind: `command`
- Detail: Action - Economy

Syntax: `(up-request-hunters <typeOp> <Value>)`

Attempt to request support hunters for the active boar lure. This only applies to boars that are lured with strategic numbers (not Direct Unit Control). It is not guaranteed to reach the total number of requested hunters.

[AIRef](https://airef.github.io/commands/commands-details.html#up-request-hunters)

Completion insert text:

```text
(up-request-hunters ${1:typeOp} ${2:Value})
```

<a id="symbol-up-research"></a>

## `up-research`

- Kind: `command`
- Detail: Action - Techs

Syntax: `(up-research <EscrowGoalId> <typeOp> <TechId>)`

Add a technology to the research queue with dynamic values.

[AIRef](https://airef.github.io/commands/commands-details.html#up-research)

Completion insert text:

```text
(up-research ${1:EscrowGoalId} ${2:typeOp} ${3:TechId})
```

<a id="symbol-up-research-status"></a>

## `up-research-status`

- Kind: `command`
- Detail: Fact - Techs

Syntax: `(up-research-status <typeOp> <TechId> <compareOp> <ResearchState>)`

Check the research status of a specific technology.

[AIRef](https://airef.github.io/commands/commands-details.html#up-research-status)

Completion insert text:

```text
(up-research-status ${1:typeOp} ${2:TechId} ${3:compareOp} ${4:ResearchState})
```

<a id="symbol-up-reset-attack-now"></a>

## `up-reset-attack-now`

- Kind: `command`
- Detail: Action - Attack

Syntax: `(up-reset-attack-now)`

Reset the infinite targeting loop flag set by attack-now.

[AIRef](https://airef.github.io/commands/commands-details.html#up-reset-attack-now)

Completion insert text:

```text
(up-reset-attack-now)
```

<a id="symbol-up-reset-building"></a>

## `up-reset-building`

- Kind: `command`
- Detail: Action - Buildings

Syntax: `(up-reset-building <Option> <typeOp> <BuildingId>)`

Halt the activity and research of all buildings of a specific type. If the Option parameter is set to 1, buildings performing research will not be reset.

[AIRef](https://airef.github.io/commands/commands-details.html#up-reset-building)

Completion insert text:

```text
(up-reset-building ${1:Option} ${2:typeOp} ${3:BuildingId})
```

<a id="symbol-up-reset-cost-data"></a>

## `up-reset-cost-data`

- Kind: `command`
- Detail: Action - Cost Data

Syntax: `(up-reset-cost-data <GoalId>)`

Reset 4 consecutive goals storing cost data to 0.

[AIRef](https://airef.github.io/commands/commands-details.html#up-reset-cost-data)

Completion insert text:

```text
(up-reset-cost-data ${1:GoalId})
```

<a id="symbol-up-reset-filters"></a>

## `up-reset-filters`

- Kind: `command`
- Detail: Action - DUC

Syntax: `(up-reset-filters)`

Reset search indices and filter states for direct unit targeting. All filter states will be set to -1. Use up-reset-search to clear search results.

[AIRef](https://airef.github.io/commands/commands-details.html#up-reset-filters)

Completion insert text:

```text
(up-reset-filters)
```

<a id="symbol-up-reset-group"></a>

## `up-reset-group`

- Kind: `command`
- Detail: Action - DUC, DUC Groups

Syntax: `(up-reset-group <typeOp> <GroupId>)`

Clear all units in a search group.

[AIRef](https://airef.github.io/commands/commands-details.html#up-reset-group)

Completion insert text:

```text
(up-reset-group ${1:typeOp} ${2:GroupId})
```

<a id="symbol-up-reset-placement"></a>

## `up-reset-placement`

- Kind: `command`
- Detail: Action - Buildings

Syntax: `(up-reset-placement <typeOp> <BuildingId>)`

Clear the placement list for the specified building type when blocked. Please use with caution.

[AIRef](https://airef.github.io/commands/commands-details.html#up-reset-placement)

Completion insert text:

```text
(up-reset-placement ${1:typeOp} ${2:BuildingId})
```

<a id="symbol-up-reset-scouts"></a>

## `up-reset-scouts`

- Kind: `command`
- Detail: Action - Units

Syntax: `(up-reset-scouts)`

Halt and disband all soldier explore groups on land.

[AIRef](https://airef.github.io/commands/commands-details.html#up-reset-scouts)

Completion insert text:

```text
(up-reset-scouts)
```

<a id="symbol-up-reset-search"></a>

## `up-reset-search`

- Kind: `command`
- Detail: Action - DUC

Syntax: `(up-reset-search <LocalIndex> <LocalList> <RemoteIndex> <RemoteList>)`

Reset the search state for the direct unit targeting system. Each of the four parameters can be 0 or 1:If the first parameter is 1, the search memory from previous local searches is reset. This allows all local objects to be available for the next local search. If the first parameter is 0, objects from previous local searches since the last local list reset will not be available in the next search.If the second parameter is 1, the local list search results will be emptied. If the second parameter is 0, objects in the local list will remain in the local list.If the third parameter is 1, the search memory from previous remote searches is reset. This allows all remote objects to be available for the next remote search. If the third parameter is 0, objects from previous remote searches since the last remote list reset will not be available in the next search.If the fourth parameter is 1, the remote list search results will be emptied. If the fourth parameter is 0, objects in the remote list will remain in the remote list.

[AIRef](https://airef.github.io/commands/commands-details.html#up-reset-search)

Completion insert text:

```text
(up-reset-search ${1:LocalIndex} ${2:LocalList} ${3:RemoteIndex} ${4:RemoteList})
```

<a id="symbol-up-reset-target-priorities"></a>

## `up-reset-target-priorities`

- Kind: `command`
- Detail: Action - Attack, Defense

Syntax: `(up-reset-target-priorities <PriorityType> <Option>)`

Reset or clear offensive or defensive targeting priorities. Restore default priorities with 0. For defensive priorities, setting the Option parameter to 1 will reset all to -1. For offensive priorities, unit types will be reset to 0, while classes will be -1. Target units on -1 offensive priority will not hold the attention of attackers if a higher priority unit appears, and you may notice attack behavior that is a bit similar to how patrol selects its targets. If the target unit is not -1 priority, the attacker may retarget, but primarily to other units with the same offensive priority. Battering rams and cannon galleons prefer to attack non-moving targets, while all other units prefer moving targets.

[AIRef](https://airef.github.io/commands/commands-details.html#up-reset-target-priorities)

Completion insert text:

```text
(up-reset-target-priorities ${1:PriorityType} ${2:Option})
```

<a id="symbol-up-reset-unit"></a>

## `up-reset-unit`

- Kind: `command`
- Detail: Action - Units

Syntax: `(up-reset-unit <typeOp> <UnitId>)`

Halt the activity of all units of a specific type. This is equivalent to clicking the &quot;stop&quot; button. my-unique-unit, my-elite-unique-unit, and my-unique-unit-line can be used for the UnitId, which will automatically get the UnitId of the unique unit, elite unique unit, or unique unit line that the AI's civ can train from the castle.

[AIRef](https://airef.github.io/commands/commands-details.html#up-reset-unit)

Completion insert text:

```text
(up-reset-unit ${1:typeOp} ${2:UnitId})
```

<a id="symbol-up-resource-amount"></a>

## `up-resource-amount`

- Kind: `command`
- Detail: Fact - Economy

Syntax: `(up-resource-amount <ResourceType> <compareOp> <Value>)`

Perform a comparison with an internal resource value.

[AIRef](https://airef.github.io/commands/commands-details.html#up-resource-amount)

Completion insert text:

```text
(up-resource-amount ${1:ResourceType} ${2:compareOp} ${3:Value})
```

<a id="symbol-up-resource-percent"></a>

## `up-resource-percent`

- Kind: `command`
- Detail: Fact - Economy

Syntax: `(up-resource-percent <ResourceType> <compareOp> <Value>)`

Perform a comparison with an internal resource value * 100.

[AIRef](https://airef.github.io/commands/commands-details.html#up-resource-percent)

Completion insert text:

```text
(up-resource-percent ${1:ResourceType} ${2:compareOp} ${3:Value})
```

<a id="symbol-up-retask-gatherers"></a>

## `up-retask-gatherers`

- Kind: `command`
- Detail: Action - Economy

Syntax: `(up-retask-gatherers <Resource> <typeOp> <Value>)`

Retask a specific number of villagers gathering from a resource. This command will attempt to retask villagers to preferred resources after dropping the resources, and it also works with fishing ships.

[AIRef](https://airef.github.io/commands/commands-details.html#up-retask-gatherers)

Completion insert text:

```text
(up-retask-gatherers ${1:Resource} ${2:typeOp} ${3:Value})
```

<a id="symbol-up-retreat-now"></a>

## `up-retreat-now`

- Kind: `command`
- Detail: Action - Attack

Syntax: `(up-retreat-now)`

Retreat all military units to the home town center. Military units within 6 range of the home town center will not be told to retreat. Active explorers will not retreat. If explorers need to retreat, use up-reset-scouts before using this command. It should work with groups and idle units. There's a chance that you may need to disband attack groups before using it, though, by setting the attack group sns to 0 (sn-number-attack-groups, min, and max). It will also work with TSA units, unless an enemy building exists in max-town-size. In that case, TSA overrides the retreat, I think, and resends them to the target. It should also work with attack-now if you use up-reset-attack-now before using up-retreat-now.

[AIRef](https://airef.github.io/commands/commands-details.html#up-retreat-now)

Completion insert text:

```text
(up-retreat-now)
```

<a id="symbol-up-retreat-to"></a>

## `up-retreat-to`

- Kind: `command`
- Detail: Action - Attack

Syntax: `(up-retreat-to <ObjectId> <typeOp> <UnitId>)`

Retreat all units of a specific type to a random instance of another. Military units within 6 range of the retreat target object (the object in the first parameter) will not be told to retreat, to allow better defense of the retreat object, such as an offensive trebuchet or a castle. Active explorers will not retreat. If explorers need to retreat, use up-reset-scouts before using this command. my-unique-unit, my-elite-unique-unit, and my-unique-unit-line can be used for the UnitId, which will automatically get the UnitId of the unique unit, elite unique unit, or unique unit line that the AI's civ can train from the castle.

[AIRef](https://airef.github.io/commands/commands-details.html#up-retreat-to)

Completion insert text:

```text
(up-retreat-to ${1:ObjectId} ${2:typeOp} ${3:UnitId})
```

<a id="symbol-up-sell-commodity"></a>

## `up-sell-commodity`

- Kind: `command`
- Detail: Action - Economy, Trading

Syntax: `(up-sell-commodity <typeOp> <ResourceType> <typeOp> <Value>)`

Sell a variable amount of resources at the market. The actual amount you sell depends on available resources.

[AIRef](https://airef.github.io/commands/commands-details.html#up-sell-commodity)

Completion insert text:

```text
(up-sell-commodity ${1:typeOp} ${2:ResourceType} ${3:typeOp} ${4:Value})
```

<a id="symbol-up-send-flare"></a>

## `up-send-flare`

- Kind: `command`
- Detail: Action - Debugging, Other Player Info, Points

Syntax: `(up-send-flare <Point>)`

Send a flare to allies from a point goal pair.

[AIRef](https://airef.github.io/commands/commands-details.html#up-send-flare)

Completion insert text:

```text
(up-send-flare ${1:Point})
```

<a id="symbol-up-send-scout"></a>

## `up-send-scout`

- Kind: `command`
- Detail: Action - Points

Syntax: `(up-send-scout <GroupType> <ScoutMethod>)`

Send a land or water scout to a specific location.

[AIRef](https://airef.github.io/commands/commands-details.html#up-send-scout)

Completion insert text:

```text
(up-send-scout ${1:GroupType} ${2:ScoutMethod})
```

<a id="symbol-up-set-attack-stance"></a>

## `up-set-attack-stance`

- Kind: `command`
- Detail: Action - Units

Syntax: `(up-set-attack-stance <UnitId> <typeOp> <AttackStance>)`

Set the attack stance for all units of a specific type.

[AIRef](https://airef.github.io/commands/commands-details.html#up-set-attack-stance)

Completion insert text:

```text
(up-set-attack-stance ${1:UnitId} ${2:typeOp} ${3:AttackStance})
```

<a id="symbol-up-set-defense-priority"></a>

## `up-set-defense-priority`

- Kind: `command`
- Detail: Action - Attack, Defense

Syntax: `(up-set-defense-priority <typeOp> <BuildingId> <typeOp> <Value>)`

Set the defensive (TSA) targeting priority for a building. This has no effect against units. Also, unit lines do not work here, so just set the base unit type id (spearman for the entire spearman-line, etc.). Classes may be used, as well. For walls, use class 927; for gates, use class 939.

[AIRef](https://airef.github.io/commands/commands-details.html#up-set-defense-priority)

Completion insert text:

```text
(up-set-defense-priority ${1:typeOp} ${2:BuildingId} ${3:typeOp} ${4:Value})
```

<a id="symbol-up-set-event"></a>

## `up-set-event`

- Kind: `command`
- Detail: Action - Scenarios

Syntax: `(up-set-event <typeOp> <EventId> <typeOp> <Value>)`

Set the value of a scenario trigger event.

[AIRef](https://airef.github.io/commands/commands-details.html#up-set-event)

Completion insert text:

```text
(up-set-event ${1:typeOp} ${2:EventId} ${3:typeOp} ${4:Value})
```

<a id="symbol-up-set-group"></a>

## `up-set-group`

- Kind: `command`
- Detail: Action - DUC, DUC Groups

Syntax: `(up-set-group <SearchSource> <typeOp> <GroupId>)`

Set the local or remote search results to a search group.

[AIRef](https://airef.github.io/commands/commands-details.html#up-set-group)

Completion insert text:

```text
(up-set-group ${1:SearchSource} ${2:typeOp} ${3:GroupId})
```

<a id="symbol-up-set-indirect-goal"></a>

## `up-set-indirect-goal`

- Kind: `command`
- Detail: Action - Goals

Syntax: `(up-set-indirect-goal <typeOp> <GoalId> <typeOp> <Value>)`

Set the value of a goal indirectly by reference.

[AIRef](https://airef.github.io/commands/commands-details.html#up-set-indirect-goal)

Completion insert text:

```text
(up-set-indirect-goal ${1:typeOp} ${2:GoalId} ${3:typeOp} ${4:Value})
```

<a id="symbol-up-set-offense-priority"></a>

## `up-set-offense-priority`

- Kind: `command`
- Detail: Action - Attack

Syntax: `(up-set-offense-priority <typeOp> <ObjectId> <typeOp> <Value>)`

Set the offensive targeting priority for an object. This is used when attacking with snNumberAttackGroups or attack-now. snEnableOffensivePriority must be set to 1 for these priorities to take effect. Note: offensive priorities have a very small range. You can turn the priorities up to 11 (highest), but no more. Also, unit lines do not work here, so just set the base unit type id (spearman for the entire spearman-line, etc.). Classes may be used, as well. If a unit has its type priority set, that will override its class priority. Target units on -1 offensive priority will not hold the attention of attackers if a higher priority unit appears. If the target unit is not -1 priority, the attacker may retarget to other units nearby, but primarily to other units with the same offensive priority. Battering rams and cannon galleons prefer to attack non-moving targets, while all other units prefer moving targets. If you clear offensive priorities with up-reset-target-priorities, you may notice attack behavior that is a bit similar to patrol.

[AIRef](https://airef.github.io/commands/commands-details.html#up-set-offense-priority)

Completion insert text:

```text
(up-set-offense-priority ${1:typeOp} ${2:ObjectId} ${3:typeOp} ${4:Value})
```

<a id="symbol-up-set-placement-data"></a>

## `up-set-placement-data`

- Kind: `command`
- Detail: Action - Buildings

Syntax: `(up-set-placement-data <PlayerNumber> <ObjectId> <typeOp> <Value>)`

Specify placement information for managed construction. Please ensure Player has at least a town-center to use for reference, if they don't have ObjectId. If Player has no objects left, placement will not work as expected. The properties assigned by up-set-placement-data that are in effect when a build command is executed are stored with them, so you can change properties immediately afterward and it won't break your previous settings. The action only allows exact player numbers, "my-player-number", or "this-any" rule variables for pPlayerNumber, such as "this-any-ally" or "this-any-computer-ally". It does not allow "any"/"every" wildcard parameters for pPlayerNumber. It cannot be used with players who aren't allies. It also allows for scenario-player-# and lobby-player-#, where # is between 1 and 8. scenario-player-# refers to the player color (where red = scenario-player-2), and lobby-player-# refers to the player slot (where the lobby host or human player playing a single player campaign is always lobby-player-1).

[AIRef](https://airef.github.io/commands/commands-details.html#up-set-placement-data)

Completion insert text:

```text
(up-set-placement-data ${1:PlayerNumber} ${2:ObjectId} ${3:typeOp} ${4:Value})
```

<a id="symbol-up-set-precise-target-point"></a>

## `up-set-precise-target-point`

- Kind: `command`
- Detail: Action - DUC

Syntax: `(up-set-precise-target-point <Point>)`

Set the target point with an unchecked extended goal pair. This command is identical to up-set-target-point, except it will not bound the point inside the map. Please ensure the point is valid with up-bound-precise-point. A precise point is expected to be a normal point x100 for 2 places of decimal precision.

[AIRef](https://airef.github.io/commands/commands-details.html#up-set-precise-target-point)

Completion insert text:

```text
(up-set-precise-target-point ${1:Point})
```

<a id="symbol-up-set-shared-goal"></a>

## `up-set-shared-goal`

- Kind: `command`
- Detail: Action - Goals, Other Player Info

Syntax: `(up-set-shared-goal <typeOp> <SharedGoalId> <typeOp> <Value>)`

Set the value of a shared goal.

[AIRef](https://airef.github.io/commands/commands-details.html#up-set-shared-goal)

Completion insert text:

```text
(up-set-shared-goal ${1:typeOp} ${2:SharedGoalId} ${3:typeOp} ${4:Value})
```

<a id="symbol-up-set-signal"></a>

## `up-set-signal`

- Kind: `command`
- Detail: Action - Scenarios

Syntax: `(up-set-signal <typeOp> <SignalId> <typeOp> <Value>)`

Set the value of a scenario trigger signal. This action only works with a single player scenario and "AI Signal" trigger condition. For a multiplayer scenario, use "Multiplayer AI Signal" and fe-set-signal.

[AIRef](https://airef.github.io/commands/commands-details.html#up-set-signal)

Completion insert text:

```text
(up-set-signal ${1:typeOp} ${2:SignalId} ${3:typeOp} ${4:Value})
```

<a id="symbol-up-set-target-by-id"></a>

## `up-set-target-by-id`

- Kind: `command`
- Detail: Fact/Action - DUC

Syntax: `(up-set-target-by-id <typeOp> <Id>)`

Set the target object for other commands by id. Reference it with up-get-point and position-object. If the Id is invalid, the current target object will remain unchanged. This command can be used as either a Fact or an Action.

[AIRef](https://airef.github.io/commands/commands-details.html#up-set-target-by-id)

Completion insert text:

```text
(up-set-target-by-id ${1:typeOp} ${2:Id})
```

<a id="symbol-up-set-target-object"></a>

## `up-set-target-object`

- Kind: `command`
- Detail: Fact/Action - DUC

Syntax: `(up-set-target-object <SearchSource> <typeOp> <Index>)`

Set the target object for other commands from your search. Reference it with up-get-point and position-object. If the Index is invalid, the current target object will remain unchanged. This command can be used as either a Fact or an Action.

[AIRef](https://airef.github.io/commands/commands-details.html#up-set-target-object)

Completion insert text:

```text
(up-set-target-object ${1:SearchSource} ${2:typeOp} ${3:Index})
```

<a id="symbol-up-set-target-point"></a>

## `up-set-target-point`

- Kind: `command`
- Detail: Action - DUC, Points

Syntax: `(up-set-target-point <Point>)`

Set the target point for other commands with an extended goal pair. This command will also safely bound the point inside the map.

[AIRef](https://airef.github.io/commands/commands-details.html#up-set-target-point)

Completion insert text:

```text
(up-set-target-point ${1:Point})
```

<a id="symbol-up-set-timer"></a>

## `up-set-timer`

- Kind: `command`
- Detail: Action - Timers

Syntax: `(up-set-timer <typeOp> <TimerId> <typeOp> <Value>)`

Disable or enable a timer by interval. Set Value to -1 to disable the timer. If Value is positive, this will perform like the enable-timer action.

[AIRef](https://airef.github.io/commands/commands-details.html#up-set-timer)

Completion insert text:

```text
(up-set-timer ${1:typeOp} ${2:TimerId} ${3:typeOp} ${4:Value})
```

<a id="symbol-up-setup-cost-data"></a>

## `up-setup-cost-data`

- Kind: `command`
- Detail: Action - Cost Data

Syntax: `(up-setup-cost-data <Option> <GoalId>)`

Set the goals to store cost data for food, wood, stone, and gold. If the Option parameter is set to 1 the values of the provided cost goal set will be reset to 0.

[AIRef](https://airef.github.io/commands/commands-details.html#up-setup-cost-data)

Completion insert text:

```text
(up-setup-cost-data ${1:Option} ${2:GoalId})
```

<a id="symbol-up-store-map-name"></a>

## `up-store-map-name`

- Kind: `command`
- Detail: Action - Game Info, Text Data

Syntax: `(up-store-map-name <Option>)`

Store the current map name in the internal buffer. For rms, this is the filename of the map. However, if the map is a dynamic loader, such as Full Random, Random Land Map, or Blind Random, this will be the loader name instead of the actual map name. For scenarios, this will be the original save filename instead of the current filename. The buffer can be referenced by the chat-data commands using %s instead of %d with c: 7031232 (7031232 cannot be stored in a defconst). This buffer is shared by all AIs, so please store data before using it in a rule pass. If the Option parameter is set to 1, the map name will be stored with the file extension in the name. If the Option parameter is set to 0, the map name will be stored without the file extension in the name.

[AIRef](https://airef.github.io/commands/commands-details.html#up-store-map-name)

Completion insert text:

```text
(up-store-map-name ${1:Option})
```

<a id="symbol-up-store-object-name"></a>

## `up-store-object-name`

- Kind: `command`
- Detail: Action - Buildings, Text Data, Units

Syntax: `(up-store-object-name)`

Store the target object's type name in the internal buffer. The buffer can be referenced by the chat-data commands using %s instead of %d with c: 7031232 (7031232 cannot be stored in a defconst). This buffer is shared by all AIs, so please store data before using it in a rule pass.

[AIRef](https://airef.github.io/commands/commands-details.html#up-store-object-name)

Completion insert text:

```text
(up-store-object-name)
```

<a id="symbol-up-store-player-chat"></a>

## `up-store-player-chat`

- Kind: `command`
- Detail: Action - Chat, Text Data

Syntax: `(up-store-player-chat <PlayerNumber>)`

Store a player chat message in the internal buffer. Note that only the last word of a chat message will be stored in the buffer and the message must be present in the host's chat history log (the PageUp key can find it). The buffer can be referenced by the chat-data commands using %s instead of %d with c: 7031232 (7031232 cannot be stored in a defconst). This buffer is shared by all AIs, so please store data before using it in a rule pass. The action only allows for exact player numbers, "my-player-number", or "this-any" rule variables for pPlayerNumber, such as "this-any-ally" or "this-any-enemy". It does not allow "any"/"every" wildcard parameters for pPlayerNumber. It also allows for scenario-player-# and lobby-player-#, where # is between 1 and 8. scenario-player-# refers to the player color (where red = scenario-player-2), and lobby-player-# refers to the player slot (where the lobby host or human player playing a single player campaign is always lobby-player-1).

[AIRef](https://airef.github.io/commands/commands-details.html#up-store-player-chat)

Completion insert text:

```text
(up-store-player-chat ${1:PlayerNumber})
```

<a id="symbol-up-store-player-name"></a>

## `up-store-player-name`

- Kind: `command`
- Detail: Action - Other Player Info, Text Data

Syntax: `(up-store-player-name <PlayerNumber>)`

Store a player name in the internal buffer. The buffer can be referenced by the chat-data commands using %s instead of %d with c: 7031232 (7031232 cannot be stored in a defconst). This buffer is shared by all AIs, so please store data before using it in a rule pass. The action only allows for exact player numbers, "my-player-number", or "this-any" rule variables for pPlayerNumber, such as "this-any-ally" or "this-any-enemy". It does not allow "any"/"every" wildcard parameters for pPlayerNumber. It also allows for scenario-player-# and lobby-player-#, where # is between 1 and 8. scenario-player-# refers to the player color (where red = scenario-player-2), and lobby-player-# refers to the player slot (where the lobby host or human player playing a single player campaign is always lobby-player-1).

[AIRef](https://airef.github.io/commands/commands-details.html#up-store-player-name)

Completion insert text:

```text
(up-store-player-name ${1:PlayerNumber})
```

<a id="symbol-up-store-tech-name"></a>

## `up-store-tech-name`

- Kind: `command`
- Detail: Action - Techs, Text Data

Syntax: `(up-store-tech-name <typeOp> <TechId>)`

Store a research tech name in the internal buffer. The buffer can be referenced by the chat-data commands using %s instead of %d with c: 7031232 (7031232 cannot be stored in a defconst). This buffer is shared by all AIs, so please store data before using it in a rule pass. You can also use my-unique-research, which will usually get the imperial age unique tech for the civilization, and you can also use my-second-unique-research, which will usually get the castle age unique tech for the civilization. The excepts are the Britons, Franks, Goths, and Saracens, whose my-unique-research and my-second-unique-research are switched.

[AIRef](https://airef.github.io/commands/commands-details.html#up-store-tech-name)

Completion insert text:

```text
(up-store-tech-name ${1:typeOp} ${2:TechId})
```

<a id="symbol-up-store-text"></a>

## `up-store-text`

- Kind: `command`
- Detail: Action - Text Data

Syntax: `(up-store-text <typeOp> <LanguageId>)`

Store a language string in the internal buffer. The buffer can be referenced by the chat-data commands using %s instead of %d with c: 7031232 (7031232 cannot be stored in a defconst). This buffer is shared by all AIs, so please store data before using it in a rule pass.

[AIRef](https://airef.github.io/commands/commands-details.html#up-store-text)

Completion insert text:

```text
(up-store-text ${1:typeOp} ${2:LanguageId})
```

<a id="symbol-up-store-type-name"></a>

## `up-store-type-name`

- Kind: `command`
- Detail: Action - Buildings, Text Data, Units

Syntax: `(up-store-type-name <typeOp> <TypeId>)`

Store an object type name in the internal buffer. The buffer can be referenced by the chat-data commands using %s instead of %d with c: 7031232 (7031232 cannot be stored in a defconst). This buffer is shared by all AIs, so please store data before using it in a rule pass.

[AIRef](https://airef.github.io/commands/commands-details.html#up-store-type-name)

Completion insert text:

```text
(up-store-type-name ${1:typeOp} ${2:TypeId})
```

<a id="symbol-up-target-objects"></a>

## `up-target-objects`

- Kind: `command`
- Detail: Action - DUC

Syntax: `(up-target-objects <Option> <DUCAction> <Formation> <AttackStance>)`

Direct local search results against remote search results. The action-default command is equivalent to a right-click. This command can only perform the following actions: action-default, action-move, action-patrol, action-guard, action-follow, action-stop, action-ground, action-garrison, action-delete, action-gather, and action-none. The other pDUCAction options available for up-target-point will not work. Set the Option parameter to 1 to target only the object set by up-set-target-object. If set to 0, the objects in the local list will evenly target all objects in the remote list. This command will aim to separate the units selected with up-find-local into groups of 20 units or less before sending them against the remote target(s). Do not use the action-default or action-move commands if the defensive targeting system (TSA) is locked on a target, or units will become "confused" and not respond for a few moments. Either bring the town size so that enemy-buildings-in-town is no longer true or set snDisableDefendGroups on. The action-patrol command seems to work regardless.

[AIRef](https://airef.github.io/commands/commands-details.html#up-target-objects)

Completion insert text:

```text
(up-target-objects ${1:Option} ${2:DUCAction} ${3:Formation} ${4:AttackStance})
```

<a id="symbol-up-target-point"></a>

## `up-target-point`

- Kind: `command`
- Detail: Action - DUC, Points

Syntax: `(up-target-point <Point> <DUCAction> <Formation> <AttackStance>)`

Direct local search results to a specific point on the map. This command can perform all actions from the DUCAction list. However, action-default, action-guard, action-follow, and action-garrison will perform as action-move. If you wish to action-move back into formation nearby after attacking, please action-move to the point (-1,-1) first to reset distance. This command will aim to separate the units selected with up-find-local into groups of 20 units or less before sending them against the remote target(s). Do not use the action-default or action-move commands if the defensive targeting system (TSA) is locked on a target, or units will become "confused" and not respond for a few moments. Either bring the town size so that enemy-buildings-in-town is no longer true or set snDisableDefendGroups on. The action-patrol command seems to work regardless.

[AIRef](https://airef.github.io/commands/commands-details.html#up-target-point)

Completion insert text:

```text
(up-target-point ${1:Point} ${2:DUCAction} ${3:Formation} ${4:AttackStance})
```

<a id="symbol-up-timer-status"></a>

## `up-timer-status`

- Kind: `command`
- Detail: Fact - Timers

Syntax: `(up-timer-status <TimerId> <compareOp> <TimerState>)`

Check whether a timer is disabled, triggered, running, or a combination.

[AIRef](https://airef.github.io/commands/commands-details.html#up-timer-status)

Completion insert text:

```text
(up-timer-status ${1:TimerId} ${2:compareOp} ${3:TimerState})
```

<a id="symbol-up-train"></a>

## `up-train`

- Kind: `command`
- Detail: Action - Units

Syntax: `(up-train <EscrowGoalId> <typeOp> <UnitId>)`

Add a unit to the training queue with dynamic values. You can also train unique units by using my-unique-unit, my-elite-unique-unit, and my-unique-unit-line, which will automatically get the UnitId of the unique unit, elite unique unit, or unique unit line that the AI's civ can train from the castle. The setting of snDockTrainingFilter affects the ability for docks to train warships with this command.

[AIRef](https://airef.github.io/commands/commands-details.html#up-train)

Completion insert text:

```text
(up-train ${1:EscrowGoalId} ${2:typeOp} ${3:UnitId})
```

<a id="symbol-up-train-site-ready"></a>

## `up-train-site-ready`

- Kind: `command`
- Detail: Fact - Buildings, Can Do

Syntax: `(up-train-site-ready <typeOp> <UnitId>)`

Check if a unit's training site is ready and available. You can also check the train site of my-unique-unit, which will automatically check the train site of the UnitId of the unique unit that the AI's civ can train from the castle. Important Note: Unit lines, negative unit IDs, or invalid unit Ids may result in a crash. Do not use unit lines or unit classes with this command. Please use the root unit type instead, such as using archer instead of archer-line, even if Crossbowman has been researched. In most cases, the unit you use to test whether a train site is ready doesn't matter. However, for docks, the unit you choose to test is important. Trade cogs may be rejected by the dock if you use snDockTrainingFilter and it hasn't found an allied dock. On the other hand, a military ship (galley works to test all of these) uses enemy ships/docks to determine if it is acceptable when that sn is in use. Fishing ships may also provide a different result sooner or later. An alternative to this command is finding a building you want to check, setting it as the target object with up-set-target-object or up-set-target-by-id and using up-get-object-data like this:(up-get-object-data object-data-progress-type gl-data) If 0 is stored in gl-data, then the building is not training or researching, and it is ready to train units.

[AIRef](https://airef.github.io/commands/commands-details.html#up-train-site-ready)

Completion insert text:

```text
(up-train-site-ready ${1:typeOp} ${2:UnitId})
```

<a id="symbol-up-tribute-to-player"></a>

## `up-tribute-to-player`

- Kind: `command`
- Detail: Action - Diplomacy

Syntax: `(up-tribute-to-player <PlayerNumber> <ResourceType> <typeOp> <Value>)`

Tribute a variable amount of resources to other players. The fact allows "focus-player", "target-player", and "any"/"every" wildcard parameters for pPlayerNumber. It also allows the use of rule variables for PlayerNumber, such as "this-any-ally" or "this-any-enemy". It also allows for scenario-player-# and lobby-player-#, where # is between 1 and 8. scenario-player-# refers to the player color (where red = scenario-player-2), and lobby-player-# refers to the player slot (where the lobby host or human player playing a single player campaign is always lobby-player-1).

[AIRef](https://airef.github.io/commands/commands-details.html#up-tribute-to-player)

Completion insert text:

```text
(up-tribute-to-player ${1:PlayerNumber} ${2:ResourceType} ${3:typeOp} ${4:Value})
```

<a id="symbol-up-ungarrison"></a>

## `up-ungarrison`

- Kind: `command`
- Detail: Action - Buildings

Syntax: `(up-ungarrison <typeOp> <ObjectId>)`

Request all objects of the specified type to ungarrison units.

[AIRef](https://airef.github.io/commands/commands-details.html#up-ungarrison)

Completion insert text:

```text
(up-ungarrison ${1:typeOp} ${2:ObjectId})
```

<a id="symbol-up-unit-type-in-town"></a>

## `up-unit-type-in-town`

- Kind: `command`
- Detail: Fact - Counting, Defense, Units

Syntax: `(up-unit-type-in-town <typeOp> <UnitId> <compareOp> <Value>)`

Check the number of a specific enemy unit type in town.

[AIRef](https://airef.github.io/commands/commands-details.html#up-unit-type-in-town)

Completion insert text:

```text
(up-unit-type-in-town ${1:typeOp} ${2:UnitId} ${3:compareOp} ${4:Value})
```

<a id="symbol-up-update-targets"></a>

## `up-update-targets`

- Kind: `command`
- Detail: Action - Attack, Defense

Syntax: `(up-update-targets)`

Perform an immediate update for objects in town size. This command is important when using TSA. If you expand town size, new targets inside sn-maximum-town-size are quickly added into the target list (the list of enemy objects within sn-maximum-town-size). However, if you reduce sn-maximum-town-size, you have to wait until the target refresh for these objects to be removed from the target list, which happens every 15 seconds. This can cause issues with retreating, for example. Using up-update-targets will immediately update the target list, resolving the issue.

[AIRef](https://airef.github.io/commands/commands-details.html#up-update-targets)

Completion insert text:

```text
(up-update-targets)
```

<a id="symbol-up-villager-type-in-town"></a>

## `up-villager-type-in-town`

- Kind: `command`
- Detail: Fact - Counting, Defense, Units

Syntax: `(up-villager-type-in-town <typeOp> <UnitId> <compareOp> <Value>)`

Check the number of a specific enemy villager type in town.

[AIRef](https://airef.github.io/commands/commands-details.html#up-villager-type-in-town)

Completion insert text:

```text
(up-villager-type-in-town ${1:typeOp} ${2:UnitId} ${3:compareOp} ${4:Value})
```

<a id="symbol-victory-condition"></a>

## `victory-condition`

- Kind: `command`
- Detail: Fact - Game Info

Syntax: `(victory-condition <VictoryCondition>)`

Checks the game victory condition. The victory conditions can be standard, conquest, time-limit, score, or custom.

[AIRef](https://airef.github.io/commands/commands-details.html#victory-condition)

Completion insert text:

```text
(victory-condition ${1:VictoryCondition})
```

<a id="symbol-wall-completed-percentage"></a>

## `wall-completed-percentage`

- Kind: `command`
- Detail: Fact - Buildings, Walls & Gates

Syntax: `(wall-completed-percentage <Perimeter> <compareOp> <Value>)`

Checks the completion percentage for a given wall perimeter. Trees and other destructible natural barriers are included and count as completed. The given perimeter must have been enabled with enable-wall-placement, and you should not check the completed percentage until the pass after the given wall perimeter has been enabled. Allowed perimeter values are 1 and 2, with 1 being closer to the Town Center than 2. Perimeter 1 is usually between 10 and 20 tiles from the starting Town Center. Perimeter 2 is usually between 18 and 30 tiles from the starting Town Center. Note: There are multiple cases where wall-completed-percentage equals 100 when you wouldn't expect:Maps with starting walls like Arena, Fortress, or Hideout.On island maps if there is an entirely water based barrier between the AI and any enemies.If a treaty is active.

[AIRef](https://airef.github.io/commands/commands-details.html#wall-completed-percentage)

Completion insert text:

```text
(wall-completed-percentage ${1:Perimeter} ${2:compareOp} ${3:Value})
```

<a id="symbol-wall-invisible-percentage"></a>

## `wall-invisible-percentage`

- Kind: `command`
- Detail: Fact - Buildings, Walls & Gates

Syntax: `(wall-invisible-percentage <Perimeter> <compareOp> <Value>)`

Checks what percentage of the potential wall placement is covered with fog. If the invisible percentage is not equal to 0 we do not know if there is a hole or not. This is because the hidden tile(s) might have a tree(s). The given perimeter must have been enabled with enable-wall-placement, and you should not check the invisible percentage until the pass after the given wall perimeter has been enabled. Allowed perimeter values are 1 and 2, with 1 being closer to the Town Center than 2. Perimeter 1 is usually between 10 and 20 tiles from the starting Town Center. Perimeter 2 is usually between 18 and 30 tiles from the starting Town Center.

[AIRef](https://airef.github.io/commands/commands-details.html#wall-invisible-percentage)

Completion insert text:

```text
(wall-invisible-percentage ${1:Perimeter} ${2:compareOp} ${3:Value})
```

<a id="symbol-warboat-count"></a>

## `warboat-count`

- Kind: `command`
- Detail: Fact - Counting, Units

Syntax: `(warboat-count <compareOp> <Value>)`

Checks the computer player's warboat count. A warboat is a ship capable of attacking. Fishing ships, transport ships, and trade cogs aren't included.

[AIRef](https://airef.github.io/commands/commands-details.html#warboat-count)

Completion insert text:

```text
(warboat-count ${1:compareOp} ${2:Value})
```

<a id="symbol-wood-amount"></a>

## `wood-amount`

- Kind: `command`
- Detail: Fact - Economy

Syntax: `(wood-amount <compareOp> <Value>)`

Checks a computer player's wood amount. This amount includes escrowed wood.

[AIRef](https://airef.github.io/commands/commands-details.html#wood-amount)

Completion insert text:

```text
(wood-amount ${1:compareOp} ${2:Value})
```

<a id="symbol-xnor"></a>

## `xnor`

- Kind: `command`
- Detail: Other - Other

Syntax: `(xnor)`

Returns true if one of the facts following this command is true and the other is false. Both facts cannot be true like or. The xnor command is one of several logical operator commands available, along with and, nand, nor, not, or, and xor. See the Logical Operator Commands guide for more information on how to use logical operator commands.

[AIRef](https://airef.github.io/commands/commands-details.html#xnor)

Completion insert text:

```text
(xnor)
```

<a id="symbol-xor"></a>

## `xor`

- Kind: `command`
- Detail: Other - Other

Syntax: `(xor)`

Returns true if one of the facts following this command is true and the other is false. Both facts cannot be true like or. The xor command is one of several logical operator commands available, along with and, nand, nor, not, or, and xnor. See the Logical Operator Commands guide for more information on how to use logical operator commands.

[AIRef](https://airef.github.io/commands/commands-details.html#xor)

Completion insert text:

```text
(xor)
```

<a id="symbol-xs-script-call"></a>

## `xs-script-call`

- Kind: `command`
- Detail: Fact/Action - Debugging, Goals, Strategic Numbers, Other

Syntax: `(xs-script-call <String>)`

DE only. Call an XS script function from an .xs file. It is not necessary to defconst the function name. If the function name is misspelled or a function with that name doesn't exist in any included .xs files, the command will do nothing, without reporting an error. For more info on XS scripting, see this exhaustive guide: link. The function must be from a .xs file that has been "included" (loaded) by the AI script. To include a .xs file in an AI script, use the include command, like (include "Example XS File.xs"). Note that the filetype (.xs) must be included in the include command, and the filepath must be inside quotes. By default, .xs files must be placed in the game's xs folder, located at: "C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\resources\_common\xs", but you can also load .xs files with a relative filepath name, using "../" to go up a filepath level from the xs folder and then follow the rest of the filepath to get to your .xs file. For example, to include a .xs file stored in your "My AI" folder within the default AI installation directory, you can use (include "../ai/My AI/Example XS File.xs"). Once you have included your .xs file, you can use xs-script-call to call any function from that file that doesn't have any parameters. So, if you have the code below in your XS file, you can call the helloWorld() function, but not the max() function. xs-script-call can be used as either a Fact or an Action, and it'll execute the function either way. However, if used as a Fact, xs-script-call will be a Fact that is considered false if your function returns 0, returns "false", or is a void function that doesn't return anything. Because of this, if you want to use xs-script-call successfully anywhere in a rule, it's a good idea to make this function a bool function that returns "true" or an int function that returns any non-zero value. The AI can't do anything with the value that is returned from this function, but the xs-script-call Fact itself will return true. If you do need an AI to be able use an integer result from an XS function, you can use the xsSetGoal() or xsSetStrategicNumber() functions within an XS function to modify the value of a goal or SN, which the AI script can then check. Likewise, xsGetGoal() and xsGetStrategicNumber() functions can allow an XS function to get the current value of a goal or SN. If you call an XS function more than once, it's a good idea to defconst it (see the examples below). Otherwise, each time you call the function in the AI script it will add an entry to the string table. Here is some example .xs code which is used in the examples section below://This code is saved in a file called Example XS File.xs float max(float a = 0.0, float b = 2.0) { if(a > b) return (a); else return (b); } bool helloWorld() { xsChatData("Hello World"); return (true); } int rand() { int rand = xsGetRandomNumber(); //generates a random number between 0 and 32766 rand++; //increase random number range to between 1 and 32767 so that zero isn't returned, making a xs-script-call condition false xsSetGoal(510, rand); return (rand); }

[AIRef](https://airef.github.io/commands/commands-details.html#xs-script-call)

Completion insert text:

```text
(xs-script-call ${1:String})
```

<a id="section-object"></a>

# object

<a id="symbol--266"></a>

## `-266`

- Kind: `object`
- Detail: Object line - Clubman

Line token from Clubman.

<a id="symbol--283"></a>

## `-283`

- Kind: `object`
- Detail: Object line - Trade Boat

Line token from Trade Boat.

<a id="symbol--284"></a>

## `-284`

- Kind: `object`
- Detail: Object line - Catapult Trireme

Line token from Catapult Trireme.

<a id="symbol--285"></a>

## `-285`

- Kind: `object`
- Detail: Object line - Scout Ship

Line token from Scout Ship.

<a id="symbol--286"></a>

## `-286`

- Kind: `object`
- Detail: Object line - Light Transport

Line token from Light Transport.

<a id="symbol--287"></a>

## `-287`

- Kind: `object`
- Detail: Object line - Fishing Boat

Line token from Fishing Boat.

<a id="symbol--288"></a>

## `-288`

- Kind: `object`
- Detail: Object line - Stone Thrower

Line token from Stone Thrower.

<a id="symbol--289"></a>

## `-289`

- Kind: `object`
- Detail: Object line - Ballista

Line token from Ballista.

<a id="symbol--290"></a>

## `-290`

- Kind: `object`
- Detail: Object line - Hoplite

Line token from Hoplite.

<a id="symbol--291"></a>

## `-291`

- Kind: `object`
- Detail: Object line - Chariot

Line token from Chariot.

<a id="symbol--292"></a>

## `-292`

- Kind: `object`
- Detail: Object line - War Elephant

Line token from War Elephant.

<a id="symbol--293"></a>

## `-293`

- Kind: `object`
- Detail: Object line - Horse Archer

Line token from Horse Archer.

<a id="symbol--294"></a>

## `-294`

- Kind: `object`
- Detail: Object line - Short Swordsman

Line token from Short Swordsman.

<a id="symbol--295"></a>

## `-295`

- Kind: `object`
- Detail: Object line - Cavalry

Line token from Cavalry.

<a id="symbol--298"></a>

## `-298`

- Kind: `object`
- Detail: Object line - Improved Bowman

Line token from Improved Bowman.

<a id="symbol--299"></a>

## `-299`

- Kind: `object`
- Detail: Object line - Bowman

Line token from Bowman.

<a id="symbol--398"></a>

## `-398`

- Kind: `object`
- Detail: Object line - Watch Tower

Line token from Watch Tower.

<a id="symbol--399"></a>

## `-399`

- Kind: `object`
- Detail: Object line - Small Wall

Line token from Small Wall.

<a id="symbol-ancient-galley-line"></a>

## `ancient-galley-line`

- Kind: `object`
- Detail: Object line - Galley (Antiquity)

Line token from Galley (Antiquity).

<a id="symbol-arambai"></a>

## `arambai`

- Kind: `object`
- Detail: Object WK: 823<br>DE: 1126 - Arambai

Class: `cavalry-cannon-class (923)`

Line: `arambai-line`

Building: Castle

<a id="symbol-arambai-line"></a>

## `arambai-line`

- Kind: `object`
- Detail: Object line - Arambai

Line token from Arambai.

<a id="symbol-arbalest"></a>

## `arbalest`

- Kind: `object`
- Detail: Object 492 - Composite Bowman

Class: `archery-class (900)`

Line: `-298`

Building: Archery Range

<a id="symbol-arbalest-arbalester-de-only-"></a>

## `arbalest, arbalester (DE only)`

- Kind: `object`
- Detail: Object 492 - Arbalest

Class: `archery-class (900)`

Line: `archer-line`

Building: Archery Range

<a id="symbol-archer"></a>

## `archer`

- Kind: `object`
- Detail: Object 4 - Archer

Class: `archery-class (900)`

Line: `archer-line`

Building: Archery Range

<a id="symbol-archer-line"></a>

## `archer-line`

- Kind: `object`
- Detail: Object line - Archer

Line token from Archer.

<a id="symbol-archery-range"></a>

## `archery-range`

- Kind: `object`
- Detail: Object 87 - Archery Range (Feudal Age)

Class: `building-class (903)`

Building: Buildings

<a id="symbol-armored-elephant"></a>

## `armored-elephant`

- Kind: `object`
- Detail: Object 1744 - Armored Elephant

Class: `cavalry-class (912)`

Line: `armored-elephant-line`

Building: Siege Workshop

<a id="symbol-armored-elephant-line"></a>

## `armored-elephant-line`

- Kind: `object`
- Detail: Object line - Armored Elephant

Line token from Armored Elephant.

<a id="symbol-ballista-elephant"></a>

## `ballista-elephant`

- Kind: `object`
- Detail: Object WK: 760<br>DE: 1120 - Ballista Elephant

Class: `cavalry-class (912)`

Line: `ballista-elephant-line`

Building: Castle

<a id="symbol-ballista-elephant-line"></a>

## `ballista-elephant-line`

- Kind: `object`
- Detail: Object line - Ballista Elephant

Line token from Ballista Elephant.

<a id="symbol-barracks"></a>

## `barracks`

- Kind: `object`
- Detail: Object 12 - Barracks (Dark Age)

Class: `building-class (903)`

Building: Buildings

<a id="symbol-battering-ram"></a>

## `battering-ram`

- Kind: `object`
- Detail: Object 35 - Battering Ram

Class: `siege-weapon-class (913)`

Line: `battering-ram-line`

Building: Siege Workshop

<a id="symbol-battering-ram-line"></a>

## `battering-ram-line`

- Kind: `object`
- Detail: Object line - Battering Ram (Feudal)

Line token from Battering Ram (Feudal).

<a id="symbol-battle-elephant"></a>

## `battle-elephant`

- Kind: `object`
- Detail: Object WK: 774<br>DE: 1132 - Battle Elephant

Class: `cavalry-class (912)`

Line: `battle-elephant-line`

Building: Stable

<a id="symbol-battle-elephant-line"></a>

## `battle-elephant-line`

- Kind: `object`
- Detail: Object line - Battle Elephant

Line token from Battle Elephant.

<a id="symbol-berserk"></a>

## `berserk`

- Kind: `object`
- Detail: Object 692 - Berserk

Class: `infantry-class (906)`

Line: `berserk-line`

Building: Castle

<a id="symbol-berserk-line"></a>

## `berserk-line`

- Kind: `object`
- Detail: Object line - Berserk

Line token from Berserk.

<a id="symbol-blacksmith"></a>

## `blacksmith`

- Kind: `object`
- Detail: Object 103 - Blacksmith (Feudal Age)

Class: `building-class (903)`

Building: Buildings

<a id="symbol-blackwood-archer-line"></a>

## `blackwood-archer-line`

- Kind: `object`
- Detail: Object line - Blackwood Archer

Line token from Blackwood Archer.

<a id="symbol-bolas-rider-line"></a>

## `bolas-rider-line`

- Kind: `object`
- Detail: Object line - Bolas Rider

Line token from Bolas Rider.

<a id="symbol-bombard-cannon"></a>

## `bombard-cannon`

- Kind: `object`
- Detail: Object 36 - Bombard Cannon

Class: `siege-weapon-class (913)`

Line: `bombard-cannon-line`

Building: Siege Workshop

<a id="symbol-bombard-cannon-line"></a>

## `bombard-cannon-line`

- Kind: `object`
- Detail: Object line - Bombard Cannon

Line token from Bombard Cannon.

<a id="symbol-bombard-tower"></a>

## `bombard-tower`

- Kind: `object`
- Detail: Object 236 - Bombard Tower

Class: `tower-class (952)`

Building: Buildings

<a id="symbol-boyar"></a>

## `boyar`

- Kind: `object`
- Detail: Object 876 - Boyar

Class: `cavalry-class (912)`

Line: `boyar-line`

Building: Castle

<a id="symbol-boyar-line"></a>

## `boyar-line`

- Kind: `object`
- Detail: Object line - Boyar

Line token from Boyar.

<a id="symbol-camel"></a>

## `camel`

- Kind: `object`
- Detail: Object 329 - Camel Rider

Class: `cavalry-class (912)`

Building: Stable

<a id="symbol-camel-archer"></a>

## `camel-archer`

- Kind: `object`
- Detail: Object WK: 203<br>DE: 1007 - Camel Archer

Class: `cavalry-archer-class (936)`

Line: `camel-archer-line`

Building: Castle

<a id="symbol-camel-archer-line"></a>

## `camel-archer-line`

- Kind: `object`
- Detail: Object line - Camel Archer

Line token from Camel Archer.

<a id="symbol-camel-line"></a>

## `camel-line`

- Kind: `object`
- Detail: Object line - Camel Scout

Line token from Camel Scout.

<a id="symbol-camel-scout"></a>

## `camel-scout`

- Kind: `object`
- Detail: Object 1755 - Camel Scout

Class: `cavalry-class (912)`

Line: `camel-line`

Building: Stable

<a id="symbol-camel-camel-rider-de-only-"></a>

## `camel, camel-rider (DE only)`

- Kind: `object`
- Detail: Object 329 - Camel [Rider]

Class: `cavalry-class (912)`

Line: `camel-line`

Building: Stable

<a id="symbol-cannon-galleon"></a>

## `cannon-galleon`

- Kind: `object`
- Detail: Object 420 - Cannon Galleon

Class: `warship-class (922)`

Line: `cannon-galleon-line`

Building: Dock

<a id="symbol-cannon-galleon-line"></a>

## `cannon-galleon-line`

- Kind: `object`
- Detail: Object line - Cannon Galleon

Line token from Cannon Galleon.

<a id="symbol-capped-ram"></a>

## `capped-ram`

- Kind: `object`
- Detail: Object 422 - Capped Ram

Class: `siege-weapon-class (913)`

Line: `battering-ram-line`

Building: Siege Workshop

<a id="symbol-caravanserai"></a>

## `caravanserai`

- Kind: `object`
- Detail: Object 1754 - Caravanserai

Class: `building-class (903)`

Building: Buildings

<a id="symbol-caravel"></a>

## `caravel`

- Kind: `object`
- Detail: Object WK: 861<br>DE: 1004 - Caravel

Class: `warship-class (922)`

Line: `caravel-line`

Building: Dock

<a id="symbol-caravel-line"></a>

## `caravel-line`

- Kind: `object`
- Detail: Object line - Caravel

Line token from Caravel.

<a id="symbol-castle"></a>

## `castle`

- Kind: `object`
- Detail: Object 82 - Castle

Class: `building-class (903)`

Building: Buildings

<a id="symbol-cataphract"></a>

## `cataphract`

- Kind: `object`
- Detail: Object 40 - Cataphract

Class: `cavalry-class (912)`

Line: `cataphract-line`

Building: Castle

<a id="symbol-cataphract-line"></a>

## `cataphract-line`

- Kind: `object`
- Detail: Object line - Cataphract

Line token from Cataphract.

<a id="symbol-catapult-ship-line"></a>

## `catapult-ship-line`

- Kind: `object`
- Detail: Object line - Catapult Ship

Line token from Catapult Ship.

<a id="symbol-cavalier"></a>

## `cavalier`

- Kind: `object`
- Detail: Object 283 - Cavalier

Class: `cavalry-class (912)`

Line: `knight-line`

Building: Stable

<a id="symbol-cavalry-archer"></a>

## `cavalry-archer`

- Kind: `object`
- Detail: Object 39 - Cavalry Archer

Class: `cavalry-archer-class (936)`

Line: `cavalry-archer-line`

Building: Archery Range

<a id="symbol-cavalry-archer-line"></a>

## `cavalry-archer-line`

- Kind: `object`
- Detail: Object line - Cavalry Archer

Line token from Cavalry Archer.

<a id="symbol-centurion"></a>

## `centurion`

- Kind: `object`
- Detail: Object 1790 - Centurion

Class: `cavalry-class (912)`

Line: `centurion-line`

Building: Castle

<a id="symbol-centurion-line"></a>

## `centurion-line`

- Kind: `object`
- Detail: Object line - Centurion

Line token from Centurion.

<a id="symbol-chakram-thrower"></a>

## `chakram-thrower`

- Kind: `object`
- Detail: Object 1741 - Chakram Thrower

Class: `infantry-class (906)`

Line: `chakram-thrower-line`

Building: Castle

<a id="symbol-chakram-thrower-line"></a>

## `chakram-thrower-line`

- Kind: `object`
- Detail: Object line - Chakram Thrower

Line token from Chakram Thrower.

<a id="symbol-champi-line"></a>

## `champi-line`

- Kind: `object`
- Detail: Object line - Champi Scout

Line token from Champi Scout.

<a id="symbol-champion"></a>

## `champion`

- Kind: `object`
- Detail: Object 567 - Champion

Class: `infantry-class (906)`

Line: `militiaman-line`

Building: Barracks

<a id="symbol-chu-ko-nu"></a>

## `chu-ko-nu`

- Kind: `object`
- Detail: Object 73 - Chu Ko Nu

Class: `archery-class (900)`

Line: `chu-ko-nu-line`

Building: Castle

<a id="symbol-chu-ko-nu-line"></a>

## `chu-ko-nu-line`

- Kind: `object`
- Detail: Object line - Chu Ko Nu

Line token from Chu Ko Nu.

<a id="symbol-composite-bowman"></a>

## `composite-bowman`

- Kind: `object`
- Detail: Object 1800 - Composite Bowman

Class: `archery-class (900)`

Line: `composite-bowman-line`

Building: Castle

<a id="symbol-composite-bowman-line"></a>

## `composite-bowman-line`

- Kind: `object`
- Detail: Object line - Composite Bowman

Line token from Composite Bowman.

<a id="symbol-condottiero"></a>

## `condottiero`

- Kind: `object`
- Detail: Object 882 - Condottiero

Class: `infantry-class (906)`

Building: Barracks

<a id="symbol-conquistador"></a>

## `conquistador`

- Kind: `object`
- Detail: Object 771 - Conquistador

Class: `cavalry-cannon-class (923)`

Line: `conquistador-line`

Building: Castle

<a id="symbol-conquistador-line"></a>

## `conquistador-line`

- Kind: `object`
- Detail: Object line - Conquistador

Line token from Conquistador.

<a id="symbol-coustillier"></a>

## `coustillier`

- Kind: `object`
- Detail: Object 1655 - Coustillier

Class: `cavalry-class (912)`

Line: `coustillier-line`

Building: Castle

<a id="symbol-coustillier-line"></a>

## `coustillier-line`

- Kind: `object`
- Detail: Object line - Coustillier

Line token from Coustillier.

<a id="symbol-crossbowman"></a>

## `crossbowman`

- Kind: `object`
- Detail: Object 24 - Crossbowman

Class: `archery-class (900)`

Line: `archer-line`

Building: Archery Range

<a id="symbol-demo-raft"></a>

## `demo-raft`

- Kind: `object`
- Detail: Object WK: 527<br>DE: 1104 - Demolition Raft

Class: `warship-class (922)`

Line: `demolition-ship-line`

Building: Dock

<a id="symbol-demolition-ship"></a>

## `demolition-ship`

- Kind: `object`
- Detail: Object 527 - Demolition Ship (non-WK)

Class: `warship-class (922)`

Line: `demolition-ship-line`

Building: Dock

<a id="symbol-demolition-ship-line"></a>

## `demolition-ship-line`

- Kind: `object`
- Detail: Object line - Demolition Raft

Line token from Demolition Raft.

<a id="symbol-dock"></a>

## `dock`

- Kind: `object`
- Detail: Object 45 - Dock (Dark Age)

Class: `building-class (903)`

Building: Buildings

<a id="symbol-donjon"></a>

## `donjon`

- Kind: `object`
- Detail: Object 1665 - Donjon

Class: `tower-class (952)`

Building: Buildings

<a id="symbol-dromon"></a>

## `dromon`

- Kind: `object`
- Detail: Object 1795 - Dromon

Class: `warship-class (922)`

Building: Dock

<a id="symbol-eagle-warrior"></a>

## `eagle-warrior`

- Kind: `object`
- Detail: Object 751 - Eagle Scout (non-TC)/<br>Eagle Warrior (TC)

Class: `infantry-class (906)`

Line: `eagle-warrior-line`

Building: Barracks

<a id="symbol-eagle-warrior-line"></a>

## `eagle-warrior-line`

- Kind: `object`
- Detail: Object line - Eagle Scout (non-TC)/<br>Eagle Warrior (TC)

Line token from Eagle Scout (non-TC)/<br>Eagle Warrior (TC).

<a id="symbol-elephant-archer"></a>

## `elephant-archer`

- Kind: `object`
- Detail: Object 873 - Elephant Archer

Class: `cavalry-archer-class (936)`

Line: `elephant-archer-line`

Building: Archery Range

<a id="symbol-elephant-archer-line"></a>

## `elephant-archer-line`

- Kind: `object`
- Detail: Object line - Elephant Archer

Line token from Elephant Archer.

<a id="symbol-elite-arambai"></a>

## `elite-arambai`

- Kind: `object`
- Detail: Object WK: 811<br>DE: 1128 - Elite Arambai

Class: `cavalry-cannon-class (923)`

Line: `arambai-line`

Building: Castle

<a id="symbol-elite-ballista-elephant"></a>

## `elite-ballista-elephant`

- Kind: `object`
- Detail: Object WK: 891<br>DE: 1122 - Elite Ballista Elephant

Class: `cavalry-class (912)`

Line: `ballista-elephant-line`

Building: Castle

<a id="symbol-elite-battle-elephant"></a>

## `elite-battle-elephant`

- Kind: `object`
- Detail: Object WK: 766<br>DE: 1134 - Elite Battle Elephant

Class: `cavalry-class (912)`

Line: `battle-elephant-line`

Building: Stable

<a id="symbol-elite-berserk"></a>

## `elite-berserk`

- Kind: `object`
- Detail: Object 694 - Elite Berserk

Class: `infantry-class (906)`

Line: `berserk-line`

Building: Castle

<a id="symbol-elite-boyar"></a>

## `elite-boyar`

- Kind: `object`
- Detail: Object 878 - Elite Boyar

Class: `cavalry-class (912)`

Line: `boyar-line`

Building: Castle

<a id="symbol-elite-camel-archer"></a>

## `elite-camel-archer`

- Kind: `object`
- Detail: Object WK: 208<br>DE: 1009 - Elite Camel Archer

Class: `cavalry-archer-class (936)`

Line: `camel-archer-line`

Building: Castle

<a id="symbol-elite-cannon-galleon"></a>

## `elite-cannon-galleon`

- Kind: `object`
- Detail: Object 691 - Elite Cannon Galleon

Class: `warship-class (922)`

Line: `cannon-galleon-line`

Building: Dock

<a id="symbol-elite-caravel"></a>

## `elite-caravel`

- Kind: `object`
- Detail: Object WK: 183<br>DE: 1006 - Elite Caravel

Class: `warship-class (922)`

Line: `caravel-line`

Building: Dock

<a id="symbol-elite-cataphract"></a>

## `elite-cataphract`

- Kind: `object`
- Detail: Object 553 - Elite Cataphract

Class: `cavalry-class (912)`

Line: `cataphract-line`

Building: Castle

<a id="symbol-elite-centurion"></a>

## `elite-centurion`

- Kind: `object`
- Detail: Object 1792 - Elite Centurion

Class: `cavalry-class (912)`

Line: `centurion-line`

Building: Castle

<a id="symbol-elite-chakram-thrower"></a>

## `elite-chakram-thrower`

- Kind: `object`
- Detail: Object 1743 - Elite Chakram Thrower

Class: `infantry-class (906)`

Line: `chakram-thrower-line`

Building: Castle

<a id="symbol-elite-chu-ko-nu"></a>

## `elite-chu-ko-nu`

- Kind: `object`
- Detail: Object 559 - Elite Chu Ko Nu

Class: `archery-class (900)`

Line: `chu-ko-nu-line`

Building: Castle

<a id="symbol-elite-composite-bowman"></a>

## `elite-composite-bowman`

- Kind: `object`
- Detail: Object 1802 - Elite Composite Bowman

Class: `archery-class (900)`

Line: `composite-bowman-line`

Building: Castle

<a id="symbol-elite-conquistador"></a>

## `elite-conquistador`

- Kind: `object`
- Detail: Object 773 - Elite Conquistador

Class: `cavalry-cannon-class (923)`

Line: `conquistador-line`

Building: Castle

<a id="symbol-elite-coustillier"></a>

## `elite-coustillier`

- Kind: `object`
- Detail: Object 1657 - Elite Coustillier

Class: `cavalry-class (912)`

Line: `coustillier-line`

Building: Castle

<a id="symbol-elite-eagle-warrior"></a>

## `elite-eagle-warrior`

- Kind: `object`
- Detail: Object 752 - Elite Eagle Warrior

Class: `infantry-class (906)`

Line: `eagle-warrior-line`

Building: Barracks

<a id="symbol-elite-elephant-archer"></a>

## `elite-elephant-archer`

- Kind: `object`
- Detail: Object 875 - Elite Elephant Archer

Class: `cavalry-archer-class (936)`

Line: `elephant-archer-line`

Building: Archery Range

<a id="symbol-elite-fire-archer"></a>

## `elite-fire-archer`

- Kind: `object`
- Detail: Object 1970 - Elite Fire Archer

Class: `archery-class (900)`

Line: `fire-archer-line`

Building: Castle

<a id="symbol-elite-foot-konnik"></a>

## `elite-foot-konnik`

- Kind: `object`
- Detail: Object 1253 - Elite Konnik (Dismounted)

Class: `infantry-class (906)`

Line: `foot-konnik-line`

Building: Castle

<a id="symbol-elite-gbeto"></a>

## `elite-gbeto`

- Kind: `object`
- Detail: Object WK: 418<br>DE: 1015 - Elite Gbeto

Class: `infantry-class (906)`

Line: `gbeto-line`

Building: Castle

<a id="symbol-elite-genitour"></a>

## `elite-genitour`

- Kind: `object`
- Detail: Object WK: 230<br>DE: 1012 - Elite Genitour

Class: `cavalry-archer-class (936)`

Line: `genitour-line`

Building: Archery Range

<a id="symbol-elite-genoese-crossbowman"></a>

## `elite-genoese-crossbowman`

- Kind: `object`
- Detail: Object 868 - Elite Genoese Crossbowman

Class: `archery-class (900)`

Line: `genoese-crossbowman-line`

Building: Castle

<a id="symbol-elite-ghulam"></a>

## `elite-ghulam`

- Kind: `object`
- Detail: Object 1749 - Elite Ghulam

Class: `infantry-class (906)`

Line: `ghulam-line`

Building: Castle

<a id="symbol-elite-huskarl"></a>

## `elite-huskarl`

- Kind: `object`
- Detail: Object 555 - Elite Huskarl

Class: `infantry-class (906)`

Line: `huskarl-line`

Building: Castle

<a id="symbol-elite-hussite-wagon"></a>

## `elite-hussite-wagon`

- Kind: `object`
- Detail: Object 1706 - Elite Hussite Wagon

Class: `scorpion-class (955)`

Line: `hussite-wagon-line`

Building: Castle

<a id="symbol-elite-iron-pagoda"></a>

## `elite-iron-pagoda`

- Kind: `object`
- Detail: Object 1910 - Elite Iron Pagoda

Class: `cavalry-class (912)`

Line: `iron-pagoda-line`

Building: Castle

<a id="symbol-elite-jaguar-man-elite-jaguar-warrior-de-only-"></a>

## `elite-jaguar-man, elite-jaguar-warrior (DE only)`

- Kind: `object`
- Detail: Object 726 - Elite Jaguar Warrior

Class: `infantry-class (906)`

Line: `jaguar-man-line`

Building: Castle

<a id="symbol-elite-janissary"></a>

## `elite-janissary`

- Kind: `object`
- Detail: Object 557 - Elite Janissary

Class: `archery-cannon-class (944)`

Line: `janissary-line`

Building: Castle

<a id="symbol-elite-kamayuk"></a>

## `elite-kamayuk`

- Kind: `object`
- Detail: Object 881 - Elite Kamayuk

Class: `infantry-class (906)`

Line: `kamayuk-line`

Building: Castle

<a id="symbol-elite-karambit-warrior"></a>

## `elite-karambit-warrior`

- Kind: `object`
- Detail: Object WK: 830<br>DE: 1125 - Elite Karambit Warrior

Class: `infantry-class (906)`

Line: `karambit-warrior-line`

Building: Castle

<a id="symbol-elite-keshik"></a>

## `elite-keshik`

- Kind: `object`
- Detail: Object 1230 - Elite Keshik

Class: `cavalry-class (912)`

Line: `keshik-line`

Building: Castle

<a id="symbol-elite-kipchak"></a>

## `elite-kipchak`

- Kind: `object`
- Detail: Object 1233 - Elite Kipchak

Class: `cavalry-archer-class (936)`

Line: `kipchak-line`

Building: Castle

<a id="symbol-elite-konnik"></a>

## `elite-konnik`

- Kind: `object`
- Detail: Object 1227 - Elite Konnik

Class: `cavalry-class (912)`

Line: `konnik-line`

Building: Castle

<a id="symbol-elite-leitis"></a>

## `elite-leitis`

- Kind: `object`
- Detail: Object 1236 - Elite Leitis

Class: `cavalry-class (912)`

Line: `leitis-line`

Building: Castle

<a id="symbol-elite-liao-dao"></a>

## `elite-liao-dao`

- Kind: `object`
- Detail: Object 1922 - Elite Liao Dao

Class: `infantry-class (906)`

Line: `liao-dao-line`

Building: Castle

<a id="symbol-elite-longboat"></a>

## `elite-longboat`

- Kind: `object`
- Detail: Object 533 - Elite Longboat

Class: `warship-class (922)`

Line: `longboat-line`

Building: Dock

<a id="symbol-elite-longbowman"></a>

## `elite-longbowman`

- Kind: `object`
- Detail: Object 530 - Elite Longbowman

Class: `archery-class (900)`

Line: `longbowman-line`

Building: Castle

<a id="symbol-elite-magyar-huszar"></a>

## `elite-magyar-huszar`

- Kind: `object`
- Detail: Object 871 - Elite Magyar Huszar

Class: `cavalry-class (912)`

Line: `magyar-huszar-line`

Building: Castle

<a id="symbol-elite-mameluke"></a>

## `elite-mameluke`

- Kind: `object`
- Detail: Object 556 - Elite Mameluke

Class: `cavalry-class (912)`

Line: `mameluke-line`

Building: Castle

<a id="symbol-elite-mangudai"></a>

## `elite-mangudai`

- Kind: `object`
- Detail: Object 561 - Elite Mangudai

Class: `cavalry-archer-class (936)`

Line: `mangudai-line`

Building: Castle

<a id="symbol-elite-monaspa"></a>

## `elite-monaspa`

- Kind: `object`
- Detail: Object 1805 - Elite Monaspa

Class: `cavalry-class (912)`

Line: `monaspa-line`

Building: Castle

<a id="symbol-elite-obuch"></a>

## `elite-obuch`

- Kind: `object`
- Detail: Object 1703 - Elite Obuch

Class: `infantry-class (906)`

Line: `obuch-line`

Building: Castle

<a id="symbol-elite-organ-gun"></a>

## `elite-organ-gun`

- Kind: `object`
- Detail: Object WK: 114<br>DE: 1003 - Elite Organ Gun

Class: `siege-weapon-class (913)`

Line: `organ-gun-line`

Building: Castle

<a id="symbol-elite-plumed-archer"></a>

## `elite-plumed-archer`

- Kind: `object`
- Detail: Object 765 - Elite Plumed Archer

Class: `archery-class (900)`

Line: `plumed-archer-line`

Building: Castle

<a id="symbol-elite-ratha-melee"></a>

## `elite-ratha-melee`

- Kind: `object`
- Detail: Object 1740 - Elite Ratha (Melee)

Class: `cavalry-class (912)`

Line: `ratha-melee-line`

Building: Castle

<a id="symbol-elite-ratha-ranged"></a>

## `elite-ratha-ranged`

- Kind: `object`
- Detail: Object 1761 - Elite Ratha (Ranged)

Class: `cavalry-archer-class (936)`

Line: `ratha-ranged-line`

Building: Castle

<a id="symbol-elite-rattan-archer"></a>

## `elite-rattan-archer`

- Kind: `object`
- Detail: Object WK: 782<br>DE: 1131 - Elite Rattan Archer

Class: `archery-class (900)`

Line: `rattan-archer-line`

Building: Castle

<a id="symbol-elite-samurai"></a>

## `elite-samurai`

- Kind: `object`
- Detail: Object 560 - Elite Samurai

Class: `infantry-class (906)`

Line: `samurai-line`

Building: Castle

<a id="symbol-elite-serjeant"></a>

## `elite-serjeant`

- Kind: `object`
- Detail: Object 1659 - Elite Serjeant

Class: `infantry-class (906)`

Line: `serjeant-line`

Building: Castle

<a id="symbol-elite-shotel-elite-shotel-warrior"></a>

## `elite-shotel, elite-shotel-warrior`

- Kind: `object`
- Detail: Object WK: 459<br>DE: 1018 - Elite Shotel Warrior

Class: `infantry-class (906)`

Line: `shotel-warrior-line`

Building: Castle

<a id="symbol-elite-shrivamsha-rider"></a>

## `elite-shrivamsha-rider`

- Kind: `object`
- Detail: Object 1753 - Elite Shrivamsha Rider

Class: `cavalry-class (912)`

Line: `shrivamsha-rider-line`

Building: Stable

<a id="symbol-elite-skirmisher"></a>

## `elite-skirmisher`

- Kind: `object`
- Detail: Object 6 - Elite Skirmisher

Class: `archery-class (900)`

Line: `skirmisher-line`

Building: Archery Range

<a id="symbol-elite-steppe-lancer"></a>

## `elite-steppe-lancer`

- Kind: `object`
- Detail: Object 1372 - Elite Steppe Lancer

Class: `cavalry-class (912)`

Line: `steppe-lancer-line`

Building: Stable

<a id="symbol-elite-tarkan"></a>

## `elite-tarkan`

- Kind: `object`
- Detail: Object 757 - Elite Tarkan

Class: `cavalry-class (912)`

Line: `tarkan-line`

Building: Castle

<a id="symbol-elite-teutonic-knight"></a>

## `elite-teutonic-knight`

- Kind: `object`
- Detail: Object 554 - Elite Teutonic Knight

Class: `infantry-class (906)`

Line: `teutonic-knight-line`

Building: Castle

<a id="symbol-elite-throwing-axeman"></a>

## `elite-throwing-axeman`

- Kind: `object`
- Detail: Object 531 - Elite Throwing Axeman

Class: `infantry-class (906)`

Line: `throwing-axeman-line`

Building: Castle

<a id="symbol-elite-tiger-cavalry"></a>

## `elite-tiger-cavalry`

- Kind: `object`
- Detail: Object 1951 - Elite Tiger Cavalry

Class: `cavalry-class (912)`

Line: `tiger-cavalry-line`

Building: Castle

<a id="symbol-elite-turtle-ship"></a>

## `elite-turtle-ship`

- Kind: `object`
- Detail: Object 832 - Elite Turtle Ship

Class: `warship-class (922)`

Line: `turtle-ship-line`

Building: Dock

<a id="symbol-elite-urumi-swordsman"></a>

## `elite-urumi-swordsman`

- Kind: `object`
- Detail: Object 1737 - Elite Urumi Swordsman

Class: `infantry-class (906)`

Line: `urumi-swordsman-line`

Building: Castle

<a id="symbol-elite-war-elephant"></a>

## `elite-war-elephant`

- Kind: `object`
- Detail: Object 558 - Elite War Elephant

Class: `cavalry-class (912)`

Line: `war-elephant-line`

Building: Castle

<a id="symbol-elite-war-wagon"></a>

## `elite-war-wagon`

- Kind: `object`
- Detail: Object 829 - Elite War Wagon

Class: `cavalry-archer-class (936)`

Line: `war-wagon-line`

Building: Castle

<a id="symbol-elite-white-feather-guard"></a>

## `elite-white-feather-guard`

- Kind: `object`
- Detail: Object 1961 - Elite White Feather Guard

Class: `infantry-class (906)`

Line: `white-feather-guard-line`

Building: Castle

<a id="symbol-elite-woad-raider"></a>

## `elite-woad-raider`

- Kind: `object`
- Detail: Object 534 - Elite Woad Raider

Class: `infantry-class (906)`

Line: `woad-raider-line`

Building: Castle

<a id="symbol-farm"></a>

## `farm`

- Kind: `object`
- Detail: Object 50 - Farm

Class: `farm-class (949)`

Building: Buildings

<a id="symbol-fast-fire-ship"></a>

## `fast-fire-ship`

- Kind: `object`
- Detail: Object 532 - Fast Fire Ship

Class: `warship-class (922)`

Line: `fire-ship-line`

Building: Dock

<a id="symbol-feitoria"></a>

## `feitoria`

- Kind: `object`
- Detail: Object WK: 734<br>DE: 1021 - Feitoria

Class: `building-class (903)`

Building: Buildings

<a id="symbol-feudal-battering-ram"></a>

## `feudal-battering-ram`

- Kind: `object`
- Detail: Object 1258 - Battering Ram (Feudal)

Class: `siege-weapon-class (913)`

Line: `battering-ram-line`

Building: Siege Workshop

<a id="symbol-fire-archer"></a>

## `fire-archer`

- Kind: `object`
- Detail: Object 1968 - Fire Archer

Class: `archery-class (900)`

Line: `fire-archer-line`

Building: Castle

<a id="symbol-fire-archer-line"></a>

## `fire-archer-line`

- Kind: `object`
- Detail: Object line - Fire Archer

Line token from Fire Archer.

<a id="symbol-fire-galley"></a>

## `fire-galley`

- Kind: `object`
- Detail: Object WK: 529<br>DE: 1103 - Fire Galley

Class: `warship-class (922)`

Line: `fire-ship-line`

Building: Dock

<a id="symbol-fire-lancer-line"></a>

## `fire-lancer-line`

- Kind: `object`
- Detail: Object line - Fire Lancer

Line token from Fire Lancer.

<a id="symbol-fire-ship"></a>

## `fire-ship`

- Kind: `object`
- Detail: Object 529 - Fire Ship (non-WK)

Class: `warship-class (922)`

Line: `fire-ship-line`

Building: Dock

<a id="symbol-fire-ship-line"></a>

## `fire-ship-line`

- Kind: `object`
- Detail: Object line - Fire Galley

Line token from Fire Galley.

<a id="symbol-fish-trap"></a>

## `fish-trap`

- Kind: `object`
- Detail: Object 199 - Fish Trap

Class: `farm-class (949)`

Building: Buildings

<a id="symbol-fishing-ship"></a>

## `fishing-ship`

- Kind: `object`
- Detail: Object 13 - Fishing Ship

Class: `fishing-ship-class (921)`

Building: Dock

<a id="symbol-flaming-camel"></a>

## `flaming-camel`

- Kind: `object`
- Detail: Object 1263 - Flaming Camel

Class: `petard-class (935)`

Building: Castle

<a id="symbol-flare"></a>

## `flare`

- Kind: `object`
- Detail: Object 274 - Flare

Class: `miscellaneous-class (911)`

Building: Other

<a id="symbol-flemish-pikeman"></a>

## `flemish-pikeman`

- Kind: `object`
- Detail: Object 1663 - Flemish Militia (Male)

Class: `infantry-class (906)`

<a id="symbol-flemish-pikeman-female"></a>

## `flemish-pikeman-female`

- Kind: `object`
- Detail: Object 1697 - Flemish Militia (Female)

Class: `infantry-class (906)`

<a id="symbol-foot-konnik"></a>

## `foot-konnik`

- Kind: `object`
- Detail: Object 1252 - Konnik (Dismounted)

Class: `infantry-class (906)`

Line: `foot-konnik-line`

Building: Castle

<a id="symbol-foot-konnik-line"></a>

## `foot-konnik-line`

- Kind: `object`
- Detail: Object line - Konnik (Dismounted)

Line token from Konnik (Dismounted).

<a id="symbol-fortified-wall"></a>

## `fortified-wall`

- Kind: `object`
- Detail: Object 155 - Fortified Wall

Class: `wall-class (927)`

Line: `stone-wall-line`

Building: Buildings

<a id="symbol-galleon"></a>

## `galleon`

- Kind: `object`
- Detail: Object 442 - Galleon

Class: `warship-class (922)`

Line: `galley-line`

Building: Dock

<a id="symbol-galley"></a>

## `galley`

- Kind: `object`
- Detail: Object 539 - Galley

Class: `warship-class (922)`

Line: `galley-line`

Building: Dock

<a id="symbol-galley-line"></a>

## `galley-line`

- Kind: `object`
- Detail: Object line - Galley

Line token from Galley.

<a id="symbol-gate-ascending-closed"></a>

## `gate-ascending-closed`

- Kind: `object`
- Detail: Object 64 - Gate (Ascending Closed)

Class: `gate-class (939)`

Building: Buildings

<a id="symbol-gate-ascending-open"></a>

## `gate-ascending-open`

- Kind: `object`
- Detail: Object 78 - Gate (Ascending Open)

Class: `gate-class (939)`

Building: Buildings

<a id="symbol-gate-descending"></a>

## `gate-descending`

- Kind: `object`
- Detail: Object 490 - Gate (Descending Foundation)

Class: `gate-class (939)`

Building: Buildings

<a id="symbol-gate-descending-closed"></a>

## `gate-descending-closed`

- Kind: `object`
- Detail: Object 88 - Gate (Descending Closed)

Class: `gate-class (939)`

Building: Buildings

<a id="symbol-gate-horizontal"></a>

## `gate-horizontal`

- Kind: `object`
- Detail: Object 665 - Gate (Horizontal Foundation)

Class: `gate-class (939)`

Building: Buildings

<a id="symbol-gate-horizontal-closed"></a>

## `gate-horizontal-closed`

- Kind: `object`
- Detail: Object 659 - Gate (Horizontal Closed)

Class: `gate-class (939)`

Building: Buildings

<a id="symbol-gate-horizontal-open"></a>

## `gate-horizontal-open`

- Kind: `object`
- Detail: Object 661 - Gate (Horizontal Open)

Class: `gate-class (939)`

Building: Buildings

<a id="symbol-gate-vertical"></a>

## `gate-vertical`

- Kind: `object`
- Detail: Object 673 - Gate (Vertical Foundation)

Class: `gate-class (939)`

Building: Buildings

<a id="symbol-gate-vertical-closed"></a>

## `gate-vertical-closed`

- Kind: `object`
- Detail: Object 667 - Gate (Vertical Closed)

Class: `gate-class (939)`

Building: Buildings

<a id="symbol-gate-vertical-open"></a>

## `gate-vertical-open`

- Kind: `object`
- Detail: Object 669 - Gate (Vertical Open)

Class: `gate-class (939)`

Building: Buildings

<a id="symbol-gate-br-gate-ascending"></a>

## `gate,<br>gate-ascending`

- Kind: `object`
- Detail: Object 487 - Gate (Ascending Foundation)

Class: `gate-class (939)`

Building: Buildings

<a id="symbol-gbeto"></a>

## `gbeto`

- Kind: `object`
- Detail: Object WK: 260<br>DE: 1013 - Gbeto

Class: `infantry-class (906)`

Line: `gbeto-line`

Building: Castle

<a id="symbol-gbeto-line"></a>

## `gbeto-line`

- Kind: `object`
- Detail: Object line - Gbeto

Line token from Gbeto.

<a id="symbol-genitour"></a>

## `genitour`

- Kind: `object`
- Detail: Object WK: 223<br>DE: 1010 - Genitour

Class: `cavalry-archer-class (936)`

Line: `genitour-line`

Building: Archery Range

<a id="symbol-genitour-line"></a>

## `genitour-line`

- Kind: `object`
- Detail: Object line - Genitour

Line token from Genitour.

<a id="symbol-genoese-crossbowman"></a>

## `genoese-crossbowman`

- Kind: `object`
- Detail: Object 866 - Genoese Crossbowman

Class: `archery-class (900)`

Line: `genoese-crossbowman-line`

Building: Castle

<a id="symbol-genoese-crossbowman-line"></a>

## `genoese-crossbowman-line`

- Kind: `object`
- Detail: Object line - Genoese Crossbowman

Line token from Genoese Crossbowman.

<a id="symbol-ghulam"></a>

## `ghulam`

- Kind: `object`
- Detail: Object 1747 - Ghulam

Class: `infantry-class (906)`

Line: `ghulam-line`

Building: Castle

<a id="symbol-ghulam-line"></a>

## `ghulam-line`

- Kind: `object`
- Detail: Object line - Ghulam

Line token from Ghulam.

<a id="symbol-guard-tower"></a>

## `guard-tower`

- Kind: `object`
- Detail: Object 234 - Guard Tower

Class: `tower-class (952)`

Line: `watch-tower-line`

Building: Buildings

<a id="symbol-guecha-warrior-line"></a>

## `guecha-warrior-line`

- Kind: `object`
- Detail: Object line - Guecha Warrior

Line token from Guecha Warrior.

<a id="symbol-halberdier"></a>

## `halberdier`

- Kind: `object`
- Detail: Object 359 - Halberdier

Class: `infantry-class (906)`

Line: `spearman-line`

Building: Barracks

<a id="symbol-hand-cannoneer"></a>

## `hand-cannoneer`

- Kind: `object`
- Detail: Object 5 - Hand Cannoneer

Class: `archery-cannon-class (944)`

Building: Archery Range

<a id="symbol-heavy-camel-heavy-camel-rider-de-only-"></a>

## `heavy-camel, heavy-camel-rider (DE only)`

- Kind: `object`
- Detail: Object 330 - Heavy Camel [Rider]

Class: `cavalry-class (912)`

Line: `camel-line`

Building: Stable

<a id="symbol-heavy-cavalry-archer"></a>

## `heavy-cavalry-archer`

- Kind: `object`
- Detail: Object 474 - Heavy Cavalry Archer

Class: `cavalry-archer-class (936)`

Line: `cavalry-archer-line`

Building: Archery Range

<a id="symbol-heavy-demolition-ship"></a>

## `heavy-demolition-ship`

- Kind: `object`
- Detail: Object 528 - Heavy Demolition Ship

Class: `warship-class (922)`

Line: `demolition-ship-line`

Building: Dock

<a id="symbol-heavy-eagle-warrior"></a>

## `heavy-eagle-warrior`

- Kind: `object`
- Detail: Object 753 - Eagle Warrior

Class: `infantry-class (906)`

Line: `eagle-warrior-line`

Building: Barracks

<a id="symbol-heavy-hei-guang-cavalry"></a>

## `heavy-hei-guang-cavalry`

- Kind: `object`
- Detail: Object 1946 - Heavy Hei Guang Cavalry

Class: `cavalry-class (912)`

Line: `hei-guang-cavalry-line`

Building: Stable

<a id="symbol-heavy-scorpion"></a>

## `heavy-scorpion`

- Kind: `object`
- Detail: Object 542 - Heavy Scorpion

Class: `scorpion-class (955)`

Line: `scorpion-line`

Building: Siege Workshop

<a id="symbol-hei-guang-cavalry"></a>

## `hei-guang-cavalry`

- Kind: `object`
- Detail: Object 1944 - Hei Guang Cavalry

Class: `cavalry-class (912)`

Line: `hei-guang-cavalry-line`

Building: Stable

<a id="symbol-hei-guang-cavalry-line"></a>

## `hei-guang-cavalry-line`

- Kind: `object`
- Detail: Object line - Hei Guang Cavalry

Line token from Hei Guang Cavalry.

<a id="symbol-houfnice"></a>

## `houfnice`

- Kind: `object`
- Detail: Object 1709 - Houfnice

Class: `siege-weapon-class (913)`

Line: `bombard-cannon-line`

Building: Siege Workshop

<a id="symbol-house"></a>

## `house`

- Kind: `object`
- Detail: Object 70 - House (Dark Age)

Class: `building-class (903)`

Building: Buildings

<a id="symbol-hulk-line"></a>

## `hulk-line`

- Kind: `object`
- Detail: Object line - Hulk

Line token from Hulk.

<a id="symbol-huskarl"></a>

## `huskarl`

- Kind: `object`
- Detail: Object 41 - Huskarl

Class: `infantry-class (906)`

Line: `huskarl-line`

Building: Castle

<a id="symbol-huskarl-line"></a>

## `huskarl-line`

- Kind: `object`
- Detail: Object line - Huskarl

Line token from Huskarl.

<a id="symbol-hussar"></a>

## `hussar`

- Kind: `object`
- Detail: Object 441 - Hussar

Class: `scout-cavalry-class (947)`

Line: `scout-cavalry-line`

Building: Stable

<a id="symbol-hussite-wagon"></a>

## `hussite-wagon`

- Kind: `object`
- Detail: Object 1704 - Hussite Wagon

Class: `scorpion-class (955)`

Line: `hussite-wagon-line`

Building: Castle

<a id="symbol-hussite-wagon-line"></a>

## `hussite-wagon-line`

- Kind: `object`
- Detail: Object line - Hussite Wagon

Line token from Hussite Wagon.

<a id="symbol-ibirapema-warrior-line"></a>

## `ibirapema-warrior-line`

- Kind: `object`
- Detail: Object line - Ibirapema Warrior

Line token from Ibirapema Warrior.

<a id="symbol-imperial-camel-imperial-camel-rider"></a>

## `imperial-camel, imperial-camel-rider`

- Kind: `object`
- Detail: Object 207 - Imperial Camel [Rider]

Class: `cavalry-class (912)`

Line: `camel-line`

Building: Stable

<a id="symbol-imperial-skirmisher"></a>

## `imperial-skirmisher`

- Kind: `object`
- Detail: Object WK: 762<br>DE: 1155 - Imperial Skirmisher

Class: `archery-class (900)`

Line: `skirmisher-line`

Building: Archery Range

<a id="symbol-incendiary-raft-line"></a>

## `incendiary-raft-line`

- Kind: `object`
- Detail: Object line - Incendiary Raft

Line token from Incendiary Raft.

<a id="symbol-iron-pagoda"></a>

## `iron-pagoda`

- Kind: `object`
- Detail: Object 1908 - Iron Pagoda

Class: `cavalry-class (912)`

Line: `iron-pagoda-line`

Building: Castle

<a id="symbol-iron-pagoda-line"></a>

## `iron-pagoda-line`

- Kind: `object`
- Detail: Object line - Iron Pagoda

Line token from Iron Pagoda.

<a id="symbol-jaguar-man-line"></a>

## `jaguar-man-line`

- Kind: `object`
- Detail: Object line - Jaguar Warrior

Line token from Jaguar Warrior.

<a id="symbol-jaguar-man-jaguar-warrior-de-only-"></a>

## `jaguar-man, jaguar-warrior (DE only)`

- Kind: `object`
- Detail: Object 725 - Jaguar Warrior

Class: `infantry-class (906)`

Line: `jaguar-man-line`

Building: Castle

<a id="symbol-janissary"></a>

## `janissary`

- Kind: `object`
- Detail: Object 46 - Janissary

Class: `archery-cannon-class (944)`

Line: `janissary-line`

Building: Castle

<a id="symbol-janissary-line"></a>

## `janissary-line`

- Kind: `object`
- Detail: Object line - Janissary

Line token from Janissary.

<a id="symbol-kamayuk"></a>

## `kamayuk`

- Kind: `object`
- Detail: Object 879 - Kamayuk

Class: `infantry-class (906)`

Line: `kamayuk-line`

Building: Castle

<a id="symbol-kamayuk-line"></a>

## `kamayuk-line`

- Kind: `object`
- Detail: Object line - Kamayuk

Line token from Kamayuk.

<a id="symbol-karambit-warrior"></a>

## `karambit-warrior`

- Kind: `object`
- Detail: Object WK: 836<br>DE: 1123 - Karambit Warrior

Class: `infantry-class (906)`

Line: `karambit-warrior-line`

Building: Castle

<a id="symbol-karambit-warrior-line"></a>

## `karambit-warrior-line`

- Kind: `object`
- Detail: Object line - Karambit Warrior

Line token from Karambit Warrior.

<a id="symbol-keep"></a>

## `keep`

- Kind: `object`
- Detail: Object 235 - Keep

Class: `tower-class (952)`

Line: `watch-tower-line`

Building: Buildings

<a id="symbol-keshik"></a>

## `keshik`

- Kind: `object`
- Detail: Object 1228 - Keshik

Class: `cavalry-class (912)`

Line: `keshik-line`

Building: Castle

<a id="symbol-keshik-line"></a>

## `keshik-line`

- Kind: `object`
- Detail: Object line - Keshik

Line token from Keshik.

<a id="symbol-kipchak"></a>

## `kipchak`

- Kind: `object`
- Detail: Object 1231 - Kipchak

Class: `cavalry-archer-class (936)`

Line: `kipchak-line`

Building: Castle

<a id="symbol-kipchak-line"></a>

## `kipchak-line`

- Kind: `object`
- Detail: Object line - Kipchak

Line token from Kipchak.

<a id="symbol-knight"></a>

## `knight`

- Kind: `object`
- Detail: Object 38 - Knight

Class: `cavalry-class (912)`

Line: `knight-line`

Building: Stable

<a id="symbol-knight-line"></a>

## `knight-line`

- Kind: `object`
- Detail: Object line - Knight

Line token from Knight.

<a id="symbol-kona-line"></a>

## `kona-line`

- Kind: `object`
- Detail: Object line - Kona

Line token from Kona.

<a id="symbol-konnik"></a>

## `konnik`

- Kind: `object`
- Detail: Object 1225 - Konnik

Class: `cavalry-class (912)`

Line: `konnik-line`

Building: Castle

<a id="symbol-konnik-line"></a>

## `konnik-line`

- Kind: `object`
- Detail: Object line - Konnik

Line token from Konnik.

<a id="symbol-krepost"></a>

## `krepost`

- Kind: `object`
- Detail: Object 1251 - Krepost

Class: `building-class (903)`

Building: Buildings

<a id="symbol-legionary"></a>

## `legionary`

- Kind: `object`
- Detail: Object 1793 - Legionary

Class: `infantry-class (906)`

Line: `militiaman-line`

Building: Barracks

<a id="symbol-leitis"></a>

## `leitis`

- Kind: `object`
- Detail: Object 1234 - Leitis

Class: `cavalry-class (912)`

Line: `leitis-line`

Building: Castle

<a id="symbol-leitis-line"></a>

## `leitis-line`

- Kind: `object`
- Detail: Object line - Leitis

Line token from Leitis.

<a id="symbol-lembos-line"></a>

## `lembos-line`

- Kind: `object`
- Detail: Object line - Lembos

Line token from Lembos.

<a id="symbol-liao-dao"></a>

## `liao-dao`

- Kind: `object`
- Detail: Object 1920 - Liao Dao

Class: `infantry-class (906)`

Line: `liao-dao-line`

Building: Castle

<a id="symbol-liao-dao-line"></a>

## `liao-dao-line`

- Kind: `object`
- Detail: Object line - Liao Dao

Line token from Liao Dao.

<a id="symbol-light-cavalry"></a>

## `light-cavalry`

- Kind: `object`
- Detail: Object 546 - Light Cavalry

Class: `scout-cavalry-class (947)`

Line: `scout-cavalry-line`

Building: Stable

<a id="symbol-long-swordsman"></a>

## `long-swordsman`

- Kind: `object`
- Detail: Object 77 - Long Swordsman

Class: `infantry-class (906)`

Line: `militiaman-line`

Building: Barracks

<a id="symbol-longboat"></a>

## `longboat`

- Kind: `object`
- Detail: Object 250 - Longboat

Class: `warship-class (922)`

Line: `longboat-line`

Building: Dock

<a id="symbol-longboat-line"></a>

## `longboat-line`

- Kind: `object`
- Detail: Object line - Longboat

Line token from Longboat.

<a id="symbol-longbowman"></a>

## `longbowman`

- Kind: `object`
- Detail: Object 8 - Longbowman

Class: `archery-class (900)`

Line: `longbowman-line`

Building: Castle

<a id="symbol-longbowman-line"></a>

## `longbowman-line`

- Kind: `object`
- Detail: Object line - Longbowman

Line token from Longbowman.

<a id="symbol-lumber-camp"></a>

## `lumber-camp`

- Kind: `object`
- Detail: Object 562 - Lumber Camp (Dark Age)

Class: `building-class (903)`

Building: Buildings

<a id="symbol-magyar-huszar"></a>

## `magyar-huszar`

- Kind: `object`
- Detail: Object 869 - Magyar Huszar

Class: `cavalry-class (912)`

Line: `magyar-huszar-line`

Building: Castle

<a id="symbol-magyar-huszar-line"></a>

## `magyar-huszar-line`

- Kind: `object`
- Detail: Object line - Magyar Huszar

Line token from Magyar Huszar.

<a id="symbol-mameluke"></a>

## `mameluke`

- Kind: `object`
- Detail: Object 282 - Mameluke

Class: `cavalry-class (912)`

Line: `mameluke-line`

Building: Castle

<a id="symbol-mameluke-line"></a>

## `mameluke-line`

- Kind: `object`
- Detail: Object line - Mameluke

Line token from Mameluke.

<a id="symbol-man-at-arms"></a>

## `man-at-arms`

- Kind: `object`
- Detail: Object 75 - Man-at-Arms

Class: `infantry-class (906)`

Line: `militiaman-line`

Building: Barracks

<a id="symbol-mangonel"></a>

## `mangonel`

- Kind: `object`
- Detail: Object 280 - Mangonel

Class: `siege-weapon-class (913)`

Line: `mangonel-line`

Building: Siege Workshop

<a id="symbol-mangonel-line"></a>

## `mangonel-line`

- Kind: `object`
- Detail: Object line - Mangonel

Line token from Mangonel.

<a id="symbol-mangudai"></a>

## `mangudai`

- Kind: `object`
- Detail: Object 11 - Mangudai

Class: `cavalry-archer-class (936)`

Line: `mangudai-line`

Building: Castle

<a id="symbol-mangudai-line"></a>

## `mangudai-line`

- Kind: `object`
- Detail: Object line - Mangudai

Line token from Mangudai.

<a id="symbol-market"></a>

## `market`

- Kind: `object`
- Detail: Object 84 - Market (Feudal Age)

Class: `building-class (903)`

Building: Buildings

<a id="symbol-mercenary-kipchak"></a>

## `mercenary-kipchak`

- Kind: `object`
- Detail: Object 1260 - Elite Kipchak (Mercenary)

Class: `cavalry-archer-class (936)`

Building: Castle

<a id="symbol-militiaman"></a>

## `militiaman`

- Kind: `object`
- Detail: Object 74 - Short Swordsman

Class: `infantry-class (906)`

Line: `-294`

Building: Barracks

<a id="symbol-militiaman-line"></a>

## `militiaman-line`

- Kind: `object`
- Detail: Object line - Militia

Line token from Militia.

<a id="symbol-militiaman-militia-de-only-"></a>

## `militiaman, militia (DE only)`

- Kind: `object`
- Detail: Object 74 - Militia

Class: `infantry-class (906)`

Line: `militiaman-line`

Building: Barracks

<a id="symbol-mill"></a>

## `mill`

- Kind: `object`
- Detail: Object 68 - Mill (Dark Age)

Class: `building-class (903)`

Building: Buildings

<a id="symbol-mining-camp"></a>

## `mining-camp`

- Kind: `object`
- Detail: Object 584 - Mining Camp (Dark Age)

Class: `building-class (903)`

Building: Buildings

<a id="symbol-missionary"></a>

## `missionary`

- Kind: `object`
- Detail: Object 775 - Missionary

Class: `monastery-class (918)`

Building: Monastery

<a id="symbol-monaspa"></a>

## `monaspa`

- Kind: `object`
- Detail: Object 1803 - Monaspa

Class: `cavalry-class (912)`

Line: `monaspa-line`

Building: Castle

<a id="symbol-monaspa-line"></a>

## `monaspa-line`

- Kind: `object`
- Detail: Object line - Monaspa

Line token from Monaspa.

<a id="symbol-monastery"></a>

## `monastery`

- Kind: `object`
- Detail: Object 104 - Monastery (Castle Age, Base)

Class: `building-class (903)`

Building: Buildings

<a id="symbol-monk"></a>

## `monk`

- Kind: `object`
- Detail: Object 125 - Monk

Class: `monastery-class (918)`

Building: Monastery

<a id="symbol-monk-with-relic"></a>

## `monk-with-relic`

- Kind: `object`
- Detail: Object 286 - Monk with Relic

Class: `monk-with-relic-class (943)`

Building: Monastery

<a id="symbol-monoreme-line"></a>

## `monoreme-line`

- Kind: `object`
- Detail: Object line - Monoreme

Line token from Monoreme.

<a id="symbol-mule-cart"></a>

## `mule-cart`

- Kind: `object`
- Detail: Object 1808 - Mule Cart

Class: `building-class (903)`

Building: Buildings

<a id="symbol-obuch"></a>

## `obuch`

- Kind: `object`
- Detail: Object 1701 - Obuch

Class: `infantry-class (906)`

Line: `obuch-line`

Building: Castle

<a id="symbol-obuch-line"></a>

## `obuch-line`

- Kind: `object`
- Detail: Object line - Obuch

Line token from Obuch.

<a id="symbol-onager"></a>

## `onager`

- Kind: `object`
- Detail: Object 550 - Onager (non-WK)

Class: `siege-weapon-class (913)`

Line: `mangonel-line`

Building: Siege Workshop

<a id="symbol-organ-gun"></a>

## `organ-gun`

- Kind: `object`
- Detail: Object WK: 106<br>DE: 1001 - Organ Gun

Class: `siege-weapon-class (913)`

Line: `organ-gun-line`

Building: Castle

<a id="symbol-organ-gun-line"></a>

## `organ-gun-line`

- Kind: `object`
- Detail: Object line - Organ Gun

Line token from Organ Gun.

<a id="symbol-outpost"></a>

## `outpost`

- Kind: `object`
- Detail: Object 598 - Outpost

Class: `building-class (903)`

Building: Buildings

<a id="symbol-paladin"></a>

## `paladin`

- Kind: `object`
- Detail: Object 569 - Paladin

Class: `cavalry-class (912)`

Line: `knight-line`

Building: Stable

<a id="symbol-palisade-wall"></a>

## `palisade-wall`

- Kind: `object`
- Detail: Object 72 - Palisade Wall

Class: `wall-class (927)`

Building: Buildings

<a id="symbol-petard"></a>

## `petard`

- Kind: `object`
- Detail: Object 440 - Petard

Class: `petard-class (935)`

Building: Castle

<a id="symbol-pikeman"></a>

## `pikeman`

- Kind: `object`
- Detail: Object 358 - Pikeman

Class: `infantry-class (906)`

Line: `spearman-line`

Building: Barracks

<a id="symbol-plumed-archer"></a>

## `plumed-archer`

- Kind: `object`
- Detail: Object 763 - Plumed Archer

Class: `archery-class (900)`

Line: `plumed-archer-line`

Building: Castle

<a id="symbol-plumed-archer-line"></a>

## `plumed-archer-line`

- Kind: `object`
- Detail: Object line - Plumed Archer

Line token from Plumed Archer.

<a id="symbol-ratha-melee"></a>

## `ratha-melee`

- Kind: `object`
- Detail: Object 1738 - Ratha (Melee)

Class: `cavalry-class (912)`

Line: `ratha-melee-line`

Building: Castle

<a id="symbol-ratha-melee-line"></a>

## `ratha-melee-line`

- Kind: `object`
- Detail: Object line - Ratha (Melee)

Line token from Ratha (Melee).

<a id="symbol-ratha-ranged"></a>

## `ratha-ranged`

- Kind: `object`
- Detail: Object 1759 - Ratha (Ranged)

Class: `cavalry-archer-class (936)`

Line: `ratha-ranged-line`

Building: Castle

<a id="symbol-ratha-ranged-line"></a>

## `ratha-ranged-line`

- Kind: `object`
- Detail: Object line - Ratha (Ranged)

Line token from Ratha (Ranged).

<a id="symbol-rattan-archer"></a>

## `rattan-archer`

- Kind: `object`
- Detail: Object WK: 784<br>DE: 1129 - Rattan Archer

Class: `archery-class (900)`

Line: `rattan-archer-line`

Building: Castle

<a id="symbol-rattan-archer-line"></a>

## `rattan-archer-line`

- Kind: `object`
- Detail: Object line - Rattan Archer

Line token from Rattan Archer.

<a id="symbol-rocket-cart-line"></a>

## `rocket-cart-line`

- Kind: `object`
- Detail: Object line - Rocket Cart

Line token from Rocket Cart.

<a id="symbol-samurai"></a>

## `samurai`

- Kind: `object`
- Detail: Object 291 - Samurai

Class: `infantry-class (906)`

Line: `samurai-line`

Building: Castle

<a id="symbol-samurai-line"></a>

## `samurai-line`

- Kind: `object`
- Detail: Object line - Samurai

Line token from Samurai.

<a id="symbol-savar"></a>

## `savar`

- Kind: `object`
- Detail: Object 1814 - Savar

Class: `cavalry-class (912)`

Line: `knight-line`

Building: Stable

<a id="symbol-scorpion"></a>

## `scorpion`

- Kind: `object`
- Detail: Object 279 - Scorpion

Class: `scorpion-class (955)`

Line: `scorpion-line`

Building: Siege Workshop

<a id="symbol-scorpion-line"></a>

## `scorpion-line`

- Kind: `object`
- Detail: Object line - Scorpion

Line token from Scorpion.

<a id="symbol-scout-cavalry"></a>

## `scout-cavalry`

- Kind: `object`
- Detail: Object 448 - Scout Cavalry

Class: `scout-cavalry-class (947)`

Line: `scout-cavalry-line`

Building: Stable

<a id="symbol-scout-cavalry-line"></a>

## `scout-cavalry-line`

- Kind: `object`
- Detail: Object line - Scout Cavalry

Line token from Scout Cavalry.

<a id="symbol-serjeant"></a>

## `serjeant`

- Kind: `object`
- Detail: Object 1658 - Serjeant

Class: `infantry-class (906)`

Line: `serjeant-line`

Building: Castle

<a id="symbol-serjeant-line"></a>

## `serjeant-line`

- Kind: `object`
- Detail: Object line - Serjeant

Line token from Serjeant.

<a id="symbol-shotel-warrior-line"></a>

## `shotel-warrior-line`

- Kind: `object`
- Detail: Object line - Shotel Warrior

Line token from Shotel Warrior.

<a id="symbol-shotel-shotel-warrior"></a>

## `shotel, shotel-warrior`

- Kind: `object`
- Detail: Object WK: 453<br>DE: 1016 - Shotel Warrior

Class: `infantry-class (906)`

Line: `shotel-warrior-line`

Building: Castle

<a id="symbol-shrivamsha-rider"></a>

## `shrivamsha-rider`

- Kind: `object`
- Detail: Object 1751 - Shrivamsha Rider

Class: `cavalry-class (912)`

Line: `shrivamsha-rider-line`

Building: Stable

<a id="symbol-shrivamsha-rider-line"></a>

## `shrivamsha-rider-line`

- Kind: `object`
- Detail: Object line - Shrivamsha Rider

Line token from Shrivamsha Rider.

<a id="symbol-siege-elephant"></a>

## `siege-elephant`

- Kind: `object`
- Detail: Object 1746 - Siege Elephant

Class: `cavalry-class (912)`

Line: `armored-elephant-line`

Building: Siege Workshop

<a id="symbol-siege-onager"></a>

## `siege-onager`

- Kind: `object`
- Detail: Object 588 - Siege Onager

Class: `siege-weapon-class (913)`

Line: `mangonel-line`

Building: Siege Workshop

<a id="symbol-siege-ram"></a>

## `siege-ram`

- Kind: `object`
- Detail: Object 548 - Siege Ram

Class: `siege-weapon-class (913)`

Line: `battering-ram-line`

Building: Siege Workshop

<a id="symbol-siege-workshop"></a>

## `siege-workshop`

- Kind: `object`
- Detail: Object 49 - Siege Workshop

Class: `building-class (903)`

Building: Buildings

<a id="symbol-skirmisher"></a>

## `skirmisher`

- Kind: `object`
- Detail: Object 7 - Skirmisher

Class: `archery-class (900)`

Line: `skirmisher-line`

Building: Archery Range

<a id="symbol-skirmisher-line"></a>

## `skirmisher-line`

- Kind: `object`
- Detail: Object line - Skirmisher

Line token from Skirmisher.

<a id="symbol-slinger"></a>

## `slinger`

- Kind: `object`
- Detail: Object 185 - Slinger

Class: `archery-class (900)`

Building: Archery Range

<a id="symbol-spearman"></a>

## `spearman`

- Kind: `object`
- Detail: Object 93 - Spearman

Class: `infantry-class (906)`

Line: `spearman-line`

Building: Barracks

<a id="symbol-spearman-line"></a>

## `spearman-line`

- Kind: `object`
- Detail: Object line - Spearman

Line token from Spearman.

<a id="symbol-stable"></a>

## `stable`

- Kind: `object`
- Detail: Object 101 - Stable (Feudal Age)

Class: `building-class (903)`

Building: Buildings

<a id="symbol-steppe-lancer"></a>

## `steppe-lancer`

- Kind: `object`
- Detail: Object 1370 - Steppe Lancer

Class: `cavalry-class (912)`

Line: `steppe-lancer-line`

Building: Stable

<a id="symbol-steppe-lancer-line"></a>

## `steppe-lancer-line`

- Kind: `object`
- Detail: Object line - Steppe Lancer

Line token from Steppe Lancer.

<a id="symbol-stone-wall"></a>

## `stone-wall`

- Kind: `object`
- Detail: Object 117 - Stone Wall

Class: `wall-class (927)`

Line: `stone-wall-line`

Building: Buildings

<a id="symbol-stone-wall-line"></a>

## `stone-wall-line`

- Kind: `object`
- Detail: Object line - Stone Wall

Line token from Stone Wall.

<a id="symbol-strategos-line"></a>

## `strategos-line`

- Kind: `object`
- Detail: Object line - Strategos

Line token from Strategos.

<a id="symbol-tarkan"></a>

## `tarkan`

- Kind: `object`
- Detail: Object 755 - Tarkan

Class: `cavalry-class (912)`

Line: `tarkan-line`

Building: Castle

<a id="symbol-tarkan-line"></a>

## `tarkan-line`

- Kind: `object`
- Detail: Object line - Tarkan

Line token from Tarkan.

<a id="symbol-temple-guard-line"></a>

## `temple-guard-line`

- Kind: `object`
- Detail: Object line - Temple Guard

Line token from Temple Guard.

<a id="symbol-teutonic-knight"></a>

## `teutonic-knight`

- Kind: `object`
- Detail: Object 25 - Teutonic Knight

Class: `infantry-class (906)`

Line: `teutonic-knight-line`

Building: Castle

<a id="symbol-teutonic-knight-line"></a>

## `teutonic-knight-line`

- Kind: `object`
- Detail: Object line - Teutonic Knight

Line token from Teutonic Knight.

<a id="symbol-thirisadai"></a>

## `thirisadai`

- Kind: `object`
- Detail: Object 1750 - Thirisadai

Class: `warship-class (922)`

Building: Dock

<a id="symbol-throwing-axeman"></a>

## `throwing-axeman`

- Kind: `object`
- Detail: Object 281 - Throwing Axeman

Class: `infantry-class (906)`

Line: `throwing-axeman-line`

Building: Castle

<a id="symbol-throwing-axeman-line"></a>

## `throwing-axeman-line`

- Kind: `object`
- Detail: Object line - Throwing Axeman

Line token from Throwing Axeman.

<a id="symbol-tiger-cavalry"></a>

## `tiger-cavalry`

- Kind: `object`
- Detail: Object 1949 - Tiger Cavalry

Class: `cavalry-class (912)`

Line: `tiger-cavalry-line`

Building: Castle

<a id="symbol-tiger-cavalry-line"></a>

## `tiger-cavalry-line`

- Kind: `object`
- Detail: Object line - Tiger Cavalry

Line token from Tiger Cavalry.

<a id="symbol-town-center"></a>

## `town-center`

- Kind: `object`
- Detail: Object 109 - Town Center (Dark Age)

Class: `building-class (903)`

Building: Buildings

<a id="symbol-town-center-flemish-pikeman"></a>

## `town-center-flemish-pikeman`

- Kind: `object`
- Detail: Object 1699 - Flemish Militia (Train)

Class: `infantry-class (906)`

Building: Barracks

<a id="symbol-town-center-foundation"></a>

## `town-center-foundation`

- Kind: `object`
- Detail: Object 621 - Town Center (Foundation)

Class: `building-class (903)`

Building: Buildings

<a id="symbol-trade-cart"></a>

## `trade-cart`

- Kind: `object`
- Detail: Object 128 - Trade Cart (Empty)

Class: `trade-cart-class (919)`

Building: Market

<a id="symbol-trade-cog"></a>

## `trade-cog`

- Kind: `object`
- Detail: Object 17 - Trade Cog

Class: `trade-cog-class (902)`

Building: Dock

<a id="symbol-transport-ship"></a>

## `transport-ship`

- Kind: `object`
- Detail: Object 545 - Transport Ship

Class: `transport-ship-class (920)`

Building: Dock

<a id="symbol-trebuchet"></a>

## `trebuchet`

- Kind: `object`
- Detail: Object 331 - Trebuchet (Packed)

Class: `packed-trebuchet-class (951)`

Building: Castle

<a id="symbol-turtle-ship"></a>

## `turtle-ship`

- Kind: `object`
- Detail: Object 831 - Turtle Ship

Class: `warship-class (922)`

Line: `turtle-ship-line`

Building: Dock

<a id="symbol-turtle-ship-line"></a>

## `turtle-ship-line`

- Kind: `object`
- Detail: Object line - Turtle Ship

Line token from Turtle Ship.

<a id="symbol-two-handed-swordsman"></a>

## `two-handed-swordsman`

- Kind: `object`
- Detail: Object 473 - Two-Handed Swordsman

Class: `infantry-class (906)`

Line: `militiaman-line`

Building: Barracks

<a id="symbol-university"></a>

## `university`

- Kind: `object`
- Detail: Object 209 - University (Castle Age)

Class: `building-class (903)`

Building: Buildings

<a id="symbol-urumi-swordsman"></a>

## `urumi-swordsman`

- Kind: `object`
- Detail: Object 1735 - Urumi Swordsman

Class: `infantry-class (906)`

Line: `urumi-swordsman-line`

Building: Castle

<a id="symbol-urumi-swordsman-line"></a>

## `urumi-swordsman-line`

- Kind: `object`
- Detail: Object line - Urumi Swordsman

Line token from Urumi Swordsman.

<a id="symbol-villager"></a>

## `villager`

- Kind: `object`
- Detail: Object 83 - Villager (Male)

Class: `villager-class (904)`

Building: Town Center

<a id="symbol-war-dog-line"></a>

## `war-dog-line`

- Kind: `object`
- Detail: Object line - War Dog

Line token from War Dog.

<a id="symbol-war-elephant"></a>

## `war-elephant`

- Kind: `object`
- Detail: Object 239 - War Elephant

Class: `cavalry-class (912)`

Line: `war-elephant-line`

Building: Castle

<a id="symbol-war-elephant-line"></a>

## `war-elephant-line`

- Kind: `object`
- Detail: Object line - War Elephant

Line token from War Elephant.

<a id="symbol-war-galley"></a>

## `war-galley`

- Kind: `object`
- Detail: Object 21 - War Galley

Class: `warship-class (922)`

Line: `galley-line`

Building: Dock

<a id="symbol-war-wagon"></a>

## `war-wagon`

- Kind: `object`
- Detail: Object 827 - War Wagon

Class: `cavalry-archer-class (936)`

Line: `war-wagon-line`

Building: Castle

<a id="symbol-war-wagon-line"></a>

## `war-wagon-line`

- Kind: `object`
- Detail: Object line - War Wagon

Line token from War Wagon.

<a id="symbol-warrior-priest"></a>

## `warrior-priest`

- Kind: `object`
- Detail: Object 1811 - Warrior Priest

Class: `infantry-class (906)`

Building: Monastery

<a id="symbol-watch-tower"></a>

## `watch-tower`

- Kind: `object`
- Detail: Object 79 - Watch Tower

Class: `tower-class (952)`

Line: `watch-tower-line`

Building: Buildings

<a id="symbol-watch-tower-line"></a>

## `watch-tower-line`

- Kind: `object`
- Detail: Object line - Watch Tower

Line token from Watch Tower.

<a id="symbol-white-feather-guard-line"></a>

## `white-feather-guard-line`

- Kind: `object`
- Detail: Object line - White Feather Guard

Line token from White Feather Guard.

<a id="symbol-winged-hussar"></a>

## `winged-hussar`

- Kind: `object`
- Detail: Object 1707 - Winged Hussar

Class: `scout-cavalry-class (947)`

Line: `scout-cavalry-line`

Building: Stable

<a id="symbol-woad-raider"></a>

## `woad-raider`

- Kind: `object`
- Detail: Object 232 - Woad Raider

Class: `infantry-class (906)`

Line: `woad-raider-line`

Building: Castle

<a id="symbol-woad-raider-line"></a>

## `woad-raider-line`

- Kind: `object`
- Detail: Object line - Woad Raider

Line token from Woad Raider.

<a id="symbol-wonder"></a>

## `wonder`

- Kind: `object`
- Detail: Object 276 - Wonder

Class: `building-class (903)`

Building: Buildings

<a id="section-strategic-number"></a>

# strategic-number

<a id="symbol-sn-add-starting-resource-food"></a>

## `sn-add-starting-resource-food`

- Kind: `strategic-number`
- Detail: SN 138 - Economy

Cheat - adds extra food to starting resources.

Default: `0`

Required range: `Min to Max`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-add-starting-resource-food)

<a id="symbol-sn-add-starting-resource-gold"></a>

## `sn-add-starting-resource-gold`

- Kind: `strategic-number`
- Detail: SN 139 - Economy

Cheat - adds extra gold to starting resources.

Default: `0`

Required range: `Min to Max`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-add-starting-resource-gold)

<a id="symbol-sn-add-starting-resource-stone"></a>

## `sn-add-starting-resource-stone`

- Kind: `strategic-number`
- Detail: SN 140 - Economy

Cheat - adds extra stone to starting resources.

Default: `0`

Required range: `Min to Max`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-add-starting-resource-stone)

<a id="symbol-sn-add-starting-resource-wood"></a>

## `sn-add-starting-resource-wood`

- Kind: `strategic-number`
- Detail: SN 141 - Economy

Cheat - adds extra wood to starting resources.

Default: `0`

Required range: `Min to Max`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-add-starting-resource-wood)

<a id="symbol-sn-allow-adjacent-dropsites"></a>

## `sn-allow-adjacent-dropsites`

- Kind: `strategic-number`
- Detail: SN 272 - Buildings

Set to 1 to eliminate the standard requirement for a 1 tile buffer around mills, lumber camps, and mining camps. If set to 0, the 1 tile buffer is enforced as usual.

Default: `0`

Required range: `0 to 1`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-allow-adjacent-dropsites)

<a id="symbol-sn-allow-capturing-gaia-units"></a>

## `sn-allow-capturing-gaia-units`

- Kind: `strategic-number`
- Detail: SN 309 - Other

Set > 0 to allow AI player to convert units owned by Gaia.

Default: `0`

Required range: `0 to Max`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-allow-capturing-gaia-units)

<a id="symbol-sn-allow-civilian-defense"></a>

## `sn-allow-civilian-defense`

- Kind: `strategic-number`
- Detail: SN 225 - Defense

Set to 0 to disable civilian defense except against gaia (wolves, etc.), 1 to defend against weak, non-ranged units (like AoC), 2 for all weak units except warships and units faster than villagers, and 3 for all weak units except warships. For reference, villager speed: default: 0.8, wheelbarrow: 0.88, hand-cart: 0.97. For archer-line and skirmisher-line, speed: 0.96. With sn-allow-civilian-offense set to 1, the "weak units" check is eliminated, allowing for a more aggressive response. Despite the speed advantage, even with only wheelbarrow, early ranged units are swiftly eliminated by villagers with minimal losses and luring.

Default: `1`

Required range: `0 to 3`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-allow-civilian-defense)

<a id="symbol-sn-allow-civilian-offense"></a>

## `sn-allow-civilian-offense`

- Kind: `strategic-number`
- Detail: SN 258 - Attack

Set to 1 to allow villagers to participate as soldiers in town-size attacks. If set to 2, villagers will target enemy villagers and buildings even if defensive military units are available. If set to 0, villagers will only be sent to attack enemy forward towers, without murder holes. When set to 1 or 2, this strategic number also disables the "weak units" check of sn-allow-civilian-defense.

Default: `0`

Required range: `0 to 2`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-allow-civilian-offense)

<a id="symbol-sn-allow-gathering-sea-fish-with-villagers"></a>

## `sn-allow-gathering-sea-fish-with-villagers`

- Kind: `strategic-number`
- Detail: SN 308 - Economy

Set to 1 to allow villagers to gather deep sea fish in addition to shore fish.

Default: `0`

Required range: `0 to 1`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-allow-gathering-sea-fish-with-villagers)

<a id="symbol-sn-allow-serjeant-building"></a>

## `sn-allow-serjeant-building`

- Kind: `strategic-number`
- Detail: SN 307 - Buildings

Set to 1 to automatically assign Serjeants to a Donjon foundation instead of villagers if available. If there are no available Serjeants a Villager is chosen instead.

Default: `0`

Required range: `0 to 1`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-allow-serjeant-building)

<a id="symbol-sn-attack-group-gather-spacing"></a>

## `sn-attack-group-gather-spacing`

- Kind: `strategic-number`
- Detail: SN 41 - Attack

Controls the relative proximity (to the group gather point) that grouped units must be in before the group is considered gathered.

Default: `4`

Required range: `1 to 255`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-attack-group-gather-spacing)

<a id="symbol-sn-attack-group-size-randomness"></a>

## `sn-attack-group-size-randomness`

- Kind: `strategic-number`
- Detail: SN 98 - Attack

The randomness factor in the attack group size. This sets a cap on the amount of randomness in the minimum attack group size. The randomness factor is set once (when the group is created) and will be between 0 and this number.

Default: `1`

Required range: `0 to Max`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-attack-group-size-randomness)

<a id="symbol-sn-attack-intelligence"></a>

## `sn-attack-intelligence`

- Kind: `strategic-number`
- Detail: SN 103 - Attack

Specifies whether the intelligent attack system is used. The intelligent attack system tries to avoid enemy units when attacking and tries to attack from different sides. When used with the archived-non-de-strategic-number set to 2, this can create multifront attacks. Must be 0 (to turn off) and 1 (to turn on).

Default: `0`

Required range: `0 to 1`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-attack-intelligence)

<a id="symbol-sn-attack-winning-player"></a>

## `sn-attack-winning-player`

- Kind: `strategic-number`
- Detail: SN 188 - Attack

Controls whether or not the computer player will attack the winning player (if there is more than one to choose from).

Default: `1`

Required range: `0 to 1`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-attack-winning-player)

<a id="symbol-sn-attack-winning-player-factor"></a>

## `sn-attack-winning-player-factor`

- Kind: `strategic-number`
- Detail: SN 195 - Attack

The influence the sn-attack-winning-player will have on deciding who to attack if it's set to 1.

Default: `25`

Required range: `Min to Max`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-attack-winning-player-factor)

<a id="symbol-sn-blot-exploration-map"></a>

## `sn-blot-exploration-map`

- Kind: `strategic-number`
- Detail: SN 135 - Exploring

This controls whether or not the computer player re-explores previously explored regions. A value of 1 has the computer player re-explore, a value of 0 does not.

Default: `1`

Required range: `0 to 1`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-blot-exploration-map)

<a id="symbol-sn-blot-size"></a>

## `sn-blot-size`

- Kind: `strategic-number`
- Detail: SN 136 - Exploring

This controls the size of the area that a computer player marks for re-exploration.

Default: `15`

Required range: `1 to 255`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-blot-size)

<a id="symbol-sn-boar-lure-destination"></a>

## `sn-boar-lure-destination`

- Kind: `strategic-number`
- Detail: SN 295 - Economy

Set to a value from this image to adjust the boar lure destination at the town center. Add 12 to the normal value (0 to 11) to shift the point down to the grid corner. If set to 0, lurers will attempt to reach the center tile of the town center.

Default: `0`

Required range: `0 to 23`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-boar-lure-destination)

<a id="symbol-sn-building-targeting-mode"></a>

## `sn-building-targeting-mode`

- Kind: `strategic-number`
- Detail: SN 255 - Attack

Set to 0 to target all buildings, 1 to ignore walls and gates, or 2 to ignore walls, gates, and dropsites. Please avoid this strategic number, as you may experience targeting failures under certain circumstances.

Default: `0`

Required range: `0 to 2`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-building-targeting-mode)

<a id="symbol-sn-camp-max-distance"></a>

## `sn-camp-max-distance`

- Kind: `strategic-number`
- Detail: SN 86 - Buildings

Sets the maximum distance that lumber camps and mining camps may be placed from a Town Center.

Default: `25`

Required range: `7 to 255`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-camp-max-distance)

<a id="symbol-sn-cap-civilian-builders"></a>

## `sn-cap-civilian-builders`

- Kind: `strategic-number`
- Detail: SN 4 - Buildings

Caps the number of builders allocated. Factored in after the percentage is calculated. Some previous documentation says this strategic number is ignored when set to -1, but using -1 has the same effect as setting the SN to 0. This is an SN that you should change from its default value. Set it high, like 200, but really any reasonably high number is fine. The default is 2, but there is no real reason to cap the number of builders your AI can use at once. The AI will only assign builders as necessary, so setting this SN to a huge number like 200 won't tell your AI to send all of its villagers to construct buildings. Instead, the AI will automatically assign one builder at minimum to every building foundation unless you place the building with up-build-line and you set up-assign-builders to -1 for that building beforehand (setting up-assign-builders to 0 still assigns one builder). Then, it will assign builders to that building type until the number for up-assign-builders is reached for that whole building type or sn-cap-civilian-builders is reached. For example, if you use (up-assign-builders c: farm c: 4) and you order two farms to be built, the AI will distribute four builders total to build those two farms, usually two to each farm. By default up-assign-builders is set to 1 for each building type. sn-percent-civilian-builders won't affect how many builders are assigned, so you can ignore sn-percent-civilian-builders.

Default: `2`

Required range: `-1 to Max`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-cap-civilian-builders)

<a id="symbol-sn-cap-civilian-explorers"></a>

## `sn-cap-civilian-explorers`

- Kind: `strategic-number`
- Detail: SN 3 - Exploring

Caps the number of civilian explorers allocated. Ignored when set to -1. The default of this SN is 2, which means that 2 villagers will start exploring by default, and this setting should almost always be changed to 0 unless the AI is playing a nomad map. This SN does not affect fishing ships, and sn-number-boat-explore-groups should be used instead for fishing ships. The AI will calculate the number of villagers to task to explore based on sn-percent-civilian-explorers, sn-cap-civilian-explorers, and sn-total-number-explorers, ultimately using whichever SN results in the smallest number of explorers. If at least sn-percent-half-exploration percent of the map is explored, this number is cut in half, so it's best to set sn-percent-half-exploration to 100 to have full control over the number of exploring villagers. The AI will try assign as many villagers as possible to reach the desired number of explorers, but villagers currently tasked to build, repair, explore, or gather (except non-luring hunters and miners) are not available to be tasked to explore. Instead, villagers assigned to these tasks must have their current task cancelled first, such as with up-retask-gatherers or garrisoning the villagers, or the AI will wait until their current task is finished before tasking the villager to explore, such as a lumberjack finishing the current tree. To stop villagers from exploring, set sn-percent-civilian-explorers, sn-cap-civilian-explorers, or sn-total-number-explorers to 0, and use up-reset-scouts. All land explorers will explore around the AI's town when the game time is less than sn-home-exploration-time. After the game time exceeds the value of sn-home-exploration-time, explorers will start exploring locations further away. It's usually simplest to use just one of sn-percent-civilian-explorers, sn-cap-civilian-explorers, and sn-total-number-explorers to cap villager exploration. Often, sn-cap-civilian-explorers is the easiest to use, and you can just set sn-percent-civilian-explorers to 100 and sn-total-number-explorers to a high number like 10, and then not worry about having to change them later. However, if you don't have a specific desired number of villager explorers that you want, and you just want to set a certain % of them to explore, you can set sn-cap-civilian-explorers to -1 and just use sn-percent-civilian-explorers instead. The settings of sn-percent-civilian-builders and sn-percent-civilian-gatherers do not affect the number of villagers that can be tasked to explore. Also, sn-minimum-civilian-explorers and archived-non-de-strategic-number don't appear to affect the number of villager explorers, so you can ignore these SNs.

Default: `2`

Required range: `-1 to Max`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-cap-civilian-explorers)

<a id="symbol-sn-cap-civilian-gatherers"></a>

## `sn-cap-civilian-gatherers`

- Kind: `strategic-number`
- Detail: SN 5 - Economy

Caps the number of gatherers allocated. Factored in after the percentage is calculated. Ignored when set to -1, meaning there is no cap on the number of gatherers. Unless this SN caps gatherers, all villagers who aren't exploring or building will start gathering resources so that they aren't idle. In virtually all cases this is what you want, so there usually isn't any reason to change this SN from the default -1 setting. sn-percent-civilian-gatherers does not affect the number of gatherers, so you can rely on this SN alone to determine the number of gatherers that your AI has.

Default: `-1`

Required range: `-1 to Max`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-cap-civilian-gatherers)

<a id="symbol-sn-consecutive-idle-unit-limit"></a>

## `sn-consecutive-idle-unit-limit`

- Kind: `strategic-number`
- Detail: SN 76 - Attack

Sets the number of consecutive seconds that pass before a group is set to idle if all of its units are idle. The original documentation says this is only used during attack and retreat phases, but it applies to scouting units as well. This SN should be changed from its default value, which is 15. If you leave the SN unchanged and an exploring unit is given a non-exploring task, such as claiming sheep with DUC, it will wait 15 seconds before going back to exploring once it finished its non-exploring task. To remove this delay, you'll want this SN to be 0. There is likely no downside to setting this to 0.

Default: `15`

Required range: `0 to Max`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-consecutive-idle-unit-limit)

<a id="symbol-sn-coop-share-attacking"></a>

## `sn-coop-share-attacking`

- Kind: `strategic-number`
- Detail: SN 196 - Attack

Controls whether allied computer players can attack to defend each other. If set to 1, it appears to run computations any time a unit takes damage, and if it's an ally unit it will increase the likelihood that attack groups will come help the ally whenever sn-number-attack-groups is set > 0. It should have no effect on attack-now, TSA, or any other attack methods. If you don't use attack groups, or you use sn-target-player-number to select the enemy player to attack, it's best to set this SN to 0 to improve game performance.

Default: `1`

Required range: `0 to 1`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-coop-share-attacking)

<a id="symbol-sn-coop-share-attacking-interval"></a>

## `sn-coop-share-attacking-interval`

- Kind: `strategic-number`
- Detail: SN 197 - Attack

Controls how often this computer player can ask another for help (in seconds).

Default: `120`

Required range: `0 to Max`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-coop-share-attacking-interval)

<a id="symbol-sn-coop-share-information"></a>

## `sn-coop-share-information`

- Kind: `strategic-number`
- Detail: SN 194 - Diplomacy

Controls whether or not allied computer players share information about what they uncover (this is not like Cartography; instead, it's analogous to two humans chatting).

Default: `1`

Required range: `0 to 1`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-coop-share-information)

<a id="symbol-sn-defer-dropsite-update"></a>

## `sn-defer-dropsite-update`

- Kind: `strategic-number`
- Detail: SN 273 - Economy

Set to 1 to defer the dropsite-min-distance update until construction is complete. If set to 0, the dropsite update occurs when the building is placed on the map.

Default: `0`

Required range: `0 to 1`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-defer-dropsite-update)

<a id="symbol-sn-disable-attack-groups"></a>

## `sn-disable-attack-groups`

- Kind: `strategic-number`
- Detail: SN 271 - Attack

Set to 1 to disable automatic attack group targeting. Once groups are created, they can be used for defensive attack purposes using TSA. If set to 0, attack groups will perform offensive targeting as usual.

Default: `0`

Required range: `0 to 1`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-disable-attack-groups)

<a id="symbol-sn-disable-builder-assistance"></a>

## `sn-disable-builder-assistance`

- Kind: `strategic-number`
- Detail: SN 285 - Buildings

Set to 1 to prevent builders from assisting on nearby foundations after their work is complete. If set to 0, they will assist as usual.

Default: `0`

Required range: `0 to 1`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-disable-builder-assistance)

<a id="symbol-sn-disable-defend-groups"></a>

## `sn-disable-defend-groups`

- Kind: `strategic-number`
- Detail: SN 277 - Defense

Append flags to disable various defense systems: 1 to disable the defensive (TSA) targeting system, 2 to disable assistance inside sn-safe-town-size, 4 to disable assistance between sn-safe-town-size and sn-maximum-town-size, 8 to disable assistance outside sn-maximum-town-size. When assistance is disabled, please be aware that your units will only respond to attackers within their individual line of sight. If set to 0, units will respond to threats in town as usual.

Default: `0`

Required range: `0 to 15`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-disable-defend-groups)

<a id="symbol-sn-disable-sighted-response-cap"></a>

## `sn-disable-sighted-response-cap`

- Kind: `strategic-number`
- Detail: SN 284 - Attack

Set to 1 to eliminate the cap of 50 on sn-enemy-sighted-response-distance. If set to 0, the cap will remain in effect for changes to sn-enemy-sighted-response-distance.

Default: `0`

Required range: `0 to 1`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-disable-sighted-response-cap)

<a id="symbol-sn-disable-tower-priority"></a>

## `sn-disable-tower-priority`

- Kind: `strategic-number`
- Detail: SN 267 - Attack

Set to 1 to prevent the local targeting system from giving special priority to towers and other fortifications, including town centers and castles. If set to 0, these buildings will receive the usual special priority. In combination with sn-ignore-attack-group-under-attack:1, you can better avoid being lured by town centers during early attacks, though using retreat or DUC commands to avoid town centers will be more effective overall. Note: this sn requires a packet to be sent for each change in a multiplayer game, so please consider this when using it.

Default: `0`

Required range: `0 to 1`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-disable-tower-priority)

<a id="symbol-sn-disable-trade-evasion"></a>

## `sn-disable-trade-evasion`

- Kind: `strategic-number`
- Detail: SN 294 - Defense

Set to 1 to prevent trade carts from abandoning their gold and trade route in order to evade attackers. If set to 0, trade carts will attempt to evade attackers as usual.

Default: `0`

Required range: `0 to 1`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-disable-trade-evasion)

<a id="symbol-sn-disable-villager-garrison"></a>

## `sn-disable-villager-garrison`

- Kind: `strategic-number`
- Detail: SN 291 - Defense

Set to 3 to prevent villagers from auto-garrisoning for any reason. If set to 2, gaia is ignored and villagers will only garrison for enemy attacks if they can enter a town center. If set to 1, gaia is ignored and villagers will garrison for any enemy attacks. If set to 0, villagers will garrison as usual.

Default: `0`

Required range: `0 to 3`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-disable-villager-garrison)

<a id="symbol-sn-do-not-scale-for-difficulty-level"></a>

## `sn-do-not-scale-for-difficulty-level`

- Kind: `strategic-number`
- Detail: SN 229 - Other

Disables the automatic difficulty-scaling. It is recommended to set this to 1 and do any difficulty adjustments manually. This needs to be issued BEFORE such SN's are altered or you'll see the values change by a set percentage. The default of 0 allows these SNs to be automatically changed when set using (set-strategic-number). There are differences between Scenarios and Non-Scenarios (thanks to scripter64 for testing this).Non-Scenario GameHard and Hardest:No changeModerate: multiplied by 0.75:archived-non-de-strategic-numberboatsEasy: multiplied by 0.5:same list as moderateEasiest: multiplied by 0.25:same list as moderateScenario GameHardest:No changeHard: multiplied by 0.8:archived-non-de-strategic-numberdistanceModerate: multiplied by 0.6:archived-non-de-strategic-numberdistanceEasy: multiplied by 0.4:same list as moderateEasiest: multiplied by 0.2:same list as moderate

Default: `0`

Required range: `0 to 1`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-do-not-scale-for-difficulty-level)

<a id="symbol-sn-do-not-transport-from-same-zone"></a>

## `sn-do-not-transport-from-same-zone`

- Kind: `strategic-number`
- Detail: SN 241 - Water

The UP reference says that you can set this to 1 to influence transport ship behavior. However, most other sources of documentation leave this SN undocumented, so this SN may not have an effect. This SN was added in the Conquerors expansion, so it is not available in the original Age of Kings version.

Default: `0`

Required range: `0 to 1`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-do-not-transport-from-same-zone)

<a id="symbol-sn-dock-avoidance-factor"></a>

## `sn-dock-avoidance-factor`

- Kind: `strategic-number`
- Detail: SN 280 - Water

Set to the avoidance factor for docks in the same zone (body of water). Positive values avoid placement in the same zone, while negative values prefer it.

Default: `1000`

Required range: `-10000 to 10000`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-dock-avoidance-factor)

<a id="symbol-sn-dock-placement-mode"></a>

## `sn-dock-placement-mode`

- Kind: `strategic-number`
- Detail: SN 278 - Water

Set to 1 to prefer placement toward the front, -1 to prefer placement toward the back, or 0 for standard placement. Placement toward the front or back means closer to the map center or further away from the map center, relative to the home town center. Higher positive values like 2 or 3 can theoretically set an even higher priority toward placing the dock near the map center. Note: it is important to explore the area you want the AI to build the dock. Otherwise, it will only build the dock on shoreline you have explored.

Default: `0`

Required range: `-1 to 1`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-dock-placement-mode)

<a id="symbol-sn-dock-proximity-factor"></a>

## `sn-dock-proximity-factor`

- Kind: `strategic-number`
- Detail: SN 279 - Water

Set to the proximity factor for docks to be placed relative to one another. Positive values prefer more distance, while negative values prefer less distance.

Default: `10000`

Required range: `-10000 to 10000`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-dock-proximity-factor)

<a id="symbol-sn-dock-training-filter"></a>

## `sn-dock-training-filter`

- Kind: `strategic-number`
- Detail: SN 281 - Water

Set to 1 or 2 to enable the intelligent dock training filter. This will prevent docks from training ships that would likely be useless in their body of water. If set to 1, docks will continue to train in seas that no longer contain recently sighted targets, while 2 will block training. If set to 0, docks will train units without additional consideration. When sn-dock-training-filter is not 0, fishing ships will only be trained from docks that are able to reach, and are closest to, deep sea fish. This means that if you have 4 docks in an ocean with deep sea fish, side by side, the two outside docks are likely to be set aside to train fishing ships, while the center docks will be free to create warships without interruption. If you aren't training fishing ships, the two outside docks will also be able to train warships, of course. Additionally, when sn-dock-training-filter is not 0, trade cogs may be rejected by the dock if it hasn't found an allied dock in the same sea that could be reached from it. On the other hand, a military ship uses enemy ships/docks to determine if it is acceptable when that sn is in use. Here is some sample code from scripter64 to set sn-dock-training-filter to the best possible state: (defrule (true) => (set-strategic-number sn-dock-training-filter 0) (set-goal gl-dock-attack-training 0) ) (defrule (up-train-site-ready c: galley) => (chat-to-all "A dock is available to train warships.") (set-strategic-number sn-dock-training-filter 2) (set-goal gl-dock-attack-training 1) ) (defrule (goal gl-dock-attack-training 1) (not(up-train-site-ready c: galley)) => (chat-to-all "A dock is not available to train warships with recent sighting data.") (set-strategic-number sn-dock-training-filter 1) ) (defrule (goal gl-dock-attack-training 1) (not(up-train-site-ready c: galley)) => (chat-to-all "A dock is not available to train warships with any sighting data.") (set-strategic-number sn-dock-training-filter 0) ) ;sn-dock-training-filter is now set to the best possible state

Default: `0`

Required range: `0 to 2`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-dock-training-filter)

<a id="symbol-sn-dropsite-separation-distance"></a>

## `sn-dropsite-separation-distance`

- Kind: `strategic-number`
- Detail: SN 248 - Buildings

Set to suggest the minimum distance between dropsites. From scripter64: "I've found the best value, in general, to be around 3 or 4, which allows mills, mining camps, and lumber camps to be built near each other, but not too near. Setting it to higher values can be useful if you'd like to build an escape camp for when your gatherers are under attack."

Default: `10`

Required range: `1 to 255`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-dropsite-separation-distance)

<a id="symbol-sn-easier-reaction-percentage"></a>

## `sn-easier-reaction-percentage`

- Kind: `strategic-number`
- Detail: SN 219 - Defense

Sets the effective reaction percentage (of normal LOS) a computer player unit will use in single-player easier scenario or campaign games.

Default: `100`

Required range: `0 to 100`

Range: `100 to 100`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-easier-reaction-percentage)

<a id="symbol-sn-easiest-reaction-percentage"></a>

## `sn-easiest-reaction-percentage`

- Kind: `strategic-number`
- Detail: SN 218 - Defense

Sets the effective reaction percentage (of normal LOS) a computer player unit will use in single-player Easiest level scenario or campaign games.

Default: `100`

Required range: `0 to 100`

Range: `100 to 100`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-easiest-reaction-percentage)

<a id="symbol-sn-enable-boar-hunting"></a>

## `sn-enable-boar-hunting`

- Kind: `strategic-number`
- Detail: SN 244 - Economy

Set to 1 to target deer and boar; if it's set to 2, deer will be ignored. Keep sn-enable-boar-hunting at the default setting of 0 to target deer and ignore boar. To ignore both deer and boar, set sn-minimum-number-hunters to 0, and set sn-maximum-hunt-drop-distance to -2. This SN's default value is 0, which is usually not the value you want. Make sure to change the setting of this SN if you want your AI to hunt boar. The recommended setting is 1 when you are just starting to script so that your AI doesn't ignore free and valuable food resources. Hunting is one of the fastest sources of food. See this page for examples on how different SN hunting values affects your hunting.

Default: `0`

Required range: `0 to 2`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-enable-boar-hunting)

<a id="symbol-sn-enable-full-vision"></a>

## `sn-enable-full-vision`

- Kind: `strategic-number`
- Detail: SN 315 - Exploring

Unknown. This SN is undocumented. It doesn't appear to affect player count commands, DUC searches, or point commands.

Default: `-1`

Required range: `Min to Max`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-enable-full-vision)

<a id="symbol-sn-enable-new-building-system"></a>

## `sn-enable-new-building-system`

- Kind: `strategic-number`
- Detail: SN 242 - Buildings

Set to 1 only once to request the new building system, featuring simultaneous construction and cancellation control. If you want to enable new building system, you should do it either first thing in the script, or at any time that you have zero builders and zero pending buildings.

Default: `0`

Required range: `0 to 1`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-enable-new-building-system)

<a id="symbol-sn-enable-offensive-priority"></a>

## `sn-enable-offensive-priority`

- Kind: `strategic-number`
- Detail: SN 254 - Attack

Set to 1 to enable attack-now and attack groups to target using the priorities set by up-set-offense-priority. This SN is turned off by default, so the SN should be changed to 1. Using up-set-offense-priority allows you to control which buildings and units have lower and higher priority when the AI is selecting an attack target. If you don't set sn-enable-offensive-priority to 1, up-set-offense-priority will have no effect. up-set-defense-priority does not have a corresponding strategic number that you need to set to 1 for the command to work, just up-set-offense-priority.

Default: `0`

Required range: `0 to 1`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-enable-offensive-priority)

<a id="symbol-sn-enable-patrol-attack"></a>

## `sn-enable-patrol-attack`

- Kind: `strategic-number`
- Detail: SN 247 - Attack

Set to 1 to enable the patrol-style local targeting system. When attacking a distant target, this causes units to retarget against nearby sighted units immediately instead of waiting until they are in proximity to the original target. Note: this SN does not work on units that are information, so it will not work on grouped soldiers attacking with attack-now or sn-number-attack-groups. It doesn't cause your AI to put soldiers into formation and patrol a formed group toward the enemy, as the name might suggest. Instead ungrouped units sent to attack will patrol toward their target. If you use one-soldier attack groups or TSA, you'll almost always want to set this SN to 1. There may be cases where you may want to keep this SN at zero, such as if your AI is trying to raid or if the enemy has a forward tower that you want to ignore, so that your soldiers will march all the way to their attack target without getting sidetracked.

Default: `0`

Required range: `0 to 1`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-enable-patrol-attack)

<a id="symbol-sn-enable-research-queue"></a>

## `sn-enable-research-queue`

- Kind: `strategic-number`
- Detail: SN 306 - Economy

Controls whether AI players can (or cannot) queue technologies along with units when sn-enable-training-queue is enabled. Set to 1 to enable queued technologies.

Default: `0`

Required range: `0 to 1`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-enable-research-queue)

<a id="symbol-sn-enable-training-queue"></a>

## `sn-enable-training-queue`

- Kind: `strategic-number`
- Detail: SN 264 - Economy

Set to values > 0 to allow an additional unit(s) to be queued at each building. For example, if set to 3, then 3 units can be queued to be trained after the currently training unit. If set to 0, buildings will train one unit at a time. By default, technologies can't be queued. To enable queued technologies in DE, set sn-enable-research-queue to 1, and technologies will use sn-enable-training-queue as well.

Default: `0`

Required range: `0 to 15`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-enable-training-queue)

<a id="symbol-sn-enemy-sighted-response-distance"></a>

## `sn-enemy-sighted-response-distance`

- Kind: `strategic-number`
- Detail: SN 20 - Attack

Sets the distance inside of which units will be candidates for response to an enemy attack. The maximum distance is 50 tiles, unless sn-disable-sighted-response-cap is set to 1. Once an enemy attack is detected, sn-percent-enemy-sighted-response sets the percentage of the AI's military units within sn-enemy-sighted-response-distance from the attack who will respond to the attack. They will respond by targeting the enemy unit that initiated the attack. This response only applies to an AI's units that are attacked outside of either sn-maximum-town-size or sn-safe-town-size. Otherwise, the town defense system takes over. See sn-disable-defend-groups for details on the town defense system.

Default: `25`

Required range: `0 to 50`

Range: `Min to 50`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-enemy-sighted-response-distance)

<a id="symbol-sn-filter-under-attack"></a>

## `sn-filter-under-attack`

- Kind: `strategic-number`
- Detail: SN 276 - Attack

Set to 1 or 2 to filter retreat commands to only those units that are under attack. When this is 2, units near threatened units (within 6 tiles) will also be retreated, not just units that are under attack, which may be computationally expensive. The nearby units that will be retreated do not consider the filter type provided to up-retreat-to, and will be all military units except monks. The 1 and 2 states will also reject high base pierce armor units >= 20, so rams are left despite being attacked. If set to 0, the filter is disabled.

Default: `0`

Required range: `0 to 2`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-filter-under-attack)

<a id="symbol-sn-fishing-boat-whaling-percentage"></a>

## `sn-fishing-boat-whaling-percentage`

- Kind: `strategic-number`
- Detail: SN 316 - Water

The percentage of fishing ships which will gather from whales. All other ships will gather from food fish.

Default: `-1`

Required range: `0 to 100`

Range: `0 to 100`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-fishing-boat-whaling-percentage)

<a id="symbol-sn-focus-player-number"></a>

## `sn-focus-player-number`

- Kind: `strategic-number`
- Detail: SN 251 - Attack

Set to any player number in order to use the &quot;focus-player&quot; identifier in facts and actions.

Default: `0`

Required range: `0 to 8`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-focus-player-number)

<a id="symbol-sn-food-dropsite-distance"></a>

## `sn-food-dropsite-distance`

- Kind: `strategic-number`
- Detail: SN 163 - Economy

The maximum number of tiles a computer player likes to walk to drop off its food.

Default: `3`

Required range: `3 to 255`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-food-dropsite-distance)

<a id="symbol-sn-food-gatherer-percentage"></a>

## `sn-food-gatherer-percentage`

- Kind: `strategic-number`
- Detail: SN 117 - Economy

Set to configure food gatherers: foodGatherers = ( this + sn-food-modifier-percentage ) * gathererTotal * 0.01 + 0.5.

Default: `0`

Required range: `0 to 100`

Range: `0 to 100`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-food-gatherer-percentage)

<a id="symbol-sn-food-modifier-percentage"></a>

## `sn-food-modifier-percentage`

- Kind: `strategic-number`
- Detail: SN 156 - Economy

Set to configure food gatherers: foodGatherers = ( sn-food-gatherer-percentage + this ) * gathererTotal * 0.01 + 0.5.

Default: `0`

Required range: `-100 to 100`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-food-modifier-percentage)

<a id="symbol-sn-free-siege-targeting"></a>

## `sn-free-siege-targeting`

- Kind: `strategic-number`
- Detail: SN 282 - Attack

Add bit flags together to generate a value: 1 = trebuchet; 2 = cannon-galleon. Set a flag for a unit to enable free offensive targeting with attack-now or attack groups. This may result in the targeting of units other than buildings. If set to 0, non-buildings will be ignored unless units must respond due to sn-enemy-sighted-response-distance.

Default: `0`

Required range: `0 to 3`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-free-siege-targeting)

<a id="symbol-sn-garrison-rams"></a>

## `sn-garrison-rams`

- Kind: `strategic-number`
- Detail: SN 240 - Attack

Set to 0 to turn off. When on, the CP AI tries (but doesn't always succeed) to put infantry units into rams before the attack group departs. This SN was added in the Conquerors expansion, so it is not available in the original Age of Kings version.

Default: `1`

Required range: `0 to 1`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-garrison-rams)

<a id="symbol-sn-gate-type-for-wall"></a>

## `sn-gate-type-for-wall`

- Kind: `strategic-number`
- Detail: SN 304 - Defense

0 for stone gates, 1 for palisade gates when using the build-gate/can-build-gate command.

Default: `0`

Required range: `0 to 1`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-gate-type-for-wall)

<a id="symbol-sn-gather-defense-units"></a>

## `sn-gather-defense-units`

- Kind: `strategic-number`
- Detail: SN 232 - Defense

Set to 1 to send units to gather untasked defense units more or less around the town center if sn-gather-idle-soldiers-at-center isn't also set to 1. The original documentation says you can set this to 1 to send units to defend buildings under construction, so there might be times where this also works.

Default: `0`

Required range: `0 to 1`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-gather-defense-units)

<a id="symbol-sn-gather-idle-soldiers-at-center"></a>

## `sn-gather-idle-soldiers-at-center`

- Kind: `strategic-number`
- Detail: SN 239 - Defense

When set to 1, it will &quot;move&quot; the town defense gather point to the &quot;center&quot; (randomized +-6 tiles) of the map. No provision is made if the center is in an unreachable spot. When it's set, all idle and retreating units will try to go to the center. Useful for King of the Hill and similar variants to get the CP to group near the middle. This SN was added in the Conquerors expansion, so it is not available in the original Age of Kings version.

Default: `-1`

Required range: `0 to 1`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-gather-idle-soldiers-at-center)

<a id="symbol-sn-gather-idle-soldiers-at-spawn-point"></a>

## `sn-gather-idle-soldiers-at-spawn-point`

- Kind: `strategic-number`
- Detail: SN 318 - Defense

Controls whether military units will walk back to the building they were trained out of after they are idle for a certain period of time. Mainly intended for campaign designers.

Default: `-1`

Required range: `0 to 1`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-gather-idle-soldiers-at-spawn-point)

<a id="symbol-sn-gold-dropsite-distance"></a>

## `sn-gold-dropsite-distance`

- Kind: `strategic-number`
- Detail: SN 166 - Economy

The maximum number of tiles a computer player likes to walk to drop off its gold.

Default: `3`

Required range: `3 to 255`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-gold-dropsite-distance)

<a id="symbol-sn-gold-gatherer-percentage"></a>

## `sn-gold-gatherer-percentage`

- Kind: `strategic-number`
- Detail: SN 118 - Economy

Set to configure gold gatherers: goldGatherers = ( this + sn-gold-modifier-percentage ) * gathererTotal * 0.01 + 0.5.

Default: `0`

Required range: `0 to 100`

Range: `0 to 100`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-gold-gatherer-percentage)

<a id="symbol-sn-gold-modifier-percentage"></a>

## `sn-gold-modifier-percentage`

- Kind: `strategic-number`
- Detail: SN 159 - Economy

Set to configure gold gatherers: goldGatherers = ( sn-gold-gatherer-percentage + this ) * gathererTotal * 0.01 + 0.5.

Default: `0`

Required range: `-100 to 100`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-gold-modifier-percentage)

<a id="symbol-sn-group-commander-selection-method"></a>

## `sn-group-commander-selection-method`

- Kind: `strategic-number`
- Detail: SN 75 - Attack

Sets the method by which group commanders are selected. 0 selects the unit with the most hit points. 1 selects the unit with the fewest hit points. 2 selects the unit with the most range. The commander is set once during a group's creation and is only reset when the commander dies.

Default: `3`

Required range: `0 to 3`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-group-commander-selection-method)

<a id="symbol-sn-group-form-distance"></a>

## `sn-group-form-distance`

- Kind: `strategic-number`
- Detail: SN 230 - Attack

Sets the distance over which attack soldiers will group. Set this value high if buildings that train military units are far apart.

Default: `20`

Required range: `0 to 30`

Range: `Min to 30`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-group-form-distance)

<a id="symbol-sn-group-leader-defense-distance"></a>

## `sn-group-leader-defense-distance`

- Kind: `strategic-number`
- Detail: SN 131 - Attack

Sets the defense distance for defenders of an important attack group leader.

Default: `3`

Required range: `1 to 255`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-group-leader-defense-distance)

<a id="symbol-sn-home-exploration-time"></a>

## `sn-home-exploration-time`

- Kind: `strategic-number`
- Detail: SN 256 - Exploring

Set to the maximum amount of time, in seconds, that should be dedicated to exploring the home town center region.

Default: `300`

Required range: `0 to Max`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-home-exploration-time)

<a id="symbol-sn-ignore-attack-group-under-attack"></a>

## `sn-ignore-attack-group-under-attack`

- Kind: `strategic-number`
- Detail: SN 231 - Attack

Set to 1 to specify that defensive units should ignore attack-now attack groups under attack. If set to 0, it will cause the attack-now attack group to respond to being attacked. Unfortunately the response for an AI is limited to 1 unit from the group responding at a time until it is killed, then the next unit in the group will peel off and respond to the attack.

Default: `0`

Required range: `0 to 1`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-ignore-attack-group-under-attack)

<a id="symbol-sn-ignore-tower-elevation"></a>

## `sn-ignore-tower-elevation`

- Kind: `strategic-number`
- Detail: SN 265 - Defense

Set to 1 to ignore elevation when placing towers. If set to 0, the AI will try to seek elevation advantage.

Default: `0`

Required range: `0 to 1`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-ignore-tower-elevation)

<a id="symbol-sn-initial-attack-delay"></a>

## `sn-initial-attack-delay`

- Kind: `strategic-number`
- Detail: SN 104 - Attack

The forced, initial delay before any computer player attacks (in seconds).

Default: `0`

Required range: `0 to Max`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-initial-attack-delay)

<a id="symbol-sn-initial-attack-delay-type"></a>

## `sn-initial-attack-delay-type`

- Kind: `strategic-number`
- Detail: SN 134 - Attack

The type of initial attack delay. A value of 1 denotes a delay ended by the build list. A value of 2 uses the sn-initial-attack-delay timeout. A value of 3 allows the computer player to attack after he has been attacked by a non-Gaia player. A value of 0 allows any of the three occurrences to enable attacks.

Default: `0`

Required range: `0 to 3`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-initial-attack-delay-type)

<a id="symbol-sn-initial-exploration-required"></a>

## `sn-initial-exploration-required`

- Kind: `strategic-number`
- Detail: SN 167 - Buildings

The percentage of the map that must be explored by a computer player before any building is allowed. Please change this SN in your AI. The default is 2%. On larger maps this can cause your AI to significantly delay the construction of its first houses. Just set this SN to 0 and forget about it. The default value is annoying and causes a lot of hair-pulling until the scripter realizes they didn't change this SN.

Default: `2`

Required range: `0 to 100`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-initial-exploration-required)

<a id="symbol-sn-keystates"></a>

## `sn-keystates`

- Kind: `strategic-number`
- Detail: SN 312 - Other

This allows the AI to input ctrl and shift inputs when issuing commands. Setting to 1 corresponds to shift, setting to 2 corresponds to ctrl and setting to 3 corresponds to both. sn-keystates affects the behavior of up-target-objects and up-target-point, and it affects them at the moment those commands are used, so set this strategic number before using them. sn-keystates can safely be set back to another value immediately after those commands are used. Using the Shift option allows AI scripters to set movement waypoints or queue commands for units, like using Shift in a normal game. Using the Ctrl option allows AI scripters to force units to target an object more directly than normal, making the units less likely to retarget to another object.

Default: `0`

Required range: `0 to 3`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-keystates)

<a id="symbol-sn-livestock-to-town-center"></a>

## `sn-livestock-to-town-center`

- Kind: `strategic-number`
- Detail: SN 263 - Economy

Set to 1 to require livestock, such as sheep, to gather at the town center. If set to 0, they will gather at mills, as well.

Default: `0`

Required range: `0 to 1`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-livestock-to-town-center)

<a id="symbol-sn-local-targeting-mode"></a>

## `sn-local-targeting-mode`

- Kind: `strategic-number`
- Detail: SN 286 - Attack

Set to 1 to prioritize attack bonuses and overall damage per hit. If set to 2, units will prioritize targets with high base pierce armor, such as rams; otherwise, they will target as usual. The offensive priority value of a target (-1 to 11) is added to the weight for modes 1 and 2, as well. If set to 0, units will target as usual. Note that units that do 1hp or less damage per hit (like archers) will intentionally try to avoid wasting shots on high-pierce targets like rams on modes 1 and 2, if a better target is available. Here are the exact weight calculations:SN = 0 (AoC local targeting system): 5 weight is given to the current target, 0-75 weight based on distance (nearest available target is 75, farthest is 0), and 0-10 weight is given to time to eliminate the target based on number of hits and reload time.SN = 1: Weight = the net attack value (i.e. attack+bonuses-armor) * 3 + offensive-priority-value. If the net attack value is SN = 2: Weight is the same as SN = 1, but only if the target has >= 40 base pierce armor; otherwise default local targeting behavior is used (the SN=0 weights).In other words, SN=2 is primarily for defense from things like rams coming for your trebuchets, etc. With SN=1, you might get the best behavior. After all weights are added together, the target with the highest weight is attacked. It's possible that the weights from SN=0 are added to the weights of SN=1 when sn-local-targeting-mode is set to 1, but probably not. The explanations from patch notes are unclear. However, units that don't move have reduced priority compared to units that move, except rams, cannon galleons, petards, and trebuchets have this ordering reversed and prioritize units that don't move first.

Default: `0`

Required range: `0 to 2`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-local-targeting-mode)

<a id="symbol-sn-lumber-camp-max-distance"></a>

## `sn-lumber-camp-max-distance`

- Kind: `strategic-number`
- Detail: SN 260 - Buildings

Sets the maximum-town-size for lumber-camp placement, when non-zero. If set to 0, sn-camp-max-distance will be used instead.

Default: `0`

Required range: `0 to 255`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-lumber-camp-max-distance)

<a id="symbol-sn-max-retask-gather-amount"></a>

## `sn-max-retask-gather-amount`

- Kind: `strategic-number`
- Detail: SN 149 - Economy

The maximum amount that a gatherer can be told to gather before being allowed to be retasked. Some code may override this. This SN effectively caps sn-retask-gather-amount. If sn-retask-gather-amount is higher than archived-non-de-strategic-number amount, sn-max-retask-gather-amount will be used instead.

Default: `40`

Required range: `0 to Max`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-max-retask-gather-amount)

<a id="symbol-sn-maximum-attack-group-size"></a>

## `sn-maximum-attack-group-size`

- Kind: `strategic-number`
- Detail: SN 26 - Attack

Sets the maximum size of land-based attack groups. Must be >= 0 and >= sn-minimum-attack-group-size.

Default: `10`

Required range: `0 to Max`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-maximum-attack-group-size)

<a id="symbol-sn-maximum-boat-attack-group-size"></a>

## `sn-maximum-boat-attack-group-size`

- Kind: `strategic-number`
- Detail: SN 60 - Water

Sets the maximum size of boat attack groups.

Default: `5`

Required range: `0 to Max`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-maximum-boat-attack-group-size)

<a id="symbol-sn-maximum-boat-explore-group-size"></a>

## `sn-maximum-boat-explore-group-size`

- Kind: `strategic-number`
- Detail: SN 63 - Water

Sets the maximum size of boat exploration groups. Setting this SN to 0 disables explore groups. The only value that seems to work is 1 because boat explore groups always have only one unit.

Default: `2`

Required range: `0 to Max`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-maximum-boat-explore-group-size)

<a id="symbol-sn-maximum-explore-group-size"></a>

## `sn-maximum-explore-group-size`

- Kind: `strategic-number`
- Detail: SN 44 - Exploring

Sets the maximum size of land-based soldier exploration groups. Setting this SN to 0 disables explore groups. The only value that seems to work is 1 because explore groups always have only one unit.

Default: `1`

Required range: `0 to 1`

Range: `Min to 1`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-maximum-explore-group-size)

<a id="symbol-sn-maximum-fish-boat-drop-distance"></a>

## `sn-maximum-fish-boat-drop-distance`

- Kind: `strategic-number`
- Detail: SN 236 - Water

The parameters control how far from a dropsite a given resource type can be before the CP ignores it. -1 indicates a &quot;don't care&quot; -- i.e. it can be any distance (as it used to be). If set to 0, all fishing ships will explore the water. -2 disables fish gathering for fishing ships. The default of this SN is -1, meaning the SN is ignored by default. This can allow the AI's fishing ships to go all the across the map to gather fish if the AI ran out of that resource at home. To fix this, set a reasonable maximum distance at the beginning of the game, such as 30, and increase it throughout the game, perhaps per age. You'll probably want to set these SNs back to -1 later on in the game, perhaps in the Imperial Age or after an hour of game time, to prevent your AI from ignoring certain resources.

Default: `-1`

Required range: `-2 to 255`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-maximum-fish-boat-drop-distance)

<a id="symbol-sn-maximum-food-drop-distance"></a>

## `sn-maximum-food-drop-distance`

- Kind: `strategic-number`
- Detail: SN 234 - Economy

The parameters control how far from a dropsite a given resource type can be before the CP ignores it. -1 indicates a &quot;don't care&quot; -- i.e. it can be any distance (as it used to be). -2 disables all food gathering, except for hunting. The default of this SN is -1, meaning the SN is ignored by default. This can allow the AI's villagers to go all the across the map to gather food if the AI ran out of that resource at home. To fix this, set a reasonable maximum distance at the beginning of the game, such as 20, and increase it throughout the game, perhaps per age. You'll probably want to set these SNs back to -1 later on in the game, perhaps in the Imperial Age or after an hour of game time, to prevent your AI from ignoring certain resources.

Default: `-1`

Required range: `-2 to 255`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-maximum-food-drop-distance)

<a id="symbol-sn-maximum-gaia-attack-response"></a>

## `sn-maximum-gaia-attack-response`

- Kind: `strategic-number`
- Detail: SN 100 - Defense

The maximum number of villagers that respond to another civilian getting attacked by a Gaia animal.

Default: `3`

Required range: `0 to Max`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-maximum-gaia-attack-response)

<a id="symbol-sn-maximum-garrison-fill"></a>

## `sn-maximum-garrison-fill`

- Kind: `strategic-number`
- Detail: SN 274 - Defense

Set to the number of units to fill into each garrison target per command. If set to 0, this limit is removed.

Default: `0`

Required range: `0 to 20`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-maximum-garrison-fill)

<a id="symbol-sn-maximum-gold-drop-distance"></a>

## `sn-maximum-gold-drop-distance`

- Kind: `strategic-number`
- Detail: SN 237 - Economy

The parameters control how far from a dropsite a given resource type can be before the CP ignores it. -1 indicates a &quot;don't care&quot; -- i.e. it can be any distance (as it used to be). -2 disables gold gathering. The default of this SN is -1, meaning the SN is ignored by default. This can allow the AI's villagers to go all the across the map to gather gold if the AI ran out of that resource at home. To fix this, set a reasonable maximum distance at the beginning of the game, such as 20, and increase it throughout the game, perhaps per age. You'll probably want to set these SNs back to -1 later on in the game, perhaps in the Imperial Age or after an hour of game time, to prevent your AI from ignoring certain resources.

Default: `-1`

Required range: `-2 to 255`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-maximum-gold-drop-distance)

<a id="symbol-sn-maximum-hunt-drop-distance"></a>

## `sn-maximum-hunt-drop-distance`

- Kind: `strategic-number`
- Detail: SN 235 - Economy

The parameters control how far from a dropsite a given resource type can be before the CP ignores it. -1 indicates a &quot;don't care&quot; -- i.e. it can be any distance (as it used to be). -2 disables hunting gathering. The default of this SN is -1, meaning the SN is ignored by default. This can allow the AI's villagers to go all the across the map to hunt if the AI ran out of that resource at home. To fix this, set a reasonable maximum distance at the beginning of the game, such as 30, and increase it throughout the game, perhaps per age. You'll probably want to set these SNs back to -1 later on in the game, perhaps in the Imperial Age or after an hour of game time, to prevent your AI from ignoring certain resources.

Default: `-1`

Required range: `-2 to 255`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-maximum-hunt-drop-distance)

<a id="symbol-sn-maximum-patrol-distance"></a>

## `sn-maximum-patrol-distance`

- Kind: `strategic-number`
- Detail: SN 302 - Attack

How far a unit likes to travel from the patrol path, if the unit goes outside this distance on the patrol path, it'll return to patrolling. -1 means no maximum distance.

Default: `0`

Required range: `-1 to Max`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-maximum-patrol-distance)

<a id="symbol-sn-maximum-stone-drop-distance"></a>

## `sn-maximum-stone-drop-distance`

- Kind: `strategic-number`
- Detail: SN 238 - Economy

The parameters control how far from a dropsite a given resource type can be before the CP ignores it. -1 indicates a &quot;don't care&quot; -- i.e. it can be any distance (as it used to be). -2 disables stone gathering. The default of this SN is -1, meaning the SN is ignored by default. This can allow the AI's villagers to go all the across the map to gather stone if the AI ran out of that resource at home. To fix this, set a reasonable maximum distance at the beginning of the game, such as 20, and increase it throughout the game, perhaps per age. You'll probably want to set these SNs back to -1 later on in the game, perhaps in the Imperial Age or after an hour of game time, to prevent your AI from ignoring certain resources.

Default: `-1`

Required range: `-2 to 255`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-maximum-stone-drop-distance)

<a id="symbol-sn-maximum-tasked-units"></a>

## `sn-maximum-tasked-units`

- Kind: `strategic-number`
- Detail: SN 290 - Other

Found in the local AoE2DE executable strategic-number string dump, but not documented by AIRef. Community-confirmed id: 290.

[AIRef](docs\extracted\raw\aoe2de\aoe2de-strategic-number-strings.txt)

<a id="symbol-sn-maximum-town-size"></a>

## `sn-maximum-town-size`

- Kind: `strategic-number`
- Detail: SN 74 - Buildings

Sets the maximum size of a computer player town.

Default: `20`

Required range: `0 to 255`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-maximum-town-size)

<a id="symbol-sn-maximum-wood-drop-distance"></a>

## `sn-maximum-wood-drop-distance`

- Kind: `strategic-number`
- Detail: SN 233 - Economy

The parameters control how far from a dropsite a given resource type can be before the CP ignores it. -1 indicates a &quot;don't care&quot; -- i.e. it can be any distance (as it used to be). -2 disables wood gathering. The default of this SN is -1, meaning the SN is ignored by default. This can allow the AI's villagers to go all the across the map to gather wood if the AI ran out of that resource at home. To fix this, set a reasonable maximum distance at the beginning of the game, such as 30, and increase it throughout the game, perhaps per age. You'll probably want to set these SNs back to -1 later on in the game, perhaps in the Imperial Age or after an hour of game time, to prevent your AI from ignoring certain resources.

Default: `-1`

Required range: `-2 to 255`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-maximum-wood-drop-distance)

<a id="symbol-sn-mill-max-distance"></a>

## `sn-mill-max-distance`

- Kind: `strategic-number`
- Detail: SN 87 - Buildings

Sets the maximum distance that mills may be placed from a Town Center.

Default: `100`

Required range: `4 to 255`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-mill-max-distance)

<a id="symbol-sn-minimum-attack-group-size"></a>

## `sn-minimum-attack-group-size`

- Kind: `strategic-number`
- Detail: SN 16 - Attack

Sets the minimum size of land-based attack groups. A group must meet its minimum size as one of the tasking prerequisites. The game can change this itself during the game.

Default: `4`

Required range: `0 to Max`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-minimum-attack-group-size)

<a id="symbol-sn-minimum-boar-hunt-group-size"></a>

## `sn-minimum-boar-hunt-group-size`

- Kind: `strategic-number`
- Detail: SN 204 - Economy

The number of villagers a computer player must collect before allowing boars to be hunted for food.

Default: `5`

Required range: `0 to 8`

Range: `Min to 8`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-minimum-boar-hunt-group-size)

<a id="symbol-sn-minimum-boar-lure-group-size"></a>

## `sn-minimum-boar-lure-group-size`

- Kind: `strategic-number`
- Detail: SN 252 - Economy

Set to the number of villagers that will be sent in the initial boar luring group. The initial luring group size is determined exclusively by sn-minimum-boar-lure-group-size. If this is set excessively high, luring a new boar will be blocked, which is useful to ensure that all new hunters will help with an existing lure only. If sn-minimum-boar-lure-group-size is set to 0, a new boar lure is guaranteed to start if sn-minimum-number-hunters requests at least 1 hunter and sn-enable-boar-hunting is set appropriately. The sn-minimum-boar-hunt-group-size value is used only to determine how many hunters should be active during a lure. Each time a lurer is hit, it will try to request up to sn-minimum-boar-hunt-group-size hunters in total to help with the hunt. If it's set to 7, for example, it will request support hunters until there are 7 total hunters. After it is down, each boar will accept a maximum of 8 gatherers. The 9th will have to seek a new boar, if sn-minimum-boar-lure-group-size permits it.

Default: `0`

Required range: `0 to 8`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-minimum-boar-lure-group-size)

<a id="symbol-sn-minimum-boat-attack-group-size"></a>

## `sn-minimum-boat-attack-group-size`

- Kind: `strategic-number`
- Detail: SN 59 - Water

Sets the minimum size of boat attack groups. A group must meet its minimum size as one of the tasking prerequisites.

Default: `1`

Required range: `0 to Max`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-minimum-boat-attack-group-size)

<a id="symbol-sn-minimum-boat-explore-group-size"></a>

## `sn-minimum-boat-explore-group-size`

- Kind: `strategic-number`
- Detail: SN 62 - Water

Sets the minimum size of boat exploration groups. Setting this SN to 0 disables explore groups. The only value that seems to work is 1 because boat explore groups always have only one unit.

Default: `1`

Required range: `0 to Max`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-minimum-boat-explore-group-size)

<a id="symbol-sn-minimum-civilian-explorers"></a>

## `sn-minimum-civilian-explorers`

- Kind: `strategic-number`
- Detail: SN 35 - Exploring

Sets a minimum number of civilian explorers.

Default: `0`

Required range: `0 to Max`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-minimum-civilian-explorers)

<a id="symbol-sn-minimum-explore-group-size"></a>

## `sn-minimum-explore-group-size`

- Kind: `strategic-number`
- Detail: SN 43 - Exploring

Sets the minimum size of land-based soldier exploration groups. A group must meet its minimum size as one of the tasking prerequisites. Setting this SN to 0 disables explore groups. The only value that seems to work is 1 because explore groups always have only one unit.

Default: `1`

Required range: `0 to 1`

Range: `Min to 1`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-minimum-explore-group-size)

<a id="symbol-sn-minimum-number-hunters"></a>

## `sn-minimum-number-hunters`

- Kind: `strategic-number`
- Detail: SN 245 - Economy

Set to force hunting. For best results when hunting boar, set this in conjunction with sn-minimum-boar-hunt-group-size.

Default: `0`

Required range: `0 to Max`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-minimum-number-hunters)

<a id="symbol-sn-minimum-tasked-units"></a>

## `sn-minimum-tasked-units`

- Kind: `strategic-number`
- Detail: SN 289 - Other

Found in the local AoE2DE executable strategic-number string dump, but not documented by AIRef. Community-confirmed id: 289.

[AIRef](docs\extracted\raw\aoe2de\aoe2de-strategic-number-strings.txt)

<a id="symbol-sn-minimum-town-size"></a>

## `sn-minimum-town-size`

- Kind: `strategic-number`
- Detail: SN 73 - Buildings

Sets the minimum size of a computer player town.

Default: `12`

Required range: `0 to 255`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-minimum-town-size)

<a id="symbol-sn-minimum-water-body-size-for-dock"></a>

## `sn-minimum-water-body-size-for-dock`

- Kind: `strategic-number`
- Detail: SN 112 - Water

The minimum number of tiles (in surface area) that a body of water must be for a Dock to be placed on it.

Default: `300`

Required range: `10 to Max`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-minimum-water-body-size-for-dock)

<a id="symbol-sn-mining-camp-max-distance"></a>

## `sn-mining-camp-max-distance`

- Kind: `strategic-number`
- Detail: SN 261 - Buildings

Sets the maximum-town-size for mining-camp placement, when non-zero. If set to 0, sn-camp-max-distance will be used instead.

Default: `0`

Required range: `0 to 255`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-mining-camp-max-distance)

<a id="symbol-sn-mule-cart-dropsite-placement"></a>

## `sn-mule-cart-dropsite-placement`

- Kind: `strategic-number`
- Detail: SN 310 - Economy

Controls the placement of newly constructed mule carts. Set to "lumber-camp" to prioritize placement by wood or "mining-camp" to prioritize placement by gold or stone.

Default: `0`

Required range: `0 to Max`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-mule-cart-dropsite-placement)

<a id="symbol-sn-number-attack-groups"></a>

## `sn-number-attack-groups`

- Kind: `strategic-number`
- Detail: SN 36 - Attack

Sets the desired number of land-based attack groups. Sn-percent-attack-soldiers generally works better.

Default: `0`

Required range: `0 to Max`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-number-attack-groups)

<a id="symbol-sn-number-boat-attack-groups"></a>

## `sn-number-boat-attack-groups`

- Kind: `strategic-number`
- Detail: SN 58 - Water

Sets the desired number of boat attack groups. Setting archived-non-de-strategic-number usually works better.

Default: `0`

Required range: `0 to Max`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-number-boat-attack-groups)

<a id="symbol-sn-number-boat-explore-groups"></a>

## `sn-number-boat-explore-groups`

- Kind: `strategic-number`
- Detail: SN 61 - Water

Sets the desired number of military boat exploration groups. This is not affected by sn-total-number-explorers.

Default: `0`

Required range: `0 to Max`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-number-boat-explore-groups)

<a id="symbol-sn-number-civilian-militia"></a>

## `sn-number-civilian-militia`

- Kind: `strategic-number`
- Detail: SN 257 - Attack

Set to the maximum number of villagers who may be used to attack the enemy.

Default: `10`

Required range: `0 to 200`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-number-civilian-militia)

<a id="symbol-sn-number-explore-groups"></a>

## `sn-number-explore-groups`

- Kind: `strategic-number`
- Detail: SN 42 - Exploring

Sets the desired number of land-based soldier exploration groups. Each explore group will only have one unit. sn-minimum-explore-group-size and sn-maximum-explore-group-size have no effect. To explore with ships, use sn-number-boat-explore-groups. The number of land-based soldier exploration groups are also affected by sn-total-number-explorers which caps the total number of land-based soldier and villager explorers. The number of villager explorers are calculated first (see sn-cap-civilian-explorers for details). Then, if the number of villager explorers is less than sn-total-number-explorers, the AI will send military units to explore until it reaches the number of sn-number-explore-groups or the total number of land explorers reaches sn-total-number-explorers. If at least sn-percent-half-exploration percent of the map is explored, the amount of this SN is cut in half, so it's best to set sn-percent-half-exploration to 100 to have full control over the number of exploring units. To stop land-based soldier units from exploring, set sn-number-explore-groups or sn-total-number-explorers to 0, and use up-reset-scouts. All land explorers will explore around the AI's town when the game time is less than sn-home-exploration-time. After the game time exceeds the value of sn-home-exploration-time, explorers will start exploring locations further away. It's usually simplest to use just one of sn-number-explore-groups and sn-total-number-explorers to cap military exploration. Often, it's usually simplest to set sn-total-number-explorers to a high number like 10 and just use sn-number-explore-groups.

Default: `0`

Required range: `0 to Max`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-number-explore-groups)

<a id="symbol-sn-number-forward-builders"></a>

## `sn-number-forward-builders`

- Kind: `strategic-number`
- Detail: SN 226 - Attack

The number of villagers a computer player uses to build outside of an enemy town. Forward builders refer specifically to those villagers that must board a Transport to cross over water that cannot otherwise be pathed, either because players are on islands, or because other forms of access have been walled-off. It is not necessary to specify forward builders, unless the villagers need to board a Transport.

Default: `0`

Required range: `0 to Max`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-number-forward-builders)

<a id="symbol-sn-number-garrison-units"></a>

## `sn-number-garrison-units`

- Kind: `strategic-number`
- Detail: SN 275 - Defense

Set to the number of units that will garrison per command. If set to 0, it will default to the maximum of 40.

Default: `0`

Required range: `0 to 40`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-number-garrison-units)

<a id="symbol-sn-number-tasked-units"></a>

## `sn-number-tasked-units`

- Kind: `strategic-number`
- Detail: SN 288 - Other

Set to the number of units to require per group tasked by up-target-objects or up-target-point. The last group sent by a command may not reach the minimum required number. It's possible that no units will be sent to some of the last remote targets. If set to 0, units will be spread in order to ensure balanced group sizes to all remote targets.

Default: `0`

Required range: `0 to 40`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-number-tasked-units)

<a id="symbol-sn-object-repair-level"></a>

## `sn-object-repair-level`

- Kind: `strategic-number`
- Detail: SN 246 - Defense

Add bit flags together to generate a value: 0 = wonder; 1 = castle, monastery; 2 = town-center; 4 = barracks; 8 = archery-range; 16 = stable; 32 = siege-workshop; 64 = dock; 128 = market; 256 = university; 512 = blacksmith; 1024 = lumber-camp, mining-camp, mill; 2048 = house; 4096 = towers; 8192 = walls and gates; 16384 = siege weapons. For scenarios and campaigns, the default is 1 for compatibility. The default is 16387 (wonder, castle, monastery, town-center, siege) for all other game modes. Examples: 0 = wonder only (essentially disabled) 1 = wonder, castle, monastery (the AoC repair level) 3 = wonder, castle, monastery, town-center 20547 = wonder, castle, monastery, town-center, dock, towers, siege weapons (scripter64 uses this in Chameleon) 20547 = 0 + 1 + 2 + 64 + 4096 + 16384

Default: `16387`

Required range: `0 to Max`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-object-repair-level)

<a id="symbol-sn-percent-attack-boats"></a>

## `sn-percent-attack-boats`

- Kind: `strategic-number`
- Detail: SN 228 - Water

Sets the percentage of defense boats that will be sent into battle (modified for difficulty level) the next time attack-now is issued. All newly created boats are defense boats by default, and will remain defense boats until attack-now is issued. Both attack soldiers and attack boats will attack when attack-now is issued. This SN only needs to be set once, but it can be changed as needed.

Default: `75`

Required range: `0 to 100`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-percent-attack-boats)

<a id="symbol-sn-percent-attack-soldiers"></a>

## `sn-percent-attack-soldiers`

- Kind: `strategic-number`
- Detail: SN 227 - Attack

Sets the percentage of defense soldiers that will be sent into battle (modified for difficulty level) the next time attack-now is issued. All newly created soldiers are defense soldiers by default, and will remain defense soldiers until attack-now is issued. For example, if 10 soldiers were defending a town, and sn-percent-attack-soldiers was set to 50, then 5 soldiers will form an attack group and attack. This SN only needs to be set once, but it can be changed as needed. sn-percent-attack-soldiers works best when not using archived-non-de-strategic-number.

Default: `75`

Required range: `0 to 100`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-percent-attack-soldiers)

<a id="symbol-sn-percent-building-cancellation"></a>

## `sn-percent-building-cancellation`

- Kind: `strategic-number`
- Detail: SN 243 - Buildings

Set to the maximum allowable completion percentage for building cancellation.

Default: `100`

Required range: `1 to 100`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-percent-building-cancellation)

<a id="symbol-sn-percent-civilian-builders"></a>

## `sn-percent-civilian-builders`

- Kind: `strategic-number`
- Detail: SN 1 - Buildings

In AoE1, this strategic number controls the normal, formula-based percentage of builders allocated. However, in AoE2, this SN appears to do nothing. It can be set to 0, and it won't prevent villagers from constructing buildings or assisting with up-assign-builders. The setting of this SN doesn't affect the behavior of sn-percent-civilian-explorers or sn-percent-civilian-gatherers.

Default: `0`

Required range: `0 to 100`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-percent-civilian-builders)

<a id="symbol-sn-percent-civilian-explorers"></a>

## `sn-percent-civilian-explorers`

- Kind: `strategic-number`
- Detail: SN  - Exploring

Caps the number of villagers assigned to explore to the given percentage. It's recommended to set this SN to 100 and use other SNs to control villager exploration. Setting this SN to 100 will not prevent villagers from gathering or constructing buildings. This SN does not affect fishing ships, and sn-number-boat-explore-groups should be used instead for fishing ships. In practice, this SN caps the number of villagers to a percentage of all villagers, rounded up. So, if it is set to 33%, one of the three starting villagers will explore, but if it is set to 34%, then two villagers will explore (34% of 3 is 1.02, which when rounded up is 2). The AI will calculate the number of villagers to task to explore based on sn-percent-civilian-explorers, sn-cap-civilian-explorers, and sn-total-number-explorers, ultimately using whichever SN results in the smallest number of explorers. If at least sn-percent-half-exploration percent of the map is explored, this number is cut in half, so it's best to set sn-percent-half-exploration to 100 to have full control over the number of exploring villagers. The AI will try assign as many villagers as possible to reach the desired number of explorers, but villagers currently tasked to build, repair, explore, or gather (except non-luring hunters and miners) are not available to be tasked to explore. Instead, villagers assigned to these tasks must have their current task cancelled first, such as with up-retask-gatherers or garrisoning the villagers, or the AI will wait until their current task is finished before tasking the villager to explore, such as a lumberjack finishing the current tree. To stop villagers from exploring, set sn-percent-civilian-explorers, sn-cap-civilian-explorers, or sn-total-number-explorers to 0, and use up-reset-scouts. All land explorers will explore around the AI's town when the game time is less than sn-home-exploration-time. After the game time exceeds the value of sn-home-exploration-time, explorers will start exploring locations further away. It's usually simplest to use just one of sn-percent-civilian-explorers, sn-cap-civilian-explorers, and sn-total-number-explorers to cap villager exploration. Often, sn-cap-civilian-explorers is the easiest to use, and you can just set sn-percent-civilian-explorers to 100 and sn-total-number-explorers to a high number like 10, and then not worry about having to change them later. However, if you don't have a specific desired number of villager explorers that you want, and you just want to set a certain % of them to explore, you can set sn-cap-civilian-explorers to -1 (-1 = ignore sn-cap-civilian-explorers), and just use sn-percent-civilian-explorers instead. The settings of sn-percent-civilian-builders and sn-percent-civilian-gatherers do not affect the number of villagers that can be tasked to explore. Also, sn-minimum-civilian-explorers and archived-non-de-strategic-number don't appear to affect the number of villager explorers, so you can ignore these SNs.

Default: `34`

Required range: `0 to 100`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-percent-civilian-explorers)

<a id="symbol-sn-percent-civilian-gatherers"></a>

## `sn-percent-civilian-gatherers`

- Kind: `strategic-number`
- Detail: SN 2 - Economy

In AoE1, this strategic number controls the normal, formula-based percentage of gatherers allocated. However, in AoE2, this SN appears to do nothing. It can be set to 0, and it won't prevent villagers from gathering. The setting of this SN doesn't affect the behavior of sn-percent-civilian-explorers or sn-percent-civilian-builders.

Default: `66`

Required range: `0 to 100`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-percent-civilian-gatherers)

<a id="symbol-sn-percent-enemy-sighted-response"></a>

## `sn-percent-enemy-sighted-response`

- Kind: `strategic-number`
- Detail: SN 19 - Defense

Sets the percentage of idle troops that will respond to another unit being attacked.

Default: `50`

Required range: `0 to 100`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-percent-enemy-sighted-response)

<a id="symbol-sn-percent-exploration-required"></a>

## `sn-percent-exploration-required`

- Kind: `strategic-number`
- Detail: SN 32 - Exploring

Sets the minimum amount of exploration that a computer player must have accomplished before being allowed to retask civilian explorers.

Default: `100`

Required range: `0 to 100`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-percent-exploration-required)

<a id="symbol-sn-percent-half-exploration"></a>

## `sn-percent-half-exploration`

- Kind: `strategic-number`
- Detail: SN 179 - Exploring

The percentage of map exploration that allows the computer player to task down to half the number of explorers.

Default: `30`

Required range: `0 to 100`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-percent-half-exploration)

<a id="symbol-sn-placement-fail-delta"></a>

## `sn-placement-fail-delta`

- Kind: `strategic-number`
- Detail: SN 269 - Buildings

Set to the value that will be added to the placement distance set by up-set-placement-data for every pass that a building cannot be placed. This sn does not affect forward building. It should be a low value (-2 to 2). The default is 0, which means that only the per-building zone-size is increased for each placement failure. This zone size expands by 1 per building every 7 "internal" passes. These internal passes usually happen ~10 times for each AI script pass. Unlike sn-placement-zone-size, sn-placement-fail-delta is not stored with the placement data.

Default: `0`

Required range: `-10 to 10`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-placement-fail-delta)

<a id="symbol-sn-placement-to-center"></a>

## `sn-placement-to-center`

- Kind: `strategic-number`
- Detail: SN 270 - Buildings

Set to 1 to force place-control to use the map center as the second point of reference for placement. The first point of reference is set with up-set-placement-data. If set to 0, the active target player's nearest building will become the second point of reference instead, once discovered. If sn-target-player-number is 0, the target enemy will be determined by sn-attack-winning-player.

Default: `0`

Required range: `0 to 1`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-placement-to-center)

<a id="symbol-sn-placement-zone-size"></a>

## `sn-placement-zone-size`

- Kind: `strategic-number`
- Detail: SN 268 - Buildings

Set to the size of the tile zone used for forward and controlled building placement. All build commands store this value and the up-set-placement-data information with each successful call. For every pass that a building cannot be placed, its zone size will be increased from this starting point. The placement region set by sn-placement-zone-size expands by 1 tile per building every 7 "internal" passes. These internal passes usually happen ~10 times for each AI script pass. The default for this sn is 20. A small zone size (0) will provide more precise positioning. A large value allows you to surround the enemy when forward building. sn-placement-zone-size is stored with the placement data, so this SN can be changed once the building has been added to the building placement queue.

Default: `20`

Required range: `0 to 255`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-placement-zone-size)

<a id="symbol-sn-preferred-mill-placement"></a>

## `sn-preferred-mill-placement`

- Kind: `strategic-number`
- Detail: SN 253 - Buildings

Set to 0 for forage, 1 for deer, or 2 for shore fish.

Default: `0`

Required range: `0 to 2`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-preferred-mill-placement)

<a id="symbol-sn-preferred-settlement-placement"></a>

## `sn-preferred-settlement-placement`

- Kind: `strategic-number`
- Detail: SN 314 - Buildings

Controls the resource that settlements are placed nearby. Here are the effective values:-1: seems to prioritize wood0: unknown1: deer and prey huntable animals2: Shore Fish3: Wood4: Gold5: Stone6: Forage

Default: `-1`

Required range: `-1 to 6`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-preferred-settlement-placement)

<a id="symbol-sn-preferred-storage-pit-placement"></a>

## `sn-preferred-storage-pit-placement`

- Kind: `strategic-number`
- Detail: SN 311 - Buildings

Controls the preferred resource the AI will place its storage pits nearby. Return of Rome DLC only. Currently this SN seems bugged, but the following values are what is supposed to work. Setting the SN to -1 seems to currently work for placing storage pits near wood.(defconst storage-pit-default -1)(defconst storage-pit-forage 0)(defconst storage-pit-hunting 1)(defconst storage-pit-fishing 2)(defconst storage-pit-wood 3)(defconst storage-pit-gold 4)(defconst storage-pit-stone 5)

Default: `-1`

Required range: `-1 to 5`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-preferred-storage-pit-placement)

<a id="symbol-sn-preferred-trade-distance"></a>

## `sn-preferred-trade-distance`

- Kind: `strategic-number`
- Detail: SN 259 - Economy

Set to the preferred distance between local and remote trade buildings. Every 4 gold drops, trade units will check if a new trade building is better and retarget if necessary.

Default: `100`

Required range: `0 to 255`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-preferred-trade-distance)

<a id="symbol-sn-profiling-threshold"></a>

## `sn-profiling-threshold`

- Kind: `strategic-number`
- Detail: SN 305 - Other

The maximum number of milliseconds between script passes before the game will be stopped and the debug screen will appear. Ignored if set to -1 (the default). For this SN to work, you must also add the Steam launch parameters AIDEBUGGING and AISCRIPTPROFILING. To set launch parameters, open Steam => Right click the game in the Library view => click Properties => and type the launch parameters, separated by spaces (not commas). According to offwo, the DE devs give a rough guideline that this shouldn't trigger at 1000 and under 600 was ideal, but offwo suggests that setting this SN to 1500-2000 is fine for a custom AI. Setting this SN to a higher value like 10000 can help find jump freezes too without having to wait a long time.

Default: `-1`

Required range: `Min to Max`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-profiling-threshold)

<a id="symbol-sn-random-placement-factor"></a>

## `sn-random-placement-factor`

- Kind: `strategic-number`
- Detail: SN 168 - Buildings

A number that gets added into the placement of the computer player to randomize building placement (off of the calculated ideal).

Default: `50`

Required range: `0 to Max`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-random-placement-factor)

<a id="symbol-sn-remove-units-from-control-groups"></a>

## `sn-remove-units-from-control-groups`

- Kind: `strategic-number`
- Detail: SN 313 - Economy

Unknown. This SN is undocumented. It doesn't appear to affect manually created control groups with Ctrl+#, and it doesn't appear to change groups created with up-create-group or up-modify-group-flag.

Default: `-1`

Required range: `Min to Max`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-remove-units-from-control-groups)

<a id="symbol-sn-retask-gather-amount"></a>

## `sn-retask-gather-amount`

- Kind: `strategic-number`
- Detail: SN 148 - Economy

The minimum amount that a gatherer must gather before the computer player allows him to be retasked to another resource type. Some code may override this.

Default: `20`

Required range: `0 to Max`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-retask-gather-amount)

<a id="symbol-sn-safe-town-size"></a>

## `sn-safe-town-size`

- Kind: `strategic-number`
- Detail: SN 250 - Defense

If an enemy building is inside both sn-maximum-town-size and the region specified by this sn, it will be targeted by defensive units. If the building is inside sn-maximum-town-size, but outside this region, it will be targeted only if it belongs to the player specified by sn-target-player-number.

Default: `255`

Required range: `1 to 255`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-safe-town-size)

<a id="symbol-sn-scale-maximum-attack-group-size"></a>

## `sn-scale-maximum-attack-group-size`

- Kind: `strategic-number`
- Detail: SN 94 - Attack

The scaling factor for the maximum attack group size. Added to sn-minimum-attack-group-size when the tactical AI does its scaling.

Default: `0`

Required range: `0 to Max`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-scale-maximum-attack-group-size)

<a id="symbol-sn-scale-minimum-attack-group-size"></a>

## `sn-scale-minimum-attack-group-size`

- Kind: `strategic-number`
- Detail: SN 93 - Attack

The scaling factor for the minimum attack group size. Added to sn-minimum-attack-group-size when the tactical AI does its scaling. The SN automatically increases sn-minimum-attack-group-size by the value of sn-scale-minimum-attack-group-size every X minutes, where X is the value of sn-scaling-frequency. If sn-scale-minimum-attack-group-size is kept at the default of 1 and sn-scaling-frequency is kept at the default value of 10, then sn-minimum-attack-group-size will increase by 1 every 10 minutes. It's best to set sn-scale-minimum-attack-group-size to 0 and modify sn-minimum-attack-group-size directly. The automatic scaling behavior from this SN on its own isn't a big deal, but the default value of the corresponding SN sn-scale-maximum-attack-group-size is zero, meaning that sn-maximum-attack-group-size isn't automatically increased in the same manner, and eventually sn-minimum-attack-group-size can exceed sn-maximum-attack-group-size. My understanding is that this will prevent attack groups from being sent, since it is impossible for attack groups to have a valid size in this situation. Even if attack groups are still sent, it is more straightforward for scripters to set sn-scale-minimum-attack-group-size to zero and to increase sn-minimum-attack-group-size directly over time.

Default: `1`

Required range: `0 to Max`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-scale-minimum-attack-group-size)

<a id="symbol-sn-scaling-frequency"></a>

## `sn-scaling-frequency`

- Kind: `strategic-number`
- Detail: SN 99 - Attack

Sets the number of minutes that pass between each scaling inside the tactical AI. Every X minutes, where X is the number of minutes set by sn-scaling-frequency, sn-minimum-attack-group-size increases by the value of sn-scale-minimum-attack-group-size, and sn-maximum-attack-group-size increases by the value of sn-scale-maximum-attack-group-size.

Default: `10`

Required range: `0 to Max`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-scaling-frequency)

<a id="symbol-sn-sentry-distance"></a>

## `sn-sentry-distance`

- Kind: `strategic-number`
- Detail: SN 22 - Defense

Sets the distance at which the town is defended. This distance varies (in some way) by sn-sentry-distance-variation. Some scripters have concluded that this distance is added to sn-maximum-town-size for the purposes of town defense but not for building construction. Others have said that it's only used for gathering soldiers. Do some testing before using this SN. If you want simplified control of your town defense, set this to 0 so that you don't have to worry about it.

Default: `12`

Required range: `0 to 255`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-sentry-distance)

<a id="symbol-sn-sentry-distance-variation"></a>

## `sn-sentry-distance-variation`

- Kind: `strategic-number`
- Detail: SN 72 - Defense

Sets the amount of allowable variation in the defense distances. See the description for sn-sentry-distance to understand how sentry distances work.

Default: `2`

Required range: `0 to Max`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-sentry-distance-variation)

<a id="symbol-sn-special-attack-influence1"></a>

## `sn-special-attack-influence1`

- Kind: `strategic-number`
- Detail: SN 109 - Attack

Sets the multiplier used for the special attack type 1 rating in computer player target evaluation. Must be &gt; 0 to influence the computer player toward attacking the special type 1, &lt; 0 to influence the computer player away from attacking the special type 1.

Default: `0`

Required range: `Min to Max`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-special-attack-influence1)

<a id="symbol-sn-special-attack-influence2"></a>

## `sn-special-attack-influence2`

- Kind: `strategic-number`
- Detail: SN 110 - Attack

Sets the multiplier used for the special attack type 2 rating in computer player target evaluation. Must be &gt; 0 to influence the computer player toward attacking the special type 2, &lt; 0 to influence the computer player away from attacking the special type 2.

Default: `0`

Required range: `Min to Max`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-special-attack-influence2)

<a id="symbol-sn-special-attack-influence3"></a>

## `sn-special-attack-influence3`

- Kind: `strategic-number`
- Detail: SN 111 - Attack

Sets the multiplier used for the special attack type 3 rating in computer player target evaluation. Must be &gt; 0 to influence the computer player toward attacking the special type 3, &lt; 0 to influence the computer player away from attacking the special type 3.

Default: `0`

Required range: `Min to Max`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-special-attack-influence3)

<a id="symbol-sn-special-attack-type1"></a>

## `sn-special-attack-type1`

- Kind: `strategic-number`
- Detail: SN 106 - Attack

Set to 1 to target monasteries and monks carrying relics.

Default: `-1`

Required range: `-1 to 1`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-special-attack-type1)

<a id="symbol-sn-special-attack-type2"></a>

## `sn-special-attack-type2`

- Kind: `strategic-number`
- Detail: SN 107 - Attack

Set to any unit, building, or group id to direct attacks. Unit lines do not work. This SN only affects soldiers attacking with attack groups or attack-now. scripter64 created a test scenario and was able to switch between targeting a mill and a lumber camp on demand using the following steps: Set special-attack-type2 to millDisband groups (I set group-form-distance:0, minimum/maximum-attack-group-size:0, number-attack-groups:0)Wait a turn or two (more turns gives more time for groups to disband)Assign multi-unit attack groups as usual (single-unit groups do not use attack-intelligence)Units depart for the enemy mill as expectedSet special-attack-type2 to lumber-campDisband groups againWait a turn or twoAssign multi-unit attack groups as usualUnits retarget toward the enemy lumber campLoop to 01 You must defconst this SN before using it, like (defconst sn-special-attack-type2 107)

Default: `-1`

Required range: `-1 to Max`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-special-attack-type2)

<a id="symbol-sn-special-attack-type3"></a>

## `sn-special-attack-type3`

- Kind: `strategic-number`
- Detail: SN 108 - Attack

Set to 1 to target wonders. You must defconst this SN before using it, like (defconst sn-special-attack-type3 108)

Default: `-1`

Required range: `-1 to 1`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-special-attack-type3)

<a id="symbol-sn-stone-dropsite-distance"></a>

## `sn-stone-dropsite-distance`

- Kind: `strategic-number`
- Detail: SN 165 - Economy

The maximum number of tiles a computer player likes to walk to drop off its stone.

Default: `3`

Required range: `3 to 255`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-stone-dropsite-distance)

<a id="symbol-sn-stone-gatherer-percentage"></a>

## `sn-stone-gatherer-percentage`

- Kind: `strategic-number`
- Detail: SN 119 - Economy

Set to configure stone gatherers: stoneGatherers = ( this + sn-stone-modifier-percentage ) * gathererTotal * 0.01 + 0.5.

Default: `0`

Required range: `0 to 100`

Range: `0 to 100`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-stone-gatherer-percentage)

<a id="symbol-sn-stone-modifier-percentage"></a>

## `sn-stone-modifier-percentage`

- Kind: `strategic-number`
- Detail: SN 158 - Economy

Set to configure stone gatherers: stoneGatherers = ( sn-stone-gatherer-percentage + this ) * gathererTotal * 0.01 + 0.5.

Default: `0`

Required range: `-100 to 100`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-stone-modifier-percentage)

<a id="symbol-sn-target-player-number"></a>

## `sn-target-player-number`

- Kind: `strategic-number`
- Detail: SN 249 - Attack

Set to the number of the player that should be targeted for attack. If this sn is set to -1, initiating an attack will instead provide assistance to allies. When set to 0, sn-attack-winning-player will determine the target. Setting this to a player that cannot be attacked (an ally or the AI itself) will result in undefined behavior. You can also use this value with the &quot;target-player&quot; identifier in facts and actions.

Default: `0`

Required range: `-1 to 8`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-target-player-number)

<a id="symbol-sn-target-point-adjustment"></a>

## `sn-target-point-adjustment`

- Kind: `strategic-number`
- Detail: SN 292 - Other

Set to adjust the tile positioning of up-target-point toward 1:left, 2:top, 3:right, 4:bottom, 5:middle, 6:precise. If set to 0, actions will be directed to the absolute left-most point of a tile. If set to precise, you must directly pass a valid precise point goal pair (point x100 for precision) to up-target-point. Note: when set to 6 (precise), all up-target-point actions will assume the point has precise coordinates when sending the units to that point, i.e. it will assume the coordinates are multiplied by 100. So, ensure that you set this strategic number back to a value from 0 to 5 before using a point with normal coordinates in a up-target-point command. Otherwise, using up-target-point with this strategic number will send units to the left corner of the map. For example, if the point has the normal coordinates (48, 187), up-target-point would send the units to point (0.48, 1.87) when this strategic number is set to 6.

Default: `0`

Required range: `0 to 6`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-target-point-adjustment)

<a id="symbol-sn-task-ungrouped-soldiers"></a>

## `sn-task-ungrouped-soldiers`

- Kind: `strategic-number`
- Detail: SN 143 - Defense

Controls whether or not ungrouped computer player soldiers get tasked to spread out and guard the computer player's general town area. When set to the default value of 1, this SN requires all idle military units to keep a certain distance from each other, usually around 4-6 tiles. The AI will check every few seconds, and if it finds units that are too close together, it will order those units to spread out. In practice, it makes units look like the are slowly wandering around the town in a random pattern, and if the AI has a large army, these soldiers may spread out a far distance away from the center of the AI's town. In most cases the behavior of sn-task-ungrouped-soldiers is undesirable, and setting the SN to zero is better. Town defense is usually most effective when defensive soldiers aren't separated. However, some scripters will temporarily set this SN to 1 for a couple seconds every minute or so to prevent soldiers from clumping around their training buildings after being trained.

Default: `1`

Required range: `0 to 1`

Range: `1 to 1`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-task-ungrouped-soldiers)

<a id="symbol-sn-total-number-explorers"></a>

## `sn-total-number-explorers`

- Kind: `strategic-number`
- Detail: SN 18 - Exploring

Caps the total number of land explorers allocated. It's recommended to set this SN to a high number like 10 and use other SNs to control exploration. This SN sets a cap on all total land explorers, both land military units and villagers. Ship explorers aren't included. Some older documentation states that setting sn-total-number-explorers to -1 will ignore this SN, but using -1 prevents villagers from exploring. To determine the number of explorers the AI uses, first, the AI will calculate the number of villagers to task to explore based on sn-percent-civilian-explorers, sn-cap-civilian-explorers, and sn-total-number-explorers, ultimately using whichever SN results in the smallest number of villager explorers. Then, if the number of villager explorers is less than sn-total-number-explorers, the AI will send military units to explore until it reaches the number of sn-number-explore-groups or the total number of land explorers reaches sn-total-number-explorers. If at least sn-percent-half-exploration percent of the map is explored, the amount of this SN is cut in half, so it's best to set sn-percent-half-exploration to 100 to have full control over the number of exploring units. The AI will try assign as many land units as possible to reach the desired number of explorers, but villagers currently tasked to build, repair, explore, or gather (except non-luring hunters and miners) are not available to be tasked to explore. Instead, villagers assigned to these tasks must have their current task cancelled first, such as with up-retask-gatherers or garrisoning the villagers, or the AI will wait until their current task is finished before tasking the villager to explore, such as a lumberjack finishing the current tree. To stop villagers from exploring, set sn-percent-civilian-explorers, sn-cap-civilian-explorers, or sn-total-number-explorers to 0, and use up-reset-scouts. Similarly, to stop military units from exploring, set sn-number-explore-groups or sn-total-number-explorers to 0, and use up-reset-scouts. All land explorers will explore around the AI's town when the game time is less than sn-home-exploration-time. After the game time exceeds the value of sn-home-exploration-time, explorers will start exploring locations further away. It's usually simplest to use just one of sn-percent-civilian-explorers, sn-cap-civilian-explorers, and sn-total-number-explorers to cap villager exploration, and it's usually simplest to use just one of sn-number-explore-groups and sn-total-number-explorers to cap military exploration. Often, sn-cap-civilian-explorers is the easiest to use for villager exploration, and you can just set sn-percent-civilian-explorers to 100 and sn-total-number-explorers to a high number like 10, and then not worry about having to change them later. Similarly, for military exploration it's usually simplest to set sn-total-number-explorers to -1 to ignore this SN and just use sn-number-explore-groups. sn-minimum-civilian-explorers and archived-non-de-strategic-number don't appear to affect the number of villager explorers, so you can ignore these SNs.

Default: `4`

Required range: `-1 to Max`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-total-number-explorers)

<a id="symbol-sn-town-center-placement"></a>

## `sn-town-center-placement`

- Kind: `strategic-number`
- Detail: SN 266 - Buildings

Set to the building type to emulate for town center placement, like lumber-camp. If set to 0, the town center will be placed as usual. Note that it is complete emulation, so if you set it to mill, it will use sn-mill-max-distance for its maximum-town-size. Example: (set-strategic-number sn-town-center-placement mill) ;attempt to emulate mill placement

Default: `0`

Required range: `0 to 899`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-town-center-placement)

<a id="symbol-sn-ttkfactor-scalar"></a>

## `sn-ttkfactor-scalar`

- Kind: `strategic-number`
- Detail: SN 301 - Attack

Time to kill an object scalar (in seconds). The scalar is a percentage. Likely affects retargeting against nearby units.

Default: `100`

Required range: `Min to Max`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-ttkfactor-scalar)

<a id="symbol-sn-unexplored-construction"></a>

## `sn-unexplored-construction`

- Kind: `strategic-number`
- Detail: SN 293 - Buildings

Set to 1 to allow the AI to construct buildings on unexplored tiles. If set to 0, the AI will have to directly explore tiles in order to build there as usual. Please do not enable this without #load-if-not-defined REVEAL-NORMAL.

Default: `0`

Required range: `0 to 1`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-unexplored-construction)

<a id="symbol-sn-use-by-type-max-gathering"></a>

## `sn-use-by-type-max-gathering`

- Kind: `strategic-number`
- Detail: SN 203 - Economy

Controls whether or not logical, type-specific gatherer requirements are placed on the quantity of resources gatherers must collect before being allowed to be retasked.

Default: `0`

Required range: `0 to 1`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-use-by-type-max-gathering)

<a id="symbol-sn-villager-attack-reset"></a>

## `sn-villager-attack-reset`

- Kind: `strategic-number`
- Detail: SN 303 - Attack

If set to 0, disables the auto-villager attack reset so you can attack distant units/targets with villagers.

Default: `1`

Required range: `0 to 1`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-villager-attack-reset)

<a id="symbol-sn-wall-targeting-mode"></a>

## `sn-wall-targeting-mode`

- Kind: `strategic-number`
- Detail: SN 262 - Attack

Set to 1 to allow military units to automatically target nearby walls and gates. If set to 0, they will likely be ignored. It's good to use sn-wall-targeting-mode set to 1 if you are attacking with retargetable attack groups or, sometimes, TSA. It may be bad for attack-now, since they cannot be retargeted by the AI script,

Default: `0`

Required range: `0 to 1`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-wall-targeting-mode)

<a id="symbol-sn-warship-targeting-mode"></a>

## `sn-warship-targeting-mode`

- Kind: `strategic-number`
- Detail: SN 283 - Water

Set to 1 to cause warships to target based on the unit with the shortest range in the group against fortifications. Set to 2 to eliminate the range check. If set to 0, warship groups will target based on the unit with the longest range.

Default: `0`

Required range: `0 to 2`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-warship-targeting-mode)

<a id="symbol-sn-whaling-max-distance"></a>

## `sn-whaling-max-distance`

- Kind: `strategic-number`
- Detail: SN 317 - Water

Controls how far from a dropsite a whale can be before the CP ignores it. -1 indicates a &quot;don't care&quot; -- i.e. it can be any distance (as it used to be). -2 disables all whale gathering. The default of this SN is -1, meaning the SN is ignored by default. This can allow whaling ships to go all the across the map to gather from whales, which might not be what you want early in the game. You'll probably want to set it back to -1 later on in the game, perhaps in the Imperial Age or after an hour of game time.

Default: `-1`

Required range: `-2 to 255`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-whaling-max-distance)

<a id="symbol-sn-wild-animal-exploration"></a>

## `sn-wild-animal-exploration`

- Kind: `strategic-number`
- Detail: SN 300 - Exploring

Allows wild horses, wild camel and bactrian camels to explore.

Default: `0`

Required range: `0 to 1`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-wild-animal-exploration)

<a id="symbol-sn-wood-dropsite-distance"></a>

## `sn-wood-dropsite-distance`

- Kind: `strategic-number`
- Detail: SN 164 - Economy

The maximum number of tiles a computer player likes to walk to drop off its wood.

Default: `3`

Required range: `3 to 255`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-wood-dropsite-distance)

<a id="symbol-sn-wood-gatherer-percentage"></a>

## `sn-wood-gatherer-percentage`

- Kind: `strategic-number`
- Detail: SN 120 - Economy

Set to configure wood gatherers: woodGatherers = ( this + sn-wood-modifier-percentage ) * gathererTotal * 0.01 + 0.5.

Default: `0`

Required range: `0 to 100`

Range: `0 to 100`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-wood-gatherer-percentage)

<a id="symbol-sn-wood-modifier-percentage"></a>

## `sn-wood-modifier-percentage`

- Kind: `strategic-number`
- Detail: SN 157 - Economy

Set to configure wood gatherers: woodGatherers = ( sn-wood-gatherer-percentage + this ) * gathererTotal * 0.01 + 0.5.

Default: `0`

Required range: `-100 to 100`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-wood-modifier-percentage)

<a id="symbol-sn-zero-priority-distance"></a>

## `sn-zero-priority-distance`

- Kind: `strategic-number`
- Detail: SN 34 - Other

Sets the distance at which a computer player's order for a unit is set to a priority of 0. It's unknown whether the SN will cause units beyond this distance from the main town center to become idle, or whether it makes enemy targets beyond this to have zero priority, meaning the AI won't attack them. Neither outcome is desirable, so change this SN from the default value of 50 to the max value of 255 so you don't have to worry about it.

Default: `50`

Required range: `0 to 255`

Range: `Min to Max`

[AIRef](https://airef.github.io/strategic-numbers/sn-details.html#sn-zero-priority-distance)

<a id="section-tech"></a>

# tech

<a id="symbol-castle-age"></a>

## `castle-age`

- Kind: `tech`
- Detail: Tech 102 - Castle Age

Building: Town Center

<a id="symbol-feudal-age"></a>

## `feudal-age`

- Kind: `tech`
- Detail: Tech 101 - Feudal Age

Building: Town Center

<a id="symbol-imperial-age"></a>

## `imperial-age`

- Kind: `tech`
- Detail: Tech 103 - Imperial Age

Building: Town Center

<a id="symbol-ri-andean-sling"></a>

## `ri-andean-sling`

- Kind: `tech`
- Detail: Tech 516 - Andean Sling

Building: Castle

Civilization: Incas

<a id="symbol-ri-arbalest"></a>

## `ri-arbalest`

- Kind: `tech`
- Detail: Tech 237 - Arbalest

Building: Archery Range

<a id="symbol-ri-arbalester"></a>

## `ri-arbalester`

- Kind: `tech`
- Detail: Tech 237 - Arbalest

Building: Archery Range

<a id="symbol-ri-architecture"></a>

## `ri-architecture`

- Kind: `tech`
- Detail: Tech 51 - Architecture

Building: University

<a id="symbol-ri-arquebus"></a>

## `ri-arquebus`

- Kind: `tech`
- Detail: Tech 573 - Arquebus

Building: Castle

Civilization: Portuguese

<a id="symbol-ri-arrowslits"></a>

## `ri-arrowslits`

- Kind: `tech`
- Detail: Tech 608 - Arrowslits

Building: University

<a id="symbol-ri-arson"></a>

## `ri-arson`

- Kind: `tech`
- Detail: Tech 602 - Arson

Building: Barracks

<a id="symbol-ri-atlatl"></a>

## `ri-atlatl`

- Kind: `tech`
- Detail: Tech 460 - Atlatl

Building: Castle

Civilization: Aztecs

<a id="symbol-ri-atonement"></a>

## `ri-atonement`

- Kind: `tech`
- Detail: Tech 319 - Atonement

Building: Monastery

<a id="symbol-ri-aznauri-cavalry"></a>

## `ri-aznauri-cavalry`

- Kind: `tech`
- Detail: Tech 924 - Aznauri Cavalry

Building: Castle

Civilization: Georgians

<a id="symbol-ri-bagains"></a>

## `ri-bagains`

- Kind: `tech`
- Detail: Tech 686 - Bagains

Building: Castle

Civilization: Bulgarians

<a id="symbol-ri-ballistas"></a>

## `ri-ballistas`

- Kind: `tech`
- Detail: Tech 883 - Ballistas

Building: Castle

Civilization: Romans

<a id="symbol-ri-ballistics"></a>

## `ri-ballistics`

- Kind: `tech`
- Detail: Tech 93 - Ballistics

Building: University

<a id="symbol-ri-banking"></a>

## `ri-banking`

- Kind: `tech`
- Detail: Tech 17 - Banking

Building: Market

<a id="symbol-ri-blast-furnace"></a>

## `ri-blast-furnace`

- Kind: `tech`
- Detail: Tech 75 - Blast Furnace

Building: Blacksmith

<a id="symbol-ri-block-printing"></a>

## `ri-block-printing`

- Kind: `tech`
- Detail: Tech 230 - Block Printing

Building: Monastery

<a id="symbol-ri-bloodlines"></a>

## `ri-bloodlines`

- Kind: `tech`
- Detail: Tech 435 - Bloodlines

Building: Stable

<a id="symbol-ri-bodkin-arrow"></a>

## `ri-bodkin-arrow`

- Kind: `tech`
- Detail: Tech 200 - Bodkin Arrow

Building: Blacksmith

<a id="symbol-ri-bolt-magazine"></a>

## `ri-bolt-magazine`

- Kind: `tech`
- Detail: Tech 1069 - Bolt Magazine

Building: Castle

Civilization: Shu

<a id="symbol-ri-bombard-tower"></a>

## `ri-bombard-tower`

- Kind: `tech`
- Detail: Tech 64 - Bombard Tower

Building: University

<a id="symbol-ri-bow-saw"></a>

## `ri-bow-saw`

- Kind: `tech`
- Detail: Tech 203 - Bow Saw

Building: Lumber Camp

<a id="symbol-ri-bracer"></a>

## `ri-bracer`

- Kind: `tech`
- Detail: Tech 201 - Bracer

Building: Blacksmith

<a id="symbol-ri-burgundian-vineyards"></a>

## `ri-burgundian-vineyards`

- Kind: `tech`
- Detail: Tech 754 - Burgundian Vineyards

Building: Castle

Civilization: Burgundians

<a id="symbol-ri-capped-ram"></a>

## `ri-capped-ram`

- Kind: `tech`
- Detail: Tech 96 - Capped Ram

Building: Siege Workshop

<a id="symbol-ri-caravan"></a>

## `ri-caravan`

- Kind: `tech`
- Detail: Tech 48 - Caravan

Building: Market

<a id="symbol-ri-careening"></a>

## `ri-careening`

- Kind: `tech`
- Detail: Tech 374 - Careening

Building: University

<a id="symbol-ri-cavalier"></a>

## `ri-cavalier`

- Kind: `tech`
- Detail: Tech 209 - Cavalier

Building: Stable

<a id="symbol-ri-chain-barding"></a>

## `ri-chain-barding`

- Kind: `tech`
- Detail: Tech 82 - Chain Barding Armor

Building: Blacksmith

<a id="symbol-ri-chain-mail"></a>

## `ri-chain-mail`

- Kind: `tech`
- Detail: Tech 76 - Chain Mail Armor

Building: Blacksmith

<a id="symbol-ri-champion"></a>

## `ri-champion`

- Kind: `tech`
- Detail: Tech 264 - Champion

Building: Barracks

<a id="symbol-ri-chatras"></a>

## `ri-chatras`

- Kind: `tech`
- Detail: Tech 628 - Chatras

Building: Castle

Civilization: Vietnamese

<a id="symbol-ri-chemistry"></a>

## `ri-chemistry`

- Kind: `tech`
- Detail: Tech 47 - Chemistry

Building: University

<a id="symbol-ri-chieftains"></a>

## `ri-chieftains`

- Kind: `tech`
- Detail: Tech 463 - Chieftains

Building: Castle

Civilization: Vikings

<a id="symbol-ri-chivalry"></a>

## `ri-chivalry`

- Kind: `tech`
- Detail: Tech 493 - Chivalry

Building: Castle

Civilization: Franks

<a id="symbol-ri-cilician-fleet"></a>

## `ri-cilician-fleet`

- Kind: `tech`
- Detail: Tech 922 - Cilician Fleet

Building: Castle

Civilization: Armenians

<a id="symbol-ri-coiled-serpent-array"></a>

## `ri-coiled-serpent-array`

- Kind: `tech`
- Detail: Tech 1070 - Coiled Serpent Array

Building: Castle

Civilization: Shu

<a id="symbol-ri-coinage"></a>

## `ri-coinage`

- Kind: `tech`
- Detail: Tech 23 - Coinage

Building: Market

<a id="symbol-ri-comitatenses"></a>

## `ri-comitatenses`

- Kind: `tech`
- Detail: Tech 884 - Comitatenses

Building: Castle

Civilization: Romans

<a id="symbol-ri-conscription"></a>

## `ri-conscription`

- Kind: `tech`
- Detail: Tech 315 - Conscription

Building: Castle

<a id="symbol-ri-corvinian-army"></a>

## `ri-corvinian-army`

- Kind: `tech`
- Detail: Tech 514 - Corvinian Army/Mercenaries

Building: Castle

Civilization: Magyars

<a id="symbol-ri-counterweights"></a>

## `ri-counterweights`

- Kind: `tech`
- Detail: Tech 454 - Counterweights

Building: Castle

Civilization: Saracens

<a id="symbol-ri-crop-rotation"></a>

## `ri-crop-rotation`

- Kind: `tech`
- Detail: Tech 12 - Crop Rotation

Building: Mill

<a id="symbol-ri-crossbow"></a>

## `ri-crossbow`

- Kind: `tech`
- Detail: Tech 100 - Crossbowman

Building: Archery Range

<a id="symbol-ri-crossbowman"></a>

## `ri-crossbowman`

- Kind: `tech`
- Detail: Tech 100 - Crossbowman

Building: Archery Range

<a id="symbol-ri-cuman-mercenaries"></a>

## `ri-cuman-mercenaries`

- Kind: `tech`
- Detail: Tech 690 - Cuman Mercenaries

Building: Castle

Civilization: Cumans

<a id="symbol-ri-deck-guns"></a>

## `ri-deck-guns`

- Kind: `tech`
- Detail: Tech 376 - Elite Cannon Galleon

Building: Dock

<a id="symbol-ri-detinets"></a>

## `ri-detinets`

- Kind: `tech`
- Detail: Tech 455 - Detinets

Building: Castle

Civilization: Slavs

<a id="symbol-ri-devotion"></a>

## `ri-devotion`

- Kind: `tech`
- Detail: Tech 46 - Devotion

Building: Monastery

<a id="symbol-ri-double-bit-axe"></a>

## `ri-double-bit-axe`

- Kind: `tech`
- Detail: Tech 202 - Double-Bit Axe

Building: Lumber Camp

<a id="symbol-ri-double-crossbow"></a>

## `ri-double-crossbow`

- Kind: `tech`
- Detail: Tech 623 - Double Crossbow

Building: Castle

Civilization: Khmer

<a id="symbol-ri-druzhina"></a>

## `ri-druzhina`

- Kind: `tech`
- Detail: Tech 513 - Druzhina

Building: Castle

Civilization: Slavs

<a id="symbol-ri-dry-dock"></a>

## `ri-dry-dock`

- Kind: `tech`
- Detail: Tech 375 - Dry Dock

Building: University

<a id="symbol-ri-eagle-warrior"></a>

## `ri-eagle-warrior`

- Kind: `tech`
- Detail: Tech 384 - Eagle Warrior

Building: Barracks

<a id="symbol-ri-elite-arambai"></a>

## `ri-elite-arambai`

- Kind: `tech`
- Detail: Tech 619 - Elite Arambai

Building: Castle

Civilization: Burmese

<a id="symbol-ri-elite-ballista-elephant"></a>

## `ri-elite-ballista-elephant`

- Kind: `tech`
- Detail: Tech 615 - Elite Ballista Elephant

Building: Castle

Civilization: Khmer

<a id="symbol-ri-elite-battle-elephant"></a>

## `ri-elite-battle-elephant`

- Kind: `tech`
- Detail: Tech 631 - Elite Battle Elephant

Building: Stable

<a id="symbol-ri-elite-berserk"></a>

## `ri-elite-berserk`

- Kind: `tech`
- Detail: Tech 398 - Elite Berserk

Building: Castle

Civilization: Vikings

<a id="symbol-ri-elite-boyar"></a>

## `ri-elite-boyar`

- Kind: `tech`
- Detail: Tech 504 - Elite Boyar

Building: Castle

Civilization: Slavs

<a id="symbol-ri-elite-camel-archer"></a>

## `ri-elite-camel-archer`

- Kind: `tech`
- Detail: Tech 565 - Elite Camel Archer

Building: Castle

Civilization: Berbers

<a id="symbol-ri-elite-cannon-galleon"></a>

## `ri-elite-cannon-galleon`

- Kind: `tech`
- Detail: Tech 376 - Elite Cannon Galleon

Building: Dock

<a id="symbol-ri-elite-caravel"></a>

## `ri-elite-caravel`

- Kind: `tech`
- Detail: Tech 597 - Elite Caravel

Building: Dock

Civilization: Portuguese

<a id="symbol-ri-elite-cataphract"></a>

## `ri-elite-cataphract`

- Kind: `tech`
- Detail: Tech 361 - Elite Cataphract

Building: Castle

Civilization: Byzantines

<a id="symbol-ri-elite-centurion"></a>

## `ri-elite-centurion`

- Kind: `tech`
- Detail: Tech 882 - Elite Centurion

Building: Castle

Civilization: Romans

<a id="symbol-ri-elite-chakram-thrower"></a>

## `ri-elite-chakram-thrower`

- Kind: `tech`
- Detail: Tech 830 - Elite Chakram Thrower

Building: Castle

Civilization: Gurjaras

<a id="symbol-ri-elite-chu-ko-nu"></a>

## `ri-elite-chu-ko-nu`

- Kind: `tech`
- Detail: Tech 362 - Elite Chu Ko Nu

Building: Castle

Civilization: Chinese

<a id="symbol-ri-elite-composite-bowman"></a>

## `ri-elite-composite-bowman`

- Kind: `tech`
- Detail: Tech 918 - Elite Composite Bowman

Building: Castle

Civilization: Armenians

<a id="symbol-ri-elite-conquistador"></a>

## `ri-elite-conquistador`

- Kind: `tech`
- Detail: Tech 60 - Elite Conquistador

Building: Castle

Civilization: Spanish

<a id="symbol-ri-elite-coustillier"></a>

## `ri-elite-coustillier`

- Kind: `tech`
- Detail: Tech 751 - Elite Coustillier

Building: Castle

Civilization: Burgundians

<a id="symbol-ri-elite-eagle-warrior"></a>

## `ri-elite-eagle-warrior`

- Kind: `tech`
- Detail: Tech 434 - Elite Eagle Warrior

Building: Barracks

<a id="symbol-ri-elite-elephant-archer"></a>

## `ri-elite-elephant-archer`

- Kind: `tech`
- Detail: Tech 481 - Elite Elephant Archer

Building: Archery Range

<a id="symbol-ri-elite-fire-archer"></a>

## `ri-elite-fire-archer`

- Kind: `tech`
- Detail: Tech 1074 - Elite Fire Archer

Building: Castle

Civilization: Wu

<a id="symbol-ri-elite-gbeto"></a>

## `ri-elite-gbeto`

- Kind: `tech`
- Detail: Tech 567 - Elite Gbeto

Building: Castle

Civilization: Malians

<a id="symbol-ri-elite-genitour"></a>

## `ri-elite-genitour`

- Kind: `tech`
- Detail: Tech 599 - Elite Genitour

Building: Archery Range

Civilization: Berbers

<a id="symbol-ri-elite-genoese-crossbowman"></a>

## `ri-elite-genoese-crossbowman`

- Kind: `tech`
- Detail: Tech 468 - Elite Genoese Crossbowman

Building: Castle

Civilization: Italians

<a id="symbol-ri-elite-ghulam"></a>

## `ri-elite-ghulam`

- Kind: `tech`
- Detail: Tech 840 - Elite Ghulam

Building: Castle

Civilization: Hindustanis

<a id="symbol-ri-elite-huskarl"></a>

## `ri-elite-huskarl`

- Kind: `tech`
- Detail: Tech 365 - Elite Huskarl

Building: Castle

Civilization: Goths

<a id="symbol-ri-elite-hussite-wagon"></a>

## `ri-elite-hussite-wagon`

- Kind: `tech`
- Detail: Tech 781 - Elite Hussite Wagon

Building: Castle

Civilization: Bohemians

<a id="symbol-ri-elite-iron-pagoda"></a>

## `ri-elite-iron-pagoda`

- Kind: `tech`
- Detail: Tech 991 - Elite Iron Pagoda

Building: Castle

Civilization: Jurchens

<a id="symbol-ri-elite-jaguar-man"></a>

## `ri-elite-jaguar-man`

- Kind: `tech`
- Detail: Tech 432 - Elite Jaguar Warrior

Building: Castle

Civilization: Aztecs

<a id="symbol-ri-elite-jaguar-warrior"></a>

## `ri-elite-jaguar-warrior`

- Kind: `tech`
- Detail: Tech 432 - Elite Jaguar Warrior

Building: Castle

Civilization: Aztecs

<a id="symbol-ri-elite-janissary"></a>

## `ri-elite-janissary`

- Kind: `tech`
- Detail: Tech 369 - Elite Janissary

Building: Castle

Civilization: Turks

<a id="symbol-ri-elite-kamayuk"></a>

## `ri-elite-kamayuk`

- Kind: `tech`
- Detail: Tech 509 - Elite Kamayuk

Building: Castle

Civilization: Incas

<a id="symbol-ri-elite-karambit-warrior"></a>

## `ri-elite-karambit-warrior`

- Kind: `tech`
- Detail: Tech 617 - Elite Karambit Warrior

Building: Castle

Civilization: Malay

<a id="symbol-ri-elite-keshik"></a>

## `ri-elite-keshik`

- Kind: `tech`
- Detail: Tech 680 - Elite Keshik

Building: Castle

Civilization: Tatars

<a id="symbol-ri-elite-kipchak"></a>

## `ri-elite-kipchak`

- Kind: `tech`
- Detail: Tech 682 - Elite Kipchak

Building: Castle

Civilization: Cumans

<a id="symbol-ri-elite-konnik"></a>

## `ri-elite-konnik`

- Kind: `tech`
- Detail: Tech 678 - Elite Konnik

Building: Castle

Civilization: Bulgarians

<a id="symbol-ri-elite-leitis"></a>

## `ri-elite-leitis`

- Kind: `tech`
- Detail: Tech 684 - Elite Leitis

Building: Castle

Civilization: Lithuanians

<a id="symbol-ri-elite-liao-dao"></a>

## `ri-elite-liao-dao`

- Kind: `tech`
- Detail: Tech 1002 - Elite Liao Dao

Building: Castle

Civilization: Khitans

<a id="symbol-ri-elite-longboat"></a>

## `ri-elite-longboat`

- Kind: `tech`
- Detail: Tech 372 - Elite Longboat

Building: Dock

Civilization: Vikings

<a id="symbol-ri-elite-longbowman"></a>

## `ri-elite-longbowman`

- Kind: `tech`
- Detail: Tech 360 - Elite Longbowman

Building: Castle

Civilization: Britons

<a id="symbol-ri-elite-magyar-huszar"></a>

## `ri-elite-magyar-huszar`

- Kind: `tech`
- Detail: Tech 472 - Elite Magyar Huszar

Building: Castle

Civilization: Magyars

<a id="symbol-ri-elite-mameluke"></a>

## `ri-elite-mameluke`

- Kind: `tech`
- Detail: Tech 368 - Elite Mameluke

Building: Castle

Civilization: Saracens

<a id="symbol-ri-elite-mangudai"></a>

## `ri-elite-mangudai`

- Kind: `tech`
- Detail: Tech 371 - Elite Mangudai

Building: Castle

Civilization: Mongols

<a id="symbol-ri-elite-monaspa"></a>

## `ri-elite-monaspa`

- Kind: `tech`
- Detail: Tech 920 - Elite Monaspa

Building: Castle

Civilization: Georgians

<a id="symbol-ri-elite-obuch"></a>

## `ri-elite-obuch`

- Kind: `tech`
- Detail: Tech 779 - Elite Obuch

Building: Castle

Civilization: Poles

<a id="symbol-ri-elite-organ-gun"></a>

## `ri-elite-organ-gun`

- Kind: `tech`
- Detail: Tech 563 - Elite Organ Gun

Building: Castle

Civilization: Portuguese

<a id="symbol-ri-elite-plumed-archer"></a>

## `ri-elite-plumed-archer`

- Kind: `tech`
- Detail: Tech 27 - Elite Plumed Archer

Building: Castle

Civilization: Mayans

<a id="symbol-ri-elite-ratha"></a>

## `ri-elite-ratha`

- Kind: `tech`
- Detail: Tech 828 - Elite Ratha

Building: Castle

Civilization: Bengalis

<a id="symbol-ri-elite-rattan-archer"></a>

## `ri-elite-rattan-archer`

- Kind: `tech`
- Detail: Tech 621 - Elite Rattan Archer

Building: Castle

Civilization: Vietnamese

<a id="symbol-ri-elite-samurai"></a>

## `ri-elite-samurai`

- Kind: `tech`
- Detail: Tech 366 - Elite Samurai

Building: Castle

Civilization: Japanese

<a id="symbol-ri-elite-serjeant"></a>

## `ri-elite-serjeant`

- Kind: `tech`
- Detail: Tech 753 - Elite Serjeant

Building: Castle

Civilization: Sicilians

<a id="symbol-ri-elite-shotel"></a>

## `ri-elite-shotel`

- Kind: `tech`
- Detail: Tech 569 - Elite Shotel Warrior

Building: Castle

Civilization: Ethiopians

<a id="symbol-ri-elite-shrivamsha-rider"></a>

## `ri-elite-shrivamsha-rider`

- Kind: `tech`
- Detail: Tech 843 - Elite Shrivamsha Rider

Building: Stable

Civilization: Gurjaras

<a id="symbol-ri-elite-skirmisher"></a>

## `ri-elite-skirmisher`

- Kind: `tech`
- Detail: Tech 98 - Elite Skirmisher

Building: Archery Range

<a id="symbol-ri-elite-steppe-lancer"></a>

## `ri-elite-steppe-lancer`

- Kind: `tech`
- Detail: Tech 715 - Elite Steppe Lancer

Building: Stable

<a id="symbol-ri-elite-tarkan"></a>

## `ri-elite-tarkan`

- Kind: `tech`
- Detail: Tech 2 - Elite Tarkan

Building: Castle

Civilization: Huns

<a id="symbol-ri-elite-teutonic-knight"></a>

## `ri-elite-teutonic-knight`

- Kind: `tech`
- Detail: Tech 364 - Elite Teutonic Knight

Building: Castle

Civilization: Teutons

<a id="symbol-ri-elite-throwing-axeman"></a>

## `ri-elite-throwing-axeman`

- Kind: `tech`
- Detail: Tech 363 - Elite Throwing Axeman

Building: Castle

Civilization: Franks

<a id="symbol-ri-elite-turtle-ship"></a>

## `ri-elite-turtle-ship`

- Kind: `tech`
- Detail: Tech 448 - Elite Turtle Ship

Building: Dock

Civilization: Koreans

<a id="symbol-ri-elite-urumi-swordsman"></a>

## `ri-elite-urumi-swordsman`

- Kind: `tech`
- Detail: Tech 826 - Elite Urumi Swordsman

Building: Castle

Civilization: Dravidians

<a id="symbol-ri-elite-war-elephant"></a>

## `ri-elite-war-elephant`

- Kind: `tech`
- Detail: Tech 367 - Elite War Elephant

Building: Castle

Civilization: Persians

<a id="symbol-ri-elite-war-wagon"></a>

## `ri-elite-war-wagon`

- Kind: `tech`
- Detail: Tech 450 - Elite War Wagon

Building: Castle

Civilization: Koreans

<a id="symbol-ri-elite-white-feather-guard"></a>

## `ri-elite-white-feather-guard`

- Kind: `tech`
- Detail: Tech 1064 - Elite White Feather Guard

Building: Castle

Civilization: Shu

<a id="symbol-ri-elite-woad-raider"></a>

## `ri-elite-woad-raider`

- Kind: `tech`
- Detail: Tech 370 - Elite Woad Raider

Building: Castle

Civilization: Celts

<a id="symbol-ri-eupseong"></a>

## `ri-eupseong`

- Kind: `tech`
- Detail: Tech 486 - Eupseong/Panokseon

Building: Castle

Civilization: Koreans

<a id="symbol-ri-fabric-shields"></a>

## `ri-fabric-shields`

- Kind: `tech`
- Detail: Tech 517 - Fabric Shields/Couriers

Building: Castle

Civilization: Incas

<a id="symbol-ri-faith"></a>

## `ri-faith`

- Kind: `tech`
- Detail: Tech 45 - Faith

Building: Monastery

<a id="symbol-ri-farimba"></a>

## `ri-farimba`

- Kind: `tech`
- Detail: Tech 577 - Farimba

Building: Castle

Civilization: Malians

<a id="symbol-ri-fereters"></a>

## `ri-fereters`

- Kind: `tech`
- Detail: Tech 921 - Fereters

Building: Castle

Civilization: Armenians

<a id="symbol-ri-fervor"></a>

## `ri-fervor`

- Kind: `tech`
- Detail: Tech 252 - Fervor

Building: Monastery

<a id="symbol-ri-first-crusade"></a>

## `ri-first-crusade`

- Kind: `tech`
- Detail: Tech 756 - First Crusade

Building: Castle

Civilization: Sicilians

<a id="symbol-ri-flemish-revolution"></a>

## `ri-flemish-revolution`

- Kind: `tech`
- Detail: Tech 755 - Flemish Revolution

Building: Castle

Civilization: Burgundians

<a id="symbol-ri-fletching"></a>

## `ri-fletching`

- Kind: `tech`
- Detail: Tech 199 - Fletching

Building: Blacksmith

<a id="symbol-ri-forced-levy"></a>

## `ri-forced-levy`

- Kind: `tech`
- Detail: Tech 625 - Forced Levy

Building: Castle

Civilization: Malay

<a id="symbol-ri-forging"></a>

## `ri-forging`

- Kind: `tech`
- Detail: Tech 67 - Forging

Building: Blacksmith

<a id="symbol-ri-fortified-bastions"></a>

## `ri-fortified-bastions`

- Kind: `tech`
- Detail: Tech 996 - Fortified Bastions

Building: Castle

Civilization: Jurchens

<a id="symbol-ri-fortified-wall"></a>

## `ri-fortified-wall`

- Kind: `tech`
- Detail: Tech 194 - Fortified Wall

Building: University

<a id="symbol-ri-frontier-guards"></a>

## `ri-frontier-guards`

- Kind: `tech`
- Detail: Tech 836 - Frontier Guards

Building: Castle

Civilization: Gurjaras

<a id="symbol-ri-galleon"></a>

## `ri-galleon`

- Kind: `tech`
- Detail: Tech 35 - Heavy Warships

Building: Dock

<a id="symbol-ri-gambesons"></a>

## `ri-gambesons`

- Kind: `tech`
- Detail: Tech 875 - Gambesons

Building: Barracks

<a id="symbol-ri-gillnets"></a>

## `ri-gillnets`

- Kind: `tech`
- Detail: Tech 65 - Gillnets

Building: Dock

<a id="symbol-ri-gold-mining"></a>

## `ri-gold-mining`

- Kind: `tech`
- Detail: Tech 55 - Gold Mining

Building: Mining Camp

<a id="symbol-ri-gold-shaft-mining"></a>

## `ri-gold-shaft-mining`

- Kind: `tech`
- Detail: Tech 182 - Gold Shaft Mining

Building: Mining Camp

<a id="symbol-ri-grand-trunk-road"></a>

## `ri-grand-trunk-road`

- Kind: `tech`
- Detail: Tech 506 - Grand Trunk Road

Building: Castle

Civilization: Hindustanis

<a id="symbol-ri-great-wall"></a>

## `ri-great-wall`

- Kind: `tech`
- Detail: Tech 462 - Great Wall

Building: Castle

Civilization: Chinese

<a id="symbol-ri-greek-fire"></a>

## `ri-greek-fire`

- Kind: `tech`
- Detail: Tech 464 - Greek Fire

Building: Castle

Civilization: Byzantines

<a id="symbol-ri-guard-tower"></a>

## `ri-guard-tower`

- Kind: `tech`
- Detail: Tech 140 - Guard Tower

Building: University

<a id="symbol-ri-guilds"></a>

## `ri-guilds`

- Kind: `tech`
- Detail: Tech 15 - Guilds

Building: Market

<a id="symbol-ri-halberdier"></a>

## `ri-halberdier`

- Kind: `tech`
- Detail: Tech 429 - Halberdier

Building: Barracks

<a id="symbol-ri-hand-cart"></a>

## `ri-hand-cart`

- Kind: `tech`
- Detail: Tech 249 - Hand Cart

Building: Town Center

<a id="symbol-ri-hauberk"></a>

## `ri-hauberk`

- Kind: `tech`
- Detail: Tech 757 - Hauberk

Building: Castle

Civilization: Sicilians

<a id="symbol-ri-heated-shot"></a>

## `ri-heated-shot`

- Kind: `tech`
- Detail: Tech 380 - Heated Shot

Building: University

<a id="symbol-ri-heavy-camel"></a>

## `ri-heavy-camel`

- Kind: `tech`
- Detail: Tech 236 - Heavy Camel [Rider]

Building: Stable

<a id="symbol-ri-heavy-camel-rider"></a>

## `ri-heavy-camel-rider`

- Kind: `tech`
- Detail: Tech 236 - Heavy Camel [Rider]

Building: Stable

<a id="symbol-ri-heavy-cavalry-archer"></a>

## `ri-heavy-cavalry-archer`

- Kind: `tech`
- Detail: Tech 218 - Heavy Cavalry Archer

Building: Archery Range

<a id="symbol-ri-heavy-demolition-ship"></a>

## `ri-heavy-demolition-ship`

- Kind: `tech`
- Detail: Tech 244 - Heavy Demolition Ship

Building: Dock

<a id="symbol-ri-heavy-plow"></a>

## `ri-heavy-plow`

- Kind: `tech`
- Detail: Tech 13 - Heavy Plow

Building: Mill

<a id="symbol-ri-heavy-scorpion"></a>

## `ri-heavy-scorpion`

- Kind: `tech`
- Detail: Tech 239 - Heavy Scorpion

Building: Siege Workshop

<a id="symbol-ri-heresy"></a>

## `ri-heresy`

- Kind: `tech`
- Detail: Tech 439 - Heresy

Building: Monastery

<a id="symbol-ri-hill-forts"></a>

## `ri-hill-forts`

- Kind: `tech`
- Detail: Tech 691 - Hill Forts

Building: Castle

Civilization: Lithuanians

<a id="symbol-ri-hoardings"></a>

## `ri-hoardings`

- Kind: `tech`
- Detail: Tech 379 - Hoardings

Building: Castle

<a id="symbol-ri-horse-collar"></a>

## `ri-horse-collar`

- Kind: `tech`
- Detail: Tech 14 - Horse Collar

Building: Mill

<a id="symbol-ri-houfnice"></a>

## `ri-houfnice`

- Kind: `tech`
- Detail: Tech 787 - Houfnice

Building: Siege Workshop

Civilization: Bohemians

<a id="symbol-ri-howdah"></a>

## `ri-howdah`

- Kind: `tech`
- Detail: Tech 626 - Howdah

Building: Castle

Civilization: Burmese

<a id="symbol-ri-husbandry"></a>

## `ri-husbandry`

- Kind: `tech`
- Detail: Tech 39 - Husbandry

Building: Stable

<a id="symbol-ri-hussar"></a>

## `ri-hussar`

- Kind: `tech`
- Detail: Tech 428 - Hussar

Building: Stable

<a id="symbol-ri-hussite-reforms"></a>

## `ri-hussite-reforms`

- Kind: `tech`
- Detail: Tech 785 - Hussite Reforms

Building: Castle

Civilization: Bohemians

<a id="symbol-ri-illumination"></a>

## `ri-illumination`

- Kind: `tech`
- Detail: Tech 233 - Illumination

Building: Monastery

<a id="symbol-ri-imperial-camel-rider"></a>

## `ri-imperial-camel-rider`

- Kind: `tech`
- Detail: Tech 521 - Imperial Camel [Rider]

Building: Stable

Civilization: Hindustanis/Indians

<a id="symbol-ri-imperial-skirmisher"></a>

## `ri-imperial-skirmisher`

- Kind: `tech`
- Detail: Tech 655 - Imperial Skirmisher

Building: Archery Range

Civilization: Vietnamese

<a id="symbol-ri-inquisition"></a>

## `ri-inquisition`

- Kind: `tech`
- Detail: Tech 492 - Inquisition

Building: Castle

Civilization: Spanish

<a id="symbol-ri-iron-casting"></a>

## `ri-iron-casting`

- Kind: `tech`
- Detail: Tech 68 - Iron Casting

Building: Blacksmith

<a id="symbol-ri-ironclad"></a>

## `ri-ironclad`

- Kind: `tech`
- Detail: Tech 489 - Ironclad

Building: Castle

Civilization: Teutons

<a id="symbol-ri-kamandaran"></a>

## `ri-kamandaran`

- Kind: `tech`
- Detail: Tech 488 - Kamandaran

Building: Castle

Civilization: Persians

<a id="symbol-ri-kasbah"></a>

## `ri-kasbah`

- Kind: `tech`
- Detail: Tech 578 - Kasbah

Building: Castle

Civilization: Berbers

<a id="symbol-ri-keep"></a>

## `ri-keep`

- Kind: `tech`
- Detail: Tech 63 - Keep

Building: University

<a id="symbol-ri-kshatriyas"></a>

## `ri-kshatriyas`

- Kind: `tech`
- Detail: Tech 835 - Kshatriyas

Building: Castle

Civilization: Gurjaras

<a id="symbol-ri-lamellar-armor"></a>

## `ri-lamellar-armor`

- Kind: `tech`
- Detail: Tech 1006 - Lamellar Armor

Building: Castle

Civilization: Khitans

<a id="symbol-ri-leather-archer-armor"></a>

## `ri-leather-archer-armor`

- Kind: `tech`
- Detail: Tech 212 - Leather Archer Armor

Building: Blacksmith

<a id="symbol-ri-lechitic-legacy"></a>

## `ri-lechitic-legacy`

- Kind: `tech`
- Detail: Tech 783 - Lechitic Legacy

Building: Castle

Civilization: Poles

<a id="symbol-ri-legionary"></a>

## `ri-legionary`

- Kind: `tech`
- Detail: Tech 885 - Legionary

Building: Barracks

Civilization: Romans

<a id="symbol-ri-light-cavalry"></a>

## `ri-light-cavalry`

- Kind: `tech`
- Detail: Tech 254 - Light Cavalry

Building: Stable

<a id="symbol-ri-long-swordsman"></a>

## `ri-long-swordsman`

- Kind: `tech`
- Detail: Tech 207 - Long Swordsman

Building: Barracks

<a id="symbol-ri-loom"></a>

## `ri-loom`

- Kind: `tech`
- Detail: Tech 22 - Loom

Building: Town Center

<a id="symbol-ri-maghrebi-camels"></a>

## `ri-maghrebi-camels`

- Kind: `tech`
- Detail: Tech 579 - Maghrebi Camels

Building: Castle

Civilization: Berbers

<a id="symbol-ri-mahayana"></a>

## `ri-mahayana`

- Kind: `tech`
- Detail: Tech 834 - Mahayana

Building: Castle

Civilization: Bengalis

<a id="symbol-ri-man-at-arms"></a>

## `ri-man-at-arms`

- Kind: `tech`
- Detail: Tech 222 - Man-at-Arms

Building: Barracks

<a id="symbol-ri-manipur-cavalry"></a>

## `ri-manipur-cavalry`

- Kind: `tech`
- Detail: Tech 627 - Manipur Cavalry

Building: Castle

Civilization: Burmese

<a id="symbol-ri-marauders"></a>

## `ri-marauders`

- Kind: `tech`
- Detail: Tech 483 - Marauders

Building: Castle

Civilization: Huns

<a id="symbol-ri-masonry"></a>

## `ri-masonry`

- Kind: `tech`
- Detail: Tech 50 - Masonry

Building: University

<a id="symbol-ri-medical-corps"></a>

## `ri-medical-corps`

- Kind: `tech`
- Detail: Tech 831 - Medical Corps

Building: Castle

Civilization: Dravidians

<a id="symbol-ri-ming-guang-armor"></a>

## `ri-ming-guang-armor`

- Kind: `tech`
- Detail: Tech 1062 - Ming Guang Armor

Building: Castle

Civilization: Wei

<a id="symbol-ri-murder-holes"></a>

## `ri-murder-holes`

- Kind: `tech`
- Detail: Tech 322 - Murder Holes

Building: University

<a id="symbol-ri-nomads"></a>

## `ri-nomads`

- Kind: `tech`
- Detail: Tech 487 - Nomads

Building: Castle

Civilization: Mongols

<a id="symbol-ri-onager"></a>

## `ri-onager`

- Kind: `tech`
- Detail: Tech 257 - Onager

Building: Siege Workshop

<a id="symbol-ri-ordo-cavalry"></a>

## `ri-ordo-cavalry`

- Kind: `tech`
- Detail: Tech 1007 - Ordo Cavalry

Building: Castle

Civilization: Khitans

<a id="symbol-ri-padded-archer-armor"></a>

## `ri-padded-archer-armor`

- Kind: `tech`
- Detail: Tech 211 - Padded Archer Armor

Building: Blacksmith

<a id="symbol-ri-paiks"></a>

## `ri-paiks`

- Kind: `tech`
- Detail: Tech 833 - Paiks

Building: Castle

Civilization: Bengalis

<a id="symbol-ri-paladin"></a>

## `ri-paladin`

- Kind: `tech`
- Detail: Tech 265 - Paladin

Building: Stable

<a id="symbol-ri-paper-money"></a>

## `ri-paper-money`

- Kind: `tech`
- Detail: Tech 629 - Paper Money

Building: Castle

Civilization: Vietnamese

<a id="symbol-ri-parthian-tactics"></a>

## `ri-parthian-tactics`

- Kind: `tech`
- Detail: Tech 436 - Parthian Tactics

Building: Archery Range

<a id="symbol-ri-pavise"></a>

## `ri-pavise`

- Kind: `tech`
- Detail: Tech 494 - Pavise

Building: Castle

Civilization: Italians

<a id="symbol-ri-pikeman"></a>

## `ri-pikeman`

- Kind: `tech`
- Detail: Tech 197 - Pikeman

Building: Barracks

<a id="symbol-ri-plate-barding"></a>

## `ri-plate-barding`

- Kind: `tech`
- Detail: Tech 80 - Plate Barding Armor

Building: Blacksmith

<a id="symbol-ri-plate-mail"></a>

## `ri-plate-mail`

- Kind: `tech`
- Detail: Tech 77 - Plate Mail Armor

Building: Blacksmith

<a id="symbol-ri-recurve-bow"></a>

## `ri-recurve-bow`

- Kind: `tech`
- Detail: Tech 515 - Recurve Bow

Building: Castle

Civilization: Magyars

<a id="symbol-ri-red-cliffs-tactics"></a>

## `ri-red-cliffs-tactics`

- Kind: `tech`
- Detail: Tech 1080 - Red Cliffs Tactics

Building: Castle

Civilization: Wu

<a id="symbol-ri-redemption"></a>

## `ri-redemption`

- Kind: `tech`
- Detail: Tech 316 - Redemption

Building: Monastery

<a id="symbol-ri-ring-archer-armor"></a>

## `ri-ring-archer-armor`

- Kind: `tech`
- Detail: Tech 219 - Ring Archer Armor

Building: Blacksmith

<a id="symbol-ri-royal-heirs"></a>

## `ri-royal-heirs`

- Kind: `tech`
- Detail: Tech 574 - Royal Heirs

Building: Castle

Civilization: Ethiopians

<a id="symbol-ri-sanctity"></a>

## `ri-sanctity`

- Kind: `tech`
- Detail: Tech 231 - Sanctity

Building: Monastery

<a id="symbol-ri-sappers"></a>

## `ri-sappers`

- Kind: `tech`
- Detail: Tech 321 - Sappers

Building: Castle

<a id="symbol-ri-savar"></a>

## `ri-savar`

- Kind: `tech`
- Detail: Tech 526 - Savar

Building: Stable

Civilization: Persians

<a id="symbol-ri-scale-barding"></a>

## `ri-scale-barding`

- Kind: `tech`
- Detail: Tech 81 - Scale Barding Armor

Building: Blacksmith

<a id="symbol-ri-scale-mail"></a>

## `ri-scale-mail`

- Kind: `tech`
- Detail: Tech 74 - Scale Mail Armor

Building: Blacksmith

<a id="symbol-ri-shatagni"></a>

## `ri-shatagni`

- Kind: `tech`
- Detail: Tech 507 - Shatagni

Building: Castle

Civilization: Hindustanis

<a id="symbol-ri-shipwright"></a>

## `ri-shipwright`

- Kind: `tech`
- Detail: Tech 373 - Shipwright

Building: University

<a id="symbol-ri-siege-elephant"></a>

## `ri-siege-elephant`

- Kind: `tech`
- Detail: Tech 838 - Siege Elephant

Building: Siege Workshop

<a id="symbol-ri-siege-engineers"></a>

## `ri-siege-engineers`

- Kind: `tech`
- Detail: Tech 377 - Siege Engineers

Building: University

<a id="symbol-ri-siege-onager"></a>

## `ri-siege-onager`

- Kind: `tech`
- Detail: Tech 320 - Siege Onager

Building: Siege Workshop

<a id="symbol-ri-siege-ram"></a>

## `ri-siege-ram`

- Kind: `tech`
- Detail: Tech 255 - Siege Ram

Building: Siege Workshop

<a id="symbol-ri-silk-armor"></a>

## `ri-silk-armor`

- Kind: `tech`
- Detail: Tech 687 - Silk Armor

Building: Castle

Civilization: Tatars

<a id="symbol-ri-silk-road"></a>

## `ri-silk-road`

- Kind: `tech`
- Detail: Tech 499 - Silk Road

Building: Castle

Civilization: Italians

<a id="symbol-ri-sipahi"></a>

## `ri-sipahi`

- Kind: `tech`
- Detail: Tech 491 - Sipahi

Building: Castle

Civilization: Turks

<a id="symbol-ri-sitting-tiger"></a>

## `ri-sitting-tiger`

- Kind: `tech`
- Detail: Tech 1081 - Sitting Tiger

Building: Castle

Civilization: Wu

<a id="symbol-ri-squires"></a>

## `ri-squires`

- Kind: `tech`
- Detail: Tech 215 - Squires

Building: Barracks

<a id="symbol-ri-steppe-husbandry"></a>

## `ri-steppe-husbandry`

- Kind: `tech`
- Detail: Tech 689 - Steppe Husbandry

Building: Castle

Civilization: Cumans

<a id="symbol-ri-stirrups"></a>

## `ri-stirrups`

- Kind: `tech`
- Detail: Tech 685 - Stirrups

Building: Castle

Civilization: Bulgarians

<a id="symbol-ri-stone-mining"></a>

## `ri-stone-mining`

- Kind: `tech`
- Detail: Tech 278 - Stone Mining

Building: Mining Camp

<a id="symbol-ri-stone-shaft-mining"></a>

## `ri-stone-shaft-mining`

- Kind: `tech`
- Detail: Tech 279 - Stone Shaft Mining

Building: Mining Camp

<a id="symbol-ri-stonecutting"></a>

## `ri-stonecutting`

- Kind: `tech`
- Detail: Tech 54 - Treadmill Crane

Building: University

<a id="symbol-ri-stronghold"></a>

## `ri-stronghold`

- Kind: `tech`
- Detail: Tech 482 - Stronghold

Building: Castle

Civilization: Celts

<a id="symbol-ri-svan-towers"></a>

## `ri-svan-towers`

- Kind: `tech`
- Detail: Tech 923 - Svan Towers

Building: Castle

Civilization: Georgians

<a id="symbol-ri-szlachta-privileges"></a>

## `ri-szlachta-privileges`

- Kind: `tech`
- Detail: Tech 782 - Szlachta Privileges

Building: Castle

Civilization: Poles

<a id="symbol-ri-thalassocracy"></a>

## `ri-thalassocracy`

- Kind: `tech`
- Detail: Tech 624 - Thalassocracy

Building: Castle

Civilization: Malay

<a id="symbol-ri-theocracy"></a>

## `ri-theocracy`

- Kind: `tech`
- Detail: Tech 438 - Theocracy

Building: Monastery

<a id="symbol-ri-thumb-ring"></a>

## `ri-thumb-ring`

- Kind: `tech`
- Detail: Tech 437 - Thumb Ring

Building: Archery Range

<a id="symbol-ri-thunderclap-bombs"></a>

## `ri-thunderclap-bombs`

- Kind: `tech`
- Detail: Tech 997 - Thunderclap Bombs

Building: Castle

Civilization: Jurchens

<a id="symbol-ri-tigui"></a>

## `ri-tigui`

- Kind: `tech`
- Detail: Tech 576 - Tigui

Building: Castle

Civilization: Malians

<a id="symbol-ri-timurid-siegecraft"></a>

## `ri-timurid-siegecraft`

- Kind: `tech`
- Detail: Tech 688 - Timurid Siegecraft

Building: Castle

Civilization: Tatars

<a id="symbol-ri-torsion"></a>

## `ri-torsion`

- Kind: `tech`
- Detail: Tech 575 - Torsion Engines

Building: Castle

Civilization: Ethiopians

<a id="symbol-ri-torsion-engines"></a>

## `ri-torsion-engines`

- Kind: `tech`
- Detail: Tech 575 - Torsion Engines

Building: Castle

Civilization: Ethiopians

<a id="symbol-ri-tower-shields"></a>

## `ri-tower-shields`

- Kind: `tech`
- Detail: Tech 692 - Tower Shields

Building: Castle

Civilization: Lithuanians

<a id="symbol-ri-town-patrol"></a>

## `ri-town-patrol`

- Kind: `tech`
- Detail: Tech 280 - Town Patrol

Building: Town Center

<a id="symbol-ri-town-watch"></a>

## `ri-town-watch`

- Kind: `tech`
- Detail: Tech 8 - Town Watch

Building: Town Center

<a id="symbol-ri-treadmill-crane"></a>

## `ri-treadmill-crane`

- Kind: `tech`
- Detail: Tech 54 - Treadmill Crane

Building: University

<a id="symbol-ri-tuntian"></a>

## `ri-tuntian`

- Kind: `tech`
- Detail: Tech 1061 - Tuntian

Building: Castle

Civilization: Wei

<a id="symbol-ri-tusk-swords"></a>

## `ri-tusk-swords`

- Kind: `tech`
- Detail: Tech 622 - Tusk Swords

Building: Castle

Civilization: Khmer

<a id="symbol-ri-two-handed-swordsman"></a>

## `ri-two-handed-swordsman`

- Kind: `tech`
- Detail: Tech 217 - Two-Handed Swordsman

Building: Barracks

<a id="symbol-ri-two-man-saw"></a>

## `ri-two-man-saw`

- Kind: `tech`
- Detail: Tech 221 - Two-Man Saw

Building: Lumber Camp

<a id="symbol-ri-wagenburg-tactics"></a>

## `ri-wagenburg-tactics`

- Kind: `tech`
- Detail: Tech 784 - Wagenburg Tactics

Building: Castle

Civilization: Bohemians

<a id="symbol-ri-war-galley"></a>

## `ri-war-galley`

- Kind: `tech`
- Detail: Tech 34 - Medium Warships

Building: Dock

<a id="symbol-ri-warwolf"></a>

## `ri-warwolf`

- Kind: `tech`
- Detail: Tech 461 - Warwolf

Building: Castle

Civilization: Britons

<a id="symbol-ri-wheel-barrow"></a>

## `ri-wheel-barrow`

- Kind: `tech`
- Detail: Tech 213 - Wheelbarrow

Building: Town Center

<a id="symbol-ri-winged-hussar"></a>

## `ri-winged-hussar`

- Kind: `tech`
- Detail: Tech 786 - Winged Hussar

Building: Stable

<a id="symbol-ri-wootz-steel"></a>

## `ri-wootz-steel`

- Kind: `tech`
- Detail: Tech 832 - Wootz Steel

Building: Castle

Civilization: Dravidians

<a id="symbol-ri-yasama"></a>

## `ri-yasama`

- Kind: `tech`
- Detail: Tech 484 - Yasama

Building: Castle

Civilization: Japanese

<a id="section-value"></a>

# value

<a id="symbol--1"></a>

## `-1`

- Kind: `value`
- Detail: ActionId value

Use -1 to ignore the ActionId of the object.

Id: `-1`

<a id="symbol--ally-id-0-description-ally-"></a>

## `"ally", // id: 0, // description: "Ally." //`

- Kind: `value`
- Detail: ESPlayerStance value

<a id="symbol--any-computer-ally-id--103-description-any-computer-ally-"></a>

## `"any-computer-ally", // id: -103, // description: "Any computer ally." //`

- Kind: `value`
- Detail: ComputerAllyPlayer value

<a id="symbol--enemy-id-3-description-enemy-"></a>

## `"enemy", // id: 3, // description: "Enemy." //`

- Kind: `value`
- Detail: ESPlayerStance value

<a id="symbol--neutral-id-1-description-neutral-"></a>

## `"neutral", // id: 1, // description: "Neutral." //`

- Kind: `value`
- Detail: ESPlayerStance value

<a id="symbol-ability-to-dodge-missiles"></a>

## `ability-to-dodge-missiles`

- Kind: `value`
- Detail: DiffParameterId value

Chance of a computer player's unit dodging a missile. Range is 0-100, and the values are opposite from what you'd expect! When set to 0, units will try to dodge immediately upon seeing a projectile in the air. When set to 100, they have to...

Id: `1`

<a id="symbol-ability-to-maintain-distance"></a>

## `ability-to-maintain-distance`

- Kind: `value`
- Detail: DiffParameterId value

Chance that a computer player's ranged unit will maintain the distance. Range is 0-100, and the values are opposite from what you'd expect! When set to 0, ranged units will frequently move back to maintain distance. When set to 100, ranged...

Id: `0`

<a id="symbol-acclivity"></a>

## `acclivity`

- Kind: `value`
- Detail: MapType value

Acclivity map.

Id: `157`

<a id="symbol-achaemenids"></a>

## `achaemenids`

- Kind: `value`
- Detail: Civ value

Achaemenids (must define with a defconst first).

Id: `46`

<a id="symbol-acropolis"></a>

## `acropolis`

- Kind: `value`
- Detail: MapType value

Acropolis map.

Id: `67`

<a id="symbol-action-attack-move"></a>

## `action-attack-move`

- Kind: `value`
- Detail: DUCAction value

Must be defined with a defconst. Only available in DE. Units in the local list will attack move to the point or the location of the target object(s).

Id: `19`

<a id="symbol-action-default"></a>

## `action-default`

- Kind: `value`
- Detail: DUCAction value

Equivalent of a right-click for all objects in the local list on the point or target object(s). For up-target-point this is the same as action-move.

Id: `0`

<a id="symbol-action-delete"></a>

## `action-delete`

- Kind: `value`
- Detail: DUCAction value

Deletable objects in the local list will be deleted.

Id: `8`

<a id="symbol-action-drop-relic"></a>

## `action-drop-relic`

- Kind: `value`
- Detail: DUCAction value

Monastery units in the local list will drop any relics they are carrying. For up-target-objects this is the same as action-none.

Id: `15`

<a id="symbol-action-follow"></a>

## `action-follow`

- Kind: `value`
- Detail: DUCAction value

Units in the local list will follow the target object(s). For up-target-point this is the same as action-move.

Id: `4`

<a id="symbol-action-garrison"></a>

## `action-garrison`

- Kind: `value`
- Detail: DUCAction value

Units in the local list will garrison inside the target object(s). For up-target-point this is the same as action-move.

Id: `7`

<a id="symbol-action-gather"></a>

## `action-gather`

- Kind: `value`
- Detail: DUCAction value

Buildings in the local list will set their gather point at the target point or at the location of the target object(s).

Id: `11`

<a id="symbol-action-ground"></a>

## `action-ground`

- Kind: `value`
- Detail: DUCAction value

Units in the local list will attack ground at the point or against the target object(s).

Id: `6`

<a id="symbol-action-guard"></a>

## `action-guard`

- Kind: `value`
- Detail: DUCAction value

Units in the local list will guard the target object(s). For up-target-point this is the same as action-move.

Id: `3`

<a id="symbol-action-lock"></a>

## `action-lock`

- Kind: `value`
- Detail: DUCAction value

Gates in the local list will toggle their locked state. If they are locked, they will unlock. If they are unlocked, they will lock. For up-target-objects this is the same as action-none.

Id: `12`

<a id="symbol-action-move"></a>

## `action-move`

- Kind: `value`
- Detail: DUCAction value

Units in the local list will move to the point or the location of the target object(s).

Id: `1`

<a id="symbol-action-none"></a>

## `action-none`

- Kind: `value`
- Detail: DUCAction value

The current actions of the objects in the local list will not change.

Id: `18`

<a id="symbol-action-pack"></a>

## `action-pack`

- Kind: `value`
- Detail: DUCAction value

Trebuchets in the local list will pack. For up-target-objects this is the same as action-none.

Id: `16`

<a id="symbol-action-patrol"></a>

## `action-patrol`

- Kind: `value`
- Detail: DUCAction value

Units in the local list will patrol to the point or the location of the target object(s).

Id: `2`

<a id="symbol-action-research"></a>

## `action-research`

- Kind: `value`
- Detail: DUCAction value

Must be defined with a defconst. Only available in DE. Researches a tech at a building in the local list. Use this syntax: (up-target-point EscrowGoalId action-research typeOp TypeId). Example: (up-target-point 0 action-research c: ri-loom...

Id: `21`

<a id="symbol-action-stop"></a>

## `action-stop`

- Kind: `value`
- Detail: DUCAction value

Objects in the local list will stop their current action.

Id: `5`

<a id="symbol-action-train"></a>

## `action-train`

- Kind: `value`
- Detail: DUCAction value

Buildings in the local list will train units. To train units, use this syntax: (up-target-point EscrowGoalId action-train typeOp TypeId). Example: (up-target-point 0 action-train c: spearman-line). For up-target-objects this is the same as...

Id: `10`

<a id="symbol-action-transform"></a>

## `action-transform`

- Kind: `value`
- Detail: DUCAction value

Must be defined with a defconst. Only available in DE. Rathas in the local list will switch between melee and ranged mode.

Id: `20`

<a id="symbol-action-ungarrison"></a>

## `action-ungarrison`

- Kind: `value`
- Detail: DUCAction value

Units in the local list will be ungarrisoned from the building they are garrisoned inside. For up-target-objects this is the same as action-none.

Id: `14`

<a id="symbol-action-unload"></a>

## `action-unload`

- Kind: `value`
- Detail: DUCAction value

Buildings in the local list will ungarrison to the target point. Siege (class 913) in the local list will eject in place. Transport ships in the local list will unload at the target point. For up-target-objects this is the same as action-n...

Id: `9`

<a id="symbol-action-unpack"></a>

## `action-unpack`

- Kind: `value`
- Detail: DUCAction value

Trebuchets in the local list will unpack. For up-target-objects this is the same as action-none.

Id: `17`

<a id="symbol-action-work"></a>

## `action-work`

- Kind: `value`
- Detail: DUCAction value

Buildings in the local list will send garrisoned villagers back to work. Same as clicking the Send Back to Work button. For up-target-objects this is the same as action-none.

Id: `13`

<a id="symbol-actionid-attack"></a>

## `actionid-attack`

- Kind: `value`
- Detail: ActionId value

The object is attacking.

Id: `600`

<a id="symbol-actionid-build"></a>

## `actionid-build`

- Kind: `value`
- Detail: ActionId value

The villager or fishing ship is building.

Id: `602`

<a id="symbol-actionid-convert"></a>

## `actionid-convert`

- Kind: `value`
- Detail: ActionId value

The monk or missionary is converting

Id: `604`

<a id="symbol-actionid-defend"></a>

## `actionid-defend`

- Kind: `value`
- Detail: ActionId value

The unit is defending. According to scripter64, this is hard to detect, because it quickly changes to other actions like actionid-move.

Id: `601`

<a id="symbol-actionid-enter"></a>

## `actionid-enter`

- Kind: `value`
- Detail: ActionId value

A unit that is garrisoning inside a building, ram, or a transport ship. It may also include objects that are currently garrisoned.

Id: `617`

<a id="symbol-actionid-evade"></a>

## `actionid-evade`

- Kind: `value`
- Detail: ActionId value

Could be units dodging missiles because of dpAbilityToDodgeMissiles.

Id: `616`

<a id="symbol-actionid-explore"></a>

## `actionid-explore`

- Kind: `value`
- Detail: ActionId value

A unit is exploring.

Id: `605`

<a id="symbol-actionid-follow"></a>

## `actionid-follow`

- Kind: `value`
- Detail: ActionId value

A unit that is following.

Id: `612`

<a id="symbol-actionid-gather"></a>

## `actionid-gather`

- Kind: `value`
- Detail: ActionId value

Likely a building setting a gather point.

Id: `609`

<a id="symbol-actionid-heal"></a>

## `actionid-heal`

- Kind: `value`
- Detail: ActionId value

The monk or missionary is healing.

Id: `603`

<a id="symbol-actionid-hunt"></a>

## `actionid-hunt`

- Kind: `value`
- Detail: ActionId value

A villager that is hunting. Untested if this also includes attacking wolves.

Id: `613`

<a id="symbol-actionid-move"></a>

## `actionid-move`

- Kind: `value`
- Detail: ActionId value

A unit that is moving.

Id: `610`

<a id="symbol-actionid-patrol"></a>

## `actionid-patrol`

- Kind: `value`
- Detail: ActionId value

A unit that is patrolling.

Id: `611`

<a id="symbol-actionid-relic"></a>

## `actionid-relic`

- Kind: `value`
- Detail: ActionId value

A monk trying to pick up a relic.

Id: `631`

<a id="symbol-actionid-repair"></a>

## `actionid-repair`

- Kind: `value`
- Detail: ActionId value

A villager that is repairing a building.

Id: `618`

<a id="symbol-actionid-research"></a>

## `actionid-research`

- Kind: `value`
- Detail: ActionId value

A building that is researching a technology.

Id: `620`

<a id="symbol-actionid-retreat"></a>

## `actionid-retreat`

- Kind: `value`
- Detail: ActionId value

Unknown. Probably either retreating during a up-retreat-now or up-retreat-to command, or retreating because of minimum range or dpAbilityToMaintainDistance.

Id: `608`

<a id="symbol-actionid-runaway"></a>

## `actionid-runaway`

- Kind: `value`
- Detail: ActionId value

Unknown? Could be non-combat units trying to get away from soldiers attacking them.

Id: `607`

<a id="symbol-actionid-stop"></a>

## `actionid-stop`

- Kind: `value`
- Detail: ActionId value

A unit is stopping its action.

Id: `606`

<a id="symbol-actionid-trade"></a>

## `actionid-trade`

- Kind: `value`
- Detail: ActionId value

A trade unit that is trading.

Id: `615`

<a id="symbol-actionid-train"></a>

## `actionid-train`

- Kind: `value`
- Detail: ActionId value

A building that is training a unit.

Id: `619`

<a id="symbol-actionid-transport"></a>

## `actionid-transport`

- Kind: `value`
- Detail: ActionId value

A transport ship that is transporting units. Might also include transport ships that are on their way to picking up units.

Id: `614`

<a id="symbol-actionid-unload"></a>

## `actionid-unload`

- Kind: `value`
- Detail: ActionId value

A transport ship that is unloading units.

Id: `621`

<a id="symbol-african-clearing"></a>

## `african-clearing`

- Kind: `value`
- Detail: MapType value

African Clearing map.

Id: `149`

<a id="symbol-aftermath"></a>

## `aftermath`

- Kind: `value`
- Detail: MapType value

Aftermath map.

Id: `168`

<a id="symbol-all-units-class"></a>

## `all-units-class`

- Kind: `value`
- Detail: ClassId value

All Units class. Counts all objects, including buildings.

Id: `-1`

<a id="symbol-allied-goal"></a>

## `allied-goal`

- Kind: `value`
- Detail: FactId value

The current value of an allied AI player's goal variable. The corresponding fact command is up-allied-goal.

Id: `36`

<a id="symbol-allied-sn"></a>

## `allied-sn`

- Kind: `value`
- Detail: FactId value

The current value of an allied AI player's strategic number. The corresponding fact command is up-allied-sn.

Id: `37`

<a id="symbol-ally"></a>

## `ally`

- Kind: `value`
- Detail: PlayerStance value

Ally.

Id: `0`

<a id="symbol-alpine-lakes"></a>

## `alpine-lakes`

- Kind: `value`
- Detail: MapType value

Alpine Lakes map. Must be defined with a defconst.

Id: `122`

<a id="symbol-amazon-tunnel"></a>

## `amazon-tunnel`

- Kind: `value`
- Detail: MapType value

Amazon Tunnel map.

Id: `147`

<a id="symbol-amount-all-techs-achieved"></a>

## `amount-all-techs-achieved`

- Kind: `value`
- Detail: ResourceType value

Likely set to 1 when an All Techs game is played or all techs have been researched.

Id: `39`

<a id="symbol-amount-allow-formations"></a>

## `amount-allow-formations`

- Kind: `value`
- Detail: ResourceType value

Likely either always 1 to allow formations at all, or it's 0 or 1 depending on the object.

Id: `66`

<a id="symbol-amount-berries"></a>

## `amount-berries`

- Kind: `value`
- Detail: ResourceType value

Unknown. This does not apply to forage bushes or fruit bushes.

Id: `16`

<a id="symbol-amount-berserker-heal-timer"></a>

## `amount-berserker-heal-timer`

- Kind: `value`
- Detail: ResourceType value

Set to 1 for Khmer so that farmers no longer need to drop off food from farms. Used to be for controlling berserk HP regeneration. The resource hasn't been renamed in the AI engine.

Id: `96`

<a id="symbol-amount-boarding-recharge-rate"></a>

## `amount-boarding-recharge-rate`

- Kind: `value`
- Detail: ResourceType value

Similar to monk faith regeneration, resource 35. This applies to the hidden boarding galley unit that would convert ships from 1 range away. Boarding galleys can be used in custom scenarios if a mod unhides the unit in the scenario editor,...

Id: `83`

<a id="symbol-amount-building-housing-rate"></a>

## `amount-building-housing-rate`

- Kind: `value`
- Detail: ResourceType value

Unknown.

Id: `62`

<a id="symbol-amount-building-id"></a>

## `amount-building-id`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. The ID of the building that the folwark needs to upgrade from for the farm collection ability to work. Set to 68 (mill) for Poles.

Id: `239`

<a id="symbol-amount-building-limit"></a>

## `amount-building-limit`

- Kind: `value`
- Detail: ResourceType value

Unused.

Id: `30`

<a id="symbol-amount-building-repair-cost"></a>

## `amount-building-repair-cost`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. The percentage of cost required to repair buildings. Set to 0.5 by default. Affected by Georgians team bonus.

Id: `271`

<a id="symbol-amount-buildings-value-total"></a>

## `amount-buildings-value-total`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. The total cost of all buildings constructed so far. This does not decrease when buildings are destroyed.

Id: `247`

<a id="symbol-amount-can-convert"></a>

## `amount-can-convert`

- Kind: `value`
- Detail: ResourceType value

Set to 1 if conversion has been enabled for the player. Dark Age is the prerequisite, so it should always be 1 except in scenarios where Dark Age has been disabled specifically to disable conversion.

Id: `67`

<a id="symbol-amount-captured-unit"></a>

## `amount-captured-unit`

- Kind: `value`
- Detail: ResourceType value

Unknown. Could be related to the slaver mechanic that didn't make it into the game.

Id: `57`

<a id="symbol-amount-castle"></a>

## `amount-castle`

- Kind: `value`
- Detail: ResourceType value

Likely the number of player's castles currently standing. Probably isn't equal to Total Castles on the achievements screen. This is likely Resource 173 instead.

Id: `134`

<a id="symbol-amount-cavalry-kill-reward"></a>

## `amount-cavalry-kill-reward`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. This resource effectively sets the gold generation rate per second by cavalry fighting other military units. Used to be used by Persians.

Id: `284`

<a id="symbol-amount-chopping-gold-productivity"></a>

## `amount-chopping-gold-productivity`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. Gold production while lumberjacks chop wood per 100 seconds. Affected by Paper Money.

Id: `266`

<a id="symbol-amount-civ-name-override"></a>

## `amount-civ-name-override`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. Unknown.

Id: `262`

<a id="symbol-amount-civilian-population"></a>

## `amount-civilian-population`

- Kind: `value`
- Detail: ResourceType value

The civilian population. Might be equal to Villager High in the achievements screen.

Id: `37`

<a id="symbol-amount-construction-rate-mod"></a>

## `amount-construction-rate-mod`

- Kind: `value`
- Detail: ResourceType value

Modifies the construction rate of buildings. Used by the Spanish.

Id: `195`

<a id="symbol-amount-conversions"></a>

## `amount-conversions`

- Kind: `value`
- Detail: ResourceType value

Likely equal to Units Converted in the achievements screen.

Id: `41`

<a id="symbol-amount-convert-boats"></a>

## `amount-convert-boats`

- Kind: `value`
- Detail: ResourceType value

Likely similar to resource 67, but enables boat conversion for boarding galleys. See resource 83. Could also simply allow the conversion of ships by monastery units. Is set to 1 from the start of the game.

Id: `87`

<a id="symbol-amount-convert-building"></a>

## `amount-convert-building`

- Kind: `value`
- Detail: ResourceType value

Set to 1 when Redemption is researched. If higher than 1, monks can convert buildings from range.

Id: `28`

<a id="symbol-amount-convert-building-chance"></a>

## `amount-convert-building-chance`

- Kind: `value`
- Detail: ResourceType value

The percent chance a monastery unit will successfully convert a unit each second within the minimum and maximum conversion times for the object. Default is 25%. Inquisition increases this resource to 5.

Id: `182`

<a id="symbol-amount-convert-building-max"></a>

## `amount-convert-building-max`

- Kind: `value`
- Detail: ResourceType value

An adjustment to the maximum amount of time a monastery unit must spend converting buildings. After this time, the building will automatically be converted. Inquisition sets this to -5.

Id: `181`

<a id="symbol-amount-convert-building-min"></a>

## `amount-convert-building-min`

- Kind: `value`
- Detail: ResourceType value

An adjustment to the minimum amount of time a monastery unit must spend converting before a building will be converted. Inquisition sets this to -5.

Id: `180`

<a id="symbol-amount-convert-max-adj"></a>

## `amount-convert-max-adj`

- Kind: `value`
- Detail: ResourceType value

An adjustment to the maximum amount of time a monastery unit must spend converting units. After this time, the unit will automatically be converted. Inquisition sets this to -1.

Id: `177`

<a id="symbol-amount-convert-min-adj"></a>

## `amount-convert-min-adj`

- Kind: `value`
- Detail: ResourceType value

An adjustment to the minimum amount of time a monastery unit must spend converting before a unit will be converted. Inquisition sets this to -1.

Id: `176`

<a id="symbol-amount-convert-priest"></a>

## `amount-convert-priest`

- Kind: `value`
- Detail: ResourceType value

Set to 1 when Atonement is researched.

Id: `27`

<a id="symbol-amount-convert-resist-max-adj"></a>

## `amount-convert-resist-max-adj`

- Kind: `value`
- Detail: ResourceType value

An adjustment to the conversion resistance of units. Likely adjusts the maximum amount of time monastery units must spend converting these units. After this time, the unit will automatically be converted. Used by Faith, Devotion, and the T...

Id: `179`

<a id="symbol-amount-convert-resist-min-adj"></a>

## `amount-convert-resist-min-adj`

- Kind: `value`
- Detail: ResourceType value

An adjustment to the conversion resistance of units. Likely adjusts the minimum amount of time monastery units must spend converting these units before they will be converted. Used by Faith, Devotion, and the Teutons team bonus.

Id: `178`

<a id="symbol-amount-convert-resistance"></a>

## `amount-convert-resistance`

- Kind: `value`
- Detail: ResourceType value

Amount of conversion resistance an object has. Faith increases this by 3. Teutons team bonus increases this by 2.

Id: `77`

<a id="symbol-amount-crenellations"></a>

## `amount-crenellations`

- Kind: `value`
- Detail: ResourceType value

Set to 1 when the player researches Crenellations. Probably controls whether garrisoned infantry fire arrows.

Id: `194`

<a id="symbol-amount-current-age"></a>

## `amount-current-age`

- Kind: `value`
- Detail: ResourceType value

Sets the current age. 0 = Dark Age. 1 = Feudal Age, etc.

Id: `6`

<a id="symbol-amount-decay"></a>

## `amount-decay`

- Kind: `value`
- Detail: ResourceType value

The decay time of corpses (and maybe flares too). Once this decay reaches 0, the corpse is removed from the map.

Id: `12`

<a id="symbol-amount-discovery"></a>

## `amount-discovery`

- Kind: `value`
- Detail: ResourceType value

This is likely a holdover resource from AoE1.

Id: `13`

<a id="symbol-amount-dominant-sheep-control"></a>

## `amount-dominant-sheep-control`

- Kind: `value`
- Detail: ResourceType value

The Celtic sheep bonus. Set to 1 for Celts.

Id: `97`

<a id="symbol-amount-elevation-bonus-higher"></a>

## `amount-elevation-bonus-higher`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. The fraction for additional bonus damage dealt from higher elevation. 0.25 for Tatars. Damage that units on higher elevation deal to units on lower elevation is multiplied by 1.25 + amount-elevatio...

Id: `211`

<a id="symbol-amount-elevation-bonus-lower"></a>

## `amount-elevation-bonus-lower`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. The fraction for additional bonus damage dealt from lower elevation. Not used for Tatars. Damage that units on lower elevation deal to units on higher elevation is multiplied by 0.75 + amount-eleva...

Id: `212`

<a id="symbol-amount-elevation-damage-higher"></a>

## `amount-elevation-damage-higher`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. Damage modifier for own units when attacked from higher elevation.

Id: `272`

<a id="symbol-amount-elevation-damage-lower"></a>

## `amount-elevation-damage-lower`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. Damage modifier for own units when attacked from lower elevation. Georgians modifies this by -0.15.

Id: `273`

<a id="symbol-amount-exploration"></a>

## `amount-exploration`

- Kind: `value`
- Detail: ResourceType value

Likely the % Map Explored in the achievements screen.

Id: `22`

<a id="symbol-amount-faith"></a>

## `amount-faith`

- Kind: `value`
- Detail: ResourceType value

Set to 1 when Faith is researched.

Id: `34`

<a id="symbol-amount-faith-recharge-rate"></a>

## `amount-faith-recharge-rate`

- Kind: `value`
- Detail: ResourceType value

Set the faith recharge rate. Affected by Illumination.

Id: `35`

<a id="symbol-amount-farm-food"></a>

## `amount-farm-food`

- Kind: `value`
- Detail: ResourceType value

Set to the amount of food that each farm will hold when constructed. Affected by mill techs.

Id: `36`

<a id="symbol-amount-feitoria-food-productivity"></a>

## `amount-feitoria-food-productivity`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. The amount of food obtained from owning n number of Feitorias is given by n * amount-feitoria-food-productivity * 1.6.

Id: `205`

<a id="symbol-amount-feitoria-gold-productivity"></a>

## `amount-feitoria-gold-productivity`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. The amount of gold obtained from owning n number of Feitorias is given by n * amount-feitoria-gold-productivity * 1.0.

Id: `208`

<a id="symbol-amount-feitoria-stone-productivity"></a>

## `amount-feitoria-stone-productivity`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. The amount of stone obtained from owning n number of Feitorias is given by n * amount-feitoria-stone-productivity * 0.3.

Id: `207`

<a id="symbol-amount-feitoria-wood-productivity"></a>

## `amount-feitoria-wood-productivity`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. The amount of wood obtained from owning n number of Feitorias is given by n * amount-feitoria-wood-productivity * 0.7.

Id: `206`

<a id="symbol-amount-feudal-town-center-limit"></a>

## `amount-feudal-town-center-limit`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. This is the number of extra TCs a player is allowed to build IF TCs are enabled in feudal age. Default is 1. Cumans sets this to 2.

Id: `218`

<a id="symbol-amount-fish"></a>

## `amount-fish`

- Kind: `value`
- Detail: ResourceType value

The amount of food stored in fish and fish traps.

Id: `17`

<a id="symbol-amount-fish-trap-food"></a>

## `amount-fish-trap-food`

- Kind: `value`
- Detail: ResourceType value

The max amount of food that fish traps store, similar to resource 36 for farms.

Id: `88`

<a id="symbol-amount-fishing-productivity"></a>

## `amount-fishing-productivity`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. Mayan bonus for fishing lasting longer.

Id: `219`

<a id="symbol-amount-flemish-militia-pop"></a>

## `amount-flemish-militia-pop`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. Number of alive flemish militia.

Id: `235`

<a id="symbol-amount-folwark-collection-amount"></a>

## `amount-folwark-collection-amount`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. The amount of food immediately collected from farms around a folwark. Affected by mill technologies and civ bonuses.

Id: `237`

<a id="symbol-amount-folwark-collection-type"></a>

## `amount-folwark-collection-type`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. The ID of the resource (0 = food, 1 = wood, 2 = stone, 3 = gold) that is given when a farm is constructed around a folwark. Set to 0 for Poles.

Id: `238`

<a id="symbol-amount-food"></a>

## `amount-food`

- Kind: `value`
- Detail: ResourceType value

The food stockpile. "food" can also be used instead.

Id: `0`

<a id="symbol-amount-food-bonus"></a>

## `amount-food-bonus`

- Kind: `value`
- Detail: ResourceType value

The Mayan bonus for food, where food resources last longer.

Id: `190`

<a id="symbol-amount-food-generation"></a>

## `amount-food-generation`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. Free food trickle rate per minute. Used in Battle Royale.

Id: `230`

<a id="symbol-amount-food-limit"></a>

## `amount-food-limit`

- Kind: `value`
- Detail: ResourceType value

Unused.

Id: `31`

<a id="symbol-amount-food-score"></a>

## `amount-food-score`

- Kind: `value`
- Detail: ResourceType value

Likely the amount of economic score gained from the player's current food stockpile.

Id: `185`

<a id="symbol-amount-food-total"></a>

## `amount-food-total`

- Kind: `value`
- Detail: ResourceType value

The total amount of food gathered, including food from feitorias and food bought at the market. Food from tribute is not included. Food sold at the market is not subtracted from this total.

Id: `166`

<a id="symbol-amount-foraging-wood-productivity"></a>

## `amount-foraging-wood-productivity`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. Wood production while foragers gather food per 100 seconds. Set to 10.4753 for Portuguese.

Id: `267`

<a id="symbol-amount-formations"></a>

## `amount-formations`

- Kind: `value`
- Detail: ResourceType value

Unused.

Id: `61`

<a id="symbol-amount-gaia-kill-value"></a>

## `amount-gaia-kill-value`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. The score value gained for Gaia from killing units, likely used to calculate the military score.

Id: `400`

<a id="symbol-amount-gaia-kills"></a>

## `amount-gaia-kills`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. Amount of units Gaia has killed.

Id: `300`

<a id="symbol-amount-gaia-razing-value"></a>

## `amount-gaia-razing-value`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. The score gained for Gaia from destroying buildings, likely used to calculate military score.

Id: `425`

<a id="symbol-amount-gaia-razings"></a>

## `amount-gaia-razings`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. The amount of buildings Gaia has destroyed.

Id: `350`

<a id="symbol-amount-gaia-tribute"></a>

## `amount-gaia-tribute`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. The total tribute sent by Gaia.

Id: `450`

<a id="symbol-amount-gather-accumulator"></a>

## `amount-gather-accumulator`

- Kind: `value`
- Detail: ResourceType value

Unknown.

Id: `64`

<a id="symbol-amount-gather-tax-rate"></a>

## `amount-gather-tax-rate`

- Kind: `value`
- Detail: ResourceType value

Unknown.

Id: `63`

<a id="symbol-amount-gold"></a>

## `amount-gold`

- Kind: `value`
- Detail: ResourceType value

The gold stockpile. "gold" can also be used instead.

Id: `3`

<a id="symbol-amount-gold-bonus"></a>

## `amount-gold-bonus`

- Kind: `value`
- Detail: ResourceType value

The Mayan bonus for gold, where gold resources last longer.

Id: `47`

<a id="symbol-amount-gold-counter"></a>

## `amount-gold-counter`

- Kind: `value`
- Detail: ResourceType value

Unknown.

Id: `49`

<a id="symbol-amount-gold-farming-productivity"></a>

## `amount-gold-farming-productivity`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. Farming gold production rate per 100 seconds. Burgundian Vinegards tech sets this to 2.

Id: `236`

<a id="symbol-amount-gold-generation"></a>

## `amount-gold-generation`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. Free gold trickle rate per minute. Used in Battle Royale.

Id: `233`

<a id="symbol-amount-gold-score"></a>

## `amount-gold-score`

- Kind: `value`
- Detail: ResourceType value

Likely the amount of economic score gained from the player's current gold stockpile.

Id: `188`

<a id="symbol-amount-gold-total"></a>

## `amount-gold-total`

- Kind: `value`
- Detail: ResourceType value

The total amount of gold gathered, including gold from trade carts, trade cogs, relics, feitorias, and gold from selling resources at the market. Stone sold at the market is not subtracted from this total.

Id: `169`

<a id="symbol-amount-heal-range"></a>

## `amount-heal-range`

- Kind: `value`
- Detail: ResourceType value

Sets the monk/missionary heal range. Default is 4. Set to 8 for Teutons.

Id: `90`

<a id="symbol-amount-heal-rate-modifier"></a>

## `amount-heal-rate-modifier`

- Kind: `value`
- Detail: ResourceType value

A multiplier for heal rate, used by the Byzantines team bonus.

Id: `89`

<a id="symbol-amount-heresy"></a>

## `amount-heresy`

- Kind: `value`
- Detail: ResourceType value

Set to 1 when the player researches Heresy.

Id: `192`

<a id="symbol-amount-hold-relics"></a>

## `amount-hold-relics`

- Kind: `value`
- Detail: ResourceType value

Likely set to 1 if the player's team holds all relics.

Id: `55`

<a id="symbol-amount-hold-ruins"></a>

## `amount-hold-ruins`

- Kind: `value`
- Detail: ResourceType value

Likely set to 1 if the player's team holds all Monuments.

Id: `54`

<a id="symbol-amount-hun-wonder-bonus"></a>

## `amount-hun-wonder-bonus`

- Kind: `value`
- Detail: ResourceType value

Affects the victory time of wonders. Probably also affects relic victory times. Seems to be the number of years required for victory * 10. Used for Atheism.

Id: `196`

<a id="symbol-amount-hunting-productivity"></a>

## `amount-hunting-productivity`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. Gold production while hunters gather food per 100 seconds.

Id: `268`

<a id="symbol-amount-infantry-kill-reward"></a>

## `amount-infantry-kill-reward`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. This resource currently effectively enables/disables gold generation per second by infantry killing villagers, trade units and monks. Affected by Chieftains.

Id: `274`

<a id="symbol-amount-kill-ratio"></a>

## `amount-kill-ratio`

- Kind: `value`
- Detail: ResourceType value

The difference between amount-kills and amount-killed-by-others.

Id: `44`

<a id="symbol-amount-killed-by-others"></a>

## `amount-killed-by-others`

- Kind: `value`
- Detail: ResourceType value

The total number of the player's units killed by the player's enemies. Likely is equal to Units Lost in the achievements screen.

Id: `154`

<a id="symbol-amount-kills"></a>

## `amount-kills`

- Kind: `value`
- Detail: ResourceType value

The amount of units the player has killed. Likely the Units Killed displayed in the achievements screen.

Id: `20`

<a id="symbol-amount-kills-by-gaia"></a>

## `amount-kills-by-gaia`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. Likely the number of the player's own units that were killed by Gaia. Likely used to calculate Units Lost in the achievements screen.

Id: `325`

<a id="symbol-amount-kills-by-player1"></a>

## `amount-kills-by-player1`

- Kind: `value`
- Detail: ResourceType value

Likely the number of the player's own units that were killed by player 1. Likely used to calculate Units Lost in the achievements screen.

Id: `326`

<a id="symbol-amount-kills-by-player2"></a>

## `amount-kills-by-player2`

- Kind: `value`
- Detail: ResourceType value

Likely the number of the player's own units that were killed by player 2. Likely used to calculate Units Lost in the achievements screen.

Id: `327`

<a id="symbol-amount-kills-by-player3"></a>

## `amount-kills-by-player3`

- Kind: `value`
- Detail: ResourceType value

Likely the number of the player's own units that were killed by player 3. Likely used to calculate Units Lost in the achievements screen.

Id: `328`

<a id="symbol-amount-kills-by-player4"></a>

## `amount-kills-by-player4`

- Kind: `value`
- Detail: ResourceType value

Likely the number of the player's own units that were killed by player 4. Likely used to calculate Units Lost in the achievements screen.

Id: `329`

<a id="symbol-amount-kills-by-player5"></a>

## `amount-kills-by-player5`

- Kind: `value`
- Detail: ResourceType value

Likely the number of the player's own units that were killed by player 5. Likely used to calculate Units Lost in the achievements screen.

Id: `330`

<a id="symbol-amount-kills-by-player6"></a>

## `amount-kills-by-player6`

- Kind: `value`
- Detail: ResourceType value

Likely the number of the player's own units that were killed by player 6. Likely used to calculate Units Lost in the achievements screen.

Id: `331`

<a id="symbol-amount-kills-by-player7"></a>

## `amount-kills-by-player7`

- Kind: `value`
- Detail: ResourceType value

Likely the number of the player's own units that were killed by player 7. Likely used to calculate Units Lost in the achievements screen.

Id: `332`

<a id="symbol-amount-kills-by-player8"></a>

## `amount-kills-by-player8`

- Kind: `value`
- Detail: ResourceType value

Likely the number of the player's own units that were killed by player 8. Likely used to calculate Units Lost in the achievements screen.

Id: `333`

<a id="symbol-amount-livestock-food-productivity"></a>

## `amount-livestock-food-productivity`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. Garrisoned herdable food generation rate per 60 seconds. Gurjaras sets this to 3.5.

Id: `254`

<a id="symbol-amount-maintenance"></a>

## `amount-maintenance`

- Kind: `value`
- Detail: ResourceType value

Unknown. Doesn't seem to work.

Id: `33`

<a id="symbol-amount-meat"></a>

## `amount-meat`

- Kind: `value`
- Detail: ResourceType value

Unknown. This does not apply to dead animals.

Id: `15`

<a id="symbol-amount-mercenary-kipchak-count"></a>

## `amount-mercenary-kipchak-count`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. The total number of mercenary kipchaks creatable. Researching Cuman Mercenaries sets this to 5 * the number of amount-castle.

Id: `214`

<a id="symbol-amount-mercenary-kipchak-limit"></a>

## `amount-mercenary-kipchak-limit`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. The total number of trained and/or queued mercenary kipchaks.

Id: `215`

<a id="symbol-amount-military-can-convert"></a>

## `amount-military-can-convert`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. Military units with the conversion task can convert units if this is set to > 0 for a player.

Id: `279`

<a id="symbol-amount-military-conversion-chance"></a>

## `amount-military-conversion-chance`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. Determines the conversion probability per monk second. Probably only affects military units that can convert, not monks. Set to 25 by default.

Id: `281`

<a id="symbol-amount-military-conversion-range-adj"></a>

## `amount-military-conversion-range-adj`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. Adds to the conversion range of military units. Probably only affects military units that can convert, not monks. Set to 6 by default.

Id: `280`

<a id="symbol-amount-military-conversion-recharge-rate"></a>

## `amount-military-conversion-recharge-rate`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. Determines the faith recharge rate after successful conversions. Probably only affects military units that can convert, not monks. Set to 1.6 by default.

Id: `282`

<a id="symbol-amount-military-population"></a>

## `amount-military-population`

- Kind: `value`
- Detail: ResourceType value

The military population. Might be equal to Largest Army in the achievements screen.

Id: `40`

<a id="symbol-amount-monasteries"></a>

## `amount-monasteries`

- Kind: `value`
- Detail: ResourceType value

The player's current number of monasteries.

Id: `52`

<a id="symbol-amount-monument-food-trickle"></a>

## `amount-monument-food-trickle`

- Kind: `value`
- Detail: ResourceType value

Defined as "amount-unused-1". The monument food trickle modifier. The amount of resources obtained by owning a monument is 0.7925 * amount-monument-food-trickle.

Id: `221`

<a id="symbol-amount-monument-gold-trickle"></a>

## `amount-monument-gold-trickle`

- Kind: `value`
- Detail: ResourceType value

Defined as "amount-unused-4". The monument gold trickle modifier. The amount of resources obtained by owning a monument is 0.7925 * amount-monument-gold-trickle.

Id: `224`

<a id="symbol-amount-monument-stone-trickle"></a>

## `amount-monument-stone-trickle`

- Kind: `value`
- Detail: ResourceType value

Defined as "amount-unused-3". The monument stone trickle modifier. The amount of resources obtained by owning a monument is 0.7925 * amount-monument-stone-trickle.

Id: `223`

<a id="symbol-amount-monument-wood-trickle"></a>

## `amount-monument-wood-trickle`

- Kind: `value`
- Detail: ResourceType value

Defined as "amount-unused-2". The monument wood trickle modifier. The amount of resources obtained by owning a monument is 0.7925 * amount-monument-wood-trickle.

Id: `222`

<a id="symbol-amount-object-cost-summation"></a>

## `amount-object-cost-summation`

- Kind: `value`
- Detail: ResourceType value

Likely an object's total cost. Could be used to calculate part of the player's economic score.

Id: `98`

<a id="symbol-amount-ore"></a>

## `amount-ore`

- Kind: `value`
- Detail: ResourceType value

A hidden and unused 5th resource.

Id: `56`

<a id="symbol-amount-player-killed"></a>

## `amount-player-killed`

- Kind: `value`
- Detail: ResourceType value

Likely related to Survival To Finish on the achievements screen. Untested if survival is 0 or 1.

Id: `45`

<a id="symbol-amount-player1-kill-value"></a>

## `amount-player1-kill-value`

- Kind: `value`
- Detail: ResourceType value

The score value gained for player 1 from killing units, likely used to calculate the military score.

Id: `401`

<a id="symbol-amount-player1-kills"></a>

## `amount-player1-kills`

- Kind: `value`
- Detail: ResourceType value

Amount of units Player 1 has killed.

Id: `301`

<a id="symbol-amount-player1-razing-value"></a>

## `amount-player1-razing-value`

- Kind: `value`
- Detail: ResourceType value

The score gained for player 1 from destroying buildings, likely used to calculate military score.

Id: `426`

<a id="symbol-amount-player1-razings"></a>

## `amount-player1-razings`

- Kind: `value`
- Detail: ResourceType value

The amount of buildings player 1 has destroyed.

Id: `351`

<a id="symbol-amount-player1-tribute"></a>

## `amount-player1-tribute`

- Kind: `value`
- Detail: ResourceType value

The total tribute sent by player 1.

Id: `451`

<a id="symbol-amount-player2-kill-value"></a>

## `amount-player2-kill-value`

- Kind: `value`
- Detail: ResourceType value

The score value gained for player 2 from killing units, likely used to calculate the military score.

Id: `402`

<a id="symbol-amount-player2-kills"></a>

## `amount-player2-kills`

- Kind: `value`
- Detail: ResourceType value

Amount of units Player 2 has killed.

Id: `302`

<a id="symbol-amount-player2-razing-value"></a>

## `amount-player2-razing-value`

- Kind: `value`
- Detail: ResourceType value

The score gained for player 2 from destroying buildings, likely used to calculate military score.

Id: `427`

<a id="symbol-amount-player2-razings"></a>

## `amount-player2-razings`

- Kind: `value`
- Detail: ResourceType value

The amount of buildings player 2 has destroyed.

Id: `352`

<a id="symbol-amount-player2-tribute"></a>

## `amount-player2-tribute`

- Kind: `value`
- Detail: ResourceType value

The total tribute sent by player 2.

Id: `452`

<a id="symbol-amount-player3-kill-value"></a>

## `amount-player3-kill-value`

- Kind: `value`
- Detail: ResourceType value

The score value gained for player 3 from killing units, likely used to calculate the military score.

Id: `403`

<a id="symbol-amount-player3-kills"></a>

## `amount-player3-kills`

- Kind: `value`
- Detail: ResourceType value

Amount of units Player 3 has killed.

Id: `303`

<a id="symbol-amount-player3-razing-value"></a>

## `amount-player3-razing-value`

- Kind: `value`
- Detail: ResourceType value

The score gained for player 3 from destroying buildings, likely used to calculate military score.

Id: `428`

<a id="symbol-amount-player3-razings"></a>

## `amount-player3-razings`

- Kind: `value`
- Detail: ResourceType value

The amount of buildings player 3 has destroyed.

Id: `353`

<a id="symbol-amount-player3-tribute"></a>

## `amount-player3-tribute`

- Kind: `value`
- Detail: ResourceType value

The total tribute sent by player 3.

Id: `453`

<a id="symbol-amount-player4-kill-value"></a>

## `amount-player4-kill-value`

- Kind: `value`
- Detail: ResourceType value

The score value gained for player 4 from killing units, likely used to calculate the military score.

Id: `404`

<a id="symbol-amount-player4-kills"></a>

## `amount-player4-kills`

- Kind: `value`
- Detail: ResourceType value

Amount of units Player 4 has killed.

Id: `304`

<a id="symbol-amount-player4-razing-value"></a>

## `amount-player4-razing-value`

- Kind: `value`
- Detail: ResourceType value

The score gained for player 4 from destroying buildings, likely used to calculate military score.

Id: `429`

<a id="symbol-amount-player4-razings"></a>

## `amount-player4-razings`

- Kind: `value`
- Detail: ResourceType value

The amount of buildings player 4 has destroyed.

Id: `354`

<a id="symbol-amount-player4-tribute"></a>

## `amount-player4-tribute`

- Kind: `value`
- Detail: ResourceType value

The total tribute sent by player 4.

Id: `454`

<a id="symbol-amount-player5-kill-value"></a>

## `amount-player5-kill-value`

- Kind: `value`
- Detail: ResourceType value

The score value gained for player 5 from killing units, likely used to calculate the military score.

Id: `405`

<a id="symbol-amount-player5-kills"></a>

## `amount-player5-kills`

- Kind: `value`
- Detail: ResourceType value

Amount of units Player 5 has killed.

Id: `305`

<a id="symbol-amount-player5-razing-value"></a>

## `amount-player5-razing-value`

- Kind: `value`
- Detail: ResourceType value

The score gained for player 5 from destroying buildings, likely used to calculate military score.

Id: `430`

<a id="symbol-amount-player5-razings"></a>

## `amount-player5-razings`

- Kind: `value`
- Detail: ResourceType value

The amount of buildings player 5 has destroyed.

Id: `355`

<a id="symbol-amount-player5-tribute"></a>

## `amount-player5-tribute`

- Kind: `value`
- Detail: ResourceType value

The total tribute sent by player 5.

Id: `455`

<a id="symbol-amount-player6-kill-value"></a>

## `amount-player6-kill-value`

- Kind: `value`
- Detail: ResourceType value

The score value gained for player 6 from killing units, likely used to calculate the military score.

Id: `406`

<a id="symbol-amount-player6-kills"></a>

## `amount-player6-kills`

- Kind: `value`
- Detail: ResourceType value

Amount of units Player 6 has killed.

Id: `306`

<a id="symbol-amount-player6-razing-value"></a>

## `amount-player6-razing-value`

- Kind: `value`
- Detail: ResourceType value

The score gained for player 6 from destroying buildings, likely used to calculate military score.

Id: `431`

<a id="symbol-amount-player6-razings"></a>

## `amount-player6-razings`

- Kind: `value`
- Detail: ResourceType value

The amount of buildings player 6 has destroyed.

Id: `356`

<a id="symbol-amount-player6-tribute"></a>

## `amount-player6-tribute`

- Kind: `value`
- Detail: ResourceType value

The total tribute sent by player 6.

Id: `456`

<a id="symbol-amount-player7-kill-value"></a>

## `amount-player7-kill-value`

- Kind: `value`
- Detail: ResourceType value

The score value gained for player 7 from killing units, likely used to calculate the military score.

Id: `407`

<a id="symbol-amount-player7-kills"></a>

## `amount-player7-kills`

- Kind: `value`
- Detail: ResourceType value

Amount of units Player 7 has killed.

Id: `307`

<a id="symbol-amount-player7-razing-value"></a>

## `amount-player7-razing-value`

- Kind: `value`
- Detail: ResourceType value

The score gained for player 7 from destroying buildings, likely used to calculate military score.

Id: `432`

<a id="symbol-amount-player7-razings"></a>

## `amount-player7-razings`

- Kind: `value`
- Detail: ResourceType value

The amount of buildings player 7 has destroyed.

Id: `357`

<a id="symbol-amount-player7-tribute"></a>

## `amount-player7-tribute`

- Kind: `value`
- Detail: ResourceType value

The total tribute sent by player 7.

Id: `457`

<a id="symbol-amount-player8-kill-value"></a>

## `amount-player8-kill-value`

- Kind: `value`
- Detail: ResourceType value

The score value gained for player 8 from killing units, likely used to calculate the military score.

Id: `408`

<a id="symbol-amount-player8-kills"></a>

## `amount-player8-kills`

- Kind: `value`
- Detail: ResourceType value

Amount of units Player 8 has killed.

Id: `308`

<a id="symbol-amount-player8-razing-value"></a>

## `amount-player8-razing-value`

- Kind: `value`
- Detail: ResourceType value

The score gained for player 8 from destroying buildings, likely used to calculate military score.

Id: `433`

<a id="symbol-amount-player8-razings"></a>

## `amount-player8-razings`

- Kind: `value`
- Detail: ResourceType value

The amount of buildings player 8 has destroyed.

Id: `358`

<a id="symbol-amount-player8-tribute"></a>

## `amount-player8-tribute`

- Kind: `value`
- Detail: ResourceType value

The total tribute sent by player 8.

Id: `458`

<a id="symbol-amount-population"></a>

## `amount-population`

- Kind: `value`
- Detail: ResourceType value

The player's population.

Id: `11`

<a id="symbol-amount-population-cap"></a>

## `amount-population-cap`

- Kind: `value`
- Detail: ResourceType value

This actually seems to be the population headroom. Most units decrease this by 1 when trained. Set to 1000 for Huns.

Id: `4`

<a id="symbol-amount-queued-count"></a>

## `amount-queued-count`

- Kind: `value`
- Detail: ResourceType value

The total amount of units all buildings are queued (waiting to be trained but aren't currently being trained). Doesn't seem to count technologies.

Id: `80`

<a id="symbol-amount-raider"></a>

## `amount-raider`

- Kind: `value`
- Detail: ResourceType value

Starts the player with Unit 444 (PWTC, a packed town center) if this is 1. This was a mechanic for Mongols, Celts, and Vikings who were originally designed as Raider civs. This changed before release of AoK, and this mechanic is not used.

Id: `82`

<a id="symbol-amount-raider-ability"></a>

## `amount-raider-ability`

- Kind: `value`
- Detail: ResourceType value

Enables the slaver kidnap ability that didn't make it into the game.

Id: `95`

<a id="symbol-amount-raiding-productivity"></a>

## `amount-raiding-productivity`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. Used for keshik gold generation per 100 seconds. Set to 50 for Tatars.

Id: `213`

<a id="symbol-amount-razed-by-others"></a>

## `amount-razed-by-others`

- Kind: `value`
- Detail: ResourceType value

The total number of the player's buildings by the player's enemies. Likely is equal to Buildings Lost in the achievements screen.

Id: `155`

<a id="symbol-amount-razings"></a>

## `amount-razings`

- Kind: `value`
- Detail: ResourceType value

Likely equal to Buildings Razed in the achievements screen.

Id: `43`

<a id="symbol-amount-razings-by-gaia"></a>

## `amount-razings-by-gaia`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. Likely the number of the player's own buildings that were destroyed by Gaia. Likely used to calculate Buildings Lost in the achievements screen.

Id: `375`

<a id="symbol-amount-razings-by-player1"></a>

## `amount-razings-by-player1`

- Kind: `value`
- Detail: ResourceType value

Likely the number of the player's own buildings that were destroyed by player 1. Likely used to calculate Buildings Lost in the achievements screen.

Id: `376`

<a id="symbol-amount-razings-by-player2"></a>

## `amount-razings-by-player2`

- Kind: `value`
- Detail: ResourceType value

Likely the number of the player's own buildings that were destroyed by player 2. Likely used to calculate Buildings Lost in the achievements screen.

Id: `377`

<a id="symbol-amount-razings-by-player3"></a>

## `amount-razings-by-player3`

- Kind: `value`
- Detail: ResourceType value

Likely the number of the player's own buildings that were destroyed by player 3. Likely used to calculate Buildings Lost in the achievements screen.

Id: `378`

<a id="symbol-amount-razings-by-player4"></a>

## `amount-razings-by-player4`

- Kind: `value`
- Detail: ResourceType value

Likely the number of the player's own buildings that were destroyed by player 4. Likely used to calculate Buildings Lost in the achievements screen.

Id: `379`

<a id="symbol-amount-razings-by-player5"></a>

## `amount-razings-by-player5`

- Kind: `value`
- Detail: ResourceType value

Likely the number of the player's own buildings that were destroyed by player 5. Likely used to calculate Buildings Lost in the achievements screen.

Id: `380`

<a id="symbol-amount-razings-by-player6"></a>

## `amount-razings-by-player6`

- Kind: `value`
- Detail: ResourceType value

Likely the number of the player's own buildings that were destroyed by player 6. Likely used to calculate Buildings Lost in the achievements screen.

Id: `381`

<a id="symbol-amount-razings-by-player7"></a>

## `amount-razings-by-player7`

- Kind: `value`
- Detail: ResourceType value

Likely the number of the player's own buildings that were destroyed by player 7. Likely used to calculate Buildings Lost in the achievements screen.

Id: `382`

<a id="symbol-amount-razings-by-player8"></a>

## `amount-razings-by-player8`

- Kind: `value`
- Detail: ResourceType value

Likely the number of the player's own buildings that were destroyed by player 8. Likely used to calculate Buildings Lost in the achievements screen.

Id: `383`

<a id="symbol-amount-relic-food-rate"></a>

## `amount-relic-food-rate`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. Amount of food generated per minute per relic captured. Set to 30 for Burgundians. Affected by Atheism.

Id: `225`

<a id="symbol-amount-relic-income-summation"></a>

## `amount-relic-income-summation`

- Kind: `value`
- Detail: ResourceType value

The total relic gold generated for the player. Likely is equal to Relic Gold amount in the achievements screen. Untested whether this includes feitoria gold income.

Id: `100`

<a id="symbol-amount-relic-rate"></a>

## `amount-relic-rate`

- Kind: `value`
- Detail: ResourceType value

The rate that relics accumulate gold. Default is 30. Changed by Sultans and Aztec team bonus.

Id: `191`

<a id="symbol-amount-relic-stone-rate"></a>

## `amount-relic-stone-rate`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. The relic stone production per minute.

Id: `265`

<a id="symbol-amount-relic-wood-rate"></a>

## `amount-relic-wood-rate`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. The relic wood production per minute.

Id: `264`

<a id="symbol-amount-relics"></a>

## `amount-relics`

- Kind: `value`
- Detail: ResourceType value

Likely the number of relics the player has. This could also equal the Relics Captured number displayed in the achievements screen.

Id: `7`

<a id="symbol-amount-religion"></a>

## `amount-religion`

- Kind: `value`
- Detail: ResourceType value

Unknown.

Id: `5`

<a id="symbol-amount-research-cost-mod"></a>

## `amount-research-cost-mod`

- Kind: `value`
- Detail: ResourceType value

The multiplier for the current discount on technologies for the Chinese, between 0.8 and 1.

Id: `85`

<a id="symbol-amount-research-count"></a>

## `amount-research-count`

- Kind: `value`
- Detail: ResourceType value

The amount of technologies the player has researched. Like the Research Count in the achievements screen.

Id: `21`

<a id="symbol-amount-research-summation"></a>

## `amount-research-summation`

- Kind: `value`
- Detail: ResourceType value

Likely a technology's total cost. Could be used to calculate part of the player's economic score.

Id: `99`

<a id="symbol-amount-research-time-mod"></a>

## `amount-research-time-mod`

- Kind: `value`
- Detail: ResourceType value

Appears to be unused, but probably still works for mods. Probably exists for a civ bonus that was removed before release that enabled faster researching technologies.

Id: `86`

<a id="symbol-amount-reveal-initial-type"></a>

## `amount-reveal-initial-type`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. Reveals relics on the map for Burmese.

Id: `210`

<a id="symbol-amount-ruins"></a>

## `amount-ruins`

- Kind: `value`
- Detail: ResourceType value

This applies to monuments. Each monument captured gives 1 of this resource.

Id: `14`

<a id="symbol-amount-salvage-decay-rate"></a>

## `amount-salvage-decay-rate`

- Kind: `value`
- Detail: ResourceType value

Boat decay rate. Default is 5.

Id: `65`

<a id="symbol-amount-shared-line-of-sight"></a>

## `amount-shared-line-of-sight`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. No longer used.

Id: `217`

<a id="symbol-amount-shepherd-productivity"></a>

## `amount-shepherd-productivity`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. The Tatars bonus for sheep lasting longer.

Id: `216`

<a id="symbol-amount-spawn-cap"></a>

## `amount-spawn-cap`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. Sets the limit to the number of buildings that can spawn objects for civ bonuses. Probably affected by Nomad.

Id: `234`

<a id="symbol-amount-spawn-stay-inside"></a>

## `amount-spawn-stay-inside`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. Used to spawn one relic in one Armenian fortified church once constructed.

Id: `283`

<a id="symbol-amount-speed-up-building-range"></a>

## `amount-speed-up-building-range`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. This specifies the range (in tiles) of the square area created around the speed up building for the speed up effect. The speed up building is specified by amount-speed-up-building-type. Set to 8 by...

Id: `256`

<a id="symbol-amount-speed-up-building-type"></a>

## `amount-speed-up-building-type`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. The ID of the building to use for the speed up effect. This is set to the caravanserai by default.

Id: `255`

<a id="symbol-amount-speed-up-effect-type"></a>

## `amount-speed-up-effect-type`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. The type of effect caused by the speed up building. Possible values are 5 (movement speed), 13 (work rate), and 109 (regeneration). Set to 5 by default.

Id: `259`

<a id="symbol-amount-speed-up-object-type"></a>

## `amount-speed-up-object-type`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. The class ID (900+) of units that should be affected by the speed up effect. Set to 919 (trade-cart-class) by default.

Id: `258`

<a id="symbol-amount-speed-up-percentage"></a>

## `amount-speed-up-percentage`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. The adjustment used when a unit matching the amount-speed-up-object-type is within the amount-speed-up-building-range of the speed up building. Set to 0.2 (20%) by default.

Id: `257`

<a id="symbol-amount-speed-up-secondary-effect-type"></a>

## `amount-speed-up-secondary-effect-type`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. This is the type of secondary effect caused by the speed up building. Uses same values as amount-speed-up-effect-type. Set to 109 (regeneration) by default.

Id: `260`

<a id="symbol-amount-speed-up-secondary-percentage"></a>

## `amount-speed-up-secondary-percentage`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. The adjustment used for the secondary speed up effect type when a unit matching the amount-speed-up-object-type is within the amount-speed-up-building-range of the speed up building. Set to 60 by d...

Id: `261`

<a id="symbol-amount-spies"></a>

## `amount-spies`

- Kind: `value`
- Detail: ResourceType value

Likely set to 1 if Spies is researched.

Id: `183`

<a id="symbol-amount-spies-discount"></a>

## `amount-spies-discount`

- Kind: `value`
- Detail: ResourceType value

Atheism sets this to 1. Likely applies the 50% discount to Spies if this resource is set to 1.

Id: `197`

<a id="symbol-amount-starting-food"></a>

## `amount-starting-food`

- Kind: `value`
- Detail: ResourceType value

The starting food amount. Likely is affected by StartingResources and civ bonuses.

Id: `91`

<a id="symbol-amount-starting-gold"></a>

## `amount-starting-gold`

- Kind: `value`
- Detail: ResourceType value

The starting gold amount. Likely is affected by StartingResources and civ bonuses.

Id: `94`

<a id="symbol-amount-starting-scout-id"></a>

## `amount-starting-scout-id`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. The unit ID of the starting scout.

Id: `263`

<a id="symbol-amount-starting-stone"></a>

## `amount-starting-stone`

- Kind: `value`
- Detail: ResourceType value

The starting stone amount. Likely is affected by StartingResources and civ bonuses.

Id: `93`

<a id="symbol-amount-starting-villagers"></a>

## `amount-starting-villagers`

- Kind: `value`
- Detail: ResourceType value

The number of starting villagers, depending on the civilization.

Id: `84`

<a id="symbol-amount-starting-wood"></a>

## `amount-starting-wood`

- Kind: `value`
- Detail: ResourceType value

The starting wood amount. Likely is affected by StartingResources and civ bonuses.

Id: `92`

<a id="symbol-amount-stone"></a>

## `amount-stone`

- Kind: `value`
- Detail: ResourceType value

The stone stockpile. "stone" can also be used instead.

Id: `2`

<a id="symbol-amount-stone-bonus"></a>

## `amount-stone-bonus`

- Kind: `value`
- Detail: ResourceType value

The Mayan bonus for stone, where stone resources last longer.

Id: `79`

<a id="symbol-amount-stone-generation"></a>

## `amount-stone-generation`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. Free stone trickle rate per minute. USed in Battle Royale.

Id: `232`

<a id="symbol-amount-stone-gold-mining-productivity"></a>

## `amount-stone-gold-mining-productivity`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. Gold production rate while mining stone per 100 seconds. Set to 18 for Poles and is modified by stone gathering techs.

Id: `241`

<a id="symbol-amount-stone-score"></a>

## `amount-stone-score`

- Kind: `value`
- Detail: ResourceType value

Likely the amount of economic score gained from the player's current stone stockpile.

Id: `187`

<a id="symbol-amount-stone-total"></a>

## `amount-stone-total`

- Kind: `value`
- Detail: ResourceType value

The total amount of stone gathered, including stone from feitorias and stone bought at the market. Stone from tribute is not included. Gold lost from buying resources at the market is not subtracted from this total.

Id: `168`

<a id="symbol-amount-technology-reward-effect"></a>

## `amount-technology-reward-effect`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. The ID of an additional effect which will fire when any technology is researched.

Id: `269`

<a id="symbol-amount-temporary-map-reveal"></a>

## `amount-temporary-map-reveal`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. If > 0, enemy TCs are revealed. Set to 5 for Vietnamese.

Id: `209`

<a id="symbol-amount-theocracy"></a>

## `amount-theocracy`

- Kind: `value`
- Detail: ResourceType value

Set to 1 when the player researches Theocracy.

Id: `193`

<a id="symbol-amount-total-castles-built"></a>

## `amount-total-castles-built`

- Kind: `value`
- Detail: ResourceType value

The total number of castles the player built. Likely equal to Total Castles in the achievements screen.

Id: `173`

<a id="symbol-amount-total-tribute-received"></a>

## `amount-total-tribute-received`

- Kind: `value`
- Detail: ResourceType value

The total amount of tribute received.

Id: `171`

<a id="symbol-amount-total-value-of-kills"></a>

## `amount-total-value-of-kills`

- Kind: `value`
- Detail: ResourceType value

Likely either the total cost or the military score gained from killing enemy units.

Id: `170`

<a id="symbol-amount-total-value-of-razings"></a>

## `amount-total-value-of-razings`

- Kind: `value`
- Detail: ResourceType value

Likely either the total cost or the military score gained from razing enemy buildings.

Id: `172`

<a id="symbol-amount-total-wonders-built"></a>

## `amount-total-wonders-built`

- Kind: `value`
- Detail: ResourceType value

The total number of wonders the player built. Likely equal to Total Wonders in the achievements screen.

Id: `174`

<a id="symbol-amount-town-center-unavailable"></a>

## `amount-town-center-unavailable`

- Kind: `value`
- Detail: ResourceType value

Set to 0 in Sudden Death. Otherwise, set to 1 to allow TC construction starting in the Castle Age.

Id: `48`

<a id="symbol-amount-trade-bonus"></a>

## `amount-trade-bonus`

- Kind: `value`
- Detail: ResourceType value

Unused. Doesn't appear to be connected to the Spanish team bonus.

Id: `8`

<a id="symbol-amount-trade-food-percent"></a>

## `amount-trade-food-percent`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. The percentage of gold generated from trade that is also given as food. Bengalis sets this to 10.

Id: `251`

<a id="symbol-amount-trade-good-quality"></a>

## `amount-trade-good-quality`

- Kind: `value`
- Detail: ResourceType value

Unused. Likely related to a trade mechanic that didn't make it into the game.

Id: `59`

<a id="symbol-amount-trade-goods"></a>

## `amount-trade-goods`

- Kind: `value`
- Detail: ResourceType value

Probably a leftover from a trade goods feature that was discarded before release.

Id: `9`

<a id="symbol-amount-trade-income-summation"></a>

## `amount-trade-income-summation`

- Kind: `value`
- Detail: ResourceType value

The total gold generated from trade units for the player. Likely is equal to Trade Profit in the achievements screen.

Id: `101`

<a id="symbol-amount-trade-market-level"></a>

## `amount-trade-market-level`

- Kind: `value`
- Detail: ResourceType value

Unused. Likely related to a trade mechanic that didn't make it into the game.

Id: `60`

<a id="symbol-amount-trade-production"></a>

## `amount-trade-production`

- Kind: `value`
- Detail: ResourceType value

Unused. Likely from a trade feature that didn't make it into the game.

Id: `10`

<a id="symbol-amount-trade-stone-percent"></a>

## `amount-trade-stone-percent`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. The percentage of stone generated from trade that is also given as food.

Id: `253`

<a id="symbol-amount-trade-vig-rate"></a>

## `amount-trade-vig-rate`

- Kind: `value`
- Detail: ResourceType value

Sets the trading fee. Affected by Guilds and Saracens civ bonus.

Id: `78`

<a id="symbol-amount-trade-wood-percent"></a>

## `amount-trade-wood-percent`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. The percentage of gold generated from trade that is also given as wood.

Id: `252`

<a id="symbol-amount-training-count"></a>

## `amount-training-count`

- Kind: `value`
- Detail: ResourceType value

The total amount of all units the player is currently training, not including queued units.

Id: `81`

<a id="symbol-amount-tribute"></a>

## `amount-tribute`

- Kind: `value`
- Detail: ResourceType value

Total amount of tributed resources. Likely is part of Tribute Sent/Rcvd in the achievements screen.

Id: `53`

<a id="symbol-amount-tribute-from-gaia"></a>

## `amount-tribute-from-gaia`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. Likely the total tribute received from Gaia.

Id: `475`

<a id="symbol-amount-tribute-from-player1"></a>

## `amount-tribute-from-player1`

- Kind: `value`
- Detail: ResourceType value

Likely the total tribute received from player 1.

Id: `476`

<a id="symbol-amount-tribute-from-player2"></a>

## `amount-tribute-from-player2`

- Kind: `value`
- Detail: ResourceType value

Likely the total tribute received from player 2.

Id: `477`

<a id="symbol-amount-tribute-from-player3"></a>

## `amount-tribute-from-player3`

- Kind: `value`
- Detail: ResourceType value

Likely the total tribute received from player 3.

Id: `478`

<a id="symbol-amount-tribute-from-player4"></a>

## `amount-tribute-from-player4`

- Kind: `value`
- Detail: ResourceType value

Likely the total tribute received from player 4.

Id: `479`

<a id="symbol-amount-tribute-from-player5"></a>

## `amount-tribute-from-player5`

- Kind: `value`
- Detail: ResourceType value

Likely the total tribute received from player 5.

Id: `480`

<a id="symbol-amount-tribute-from-player6"></a>

## `amount-tribute-from-player6`

- Kind: `value`
- Detail: ResourceType value

Likely the total tribute received from player 6.

Id: `481`

<a id="symbol-amount-tribute-from-player7"></a>

## `amount-tribute-from-player7`

- Kind: `value`
- Detail: ResourceType value

Likely the total tribute received from player 7.

Id: `482`

<a id="symbol-amount-tribute-from-player8"></a>

## `amount-tribute-from-player8`

- Kind: `value`
- Detail: ResourceType value

Likely the total tribute received from player 8.

Id: `483`

<a id="symbol-amount-tribute-inefficiency"></a>

## `amount-tribute-inefficiency`

- Kind: `value`
- Detail: ResourceType value

The tribute fee for trading at the market.

Id: `46`

<a id="symbol-amount-tribute-score"></a>

## `amount-tribute-score`

- Kind: `value`
- Detail: ResourceType value

Likely either the score the player gained from sending tribute or the total resources tributed + tribute taxes.

Id: `175`

<a id="symbol-amount-trigger-shared-exploration"></a>

## `amount-trigger-shared-exploration`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. Unknown.

Id: `286`

<a id="symbol-amount-trigger-shared-visibility"></a>

## `amount-trigger-shared-visibility`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. Unknown.

Id: `285`

<a id="symbol-amount-unit-limit"></a>

## `amount-unit-limit`

- Kind: `value`
- Detail: ResourceType value

This seems to be the actual population limit resource. Affected by Goths population bonus.

Id: `32`

<a id="symbol-amount-unit-repair-cost"></a>

## `amount-unit-repair-cost`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. The percentage of cost required to repair siege units and ships. Set to 0.5 by default.

Id: `270`

<a id="symbol-amount-units-converted"></a>

## `amount-units-converted`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. The amount of units lost to enemy conversions.

Id: `240`

<a id="symbol-amount-units-value-total"></a>

## `amount-units-value-total`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. The total cost of all units trained so far. This does not decrease when units are killed.

Id: `246`

<a id="symbol-amount-unused-0"></a>

## `amount-unused-0`

- Kind: `value`
- Detail: ResourceType value

Unused. Might be usable by mods.

Id: `220`

<a id="symbol-amount-value-current-buildings"></a>

## `amount-value-current-buildings`

- Kind: `value`
- Detail: ResourceType value

Likely either the total cost or the economy score gained from the player's current buildings.

Id: `165`

<a id="symbol-amount-value-current-units"></a>

## `amount-value-current-units`

- Kind: `value`
- Detail: ResourceType value

Likely either the total cost or the economy score gained from the player's current units.

Id: `164`

<a id="symbol-amount-value-killed-by-others"></a>

## `amount-value-killed-by-others`

- Kind: `value`
- Detail: ResourceType value

Likely either the total cost or the total military score gained by all other players from killing the current player's units. Probably isn't included in the actual military score calculations, otherwise some players would have negative mil...

Id: `152`

<a id="symbol-amount-value-razed-by-others"></a>

## `amount-value-razed-by-others`

- Kind: `value`
- Detail: ResourceType value

Likely either the total cost or the total military score gained by all other players from razing the current player's buildings. Probably isn't included in the actual military score calculations, otherwise some players would have negative ...

Id: `153`

<a id="symbol-amount-value-wonders-castles"></a>

## `amount-value-wonders-castles`

- Kind: `value`
- Detail: ResourceType value

Likely either the total cost or the amount of society score gained from constructing castles and wonders.

Id: `184`

<a id="symbol-amount-villagers-created-total"></a>

## `amount-villagers-created-total`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. The total number of all villagers trained so far. This does not decrease when villagers are killed.

Id: `248`

<a id="symbol-amount-villagers-idle-periods-total"></a>

## `amount-villagers-idle-periods-total`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. The number of villagers that entered an idle state since the game started. This is only updated every 5 physical minutes, and the starting villagers are added to this resource at the beginning of t...

Id: `249`

<a id="symbol-amount-villagers-idle-seconds-total"></a>

## `amount-villagers-idle-seconds-total`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. The amount of total seconds all villagers have been idle since the start of the game. This is only updated every 5 physical minutes. Any villagers immediately add their idle time to this resource i...

Id: `250`

<a id="symbol-amount-villagers-killed-by-ai-player"></a>

## `amount-villagers-killed-by-ai-player`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. Total number of villagers lost to AIs.

Id: `228`

<a id="symbol-amount-villagers-killed-by-animal"></a>

## `amount-villagers-killed-by-animal`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. Total number of villagers lost to wild animals.

Id: `227`

<a id="symbol-amount-villagers-killed-by-gaia"></a>

## `amount-villagers-killed-by-gaia`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. Total number of villagers lost to gaia.

Id: `226`

<a id="symbol-amount-villagers-killed-by-human-player"></a>

## `amount-villagers-killed-by-human-player`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. Total number of villagers lost to human players.

Id: `229`

<a id="symbol-amount-wonder"></a>

## `amount-wonder`

- Kind: `value`
- Detail: ResourceType value

The amount of wonders the player currently has standing. Likely isn't Total Wonders in the achievements screen. This is likely Resource 174 instead.

Id: `42`

<a id="symbol-amount-wood"></a>

## `amount-wood`

- Kind: `value`
- Detail: ResourceType value

The wood stockpile. "wood" can also be used instead.

Id: `1`

<a id="symbol-amount-wood-bonus"></a>

## `amount-wood-bonus`

- Kind: `value`
- Detail: ResourceType value

The Mayan bonus for wood, where wood resources last longer.

Id: `189`

<a id="symbol-amount-wood-generation"></a>

## `amount-wood-generation`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. Free wood trickle rate per minute. Used in Battle Royale.

Id: `231`

<a id="symbol-amount-wood-score"></a>

## `amount-wood-score`

- Kind: `value`
- Detail: ResourceType value

Likely the amount of economic score gained from the player's current wood stockpile.

Id: `186`

<a id="symbol-amount-wood-total"></a>

## `amount-wood-total`

- Kind: `value`
- Detail: ResourceType value

The total amount of wood gathered, including wood from feitorias and wood bought at the market. Wood from tribute is not included. Wood sold at the market is not subtracted from this total.

Id: `167`

<a id="symbol-amount-workshop-food-trickle"></a>

## `amount-workshop-food-trickle`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. Trade workshop food production rate multiplier. The amount of food obtained from owning n number of trade workshops (Unit 1647) is given by n * amount-workshop-food-trickle * 2.25.

Id: `242`

<a id="symbol-amount-workshop-gold-trickle"></a>

## `amount-workshop-gold-trickle`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. Trade workshop gold production rate multiplier. The amount of gold obtained from owning n number of trade workshops (Unit 1647) is given by n * amount-workshop-gold-trickle * 2.25.

Id: `245`

<a id="symbol-amount-workshop-stone-trickle"></a>

## `amount-workshop-stone-trickle`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. Trade workshop stone production rate multiplier. The amount of stone obtained from owning n number of trade workshops (Unit 1647) is given by n * amount-workshop-stone-trickle * 2.25.

Id: `244`

<a id="symbol-amount-workshop-wood-trickle"></a>

## `amount-workshop-wood-trickle`

- Kind: `value`
- Detail: ResourceType value

DE only. Must be defined with a defconst. Trade workshop wood production rate multiplier. The amount of wood obtained from owning n number of trade workshops (Unit 1647) is given by n * amount-workshop-wood-trickle * 2.25.

Id: `243`

<a id="symbol-amount-writing"></a>

## `amount-writing`

- Kind: `value`
- Detail: ResourceType value

Set to 1 when Cartography is researched. Writing was the name for Cartography in AoE1.

Id: `50`

<a id="symbol-any"></a>

## `any`

- Kind: `value`
- Detail: PlayerStance value

Any stance.

Id: `2`

<a id="symbol-any-ally"></a>

## `any-ally`

- Kind: `value`
- Detail: PlayerNumber value

Any allied player.

Id: `-101`

<a id="symbol-any-ally-id--101-description-any-allied-player-can-t-be-used-with-up-set-placement-data-"></a>

## `any-ally", // id: -101, // description: "Any allied player. Can't be used with up-set-placement-data"." //`

- Kind: `value`
- Detail: AllyPlayer value

<a id="symbol-any-computer"></a>

## `any-computer`

- Kind: `value`
- Detail: PlayerNumber value

Any computer player.

Id: `-102`

<a id="symbol-any-computer-ally"></a>

## `any-computer-ally`

- Kind: `value`
- Detail: PlayerNumber value

Any computer ally.

Id: `-103`

<a id="symbol-any-computer-ally-id--103-description-any-computer-ally-can-t-be-used-with-up-set-placement-data-"></a>

## `any-computer-ally", // id: -103, // description: "Any computer ally. Can't be used with up-set-placement-data"." //`

- Kind: `value`
- Detail: AllyPlayer value

<a id="symbol-any-computer-enemy"></a>

## `any-computer-enemy`

- Kind: `value`
- Detail: PlayerNumber value

Any computer enemy.

Id: `-104`

<a id="symbol-any-computer-neutral"></a>

## `any-computer-neutral`

- Kind: `value`
- Detail: PlayerNumber value

Any neutral computer player.

Id: `-105`

<a id="symbol-any-enemy"></a>

## `any-enemy`

- Kind: `value`
- Detail: PlayerNumber value

Any enemy player.

Id: `-106`

<a id="symbol-any-human"></a>

## `any-human`

- Kind: `value`
- Detail: PlayerNumber value

Any human player.

Id: `-107`

<a id="symbol-any-human-ally"></a>

## `any-human-ally`

- Kind: `value`
- Detail: PlayerNumber value

Any human ally.

Id: `-108`

<a id="symbol-any-human-ally-id--108-description-any-human-ally-can-t-be-used-with-up-set-placement-data-"></a>

## `any-human-ally", // id: -108, // description: "Any human ally. Can't be used with up-set-placement-data"." //`

- Kind: `value`
- Detail: AllyPlayer value

<a id="symbol-any-human-enemy"></a>

## `any-human-enemy`

- Kind: `value`
- Detail: PlayerNumber value

Any human enemy.

Id: `-109`

<a id="symbol-any-human-neutral"></a>

## `any-human-neutral`

- Kind: `value`
- Detail: PlayerNumber value

Any neutral human player.

Id: `-110`

<a id="symbol-any-neutral"></a>

## `any-neutral`

- Kind: `value`
- Detail: PlayerNumber value

Any neutral player.

Id: `-111`

<a id="symbol-aquarena"></a>

## `Aquarena`

- Kind: `value`
- Detail: MapType value

Aquarena map. Notice the capitalized A.

Id: `202`

<a id="symbol-arabia"></a>

## `arabia`

- Kind: `value`
- Detail: MapType value

Arabia map.

Id: `9`

<a id="symbol-archery-cannon-class"></a>

## `archery-cannon-class`

- Kind: `value`
- Detail: ClassId value

Archery Cannon class. Includes Hand Cannoneers and Janissaries.

Id: `944`

<a id="symbol-archery-class"></a>

## `archery-class`

- Kind: `value`
- Detail: ClassId value

Foot archer class.

Id: `900`

<a id="symbol-archipelago"></a>

## `archipelago`

- Kind: `value`
- Detail: MapType value

Archipelago map.

Id: `10`

<a id="symbol-arena"></a>

## `arena`

- Kind: `value`
- Detail: MapType value

Arena map.

Id: `29`

<a id="symbol-armenians"></a>

## `armenians`

- Kind: `value`
- Detail: Civ value

Armenians.

Id: `44`

<a id="symbol-atacama"></a>

## `atacama`

- Kind: `value`
- Detail: MapType value

Atacama map.

Id: `150`

<a id="symbol-athenians"></a>

## `athenians`

- Kind: `value`
- Detail: Civ value

Athenians (must define with a defconst first).

Id: `47`

<a id="symbol-attack-soldier-count"></a>

## `attack-soldier-count`

- Kind: `value`
- Detail: FactId value

The number of the player's currently attacking land-based military units. This only counts attacking soldiers during attack-groups and attack-now attacks. The corresponding fact command is attack-soldier-count.

Id: `14`

<a id="symbol-attack-warboat-count"></a>

## `attack-warboat-count`

- Kind: `value`
- Detail: FactId value

The number of the player's currently attacking warships. This only counts attacking warships during attack-groups and attack-now attacks. The corresponding fact command is attack-warboat-count.

Id: `17`

<a id="symbol-attribute-area-effect"></a>

## `attribute-area-effect`

- Kind: `value`
- Detail: AttrId value

Likely the object's blast radius.

Id: `22`

<a id="symbol-attribute-area-effect-level-"></a>

## `attribute-area-effect-level.`

- Kind: `value`
- Detail: AttrId value

Likely the object's blast attack level. The blast damage for objects with level 3 or higher only damage the targeted object. The blast damage for objects with level 2 will damage nearby objects that are within the blast radius of the attac...

Id: `44`

<a id="symbol-attribute-armor"></a>

## `attribute-armor`

- Kind: `value`
- Detail: AttrId value

The object's armor. Unknown whether this is melee armor, pierce armor, or both, but it's likely just melee armor. It seems like there isn't a way to choose which armor type to modify, or there is a complex formula that allows you to specif...

Id: `8`

<a id="symbol-attribute-attribute-amount-held"></a>

## `attribute-attribute-amount-held`

- Kind: `value`
- Detail: AttrId value

Unknown. The attribute-attribute in the attribute name isn't a typo. ;)

Id: `21`

<a id="symbol-attribute-base-armor"></a>

## `attribute-base-armor`

- Kind: `value`
- Detail: AttrId value

Similar to attribute-armor. Untested, but this likely affects the original armor amount, so it wouldn't display as + or - like it would for blacksmith armor upgrades.

Id: `15`

<a id="symbol-attribute-blast-defense-level"></a>

## `attribute-blast-defense-level`

- Kind: `value`
- Detail: AttrId value

The object's blast defense level. The object will receive blast damage from units with a blast attack level greater than or equal to the object's blast defense level.

Id: `45`

<a id="symbol-attribute-building-facet"></a>

## `attribute-building-facet`

- Kind: `value`
- Detail: AttrId value

Unknown. Likely the rotation the building faces, though most buildings only have one direction anyway.

Id: `17`

<a id="symbol-attribute-carry-capacity"></a>

## `attribute-carry-capacity`

- Kind: `value`
- Detail: AttrId value

The amount the object can carry. This affects the resource capacity villagers can carry and also the amount of resources that Gaia/player owned resources can hold.

Id: `14`

<a id="symbol-attribute-creation-time"></a>

## `attribute-creation-time`

- Kind: `value`
- Detail: AttrId value

The amount of time to create the object, in seconds.

Id: `101`

<a id="symbol-attribute-death-spawn-obj"></a>

## `attribute-death-spawn-obj`

- Kind: `value`
- Detail: AttrId value

The ID of a new object that is spawned when an object dies. This is usually the unit's corpse or ruins, but it is used by the Konnik to spawn a dismounted Konnik when the mounted Konnik dies.

Id: `57`

<a id="symbol-attribute-defensive-terrain"></a>

## `attribute-defensive-terrain`

- Kind: `value`
- Detail: AttrId value

Unknown. Could be the same as Terrain Defense Bonus from Advanced Genie Editor.

Id: `18`

<a id="symbol-attribute-description-id"></a>

## `attribute-description-id`

- Kind: `value`
- Detail: AttrId value

Likely the language ID location of the object's description.

Id: `51`

<a id="symbol-attribute-fire-missile-at-frame"></a>

## `attribute-fire-missile-at-frame`

- Kind: `value`
- Detail: AttrId value

Likely the frame delay, the number of graphical frames to must be displayed from the attack animation before the projectile will fire.

Id: `41`

<a id="symbol-attribute-food-cost"></a>

## `attribute-food-cost`

- Kind: `value`
- Detail: AttrId value

The object's food cost.

Id: `103`

<a id="symbol-attribute-garrison-arrows"></a>

## `attribute-garrison-arrows`

- Kind: `value`
- Detail: AttrId value

Likely either the extra number of projectiles the object will fire or the max number of arrows the object can fire when fully garrisoned. Not sure how this differs from attribute-max-dup-missiles.

Id: `102`

<a id="symbol-attribute-garrison-heal-rate"></a>

## `attribute-garrison-heal-rate`

- Kind: `value`
- Detail: AttrId value

The object's heal rate for units that are garrisoned inside. Likely multiplied by 100 or 1000 (not sure which, sorry).

Id: `108`

<a id="symbol-attribute-gold-cost"></a>

## `attribute-gold-cost`

- Kind: `value`
- Detail: AttrId value

The object's gold cost.

Id: `105`

<a id="symbol-attribute-hidden-damage-resist"></a>

## `attribute-hidden-damage-resist`

- Kind: `value`
- Detail: AttrId value

Unknown. Could be the same as the Bonus Damage Resist field from Advanced Genie Editor.

Id: `24`

<a id="symbol-attribute-hit-chance"></a>

## `attribute-hit-chance`

- Kind: `value`
- Detail: AttrId value

Unknown. Probably the object's accuracy. Likely multiplied by 100.

Id: `11`

<a id="symbol-attribute-hotkey-id"></a>

## `attribute-hotkey-id`

- Kind: `value`
- Detail: AttrId value

Likely the language ID location of the letter for the object's default hotkey.

Id: `58`

<a id="symbol-attribute-hp"></a>

## `attribute-hp`

- Kind: `value`
- Detail: AttrId value

The object's hit points.

Id: `0`

<a id="symbol-attribute-icon-id"></a>

## `attribute-icon-id`

- Kind: `value`
- Detail: AttrId value

The ID of the object's icon.

Id: `25`

<a id="symbol-attribute-los"></a>

## `attribute-los`

- Kind: `value`
- Detail: AttrId value

The object's line of sight.

Id: `1`

<a id="symbol-attribute-max-dup-missiles"></a>

## `attribute-max-dup-missiles`

- Kind: `value`
- Detail: AttrId value

Likely either the extra number of projectiles the object will fire or the max number of arrows the object can fire when fully garrisoned. Not sure how this differs from attribute-garrison-arrows

Id: `107`

<a id="symbol-attribute-minimum-weapon-range"></a>

## `attribute-minimum-weapon-range`

- Kind: `value`
- Detail: AttrId value

The object's minimum range.

Id: `20`

<a id="symbol-attribute-missile-id"></a>

## `attribute-missile-id`

- Kind: `value`
- Detail: AttrId value

The ID of the object's projectile. See the Proj. ID in the <a href="https://airef.github.io/tables/objects.html">Objects Table</a> to get the projectile IDs of each unit.

Id: `16`

<a id="symbol-attribute-name-id"></a>

## `attribute-name-id`

- Kind: `value`
- Detail: AttrId value

Likely the language ID location of the object's name.

Id: `50`

<a id="symbol-attribute-obj-max"></a>

## `attribute-obj-max`

- Kind: `value`
- Detail: AttrId value

Unknown.

Id: `2`

<a id="symbol-attribute-radius-x"></a>

## `attribute-radius-x`

- Kind: `value`
- Detail: AttrId value

Unknown. Possibly the radius of the object's size in the x direction.

Id: `3`

<a id="symbol-attribute-radius-y"></a>

## `attribute-radius-y`

- Kind: `value`
- Detail: AttrId value

Unknown. Possibly the radius of the object's size in the y direction.

Id: `4`

<a id="symbol-attribute-regenration-rate"></a>

## `attribute-regenration-rate`

- Kind: `value`
- Detail: AttrId value

Note the [incorrect] spelling. The speed the object will heal at. Likely multiplied by 100 or 1000 (not sure which, sorry).

Id: `109`

<a id="symbol-attribute-resource-cost"></a>

## `attribute-resource-cost`

- Kind: `value`
- Detail: AttrId value

Likely let's you change the ResourceType cost for a resource besides food, wood, gold, or stone.

Id: `100`

<a id="symbol-attribute-search-radius"></a>

## `attribute-search-radius`

- Kind: `value`
- Detail: AttrId value

The object's search radius. This is often equal to LOS, and it determines the radius where the object will respond to enemy units.

Id: `23`

<a id="symbol-attribute-shown-attack"></a>

## `attribute-shown-attack`

- Kind: `value`
- Detail: AttrId value

The object's shown attack. A + or - value will be displayed in the interface if the actual attack is higher or lower than the shown attack, respectively.

Id: `46`

<a id="symbol-attribute-shown-melee-armor"></a>

## `attribute-shown-melee-armor`

- Kind: `value`
- Detail: AttrId value

The object's shown melee armor. A + or - value will be displayed in the interface if the actual melee armor is higher or lower than the shown attack, respectively. Uncertain if shown pierce armor can be affected with this attribute.

Id: `48`

<a id="symbol-attribute-shown-range"></a>

## `attribute-shown-range`

- Kind: `value`
- Detail: AttrId value

The object's shown range. A + or - value will be displayed in the interface if the actual range is higher or lower than the shown attack, respectively.

Id: `47`

<a id="symbol-attribute-speed"></a>

## `attribute-speed`

- Kind: `value`
- Detail: AttrId value

The object's speed. Probably multiplied by 100, but this is untested.

Id: `5`

<a id="symbol-attribute-speed-of-attack"></a>

## `attribute-speed-of-attack`

- Kind: `value`
- Detail: AttrId value

The object's attack speed. Unknown whether this is given in seconds or milliseconds, but probably the latter.

Id: `10`

<a id="symbol-attribute-stone-cost"></a>

## `attribute-stone-cost`

- Kind: `value`
- Detail: AttrId value

The object's stone cost.

Id: `106`

<a id="symbol-attribute-targetting-type"></a>

## `attribute-targetting-type`

- Kind: `value`
- Detail: AttrId value

Unknown.

Id: `19`

<a id="symbol-attribute-terrain-restriction"></a>

## `attribute-terrain-restriction`

- Kind: `value`
- Detail: AttrId value

The terrain the object can travel or be placed on. Likely the same as the Terrain Table field in Advanced Genie Editor.

Id: `53`

<a id="symbol-attribute-turn-speed"></a>

## `attribute-turn-speed`

- Kind: `value`
- Detail: AttrId value

The time it takes the object to turn from one rotation/facing direction to the next. Most objects' turn speed is zero, but this is observable for ships and trebuchets.

Id: `6`

<a id="symbol-attribute-weapon"></a>

## `attribute-weapon`

- Kind: `value`
- Detail: AttrId value

Unknown. Probably the object's attack. It's possible there is a complex formula that allows you to specify the type of attack/attack bonus and the amount in a single value.

Id: `9`

<a id="symbol-attribute-weapon-range"></a>

## `attribute-weapon-range`

- Kind: `value`
- Detail: AttrId value

The object's range.

Id: `12`

<a id="symbol-attribute-wood-cost"></a>

## `attribute-wood-cost`

- Kind: `value`
- Detail: AttrId value

The object's wood cost.

Id: `104`

<a id="symbol-attribute-work-rate"></a>

## `attribute-work-rate`

- Kind: `value`
- Detail: AttrId value

The object's work rate. This attribute is primarily relevant for buildings, which determines the speed that units and techs are trained and researched.

Id: `13`

<a id="symbol-aztec"></a>

## `aztec`

- Kind: `value`
- Detail: Civ value

Aztecs

Id: `15`

<a id="symbol-baltic"></a>

## `baltic`

- Kind: `value`
- Detail: MapType value

Baltic map.

Id: `11`

<a id="symbol-battle-on-the-ice"></a>

## `battle-on-the-ice`

- Kind: `value`
- Detail: MapType value

Battle on the Ice battle royale map.

Id: `142`

<a id="symbol-battle-royale"></a>

## `battle-royale`

- Kind: `value`
- Detail: GameType value

Battle Royale game.

Id: `12`

<a id="symbol-battle-royale-time"></a>

## `battle-royale-time`

- Kind: `value`
- Detail: FactId value

DE only. Must be defined with a defconst. The amount of battle royale time left, in seconds. There isn't a corresponding fact command.

Id: `55`

<a id="symbol-bengalis"></a>

## `bengalis`

- Kind: `value`
- Detail: Civ value

Bengalis.

Id: `41`

<a id="symbol-berbers"></a>

## `berbers`

- Kind: `value`
- Detail: Civ value

Berbers. In WK, must define with a defconst before it can be used.

Id: `27`

<a id="symbol-black-forest"></a>

## `black-forest`

- Kind: `value`
- Detail: MapType value

Black Forest map.

Id: `12`

<a id="symbol-boar-hunting"></a>

## `boar-hunting`

- Kind: `value`
- Detail: Resource value

Live and dead boar only. Only available in UP and DE. Can only be used with dropsite-min-distance. For these parameters only, invalid/not-found boar returns 255 instead of -1.

Id: `5`

<a id="symbol-bog-islands"></a>

## `bog-islands`

- Kind: `value`
- Detail: MapType value

Bog Islands map.

Id: `112`

<a id="symbol-bogland"></a>

## `bogland`

- Kind: `value`
- Detail: MapType value

Bogland map. Must be defined with a defconst.

Id: `123`

<a id="symbol-bohemians"></a>

## `bohemians`

- Kind: `value`
- Detail: Civ value

Bohemians.

Id: `39`

<a id="symbol-border-dispute"></a>

## `border-dispute`

- Kind: `value`
- Detail: MapType value

Border Dispute map.

Id: `198`

<a id="symbol-briton"></a>

## `briton`

- Kind: `value`
- Detail: Civ value

Britons

Id: `1`

<a id="symbol-budapest"></a>

## `budapest`

- Kind: `value`
- Detail: MapType value

Budapest map.

Id: `68`

<a id="symbol-building-class"></a>

## `building-class`

- Kind: `value`
- Detail: ClassId value

Buildings class. Doesn't include all buildings, like towers and walls.

Id: `903`

<a id="symbol-building-count"></a>

## `building-count`

- Kind: `value`
- Detail: FactId value

The number of buildings a player has. The corresponding fact commands are building-count and players-building-count. There isn't a corresponding FactId for building-count-total.

Id: `27`

<a id="symbol-building-type-count"></a>

## `building-type-count`

- Kind: `value`
- Detail: FactId value

The number of a given type of buildings a player has. The corresponding fact commands are building-type-count and players-building-type-count.

Id: `28`

<a id="symbol-building-type-count-total"></a>

## `building-type-count-total`

- Kind: `value`
- Detail: FactId value

The number of a given type of building a player has, including buildings currently under construction. The corresponding fact command is building-type-count-total.

Id: `29`

<a id="symbol-building-type-in-town"></a>

## `building-type-in-town`

- Kind: `value`
- Detail: FactId value

The number of enemy buildings of the given type inside the AI's town. The corresponding fact command is up-building-type-in-town.

Id: `44`

<a id="symbol-bulgarians"></a>

## `bulgarians`

- Kind: `value`
- Detail: Civ value

Bulgarians.

Id: `32`

<a id="symbol-burgundians"></a>

## `burgundians`

- Kind: `value`
- Detail: Civ value

Burgundians.

Id: `36`

<a id="symbol-burmese"></a>

## `burmese`

- Kind: `value`
- Detail: Civ value

Burmese. In WK, must define with a defconst before it can be used.

Id: `30`

<a id="symbol-byzantine"></a>

## `byzantine`

- Kind: `value`
- Detail: Civ value

Byzantines

Id: `7`

<a id="symbol-c-"></a>

## `c:`

- Kind: `value`
- Detail: compareOp value

Treats the second compared parameter in the command as a constant when doing the comparison. If the second parameter to be compared is a defined value, such as a goal or a unit type, this will use the numeric Id value assigned to this para...

<a id="symbol-c--"></a>

## `c:-`

- Kind: `value`
- Detail: mathOp value

Subtract the constant value of the second operand from the first operand.

DE id: `26`

<a id="symbol-c-"></a>

## `c:!=`

- Kind: `value`
- Detail: compareOp value

Not equal. In DE, the first DE ID is for != and the second DE ID is for c:!=.

DE id: `5,23`

<a id="symbol-c-"></a>

## `c:*`

- Kind: `value`
- Detail: mathOp value

Multiply the first operand by the constant value of the second operand.

DE id: `27`

<a id="symbol-c-"></a>

## `c:/`

- Kind: `value`
- Detail: mathOp value

Divide the first operand by the constant value of the second operand. The quotient is rounded to the nearest integer.

DE id: `28`

<a id="symbol-c-"></a>

## `c:%*`

- Kind: `value`
- Detail: mathOp value

Treat the constant value of the second operand as a percentage and find that percentage of the first parameter, truncated (not rounded) to the nearest integer, i.e. (first operand * second operand / 100).

DE id: `34`

<a id="symbol-c-"></a>

## `c:%/`

- Kind: `value`
- Detail: mathOp value

Divide the first operand by the constant value of the second operand, and convert the quotient to a percent, truncated (not rounded) to the nearest integer, i.e. (first operand / second operand * 100).

DE id: `35`

<a id="symbol-c-"></a>

## `c:+`

- Kind: `value`
- Detail: mathOp value

Add the constant value of the second operand to the first operand.

DE id: `25`

<a id="symbol-c-"></a>

## `c:<`

- Kind: `value`
- Detail: compareOp value

Less than. In DE, the first DE ID is for &#60; and the second DE ID is for c:&#60;.

DE id: `0,18`

<a id="symbol-c-"></a>

## `c:<=`

- Kind: `value`
- Detail: compareOp value

Less than or equal. In DE, the first DE ID is for &#60;= and the second DE ID is for c:&#60;=.

DE id: `1,19`

<a id="symbol-c-"></a>

## `c:=`

- Kind: `value`
- Detail: mathOp value

Set the first operand equal to the constant value of the second operand.

DE id: `24`

<a id="symbol-c-"></a>

## `c:==`

- Kind: `value`
- Detail: compareOp value

Equal. Note: one equals sign (=) is an assignment operator used in the mathOp operator. Always use "==" when you want to compare. In DE, the first DE ID is for == and the second DE ID is for c:==.

DE id: `4,22`

<a id="symbol-c-"></a>

## `c:>`

- Kind: `value`
- Detail: compareOp value

Greater than. In DE, the first DE ID is for &#62; and the second DE ID is for c:&#62;.

DE id: `2,20`

<a id="symbol-c-"></a>

## `c:>=`

- Kind: `value`
- Detail: compareOp value

Greater than or equal. In DE, the first DE ID is for &#62;= and the second DE ID is for c:&#62;=.

DE id: `3,21`

<a id="symbol-c-max"></a>

## `c:max`

- Kind: `value`
- Detail: mathOp value

Store the largest value between the first operand and the constant value of the second operand.

DE id: `30`

<a id="symbol-c-min"></a>

## `c:min`

- Kind: `value`
- Detail: mathOp value

Store the smallest value between the first operand and the constant value of the second operand.

DE id: `29`

<a id="symbol-c-mod"></a>

## `c:mod`

- Kind: `value`
- Detail: mathOp value

Divide the first operand by the constant value of the second operand. Store the remainder instead of the quotient.

DE id: `31`

<a id="symbol-c-neg"></a>

## `c:neg`

- Kind: `value`
- Detail: mathOp value

Negate the constant value of the second operand and store the result in the first operand. If the constant is already negative, this will store its positive value.

DE id: `32`

<a id="symbol-c-z-"></a>

## `c:z/`

- Kind: `value`
- Detail: mathOp value

Divide the first operand by the constant value of the second operand. The quotient is truncated (rounded down) to the nearest integer.

DE id: `33`

<a id="symbol-canals"></a>

## `canals`

- Kind: `value`
- Detail: MapType value

Canals map. Must be defined with a defconst.

Id: `34`

<a id="symbol-capricious"></a>

## `capricious`

- Kind: `value`
- Detail: MapType value

Capricious map. Must be defined with a defconst.

Id: `35`

<a id="symbol-capture-the-relic"></a>

## `capture-the-relic`

- Kind: `value`
- Detail: GameType value

Capture the Relic game.

Id: `10`

<a id="symbol-castle-age"></a>

## `castle-age`

- Kind: `value`
- Detail: Age value

Castle Age.

Id: `2`

<a id="symbol-cavalry-archer-class"></a>

## `cavalry-archer-class`

- Kind: `value`
- Detail: ClassId value

Cavalry Archer class.

Id: `936`

<a id="symbol-cavalry-cannon-class"></a>

## `cavalry-cannon-class`

- Kind: `value`
- Detail: ClassId value

Cavalry Cannon class. Includes Conquistadors and Arambai.

Id: `923`

<a id="symbol-cavalry-class"></a>

## `cavalry-class`

- Kind: `value`
- Detail: ClassId value

Cavalry class. Doesn't scout cavalry, light cavalry, or hussar, although it includes light cavalry or hussars (not scout cavalry) that are placed at the start of the game in scenarios.

Id: `912`

<a id="symbol-cc-gaia-type-count"></a>

## `cc-gaia-type-count`

- Kind: `value`
- Detail: FactId value

The total number of the given Gaia resource that currently exists on the map, regardless of whether the AI has explored it. This FactId does not have a corresponding Fact. If you need to do a comparison with the total number of a given Gai...

Id: `49`

<a id="symbol-celtic"></a>

## `celtic`

- Kind: `value`
- Detail: Civ value

Celts

Id: `13`

<a id="symbol-cenotes"></a>

## `cenotes`

- Kind: `value`
- Detail: MapType value

Cenotes map.

Id: `69`

<a id="symbol-chaos-pit"></a>

## `chaos-pit`

- Kind: `value`
- Detail: MapType value

Chaos Pit map. Must be defined with a defconst.

Id: `204`

<a id="symbol-chinese"></a>

## `chinese`

- Kind: `value`
- Detail: Civ value

Chinese

Id: `6`

<a id="symbol-cityoflakes"></a>

## `cityoflakes`

- Kind: `value`
- Detail: MapType value

City of Lakes map. Notice the lack of dashes in the name.

Id: `70`

<a id="symbol-civilian-population"></a>

## `civilian-population`

- Kind: `value`
- Detail: FactId value

The player's civilian population, including Fishing Ships and trade units. The corresponding fact commands are civilian-population and players-civilian-population.

Id: `32`

<a id="symbol-civilization"></a>

## `civilization`

- Kind: `value`
- Detail: FactId value

The player's civilization. The corresponding fact commands are civ-selected and players-civ.

Id: `21`

<a id="symbol-cliffbound"></a>

## `cliffbound`

- Kind: `value`
- Detail: MapType value

Cliffbound map.

Id: `177`

<a id="symbol-cmdid-civilian-building"></a>

## `cmdid-civilian-building`

- Kind: `value`
- Detail: CmdId value

Non-military buildings command ID.

Id: `2`

<a id="symbol-cmdid-fishing-ship"></a>

## `cmdid-fishing-ship`

- Kind: `value`
- Detail: CmdId value

Fishing Ship command ID.

Id: `9`

<a id="symbol-cmdid-flag"></a>

## `cmdid-flag`

- Kind: `value`
- Detail: CmdId value

Flag command ID. This command ID really just means the object lacks available commands and is used by most Gaia objects and dead unit IDs.

Id: `0`

<a id="symbol-cmdid-livestock-gaia"></a>

## `cmdid-livestock-gaia`

- Kind: `value`
- Detail: CmdId value

Gaia livestock command ID. Also includes wild animals and resources.

Id: `1`

<a id="symbol-cmdid-military"></a>

## `cmdid-military`

- Kind: `value`
- Detail: CmdId value

Military command ID. Used by military soldiers, siege weapons, and warships.

Id: `4`

<a id="symbol-cmdid-military-building"></a>

## `cmdid-military-building`

- Kind: `value`
- Detail: CmdId value

Military Buildings command ID.

Id: `10`

<a id="symbol-cmdid-monk"></a>

## `cmdid-monk`

- Kind: `value`
- Detail: CmdId value

Monk and Missionary command ID.

Id: `6`

<a id="symbol-cmdid-relic"></a>

## `cmdid-relic`

- Kind: `value`
- Detail: CmdId value

Relic units command ID. Includes monks carrying relics.

Id: `8`

<a id="symbol-cmdid-trade"></a>

## `cmdid-trade`

- Kind: `value`
- Detail: CmdId value

Trade units command ID. Includes both Trade Carts and Trade Cogs.

Id: `5`

<a id="symbol-cmdid-transport"></a>

## `cmdid-transport`

- Kind: `value`
- Detail: CmdId value

Transport Ship command ID.

Id: `7`

<a id="symbol-cmdid-villager"></a>

## `cmdid-villager`

- Kind: `value`
- Detail: CmdId value

Villager command ID.

Id: `3`

<a id="symbol-coastal"></a>

## `coastal`

- Kind: `value`
- Detail: MapType value

Coastal map.

Id: `13`

<a id="symbol-coastal-forest"></a>

## `coastal-forest`

- Kind: `value`
- Detail: MapType value

Coastal Forest map.

Id: `148`

<a id="symbol-colossal-map"></a>

## `colossal-map`

- Kind: `value`
- Detail: MapSize value

Colossal map size. 320x320 tiles. Requires MORE_MAP_SIZES Steam launch parameter.

Id: `320`

<a id="symbol-commodity-buying-price"></a>

## `commodity-buying-price`

- Kind: `value`
- Detail: FactId value

The current buying price for the given commodity type. The corresponding fact command is commodity-buying-price.

Id: `10`

<a id="symbol-commodity-selling-price"></a>

## `commodity-selling-price`

- Kind: `value`
- Detail: FactId value

The current selling price for the given commodity type. The corresponding fact command is commodity-selling-price.

Id: `11`

<a id="symbol-conquest"></a>

## `conquest`

- Kind: `value`
- Detail: VictoryCondition value

Conquest victory. Team only wins by defeating all enemies.

Id: `1`

<a id="symbol-continental"></a>

## `continental`

- Kind: `value`
- Detail: MapType value

Continental map.

Id: `14`

<a id="symbol-controlled-animal-class-"></a>

## `controlled-animal-class*`

- Kind: `value`
- Detail: ClassId value

Controlled animal class.

Id: `961`

<a id="symbol-crater"></a>

## `crater`

- Kind: `value`
- Detail: MapType value

Crater map.

Id: `152`

<a id="symbol-crater-lake"></a>

## `crater-lake`

- Kind: `value`
- Detail: MapType value

Crater Lake map.

Id: `15`

<a id="symbol-crossroads"></a>

## `crossroads`

- Kind: `value`
- Detail: MapType value

Crossroads map.

Id: `153`

<a id="symbol-crownwood"></a>

## `crownwood`

- Kind: `value`
- Detail: MapType value

Crownwood map.

Id: `207`

<a id="symbol-ctr-monsoon"></a>

## `ctr-monsoon`

- Kind: `value`
- Detail: MapType value

Capture the Relic Monsoon map.

Id: `80`

<a id="symbol-ctr-pyramid-descent"></a>

## `ctr-pyramid-descent`

- Kind: `value`
- Detail: MapType value

Capture the Relic Pyramid Descent map.

Id: `81`

<a id="symbol-ctr-random"></a>

## `ctr-random`

- Kind: `value`
- Detail: MapType value

Capture the Relic random map.

Id: `79`

<a id="symbol-ctr-spiral"></a>

## `ctr-spiral`

- Kind: `value`
- Detail: MapType value

Capture the Relic Spiral map.

Id: `82`

<a id="symbol-cumans"></a>

## `cumans`

- Kind: `value`
- Detail: Civ value

Cumans.

Id: `34`

<a id="symbol-current-age"></a>

## `current-age`

- Kind: `value`
- Detail: FactId value

The player's current age. The corresponding fact commands are current-age and players-current-age.

Id: `19`

<a id="symbol-current-age-time"></a>

## `current-age-time`

- Kind: `value`
- Detail: FactId value

The time the player has spent in the current age. The corresponding fact command is current-age-time.

Id: `50`

<a id="symbol-current-score"></a>

## `current-score`

- Kind: `value`
- Detail: FactId value

The player's current score. The corresponding fact commands are current-score and players-score.

Id: `20`

<a id="symbol-custom"></a>

## `custom`

- Kind: `value`
- Detail: VictoryCondition value

Custom victory. Either Relic victory from random map game menu (like Standard but without wonder victory) or a scenario is being played that has the Custom option selected in the scenario's Global Victory section.

Id: `4`

<a id="symbol-custom_map"></a>

## `custom_map`

- Kind: `value`
- Detail: MapType value

A custom random map. Notice the underscore. Defined as 44 before DE.

Id: `59`

<a id="symbol-dark-age"></a>

## `dark-age`

- Kind: `value`
- Detail: Age value

Dark Age.

Id: `0`

<a id="symbol-death-match"></a>

## `death-match`

- Kind: `value`
- Detail: GameType value

Death Match game.

Id: `2`

<a id="symbol-deer-hunting"></a>

## `deer-hunting`

- Kind: `value`
- Detail: Resource value

Deer only. Only available in UP and DE. Can only be used with dropsite-min-distance. For these parameters only, invalid/not-found deer returns 255 instead of -1.

Id: `6`

<a id="symbol-defend-soldier-count"></a>

## `defend-soldier-count`

- Kind: `value`
- Detail: FactId value

The number of the player's currently defending land-based military units. This only counts soldiers that aren't part of attack-groups and attack-now attacks. It includes idle military units not actively defending the player's town. The cor...

Id: `15`

<a id="symbol-defend-the-wonder"></a>

## `defend-the-wonder`

- Kind: `value`
- Detail: GameType value

Defend the Wonder game.

Id: `7`

<a id="symbol-defend-warboat-count"></a>

## `defend-warboat-count`

- Kind: `value`
- Detail: FactId value

The number of the player's currently defending warships. This only counts warships that aren't part of attack-groups and attack-now attacks. It includes idle warships not actively defending the player's town. The corresponding fact command...

Id: `18`

<a id="symbol-defender-count"></a>

## `defender-count`

- Kind: `value`
- Detail: FactId value

The number of soldiers actively defending its town. This only includes soldiers targeting buildings inside the AI's town. The corresponding fact command is up-defender-count.

Id: `43`

<a id="symbol-dingos"></a>

## `dingos`

- Kind: `value`
- Detail: MapType value

Dingos map. Must be defined with a defconst.

Id: `36`

<a id="symbol-dorothea-quarry"></a>

## `dorothea-quarry`

- Kind: `value`
- Detail: MapType value

Dorothea Quarry map. Must be defined with a defconst.

Id: `208`

<a id="symbol-dravidians"></a>

## `dravidians`

- Kind: `value`
- Detail: Civ value

Dravidians.

Id: `40`

<a id="symbol-dropsite-min-distance"></a>

## `dropsite-min-distance`

- Kind: `value`
- Detail: FactId value

The minimum dropsite walking distance for the given resource type. The corresponding fact command is dropsite-min-distance.

Id: `12`

<a id="symbol-dune-springs"></a>

## `dune-springs`

- Kind: `value`
- Detail: MapType value

Dune Springs map.

Id: `179`

<a id="symbol-easiest"></a>

## `easiest`

- Kind: `value`
- Detail: Difficulty value

Easiest difficulty.

Id: `4`

<a id="symbol-easy"></a>

## `easy`

- Kind: `value`
- Detail: Difficulty value

Easy difficulty. Same as Standard difficulty.

Id: `3`

<a id="symbol-effect-add-attribute"></a>

## `effect-add-attribute`

- Kind: `value`
- Detail: EffectId value

Add or subtract the specified value to/from a given object's attribute.

Id: `4`

<a id="symbol-effect-enable-object"></a>

## `effect-enable-object`

- Kind: `value`
- Detail: EffectId value

Enable the specified object for the player. Untested if this effect can also disable the specified object if the Value/Percent parameter is set to 0.

Id: `2`

<a id="symbol-effect-enable-tech"></a>

## `effect-enable-tech`

- Kind: `value`
- Detail: EffectId value

Enable the specified technology for the player. Untested if this effect can also disable the specified technology if the Value/Percent parameter is set to 0.

Id: `7`

<a id="symbol-effect-mod-resource"></a>

## `effect-mod-resource`

- Kind: `value`
- Detail: EffectId value

Add or subtract the specified value to/from a given ResourceType stockpile.

Id: `1`

<a id="symbol-effect-modify-tech"></a>

## `effect-modify-tech`

- Kind: `value`
- Detail: EffectId value

Add or subtract the given value from the attribute of the specified technology. Untested, but this likely only affects the technology cost and research time. attribute-creation-time and the various attribute-*-cost attributes seem like lik...

Id: `8`

<a id="symbol-effect-mul-attribute"></a>

## `effect-mul-attribute`

- Kind: `value`
- Detail: EffectId value

Multiply a given object's attribute by the specified value.

Id: `5`

<a id="symbol-effect-mul-resource"></a>

## `effect-mul-resource`

- Kind: `value`
- Detail: EffectId value

Multiply the player's specified ResourceType by a given value.

Id: `6`

<a id="symbol-effect-set-attribute"></a>

## `effect-set-attribute`

- Kind: `value`
- Detail: EffectId value

Set the attribute to the specified value.

Id: `0`

<a id="symbol-effect-set-player-data"></a>

## `effect-set-player-data`

- Kind: `value`
- Detail: EffectId value

Untested. Set the player's specified player data to the given value. Uncertain what this different player data could be. Perhaps this sets the data for another player?

Id: `9`

<a id="symbol-effect-upgrade-unit"></a>

## `effect-upgrade-unit`

- Kind: `value`
- Detail: EffectId value

Upgrade the specified object to a different specified object. Untested whether you need to specify the upgraded object ID in the AttrId or Value/Percent parameter, or if the effect will automatically calculate which object to upgrade to.

Id: `3`

<a id="symbol-el-dorado"></a>

## `el-dorado`

- Kind: `value`
- Detail: MapType value

El Dorado battle royale map.

Id: `143`

<a id="symbol-empire-wars"></a>

## `empire-wars`

- Kind: `value`
- Detail: GameType value

Empire Wars game.

Id: `13`

<a id="symbol-enclosed"></a>

## `enclosed`

- Kind: `value`
- Detail: MapType value

Enclosed map.

Id: `169`

<a id="symbol-enemy"></a>

## `enemy`

- Kind: `value`
- Detail: PlayerStance value

Enemy.

Id: `3`

<a id="symbol-enemy-buildings-in-town"></a>

## `enemy-buildings-in-town`

- Kind: `value`
- Detail: FactId value

The number of enemy buildings inside the AI's town. The corresponding fact command is up-enemy-buildings-in-town.

Id: `39`

<a id="symbol-enemy-treaty"></a>

## `enemy-treaty`

- Kind: `value`
- Detail: PlayerStance value

DE only. Must be defined with a defconst. This diplomatic stance is used while treaty mode is active for any players who will become enemies when the treaty ends.

Id: `4`

<a id="symbol-enemy-units-in-town"></a>

## `enemy-units-in-town`

- Kind: `value`
- Detail: FactId value

The number of enemy units inside the AI's town. The corresponding fact command is up-enemy-units-in-town.

Id: `40`

<a id="symbol-enemy-villagers-in-town"></a>

## `enemy-villagers-in-town`

- Kind: `value`
- Detail: FactId value

The number of enemy villagers inside the AI's town. The corresponding fact command is up-enemy-villagers-in-town.

Id: `41`

<a id="symbol-enormous-map"></a>

## `enormous-map`

- Kind: `value`
- Detail: MapSize value

Enormous map size. 300x300 tiles. Requires MORE_MAP_SIZES Steam launch parameter.

Id: `300`

<a id="symbol-eruption"></a>

## `eruption`

- Kind: `value`
- Detail: MapType value

Eruption map.

Id: `158`

<a id="symbol-escrow-amount"></a>

## `escrow-amount`

- Kind: `value`
- Detail: FactId value

The current amount of escrowed resources for the given resource type. The corresponding fact command is escrow-amount.

Id: `9`

<a id="symbol-ethiopian"></a>

## `ethiopian`

- Kind: `value`
- Detail: Civ value

Ethiopians. In WK, must define with a defconst before it can be used.

Id: `25`

<a id="symbol-every-ally"></a>

## `every-ally`

- Kind: `value`
- Detail: PlayerNumber value

Every allied player.

Id: `-201`

<a id="symbol-every-ally-id--201-description-every-allied-player-can-t-be-used-with-up-set-placement-data-"></a>

## `every-ally", // id: -201, // description: "Every allied player. Can't be used with up-set-placement-data"." //`

- Kind: `value`
- Detail: AllyPlayer value

<a id="symbol-every-computer"></a>

## `every-computer`

- Kind: `value`
- Detail: PlayerNumber value

Every computer player.

Id: `-202`

<a id="symbol-every-enemy"></a>

## `every-enemy`

- Kind: `value`
- Detail: PlayerNumber value

Every enemy player.

Id: `-203`

<a id="symbol-every-human"></a>

## `every-human`

- Kind: `value`
- Detail: PlayerNumber value

Every human player.

Id: `-204`

<a id="symbol-every-neutral"></a>

## `every-neutral`

- Kind: `value`
- Detail: PlayerNumber value

Every neutral player.

Id: `-205`

<a id="symbol-explored-active"></a>

## `explored-active`

- Kind: `value`
- Detail: ExploredState value

Point is currently visible by an object.

Id: `15`

<a id="symbol-explored-no"></a>

## `explored-no`

- Kind: `value`
- Detail: ExploredState value

Point has not been explored.

Id: `0`

<a id="symbol-explored-yes"></a>

## `explored-yes`

- Kind: `value`
- Detail: ExploredState value

Point has been seen in the past.

Id: `128`

<a id="symbol-extreme"></a>

## `extreme`

- Kind: `value`
- Detail: Difficulty value

Extreme difficulty. Defined only for DE.

Id: `-1`

<a id="symbol-fall-of-axum"></a>

## `fall-of-axum`

- Kind: `value`
- Detail: MapType value

Fall of Axum battle royale map.

Id: `144`

<a id="symbol-fall-of-rome"></a>

## `fall-of-rome`

- Kind: `value`
- Detail: MapType value

Fall of Rome battle royale map.

Id: `145`

<a id="symbol-farm-class"></a>

## `farm-class`

- Kind: `value`
- Detail: ClassId value

Farm class. Includes Fish Traps.

Id: `949`

<a id="symbol-feudal-age"></a>

## `feudal-age`

- Kind: `value`
- Detail: Age value

Feudal Age.

Id: `1`

<a id="symbol-find-attacker"></a>

## `find-attacker`

- Kind: `value`
- Detail: FindPlayerMethod value

Find the last player that has attacked. An invalid player number will be returned if the current player has not been attacked.

Id: `0`

<a id="symbol-find-closest"></a>

## `find-closest`

- Kind: `value`
- Detail: FindPlayerMethod value

Find the player with the closest building. An invalid player number will be returned if players of the given stance have not been found. When used with up-find-next-player the player found will be the next closest player number, looping ba...

Id: `2`

<a id="symbol-find-ordered"></a>

## `find-ordered`

- Kind: `value`
- Detail: FindPlayerMethod value

Find a player, ordered by player number. The player with the highest player number will be the found player. When used with up-find-next-player the player found will be the next matching player number in ascending order, looping back to pl...

Id: `3`

<a id="symbol-find-random"></a>

## `find-random`

- Kind: `value`
- Detail: FindPlayerMethod value

Find a random player. When used with up-find-next-player the player found will not be the previously found player, but otherwise any matching player can be found. find-random will not cycle through all matching players before allowing the ...

Id: `1`

<a id="symbol-fishing-ship-class-"></a>

## `fishing-ship-class*`

- Kind: `value`
- Detail: ClassId value

Fishing Ship Class.

Id: `921`

<a id="symbol-flag-class-"></a>

## `flag-class*`

- Kind: `value`
- Detail: ClassId value

Flag class. Includes flags and map revealers.

Id: `930`

<a id="symbol-food"></a>

## `food`

- Kind: `value`
- Detail: Commodity value

Food

Id: `0`

<a id="symbol-food-amount"></a>

## `food-amount`

- Kind: `value`
- Detail: FactId value

The current food amount. The corresponding fact command is food-amount.

Id: `5`

<a id="symbol-forage-class-"></a>

## `forage-class*`

- Kind: `value`
- Detail: ClassId value

Forage class. Includes forage and fruit bushes.

Id: `907`

<a id="symbol-formation-box"></a>

## `formation-box`

- Kind: `value`
- Detail: Formation value

Box formation. Strong units are placed on the outside of the box with weak units on the inside.

Id: `4`

<a id="symbol-formation-flank"></a>

## `formation-flank`

- Kind: `value`
- Detail: Formation value

Flank formation. The group of units will split into two smaller groups spaced a few tiles apart.

Id: `8`

<a id="symbol-formation-line"></a>

## `formation-line`

- Kind: `value`
- Detail: Formation value

Line formation. This is the standard formation.

Id: `2`

<a id="symbol-formation-stagger"></a>

## `formation-stagger`

- Kind: `value`
- Detail: Formation value

Staggered formation. This is like Line formation, but the units are more spread out.

Id: `7`

<a id="symbol-fortified-clearing"></a>

## `fortified-clearing`

- Kind: `value`
- Detail: MapType value

Fortified Clearing map.

Id: `189`

<a id="symbol-fortified-wall"></a>

## `fortified-wall`

- Kind: `value`
- Detail: WallId value

Fortified Wall.

Id: `155`

<a id="symbol-fortress"></a>

## `fortress`

- Kind: `value`
- Detail: MapType value

Fortress map.

Id: `16`

<a id="symbol-four-lakes"></a>

## `four-lakes`

- Kind: `value`
- Detail: MapType value

Four Lakes map.

Id: `140`

<a id="symbol-frankish"></a>

## `frankish`

- Kind: `value`
- Detail: Civ value

Franks

Id: `2`

<a id="symbol-frigid-lake"></a>

## `frigid-lake`

- Kind: `value`
- Detail: MapType value

Frigid Lake map.

Id: `159`

<a id="symbol-g-"></a>

## `g:`

- Kind: `value`
- Detail: compareOp value

Treats the second compared parameter in the command as a GoalId and compare to the value stored in that goal. This prefix is required when comparing to a goal's value.

<a id="symbol-g--"></a>

## `g:-`

- Kind: `value`
- Detail: mathOp value

Subtract the goal value of the second operand from the first operand.

DE id: `14`

<a id="symbol-g-"></a>

## `g:!=`

- Kind: `value`
- Detail: compareOp value

Not equal to the goal's value.

DE id: `17`

<a id="symbol-g-"></a>

## `g:*`

- Kind: `value`
- Detail: mathOp value

Multiply the first operand by the goal value of the second operand.

DE id: `15`

<a id="symbol-g-"></a>

## `g:/`

- Kind: `value`
- Detail: mathOp value

Divide the first operand by the goal value of the second operand. The quotient is rounded to the nearest integer.

DE id: `16`

<a id="symbol-g-"></a>

## `g:%*`

- Kind: `value`
- Detail: mathOp value

Treat the goal value of the second operand as a percentage and find that percentage of the first parameter, truncated (not rounded) to the nearest integer, i.e. (first operand * second operand / 100).

DE id: `22`

<a id="symbol-g-"></a>

## `g:%/`

- Kind: `value`
- Detail: mathOp value

Divide the first operand by the goal value of the second operand, and convert the quotient to a percent, truncated (not rounded) to the nearest integer, i.e. (first operand / second operand * 100).

DE id: `23`

<a id="symbol-g-"></a>

## `g:+`

- Kind: `value`
- Detail: mathOp value

Add the goal value of the second operand to the first operand.

DE id: `13`

<a id="symbol-g-"></a>

## `g:<`

- Kind: `value`
- Detail: compareOp value

Less than the goal's value.

DE id: `12`

<a id="symbol-g-"></a>

## `g:<=`

- Kind: `value`
- Detail: compareOp value

Less than or equal to the goal's value.

DE id: `13`

<a id="symbol-g-"></a>

## `g:=`

- Kind: `value`
- Detail: mathOp value

Set the first operand equal to the goal value of the second operand.

DE id: `12`

<a id="symbol-g-"></a>

## `g:==`

- Kind: `value`
- Detail: compareOp value

Equal to the goal's value. Note: one equals sign (=) is an assignment operator used in the mathOp operator. Always use "==" when you want to compare.

DE id: `16`

<a id="symbol-g-"></a>

## `g:>`

- Kind: `value`
- Detail: compareOp value

Greater than the goal's value.

DE id: `14`

<a id="symbol-g-"></a>

## `g:>=`

- Kind: `value`
- Detail: compareOp value

Greater than or equal to the goal's value.

DE id: `15`

<a id="symbol-g-max"></a>

## `g:max`

- Kind: `value`
- Detail: mathOp value

Store the largest value between the first operand and the goal value of the second operand.

DE id: `18`

<a id="symbol-g-min"></a>

## `g:min`

- Kind: `value`
- Detail: mathOp value

Store the smallest value between the first operand and the goal value of the second operand.

DE id: `17`

<a id="symbol-g-mod"></a>

## `g:mod`

- Kind: `value`
- Detail: mathOp value

Divide the first operand by the goal value of the second operand. Store the remainder instead of the quotient.

DE id: `19`

<a id="symbol-g-neg"></a>

## `g:neg`

- Kind: `value`
- Detail: mathOp value

Negate the goal value of the second operand and store the result in the first operand. If the goal is already negative, this will store its positive value.

DE id: `20`

<a id="symbol-g-z-"></a>

## `g:z/`

- Kind: `value`
- Detail: mathOp value

Divide the first operand by the goal value of the second operand. The quotient is truncated (rounded down) to the nearest integer.

DE id: `21`

<a id="symbol-gaia"></a>

## `gaia`

- Kind: `value`
- Detail: Civ value

Gaia

Id: `0`

<a id="symbol-gaia-type-count"></a>

## `gaia-type-count`

- Kind: `value`
- Detail: FactId value

The number of currently sighted Gaia resources of the given type. The corresponding fact command is up-gaia-type-count.

Id: `47`

<a id="symbol-gaia-type-count-total"></a>

## `gaia-type-count-total`

- Kind: `value`
- Detail: FactId value

The total number of sighted Gaia resources of the given type. The corresponding fact command is up-gaia-type-count-total.

Id: `48`

<a id="symbol-game-time"></a>

## `game-time`

- Kind: `value`
- Detail: FactId value

The elapsed game time in seconds. The corresponding fact command is game-time.

Id: `0`

<a id="symbol-gate-class"></a>

## `gate-class`

- Kind: `value`
- Detail: ClassId value

Gate class.

Id: `939`

<a id="symbol-georgians"></a>

## `georgians`

- Kind: `value`
- Detail: Civ value

Georgians.

Id: `45`

<a id="symbol-ghost-lake"></a>

## `ghost-lake`

- Kind: `value`
- Detail: MapType value

Ghost Lake map.

Id: `32`

<a id="symbol-giant-map"></a>

## `giant-map`

- Kind: `value`
- Detail: MapSize value

Giant map size. 252x252 tiles. Requires MORE_MAP_SIZES Steam launch parameter.

Id: `252`

<a id="symbol-glacis"></a>

## `glacis`

- Kind: `value`
- Detail: MapType value

Glacis map.

Id: `209`

<a id="symbol-glade"></a>

## `glade`

- Kind: `value`
- Detail: MapType value

Glade map.

Id: `188`

<a id="symbol-gold"></a>

## `gold`

- Kind: `value`
- Detail: Resource value

Gold.

Id: `3`

<a id="symbol-gold-amount"></a>

## `gold-amount`

- Kind: `value`
- Detail: FactId value

The current gold amount. The corresponding fact command is gold-amount.

Id: `8`

<a id="symbol-gold-fish-class-"></a>

## `gold-fish-class*`

- Kind: `value`
- Detail: ClassId value

Gold fish class. Includes oysters and whales.

Id: `963`

<a id="symbol-gold-mine-class-"></a>

## `gold-mine-class*`

- Kind: `value`
- Detail: ClassId value

Gold Mine class.

Id: `932`

<a id="symbol-gold-rush"></a>

## `gold-rush`

- Kind: `value`
- Detail: MapType value

Gold Rush map.

Id: `17`

<a id="symbol-golden-stream"></a>

## `golden-stream`

- Kind: `value`
- Detail: MapType value

Golden Stream map.

Id: `180`

<a id="symbol-golden-swamp"></a>

## `golden-swamp`

- Kind: `value`
- Detail: MapType value

Golden Swamp map.

Id: `139`

<a id="symbol-goldenpit"></a>

## `goldenpit`

- Kind: `value`
- Detail: MapType value

Golden Pit map. Notice the lack of dashes in the name.

Id: `71`

<a id="symbol-gothic"></a>

## `gothic`

- Kind: `value`
- Detail: Civ value

Goths

Id: `3`

<a id="symbol-graupel"></a>

## `graupel`

- Kind: `value`
- Detail: MapType value

Graupel map.

Id: `199`

<a id="symbol-graveyards"></a>

## `graveyards`

- Kind: `value`
- Detail: MapType value

Graveyards map. Must be defined with a defconst.

Id: `37`

<a id="symbol-greenland"></a>

## `greenland`

- Kind: `value`
- Detail: MapType value

Greenland map.

Id: `160`

<a id="symbol-group-type-fishing-ship"></a>

## `group-type-fishing-ship`

- Kind: `value`
- Detail: GroupType value

Fishing ships.

Id: `105`

<a id="symbol-group-type-forward-builder"></a>

## `group-type-forward-builder`

- Kind: `value`
- Detail: GroupType value

Villagers tasked to constructing forward buildings.

Id: `107`

<a id="symbol-group-type-land-attack"></a>

## `group-type-land-attack`

- Kind: `value`
- Detail: GroupType value

Land attack groups. Untested, but likely soldiers attacking during attack-group or attack-now attacks.

Id: `100`

<a id="symbol-group-type-land-explore"></a>

## `group-type-land-explore`

- Kind: `value`
- Detail: GroupType value

Land units currently exploring.

Id: `101`

<a id="symbol-group-type-land-trade"></a>

## `group-type-land-trade`

- Kind: `value`
- Detail: GroupType value

Trade carts currently trading.

Id: `109`

<a id="symbol-group-type-monk"></a>

## `group-type-monk`

- Kind: `value`
- Detail: GroupType value

Monks. Untested. Likely either monks gathering relics, monks that are attacking, or both.

Id: `108`

<a id="symbol-group-type-transport-ship"></a>

## `group-type-transport-ship`

- Kind: `value`
- Detail: GroupType value

Transport Ships that aren't idle.

Id: `104`

<a id="symbol-group-type-water-attack"></a>

## `group-type-water-attack`

- Kind: `value`
- Detail: GroupType value

Warship attack groups. Untested, but likely warships attacking during boat-attack-group or attack-now attacks.

Id: `102`

<a id="symbol-group-type-water-explore"></a>

## `group-type-water-explore`

- Kind: `value`
- Detail: GroupType value

Ships currently exploring.

Id: `103`

<a id="symbol-group-type-water-trade"></a>

## `group-type-water-trade`

- Kind: `value`
- Detail: GroupType value

Trade cogs currently trading.

Id: `106`

<a id="symbol-guard-flag-inverse"></a>

## `guard-flag-inverse`

- Kind: `value`
- Detail: GuardFlag value

If guard-flag-resource flag is set, resources will be added only when there are no TypeId objects left. This will not invert guard-flag-victory, only guard-flag-resource.

Id: `4`

<a id="symbol-guard-flag-resource"></a>

## `guard-flag-resource`

- Kind: `value`
- Detail: GuardFlag value

ResourceDelta/100 will slowly be added to ResourceType as long as TypeId objects remain. The ResourceDelta, ResourceType, and TypeId are defined in the guard_state command used in the custom RM script. The TypeId, ResourceDelta, and Resour...

Id: `2`

<a id="symbol-guard-flag-victory"></a>

## `guard-flag-victory`

- Kind: `value`
- Detail: GuardFlag value

AI will be defeated if no TypeId objects remain. The TypeId is defined in the guard_state command used in the custom RM script, and it is stored in the first goal value returned from up-get-guard-state.

Id: `1`

<a id="symbol-gurjaras"></a>

## `gurjaras`

- Kind: `value`
- Detail: Civ value

Gurjaras.

Id: `42`

<a id="symbol-haboob"></a>

## `haboob`

- Kind: `value`
- Detail: MapType value

Haboob map.

Id: `170`

<a id="symbol-hamburger"></a>

## `hamburger`

- Kind: `value`
- Detail: MapType value

Hamburger map.

Id: `78`

<a id="symbol-hard"></a>

## `hard`

- Kind: `value`
- Detail: Difficulty value

Hard difficulty.

Id: `1`

<a id="symbol-hardest"></a>

## `hardest`

- Kind: `value`
- Detail: Difficulty value

Hardest difficulty.

Id: `0`

<a id="symbol-hengehold"></a>

## `hengehold`

- Kind: `value`
- Detail: MapType value

Hengehold map.

Id: `210`

<a id="symbol-hideout"></a>

## `hideout`

- Kind: `value`
- Detail: MapType value

Hideout map.

Id: `72`

<a id="symbol-high-resources"></a>

## `high-resources`

- Kind: `value`
- Detail: StartingResources value

Start with 1000W, 1000F, 700G, and 800S in random map games. Other game modes may have different starting resources.

Id: `3`

<a id="symbol-highland"></a>

## `highland`

- Kind: `value`
- Detail: MapType value

Highland map.

Id: `18`

<a id="symbol-hillfort"></a>

## `hillfort`

- Kind: `value`
- Detail: MapType value

Hill Fort map. Notice the lack of dashes in the name.

Id: `73`

<a id="symbol-hollow-woodlands"></a>

## `hollow-woodlands`

- Kind: `value`
- Detail: MapType value

Hollow Woodlands map.

Id: `186`

<a id="symbol-housing-headroom"></a>

## `housing-headroom`

- Kind: `value`
- Detail: FactId value

The housing headroom. Housing headroom is the difference between current housing capacity and trained unit capacity. The corresponding fact command is housing-headroom.

Id: `3`

<a id="symbol-huge-map-giant"></a>

## `huge-map, giant`

- Kind: `value`
- Detail: MapSize value

Huge map size. 240x240 tiles. "giant" refers to the Huge map size for backwards compatibility with older AIs.

Id: `240`

<a id="symbol-hun"></a>

## `hun`

- Kind: `value`
- Detail: Civ value

Huns

Id: `17`

<a id="symbol-hunting"></a>

## `hunting`

- Kind: `value`
- Detail: Resource value

Boar and Deer. Only available in UP and DE. Can only be used with dropsite-min-distance. For these parameters only, invalid/not-found deer or boar returns 255 instead of -1.

Id: `4`

<a id="symbol-idle-farm-count"></a>

## `idle-farm-count`

- Kind: `value`
- Detail: FactId value

The number of farms with no farmers. The corresponding fact command is idle-farm-count.

Id: `4`

<a id="symbol-idle-pasture-count"></a>

## `idle-pasture-count`

- Kind: `value`
- Detail: FactId value

DE only. Must be defined with a defconst. The amount of idle pastures, with zero herders gathering from it. You can also check the number of idle pastures with fe-idle-pasture-count.

Id: `56`

<a id="symbol-idle-type-fishing-ship"></a>

## `idle-type-fishing-ship`

- Kind: `value`
- Detail: IdleType value

Idle fishing ships.

Id: `2`

<a id="symbol-idle-type-trade-cart"></a>

## `idle-type-trade-cart`

- Kind: `value`
- Detail: IdleType value

Idle trade carts.

Id: `1`

<a id="symbol-idle-type-trade-cog"></a>

## `idle-type-trade-cog`

- Kind: `value`
- Detail: IdleType value

Idle trade cogs.

Id: `3`

<a id="symbol-idle-type-villager"></a>

## `idle-type-villager`

- Kind: `value`
- Detail: IdleType value

Idle villagers.

Id: `0`

<a id="symbol-imperial-age"></a>

## `imperial-age`

- Kind: `value`
- Detail: Age value

Imperial Age.

Id: `3`

<a id="symbol-incan"></a>

## `incan`

- Kind: `value`
- Detail: Civ value

Incas. In WK, must define with a defconst before it can be used.

Id: `21`

<a id="symbol-incredible-map"></a>

## `incredible-map`

- Kind: `value`
- Detail: MapSize value

Incredible map size. 360x360 tiles. Requires MORE_MAP_SIZES Steam launch parameter.

Id: `360`

<a id="symbol-indian"></a>

## `indian`

- Kind: `value`
- Detail: Civ value

Hindustanis (DE) or Indians (for HD or WK only). In WK, must define with a defconst before it can be used. "hindustanis" CANNOT be used instead.

Id: `20`

<a id="symbol-infantry-class"></a>

## `infantry-class`

- Kind: `value`
- Detail: ClassId value

Infantry class.

Id: `906`

<a id="symbol-infinite-resources"></a>

## `infinite-resources`

- Kind: `value`
- Detail: StartingResources value

All resources are infinite. DE only.

Id: `5`

<a id="symbol-islands"></a>

## `islands`

- Kind: `value`
- Detail: MapType value

Islands map.

Id: `19`

<a id="symbol-isthmus"></a>

## `isthmus`

- Kind: `value`
- Detail: MapType value

Isthmus map.

Id: `178`

<a id="symbol-italian"></a>

## `italian`

- Kind: `value`
- Detail: Civ value

Italians. In WK, must define with a defconst before it can be used.

Id: `19`

<a id="symbol-japanese"></a>

## `japanese`

- Kind: `value`
- Detail: Civ value

Japanese

Id: `5`

<a id="symbol-jurchens"></a>

## `jurchens`

- Kind: `value`
- Detail: Civ value

Jurchens (must define with a defconst first).

Id: `52`

<a id="symbol-karsts"></a>

## `karsts`

- Kind: `value`
- Detail: MapType value

Karsts map.

Id: `187`

<a id="symbol-kawasan"></a>

## `kawasan`

- Kind: `value`
- Detail: MapType value

Kawasan map.

Id: `171`

<a id="symbol-khitans"></a>

## `khitans`

- Kind: `value`
- Detail: Civ value

Khitans (must define with a defconst first).

Id: `53`

<a id="symbol-khmer"></a>

## `khmer`

- Kind: `value`
- Detail: Civ value

Khmer. In WK, must define with a defconst before it can be used.

Id: `28`

<a id="symbol-kilimanjaro"></a>

## `kilimanjaro`

- Kind: `value`
- Detail: MapType value

Kilimanjaro map.

Id: `83`

<a id="symbol-king-class-"></a>

## `king-class*`

- Kind: `value`
- Detail: ClassId value

King class.

Id: `959`

<a id="symbol-king-of-the-hill"></a>

## `king-of-the-hill`

- Kind: `value`
- Detail: GameType value

King of the Hill game.

Id: `5`

<a id="symbol-korean"></a>

## `korean`

- Kind: `value`
- Detail: Civ value

Koreans

Id: `18`

<a id="symbol-land-madness"></a>

## `land-madness`

- Kind: `value`
- Detail: MapType value

Land Madness map.

Id: `172`

<a id="symbol-land-nomad"></a>

## `land-nomad`

- Kind: `value`
- Detail: MapType value

Land Nomad map.

Id: `141`

<a id="symbol-large-map-large"></a>

## `large-map, large`

- Kind: `value`
- Detail: MapSize value

Large (8 player) map size. 220x220 tiles.

Id: `220`

<a id="symbol-list-active"></a>

## `list-active`

- Kind: `value`
- Detail: ObjectList value

Contains most objects, especially live objects.

Id: `0`

<a id="symbol-list-inactive"></a>

## `list-inactive`

- Kind: `value`
- Detail: ObjectList value

Contains objects that are removed from the active list for performance optimization. Examples are fish, dead animals carrying food, and maybe house foundations. Chopped trees are usually list-active.

Id: `1`

<a id="symbol-lithuanians"></a>

## `lithuanians`

- Kind: `value`
- Detail: Civ value

Lithuanians.

Id: `35`

<a id="symbol-live-boar"></a>

## `live-boar`

- Kind: `value`
- Detail: Resource value

Live boar only. Only available in UP and DE. Dead boars not included. Can only be used with dropsite-min-distance. For these parameters only, invalid/not-found live boar returns 255 instead of -1.

Id: `7`

<a id="symbol-livestock-class"></a>

## `livestock-class`

- Kind: `value`
- Detail: ClassId value

Livestock class.

Id: `958`

<a id="symbol-loch-ness"></a>

## `loch-ness`

- Kind: `value`
- Detail: MapType value

Loch Ness map. Must be defined with a defconst.

Id: `211`

<a id="symbol-lombardia"></a>

## `lombardia`

- Kind: `value`
- Detail: MapType value

Lombardia map.

Id: `74`

<a id="symbol-low-resources"></a>

## `low-resources`

- Kind: `value`
- Detail: StartingResources value

Start with 200W, 200F, 100G, and 200S in random map games. Other game modes may have different starting resources. Same as standard resources start.

Id: `1`

<a id="symbol-lowland"></a>

## `lowland`

- Kind: `value`
- Detail: MapType value

Lowland map.

Id: `161`

<a id="symbol-ludicrous-map-ludicrous-ludikris"></a>

## `ludicrous-map, ludicrous, ludikris`

- Kind: `value`
- Detail: MapSize value

Ludicrous map size. 480x480 tiles for most maps.

Id: `480`

<a id="symbol-macedonians"></a>

## `macedonians`

- Kind: `value`
- Detail: Civ value

Macedonians (must define with a defconst first).

Id: `54`

<a id="symbol-magyar"></a>

## `magyar`

- Kind: `value`
- Detail: Civ value

Magyars. In WK, must define with a defconst before it can be used.

Id: `22`

<a id="symbol-malay"></a>

## `malay`

- Kind: `value`
- Detail: Civ value

Malay. In WK, must define with a defconst before it can be used.

Id: `29`

<a id="symbol-malian"></a>

## `malian`

- Kind: `value`
- Detail: Civ value

Malians. In WK, must define with a defconst before it can be used.

Id: `26`

<a id="symbol-mangrove-jungle"></a>

## `mangrove-jungle`

- Kind: `value`
- Detail: MapType value

Mangrove Jungle map.

Id: `113`

<a id="symbol-mapuche"></a>

## `mapuche`

- Kind: `value`
- Detail: Civ value

Mapuche (must define with a defconst first).

Id: `58`

<a id="symbol-marketplace"></a>

## `marketplace`

- Kind: `value`
- Detail: MapType value

Marketplace map.

Id: `162`

<a id="symbol-massive-map"></a>

## `massive-map`

- Kind: `value`
- Detail: MapSize value

Massive map size. 276x276 tiles. Requires MORE_MAP_SIZES Steam launch parameter.

Id: `276`

<a id="symbol-mayan"></a>

## `mayan`

- Kind: `value`
- Detail: Civ value

Mayans

Id: `16`

<a id="symbol-meadow"></a>

## `meadow`

- Kind: `value`
- Detail: MapType value

Meadow map.

Id: `163`

<a id="symbol-mediterranean"></a>

## `mediterranean`

- Kind: `value`
- Detail: MapType value

Mediterranean map.

Id: `20`

<a id="symbol-medium-map-medium"></a>

## `medium-map, medium`

- Kind: `value`
- Detail: MapSize value

Medium (4 player) map size. 168x168 tiles.

Id: `168`

<a id="symbol-medium-resources"></a>

## `medium-resources`

- Kind: `value`
- Detail: StartingResources value

Start with 500W, 500F, 300G, and 400S in random map games. Other game modes may have different starting resources.

Id: `2`

<a id="symbol-megarandom"></a>

## `megarandom`

- Kind: `value`
- Detail: MapType value

Megarandom map.

Id: `77`

<a id="symbol-metropolis"></a>

## `metropolis`

- Kind: `value`
- Detail: MapType value

Metropolis map. Must be defined with a defconst.

Id: `38`

<a id="symbol-migration"></a>

## `migration`

- Kind: `value`
- Detail: MapType value

Migration map.

Id: `21`

<a id="symbol-military-population"></a>

## `military-population`

- Kind: `value`
- Detail: FactId value

The player's military population, including monks and Transport Ships. The corresponding fact commands are military-population and players-military-population.

Id: `31`

<a id="symbol-miniature-map"></a>

## `miniature-map`

- Kind: `value`
- Detail: MapSize value

Miniature map size. 80x80 tiles. Requires MORE_MAP_SIZES Steam launch parameter.

Id: `80`

<a id="symbol-mired"></a>

## `Mired`

- Kind: `value`
- Detail: MapType value

Mired map. Notice the capitalized M.

Id: `205`

<a id="symbol-miscellaneous-class-"></a>

## `miscellaneous-class*`

- Kind: `value`
- Detail: ClassId value

Miscellaneous class. Includes flares. Mostly dead versions of units and eye candy.

Id: `911`

<a id="symbol-moats"></a>

## `moats`

- Kind: `value`
- Detail: MapType value

Moats map. Must be defined with a defconst.

Id: `39`

<a id="symbol-moderate"></a>

## `moderate`

- Kind: `value`
- Detail: Difficulty value

Moderate difficulty.

Id: `2`

<a id="symbol-monastery-class"></a>

## `monastery-class`

- Kind: `value`
- Detail: ClassId value

Monastery class. Includes monks and missionaries. Doesn't include monasteries. Doesn't include monks carrying relics.

Id: `918`

<a id="symbol-mongol"></a>

## `mongol`

- Kind: `value`
- Detail: Civ value

Mongols

Id: `12`

<a id="symbol-mongolia"></a>

## `mongolia`

- Kind: `value`
- Detail: MapType value

Mongolia map.

Id: `26`

<a id="symbol-monk-with-relic-class-"></a>

## `monk-with-relic-class*`

- Kind: `value`
- Detail: ClassId value

Monk With Relic class.

Id: `943`

<a id="symbol-monstrous-map"></a>

## `monstrous-map`

- Kind: `value`
- Detail: MapSize value

Monstrous map size. 400x400 tiles. Requires MORE_MAP_SIZES Steam launch parameter.

Id: `400`

<a id="symbol-monument-class-"></a>

## `monument-class*`

- Kind: `value`
- Detail: ClassId value

Monument class. Mostly includes convertible objects like Monuments.

Id: `901`

<a id="symbol-morass"></a>

## `morass`

- Kind: `value`
- Detail: MapType value

Morass map.

Id: `175`

<a id="symbol-mountain-dunes"></a>

## `mountain-dunes`

- Kind: `value`
- Detail: MapType value

Mountain Dunes map.

Id: `181`

<a id="symbol-mountain-pass"></a>

## `mountain-pass`

- Kind: `value`
- Detail: MapType value

Mountain Pass map.

Id: `84`

<a id="symbol-mountain-range"></a>

## `mountain-range`

- Kind: `value`
- Detail: MapType value

Mountain Range map.

Id: `164`

<a id="symbol-mountain-ridge"></a>

## `mountain-ridge`

- Kind: `value`
- Detail: MapType value

Mountain Ridge map. Must be defined with a defconst.

Id: `124`

<a id="symbol-muisca"></a>

## `muisca`

- Kind: `value`
- Detail: Civ value

Muisca (must define with a defconst first).

Id: `57`

<a id="symbol-murkwood"></a>

## `Murkwood`

- Kind: `value`
- Detail: MapType value

Murkwood map. Notice the capitalized M.

Id: `206`

<a id="symbol-neutral"></a>

## `neutral`

- Kind: `value`
- Detail: PlayerStance value

Neutral.

Id: `1`

<a id="symbol-nile-delta"></a>

## `nile-delta`

- Kind: `value`
- Detail: MapType value

Nile Delta map.

Id: `85`

<a id="symbol-nomad"></a>

## `nomad`

- Kind: `value`
- Detail: MapType value

Nomad map.

Id: `33`

<a id="symbol-normal-map-normal"></a>

## `normal-map, normal`

- Kind: `value`
- Detail: MapSize value

Normal (6 player) map size. 200x200 tiles.

Id: `200`

<a id="symbol-northern-isles"></a>

## `northern-isles`

- Kind: `value`
- Detail: MapType value

Northern Isles map.

Id: `165`

<a id="symbol-oasis"></a>

## `oasis`

- Kind: `value`
- Detail: MapType value

Oasis map.

Id: `31`

<a id="symbol-object-data-action"></a>

## `object-data-action`

- Kind: `value`
- Detail: ObjectData value

The object's action. See ActionId for a description and list of object action IDs. This data is NOT available for units marching in formation. When the objects is idle or marching in formation, this data returns -1.

Id: `5`

<a id="symbol-object-data-action-time"></a>

## `object-data-action-time`

- Kind: `value`
- Detail: ObjectData value

The game time in milliseconds when the object's most recently moved. In UP, it was reported that attacking an object could reset this to 0, so it's possible that this object data works differently in UP.

Id: `22`

<a id="symbol-object-data-atonement"></a>

## `object-data-atonement`

- Kind: `value`
- Detail: ObjectData value

Returns 1 if the object is benefitting from Atonement, otherwise 0.

Id: `67`

<a id="symbol-object-data-attack-count"></a>

## `object-data-attack-count`

- Kind: `value`
- Detail: ObjectData value

The number of times the object has tried to damage its most recent target. This number is not reset to 0 until a new target has been found. If the object has never targeted anything, this returns 0.

Id: `79`

<a id="symbol-object-data-attack-delay-"></a>

## `object-data-attack-delay*`

- Kind: `value`
- Detail: ObjectData value

DE only. The object's attack delay in milliseconds. Damage is not dealt at the start of a unit's attack animation, but instead they have an attack delay. For ranged units, the attack delay is equal to: (object-data-frame-delay / Number Att...

Id: `90`

<a id="symbol-object-data-attack-stance"></a>

## `object-data-attack-stance`

- Kind: `value`
- Detail: ObjectData value

The attack stance of the object. See AttackStance for a list of attack stances. Objects that cannot change their attack stance appear to have an attack stance of 0, the same as stance-aggressive.

Id: `21`

<a id="symbol-object-data-attack-timer"></a>

## `object-data-attack-timer`

- Kind: `value`
- Detail: ObjectData value

Likely a timer countdown for building objects. When a building is attacked, a 60-second timer starts and counts down toward 0. This timer is reset every time the building is attacked. Non-building objects always return 0.

Id: `36`

<a id="symbol-object-data-attacker-count"></a>

## `object-data-attacker-count`

- Kind: `value`
- Detail: ObjectData value

The number of objects that are attacking the object. Ranged units are only counted when a projectile is actively flying through the air toward the unit. Melee units are only counted after they have caused damage and will continue to be cou...

Id: `33`

<a id="symbol-object-data-attacker-id"></a>

## `object-data-attacker-id`

- Kind: `value`
- Detail: ObjectData value

The map-based Id of the enemy unit or building that is attacking the object. If multiple objects are attacking, it's either the object that most recently attacked or the attacker with the lowest map-based ID. When attacked by ranged units,...

Id: `34`

<a id="symbol-object-data-auto-heal"></a>

## `object-data-auto-heal`

- Kind: `value`
- Detail: ObjectData value

Returns 1 if the object is a full hero (hero flag 1) or it has the auto-heal hero flag set (hero flag 4, see object-data-hero-flags for details). Berserks return 0 because their health regeneration is coded separately from hero health rege...

Id: `76`

<a id="symbol-object-data-ballistics"></a>

## `object-data-ballistics`

- Kind: `value`
- Detail: ObjectData value

Returns 1 if the projectile the object fires is benefitting from Ballistics, otherwise 0.

Id: `70`

<a id="symbol-object-data-base-attack"></a>

## `object-data-base-attack`

- Kind: `value`
- Detail: ObjectData value

The object's current base attack, including researched technologies and civ bonuses. Attack bonus amounts are not included and cannot be detected by AIs. :(

Id: `28`

<a id="symbol-object-data-base-type"></a>

## `object-data-base-type`

- Kind: `value`
- Detail: ObjectData value

The ObjectId of the first unit/building in the object's line. For example, this returns 74 (militiaman) when the object is a Long Swordsman.

Id: `81`

<a id="symbol-object-data-blast-level"></a>

## `object-data-blast-level`

- Kind: `value`
- Detail: ObjectData value

The type of blast radius the object has. The blast damage for objects with level 3 or higher only damage the targeted object. The blast damage for objects with level 2 will damage nearby objects that are within the blast radius of the atta...

Id: `59`

<a id="symbol-object-data-blast-radius"></a>

## `object-data-blast-radius`

- Kind: `value`
- Detail: ObjectData value

The object's blast radius, multiplied by 100. This includes researched technologies and civ bonuses.

Id: `58`

<a id="symbol-object-data-capture-flag-"></a>

## `object-data-capture-flag*`

- Kind: `value`
- Detail: ObjectData value

DE only. Must be defined with a defconst before use with (defconst object-data-capture-flag 84). The capture type of an object owned by gaia or another player. 0 = capture never, 1 = capture once, 2 = capture multiple times, 3 = capture li...

Id: `84`

<a id="symbol-object-data-carry"></a>

## `object-data-carry`

- Kind: `value`
- Detail: ObjectData value

The amount of resources an object is carrying. This includes the amount of resources a villager is holding, the amount of food left in decaying animals, monk faith generation, flares, and unit corpses. It does not include resources that tr...

Id: `16`

<a id="symbol-object-data-category"></a>

## `object-data-category`

- Kind: `value`
- Detail: ObjectData value

The object's category. Use <a href=http://aok.heavengames.com/blacksmith/showfile.php?fileid=11002>Advanced Genie Editor</a> to determine an object's category (called &quot;Type&quot;). Category 10 = Eye Candy and resources. Category 20 = ...

Id: `3`

<a id="symbol-object-data-charge-attack-amount-"></a>

## `object-data-charge-attack-amount*`

- Kind: `value`
- Detail: ObjectData value

DE only. Must be defined with a defconst before use with (defconst object-data-charge-attack-amount 87). Gets the selected object current charge attack amount (x100). Returns -2 on UP or WK.

Id: `87`

<a id="symbol-object-data-charge-attack-event-type-"></a>

## `object-data-charge-attack-event-type*`

- Kind: `value`
- Detail: ObjectData value

DE only. Must be defined with a defconst before use with (defconst object-data-charge-attack-event-type 89). Gets the charge attack event type. Returns -2 on UP or WK.

Id: `89`

<a id="symbol-object-data-charge-attack-max-"></a>

## `object-data-charge-attack-max*`

- Kind: `value`
- Detail: ObjectData value

DE only. Gets the maximum charge attack value (x100). Returns -2 on UP or WK.

Id: `86`

<a id="symbol-object-data-charge-attack-regeneration-rate-"></a>

## `object-data-charge-attack-regeneration-rate*`

- Kind: `value`
- Detail: ObjectData value

DE only. Must be defined with a defconst before use with (defconst object-data-charge-attack-regeneration-rate 88). Gets the regeneration rate of a charge attack (x100). Returns -2 on UP or WK.

Id: `88`

<a id="symbol-object-data-charge-attack-type-"></a>

## `object-data-charge-attack-type*`

- Kind: `value`
- Detail: ObjectData value

DE only. Must be defined with a defconst before use with (defconst object-data-charge-attack-type 85). Gets the charge attack type. Returns -2 on UP or WK.

Id: `85`

<a id="symbol-object-data-class"></a>

## `object-data-class`

- Kind: `value`
- Detail: ObjectData value

The object's class. See ClassId for a description and list of object classes.

Id: `2`

<a id="symbol-object-data-cmdid"></a>

## `object-data-cmdid`

- Kind: `value`
- Detail: ObjectData value

The object's command ID. See CmdId for a description and list of object command IDs.

Id: `4`

<a id="symbol-object-data-distance"></a>

## `object-data-distance`

- Kind: `value`
- Detail: ObjectData value

The object's distance from the target-point. This does not take obstacles into account. It is simply a distance formula calculation between the target point's location and the object's location. Do not use object-data-distance with a preci...

Id: `44`

<a id="symbol-object-data-dropsite"></a>

## `object-data-dropsite`

- Kind: `value`
- Detail: ObjectData value

The UnitId of the dropsite that belongs to the resource that is being gathered by the object. This will always be the UnitId of a mill, lumber camp, and mining camp for food, wood, and gold/stone, even if resources are being dropped off at...

Id: `14`

<a id="symbol-object-data-faith"></a>

## `object-data-faith`

- Kind: `value`
- Detail: ObjectData value

Returns 1 if the object is benefitting from Faith, otherwise 0.

Id: `65`

<a id="symbol-object-data-formation-id"></a>

## `object-data-formation-id`

- Kind: `value`
- Detail: ObjectData value

The formation of the object. Unfortunately, this object data doesn't match Formation and it seems to be able to change depending on the object's action, even if the formation type isn't changed. When not marching in formation, this returns...

Id: `24`

<a id="symbol-object-data-frame-delay"></a>

## `object-data-frame-delay`

- Kind: `value`
- Detail: ObjectData value

The object's frame delay. Frame delay is the number of graphics frames between the start of the attack animation and the launch of the projectile. Unfortunately, the duration of each frame in the animation is different for each unit, so it...

Id: `78`

<a id="symbol-object-data-full-distance"></a>

## `object-data-full-distance`

- Kind: `value`
- Detail: ObjectData value

The object's precise distance from the target-point, squared. For example, if the precise distance is 41.34 tiles, object-data-full-distance will be 1709.

Id: `46`

<a id="symbol-object-data-garrison-count"></a>

## `object-data-garrison-count`

- Kind: `value`
- Detail: ObjectData value

The number of units garrisoned inside the object.

Id: `18`

<a id="symbol-object-data-garrison-id"></a>

## `object-data-garrison-id`

- Kind: `value`
- Detail: ObjectData value

Unknown. Doesn't seem to be the map-based Id of the building or unit the object is garrisoned inside. If the object is not garrisoned, object-data-garrison-id is -2.

Id: `30`

<a id="symbol-object-data-garrisoned"></a>

## `object-data-garrisoned`

- Kind: `value`
- Detail: ObjectData value

Returns 1 if the object is garrisoned. Otherwise, 0.

Id: `17`

<a id="symbol-object-data-gather-type"></a>

## `object-data-gather-type`

- Kind: `value`
- Detail: ObjectData value

The Resource that the villager is gathering, or -1 if the object isn't gathering a resource. Trade units return 3 when they are carrying gold back to the Market or Dock. Monasteries don't return 3 when relics are garrisoned inside. In DE, ...

Id: `71`

<a id="symbol-object-data-group-flag"></a>

## `object-data-group-flag`

- Kind: `value`
- Detail: ObjectData value

The group number that the object has been assigned with up-modify-group-flag. If the object hasn't been assigned to a group, object-data-group-flag returns -2.

Id: `73`

<a id="symbol-object-data-heresy"></a>

## `object-data-heresy`

- Kind: `value`
- Detail: ObjectData value

Returns 1 if the object is benefitting from Heresy, otherwise 0.

Id: `64`

<a id="symbol-object-data-hero"></a>

## `object-data-hero`

- Kind: `value`
- Detail: ObjectData value

Returns 1 if the object is a hero (has hero flag 1 set, see object-data-hero-flags for details), otherwise 0.

Id: `75`

<a id="symbol-object-data-hero-flags"></a>

## `object-data-hero-flags`

- Kind: `value`
- Detail: ObjectData value

The sum of hero flags set on the unit. Most of these, except for Flag 1 are set through UP effects in scenarios or random map scripts. Standard heroes return 1. Flag 1 = full hero. Flag 2 = disabled conversions. Flag 4 = enable hero heal r...

Id: `74`

<a id="symbol-object-data-hitpoints"></a>

## `object-data-hitpoints`

- Kind: `value`
- Detail: ObjectData value

The object's current hit points. This takes into account any damage the object has suffered.

Id: `10`

<a id="symbol-object-data-id"></a>

## `object-data-id`

- Kind: `value`
- Detail: ObjectData value

The object's map ID. All objects on the map will have a different map object ID in the order that the object appeared on the map. Same as the Id parameter.

Id: `0`

<a id="symbol-object-data-idling"></a>

## `object-data-idling`

- Kind: `value`
- Detail: ObjectData value

Returns 1 if the object is idle, otherwise 0. Does not work with villagers.

Id: `49`

<a id="symbol-object-data-index"></a>

## `object-data-index`

- Kind: `value`
- Detail: ObjectData value

Use only with up-remove-objects. This will remove objects by the search index. Returns -2 for up-get-object-data and up-object-data.

Id: `-1`

<a id="symbol-object-data-language-id"></a>

## `object-data-language-id`

- Kind: `value`
- Detail: ObjectData value

The pLanguageId of the object's current name. This is one way to determine the task a villager has been given.

Id: `72`

<a id="symbol-object-data-locked"></a>

## `object-data-locked`

- Kind: `value`
- Detail: ObjectData value

Returns 1 if the gate object (gate or palisade gate) is locked, otherwise 0. Non-gate objects return -2.

Id: `29`

<a id="symbol-object-data-map-zone-id"></a>

## `object-data-map-zone-id`

- Kind: `value`
- Detail: ObjectData value

The map zone that the object is on. Each landmass is assigned a different zone ID, so this is useful to determine if objects are on different islands.

Id: `47`

<a id="symbol-object-data-maxhp"></a>

## `object-data-maxhp`

- Kind: `value`
- Detail: ObjectData value

The object's maximum possible hit points. This includes researched technologies and civ bonuses.

Id: `11`

<a id="symbol-object-data-min-range"></a>

## `object-data-min-range`

- Kind: `value`
- Detail: ObjectData value

The minium range of the object. This includes researched technologies and civ bonuses.

Id: `62`

<a id="symbol-object-data-move-x"></a>

## `object-data-move-x`

- Kind: `value`
- Detail: ObjectData value

The x-coordinate of the object's most recent targeted location. Applies to move, attack, and other related commands. Automatic activities such as chasing enemy units will not set a new location because a direct command was never issued. If...

Id: `50`

<a id="symbol-object-data-move-y"></a>

## `object-data-move-y`

- Kind: `value`
- Detail: ObjectData value

The y-coordinate of the object's most recent targeted location. Applies to move, attack, and other related commands. Automatic activities such as chasing enemy units will not set a new location because a direct command was never issued. If...

Id: `51`

<a id="symbol-object-data-next-attack"></a>

## `object-data-next-attack`

- Kind: `value`
- Detail: ObjectData value

The time until the object can attack again, in milliseconds. The time is a countdown that starts at the object's object-data-reload-time and counts down to 0. The countdown begins at the start of the unit's attack animation. One important ...

Id: `55`

<a id="symbol-object-data-no-convert"></a>

## `object-data-no-convert`

- Kind: `value`
- Detail: ObjectData value

Returns 1 if the object is a full hero (hero flag 1) or it has the no-convert flag set (hero flag 2, see object-data-hero-flags for details). Unconvertible buildings like town centers and castles return 0 because their no-convert feature i...

Id: `77`

<a id="symbol-object-data-on-mainland"></a>

## `object-data-on-mainland`

- Kind: `value`
- Detail: ObjectData value

Returns 1 if the object is on the same landmass as the starting landmass, otherwise 0.

Id: `48`

<a id="symbol-object-data-order"></a>

## `object-data-order`

- Kind: `value`
- Detail: ObjectData value

The object's order. See OrderId for a description and list of object order IDs. This data is NOT available for units marching in formation. When the object is not executing an order or marching in formation, this data returns -1.

Id: `6`

<a id="symbol-object-data-ownership-"></a>

## `object-data-ownership*`

- Kind: `value`
- Detail: ObjectData value

DE only. Must be defined with a defconst before use with (defconst object-data-ownership 83). Returns the player number that owns the object or is the most dominant player nearby. Returns -2 if the object cannot be captured. Returns -1 if ...

Id: `83`

<a id="symbol-object-data-patrolling"></a>

## `object-data-patrolling`

- Kind: `value`
- Detail: ObjectData value

Returns 1 if the object is patrolling, otherwise 0. This data is not affected by snEnablePatrolAttack.

Id: `25`

<a id="symbol-object-data-pierce-armor"></a>

## `object-data-pierce-armor`

- Kind: `value`
- Detail: ObjectData value

The object's current pierce armor, including researched technologies and civ bonuses.

Id: `27`

<a id="symbol-object-data-player"></a>

## `object-data-player`

- Kind: `value`
- Detail: ObjectData value

The player number that the object belongs to, between 0 and 8.

Id: `20`

<a id="symbol-object-data-point-x"></a>

## `object-data-point-x`

- Kind: `value`
- Detail: ObjectData value

The x-coordinate of the tile the object is on.

Id: `8`

<a id="symbol-object-data-point-y"></a>

## `object-data-point-y`

- Kind: `value`
- Detail: ObjectData value

The y-coordinate of the tile the object is on.

Id: `9`

<a id="symbol-object-data-point-z"></a>

## `object-data-point-z`

- Kind: `value`
- Detail: ObjectData value

Likely get's the object's z-location. Only objects flying in the air like projectiles and birds have a z-coordinate > 0.

Id: `37`

<a id="symbol-object-data-precise-distance"></a>

## `object-data-precise-distance`

- Kind: `value`
- Detail: ObjectData value

The object's precise distance from the target-point, x 100. This does not take obstacles into account. Precise locations are accurate to 1/100 of a tile. It is simply a distance formula calculation between the target point's location and t...

Id: `45`

<a id="symbol-object-data-precise-move-x"></a>

## `object-data-precise-move-x`

- Kind: `value`
- Detail: ObjectData value

The precise x-coordinate of the object's most recent targeted location, multiplied by 100. Precise locations are accurate to 1/100 of a tile. Applies to move, attack, and other related commands. Automatic activities such as chasing enemy u...

Id: `52`

<a id="symbol-object-data-precise-move-y"></a>

## `object-data-precise-move-y`

- Kind: `value`
- Detail: ObjectData value

The precise y-coordinate of the object's most recent targeted location, multiplied by 100. Precise locations are accurate to 1/100 of a tile. Applies to move, attack, and other related commands. Automatic activities such as chasing enemy u...

Id: `53`

<a id="symbol-object-data-precise-x"></a>

## `object-data-precise-x`

- Kind: `value`
- Detail: ObjectData value

The object's precise x-location, multiplied by 100. Precise locations are accurate to 1/100 of a tile.

Id: `38`

<a id="symbol-object-data-precise-y"></a>

## `object-data-precise-y`

- Kind: `value`
- Detail: ObjectData value

The object's precise y-location, multiplied by 100. Precise locations are accurate to 1/100 of a tile.

Id: `39`

<a id="symbol-object-data-precise-z"></a>

## `object-data-precise-z`

- Kind: `value`
- Detail: ObjectData value

The object's precise z-location, multiplied by 100. Precise locations are accurate to 1/100 of a tile. Only objects flying in the air like projectiles and birds have a z-coordinate > 0.

Id: `40`

<a id="symbol-object-data-progress-type"></a>

## `object-data-progress-type`

- Kind: `value`
- Detail: ObjectData value

The type of progress the object has (training or researching). Objects that cannot train or research return -2. An object that can train or research but is doing neither will return 0. If the object is training or researching, a value from...

Id: `60`

<a id="symbol-object-data-progress-value"></a>

## `object-data-progress-value`

- Kind: `value`
- Detail: ObjectData value

The percent completion for the unit the object is training or the technology the object is researching. Objects that cannot train or research return -2.

Id: `61`

<a id="symbol-object-data-range"></a>

## `object-data-range`

- Kind: `value`
- Detail: ObjectData value

The object's range. This includes researched technologies and civ bonuses.

Id: `12`

<a id="symbol-object-data-redemption"></a>

## `object-data-redemption`

- Kind: `value`
- Detail: ObjectData value

Returns 1 if the object is benefitting from Redemption, otherwise 0.

Id: `66`

<a id="symbol-object-data-reload-time"></a>

## `object-data-reload-time`

- Kind: `value`
- Detail: ObjectData value

The object's reload time, in milliseconds. This is the time between subsequent attacks. This includes researched technologies and civ bonuses. For the time remaining until the unit can attack again, use object-data-next-attack.

Id: `54`

<a id="symbol-object-data-researching"></a>

## `object-data-researching`

- Kind: `value`
- Detail: ObjectData value

Returns 1 when the object is researching a technology, otherwise 0. Objects that cannot research technologies return -2.

Id: `41`

<a id="symbol-object-data-resource"></a>

## `object-data-resource`

- Kind: `value`
- Detail: ObjectData value

The object's Resource type. If the object isn't a resource, object-data-resource is -1.

Id: `15`

<a id="symbol-object-data-speed"></a>

## `object-data-speed`

- Kind: `value`
- Detail: ObjectData value

The object's speed, multiplied by 100. This includes researched technologies and civ bonuses. In UP, deer and wolves return their walking speed, even when running. In DE, deer and wolves return different speeds depending on whether they ar...

Id: `13`

<a id="symbol-object-data-spies"></a>

## `object-data-spies`

- Kind: `value`
- Detail: ObjectData value

Returns 1 if the object is benefitting from Spies, otherwise 0. Likely is true for all player objects once Spies is researched.

Id: `69`

<a id="symbol-object-data-status"></a>

## `object-data-status`

- Kind: `value`
- Detail: ObjectData value

The status of the object. See ObjectStatus for a list of possible object states.

Id: `19`

<a id="symbol-object-data-strike-armor"></a>

## `object-data-strike-armor`

- Kind: `value`
- Detail: ObjectData value

The object's current strike (melee) armor, including researched technologies and civ bonuses.

Id: `26`

<a id="symbol-object-data-target"></a>

## `object-data-target`

- Kind: `value`
- Detail: ObjectData value

The object-data-class of the object that the object is targeting. This data is NOT available for units marching in formation. In UP, when the object is not targeting anything or is marching in formation toward the target, this data returns...

Id: `7`

<a id="symbol-object-data-target-id"></a>

## `object-data-target-id`

- Kind: `value`
- Detail: ObjectData value

The ID of the object that the object is targeting. This data is NOT available for units marching in formation. When an object is not targeting anything or is marching in formation, this data returns -1.

Id: `23`

<a id="symbol-object-data-target-time"></a>

## `object-data-target-time`

- Kind: `value`
- Detail: ObjectData value

The amount of time, in milliseconds, that the object has been attacking its current target. Also seems to return negative amounts when a villager is herding animals for some reason. Objects that aren't attacking return -2.

Id: `63`

<a id="symbol-object-data-tasks-count"></a>

## `object-data-tasks-count`

- Kind: `value`
- Detail: ObjectData value

The number of units that are tasked to work on the object (sometimes 2+ per command, for example a lumberjack assigned to a tree may show 2 when the lumberjack is walking with a gather command/hunt command).

Id: `32`

<a id="symbol-object-data-theocracy"></a>

## `object-data-theocracy`

- Kind: `value`
- Detail: ObjectData value

Returns 1 if the object is benefitting from Theocracy, otherwise 0.

Id: `68`

<a id="symbol-object-data-tile-inverse"></a>

## `object-data-tile-inverse`

- Kind: `value`
- Detail: ObjectData value

The opposite tile position of the object's position on the tile. If the object is on the top part of the tile (position 2), object-data-tile-inverse will be 4 (bottom). See snTargetPointAdjustment for details on the tile positions.

Id: `43`

<a id="symbol-object-data-tile-position"></a>

## `object-data-tile-position`

- Kind: `value`
- Detail: ObjectData value

The object's position on the tile. See snTargetPointAdjustment for details on the tile positions.

Id: `42`

<a id="symbol-object-data-to-precise"></a>

## `object-data-to-precise`

- Kind: `value`
- Detail: ObjectData value

The precise distance from the object to the target point, x 100, assuming the target point is a precise point. This does not take obstacles into account. Precise locations are accurate to 1/100 of a tile. It is simply a distance formula ca...

Id: `80`

<a id="symbol-object-data-train-count"></a>

## `object-data-train-count`

- Kind: `value`
- Detail: ObjectData value

The number of units are queued at the object for training, including the unit currently being trained. Objects that cannot train units return -2.

Id: `31`

<a id="symbol-object-data-train-site"></a>

## `object-data-train-site`

- Kind: `value`
- Detail: ObjectData value

The BuildingId that can train the object.

Id: `56`

<a id="symbol-object-data-train-time"></a>

## `object-data-train-time`

- Kind: `value`
- Detail: ObjectData value

The time it takes to train the object, assuming the object's train site has a "work rate" of 1.0. This does not take into account technologies like Conscription or civ bonuses which train units faster by increasing the building's work rate...

Id: `57`

<a id="symbol-object-data-type"></a>

## `object-data-type`

- Kind: `value`
- Detail: ObjectData value

The object's type, just like unit-type-count. <strong>Note:</strong> this always returns the object-data-base-type for a unit/building line in non-scenario games. For example, if the object is a man-at-arms, this will return 74 (militiaman...

Id: `1`

<a id="symbol-object-data-under-attack"></a>

## `object-data-under-attack`

- Kind: `value`
- Detail: ObjectData value

Returns 1 if the object is being attacked, otherwise 0. When attacked by ranged units, this data returns 1 only after the projectile is launched, but when attacked by melee units this data returns 1 only after the melee unit causes damage....

Id: `35`

<a id="symbol-object-data-upgrade-type"></a>

## `object-data-upgrade-type`

- Kind: `value`
- Detail: ObjectData value

The true ObjectId of the object. If the object is a man-at-arms, this will return 75 (man-at-arms). This ObjectData was needed because object-data-type functions just like object-data-base-type under in non-scenario games.

Id: `82`

<a id="symbol-ocean-fish-class"></a>

## `ocean-fish-class`

- Kind: `value`
- Detail: ClassId value

Ocean fish class. Excludes shore fish.

Id: `905`

<a id="symbol-orderid-attack"></a>

## `orderid-attack`

- Kind: `value`
- Detail: OrderId value

The object has targeted an enemy object.

Id: `700`

<a id="symbol-orderid-build"></a>

## `orderid-build`

- Kind: `value`
- Detail: OrderId value

The object is currently tasked with constructing a building.

Id: `702`

<a id="symbol-orderid-convert"></a>

## `orderid-convert`

- Kind: `value`
- Detail: OrderId value

The object is tasked to convert an object.

Id: `704`

<a id="symbol-orderid-defend"></a>

## `orderid-defend`

- Kind: `value`
- Detail: OrderId value

The object has been ordered to defend. Occurs during guard orders, but could occur at other times. Haven't tested if this order occurs during TSA.

Id: `701`

<a id="symbol-orderid-enter"></a>

## `orderid-enter`

- Kind: `value`
- Detail: OrderId value

The object is being ordered to garrison inside a building, ram, or a transport ship. It may also include objects that are currently garrisoned.

Id: `717`

<a id="symbol-orderid-evade"></a>

## `orderid-evade`

- Kind: `value`
- Detail: OrderId value

The object is being ordered to evade. Could be units dodging missiles because of dpAbilityToDodgeMissiles.

Id: `716`

<a id="symbol-orderid-explore"></a>

## `orderid-explore`

- Kind: `value`
- Detail: OrderId value

The object is being tasked to explore, likely through snNumberExploreGroups.

Id: `705`

<a id="symbol-orderid-follow"></a>

## `orderid-follow`

- Kind: `value`
- Detail: OrderId value

The object is being orderd to follow.

Id: `712`

<a id="symbol-orderid-gather"></a>

## `orderid-gather`

- Kind: `value`
- Detail: OrderId value

The object has been ordered to gather resources.

Id: `709`

<a id="symbol-orderid-heal"></a>

## `orderid-heal`

- Kind: `value`
- Detail: OrderId value

The object is currently tasked with healing objects. Likely doesn't apply to buildings helping garrisoned units heal.

Id: `703`

<a id="symbol-orderid-hunt"></a>

## `orderid-hunt`

- Kind: `value`
- Detail: OrderId value

The object is being ordered to hunt. Untested if this also includes attacking wolves.

Id: `713`

<a id="symbol-orderid-move"></a>

## `orderid-move`

- Kind: `value`
- Detail: OrderId value

The object is being tasked to move.

Id: `710`

<a id="symbol-orderid-patrol"></a>

## `orderid-patrol`

- Kind: `value`
- Detail: OrderId value

The object is being ordered to patrol.

Id: `711`

<a id="symbol-orderid-relic"></a>

## `orderid-relic`

- Kind: `value`
- Detail: OrderId value

The object is ordered with picking up a relic.

Id: `731`

<a id="symbol-orderid-repair"></a>

## `orderid-repair`

- Kind: `value`
- Detail: OrderId value

The object is tasked with repairing a building.

Id: `718`

<a id="symbol-orderid-research"></a>

## `orderid-research`

- Kind: `value`
- Detail: OrderId value

The object is tasked with researching a technology.

Id: `720`

<a id="symbol-orderid-retreat"></a>

## `orderid-retreat`

- Kind: `value`
- Detail: OrderId value

Unknown. Probably either retreating during a up-retreat-now or up-retreat-to command, or retreating because of minimum range or dpAbilityToMaintainDistance.

Id: `708`

<a id="symbol-orderid-runaway"></a>

## `orderid-runaway`

- Kind: `value`
- Detail: OrderId value

Unknown? Could be non-combat units trying to get away from soldiers attacking them.

Id: `707`

<a id="symbol-orderid-stop"></a>

## `orderid-stop`

- Kind: `value`
- Detail: OrderId value

The object is being ordered to stop.

Id: `706`

<a id="symbol-orderid-trade"></a>

## `orderid-trade`

- Kind: `value`
- Detail: OrderId value

The object is being tasked with trading between markets or docks.

Id: `715`

<a id="symbol-orderid-train"></a>

## `orderid-train`

- Kind: `value`
- Detail: OrderId value

The object is tasked with training a unit.

Id: `719`

<a id="symbol-orderid-transport"></a>

## `orderid-transport`

- Kind: `value`
- Detail: OrderId value

The object is being ordered to transport units. Might also include transport ships that are on their way to picking up units.

Id: `714`

<a id="symbol-orderid-unload"></a>

## `orderid-unload`

- Kind: `value`
- Detail: OrderId value

The object is being ordered to unload units.

Id: `721`

<a id="symbol-pacific-islands"></a>

## `pacific-islands`

- Kind: `value`
- Detail: MapType value

Pacific Islands map.

Id: `114`

<a id="symbol-packed-trebuchet-class"></a>

## `packed-trebuchet-class`

- Kind: `value`
- Detail: ClassId value

Packed Trebuchet class.

Id: `951`

<a id="symbol-palisade-wall"></a>

## `palisade-wall`

- Kind: `value`
- Detail: WallId value

Palisade Wall.

Id: `72`

<a id="symbol-paradise-island"></a>

## `paradise-island`

- Kind: `value`
- Detail: MapType value

Paradise Island map. Must be defined with a defconst.

Id: `40`

<a id="symbol-passage"></a>

## `passage`

- Kind: `value`
- Detail: MapType value

Passage map.

Id: `185`

<a id="symbol-persian"></a>

## `persian`

- Kind: `value`
- Detail: Civ value

Persians

Id: `8`

<a id="symbol-petard-class"></a>

## `petard-class`

- Kind: `value`
- Detail: ClassId value

Petard class.

Id: `935`

<a id="symbol-pilgrims"></a>

## `pilgrims`

- Kind: `value`
- Detail: MapType value

Pilgrims map. Must be defined with a defconst.

Id: `41`

<a id="symbol-place-control"></a>

## `place-control`

- Kind: `value`
- Detail: PlacementType value

Allows more controlled building placement. Uses the settings from up-set-placement-data, snPlacementZoneSize, snPlacementFailDelta, and snPlacementToCenter to control building placement. See this image for an explanation: <a target="_blank...

Id: `2`

<a id="symbol-place-forward"></a>

## `place-forward`

- Kind: `value`
- Detail: PlacementType value

Same placement as build-forward, except that locations are affected by snPlacementZoneSize. Setting large values for sn-placement-zone-size can surround the enemy player with the forward building.

Id: `1`

<a id="symbol-place-normal"></a>

## `place-normal`

- Kind: `value`
- Detail: PlacementType value

Same placement as build.

Id: `0`

<a id="symbol-place-point"></a>

## `place-point`

- Kind: `value`
- Detail: PlacementType value

Allows placement for a building at the point specified by up-set-target-point. Building placement with place-point is affected by snPlacementZoneSize, but it is not affected by up-set-placement-data, snPlacementFailDelta, or snPlacementToC...

Id: `3`

<a id="symbol-player-distance"></a>

## `player-distance`

- Kind: `value`
- Detail: FactId value

The from the AI's town center to the nearest building of the given player number. The corresponding fact command is up-player-distance.

Id: `35`

<a id="symbol-player-in-game"></a>

## `player-in-game`

- Kind: `value`
- Detail: FactId value

Checks whether the player is valid and still playing. The corresponding fact command is player-in-game.

Id: `23`

<a id="symbol-player-number"></a>

## `player-number`

- Kind: `value`
- Detail: FactId value

The player's player number. The corresponding fact command is player-number.

Id: `22`

<a id="symbol-players-in-game"></a>

## `players-in-game`

- Kind: `value`
- Detail: FactId value

The number of players in the game that match the given stance (any, ally, neutral, or enemy). To get the total number of players, use &quot;any&quot as the PlayersStance. The AI player is considered allied with itself, so the number of all...

Id: `42`

<a id="symbol-players-tribute"></a>

## `players-tribute`

- Kind: `value`
- Detail: FactId value

The amount of the given resource for the given player throughout the game. The corresponding fact command is players-tribute.

Id: `52`

<a id="symbol-players-tribute-memory"></a>

## `players-tribute-memory`

- Kind: `value`
- Detail: FactId value

The amount of the given resource for the given player since the tribute memory has been cleared with clear-tribute-memory. The corresponding fact command is cPlayersTributeMemory.

Id: `53`

<a id="symbol-poles"></a>

## `poles`

- Kind: `value`
- Detail: Civ value

Poles.

Id: `38`

<a id="symbol-population"></a>

## `population`

- Kind: `value`
- Detail: FactId value

The player's current population. The corresponding fact commands are population and players-population.

Id: `30`

<a id="symbol-population-cap"></a>

## `population-cap`

- Kind: `value`
- Detail: FactId value

The population cap setting. The corresponding fact command is population-cap.

Id: `1`

<a id="symbol-population-headroom"></a>

## `population-headroom`

- Kind: `value`
- Detail: FactId value

The population headroom. Population headroom is the difference between the game's population cap and current housing capacity. The corresponding fact command is population-headroom.

Id: `2`

<a id="symbol-portuguese"></a>

## `portuguese`

- Kind: `value`
- Detail: Civ value

Portuguese. In WK, must define with a defconst before it can be used.

Id: `24`

<a id="symbol-position-border"></a>

## `position-border`

- Kind: `value`
- Detail: PositionType value

The point on a border that is closest to position-self. Returns the point (-1,-1) when all TCs are destroyed.

Id: `4`

<a id="symbol-position-center"></a>

## `position-center`

- Kind: `value`
- Detail: PositionType value

The center of the map.

Id: `0`

<a id="symbol-position-corner"></a>

## `position-corner`

- Kind: `value`
- Detail: PositionType value

The location of the corner closest to position-self. Returns the point (-1,-1) when all TCs are destroyed.

Id: `2`

<a id="symbol-position-enemy"></a>

## `position-enemy`

- Kind: `value`
- Detail: PositionType value

A random location +/- 8 tiles from the target player's nearest non-wall building. If the enemy hasn't been found, this is the same as position-opposite.

Id: `3`

<a id="symbol-position-flank"></a>

## `position-flank`

- Kind: `value`
- Detail: PositionType value

The expected position where the nearest enemy flank player should be, found by evaluating all of the scout-opposite points for all members of the team and picking the closest point. Returns the point (-1,-1) when all TCs are destroyed.

Id: `6`

<a id="symbol-position-focus"></a>

## `position-focus`

- Kind: `value`
- Detail: PositionType value

The location of the nearest non-wall building of the focus player. Not defined if the focus player is the same as my-player-number.

Id: `11`

<a id="symbol-position-map-size"></a>

## `position-map-size`

- Kind: `value`
- Detail: PositionType value

The rightmost point on the map, where x and y equal the map size.

Id: `8`

<a id="symbol-position-mirror"></a>

## `position-mirror`

- Kind: `value`
- Detail: PositionType value

The expected position of the mirrored opponent on the opposite team, found by mirroring from position-self across the line that separates teams. Returns the point (-1,-1) when all TCs are destroyed.

Id: `5`

<a id="symbol-position-object"></a>

## `position-object`

- Kind: `value`
- Detail: PositionType value

The location of the target object.

Id: `12`

<a id="symbol-position-opposite"></a>

## `position-opposite`

- Kind: `value`
- Detail: PositionType value

The point on the opposite side of the map from position-self. It is found reflecting position-self across the center of the map. Returns the point (-1,-1) when all TCs are destroyed.

Id: `1`

<a id="symbol-position-point"></a>

## `position-point`

- Kind: `value`
- Detail: PositionType value

The location of the target point.

Id: `13`

<a id="symbol-position-self"></a>

## `position-self`

- Kind: `value`
- Detail: PositionType value

The location of the player's oldest Town Center. When all TCs are destroyed, position-self is the location of the most-recently destroyed TC.

Id: `9`

<a id="symbol-position-target"></a>

## `position-target`

- Kind: `value`
- Detail: PositionType value

The location of the nearest non-wall building of the target player. Not defined if the target player is the same as my-player-number.

Id: `10`

<a id="symbol-position-zero"></a>

## `position-zero`

- Kind: `value`
- Detail: PositionType value

The leftmost point on the map, where x and y are 0.

Id: `7`

<a id="symbol-post-imperial-age"></a>

## `post-imperial-age`

- Kind: `value`
- Detail: Age value

Post-Imperial Age. Can only be used with starting-age facts.

Id: `105`

<a id="symbol-prairie"></a>

## `prairie`

- Kind: `value`
- Detail: MapType value

Prairie map. Must be defined with a defconst.

Id: `42`

<a id="symbol-predator-animal-class-"></a>

## `predator-animal-class*`

- Kind: `value`
- Detail: ClassId value

Predator Animal class. Includes boar, boar variants, and wolves.

Id: `910`

<a id="symbol-prey-animal-class-"></a>

## `prey-animal-class*`

- Kind: `value`
- Detail: ClassId value

Prey Animal class. Includes deer and its variants.

Id: `909`

<a id="symbol-priority-defense"></a>

## `priority-defense`

- Kind: `value`
- Detail: PriorityType value

Change the targeting priority for defensive units (units defending the town or attacking with TSA.

Id: `1`

<a id="symbol-priority-offense"></a>

## `priority-offense`

- Kind: `value`
- Detail: PriorityType value

Change the targeting priority for offensive units (units attacking with attack-now or attack-group methods).

Id: `0`

<a id="symbol-projectile-any"></a>

## `projectile-any`

- Kind: `value`
- Detail: ProjectileType value

Any projectile from soldiers, siege weapons, scorpions, ships, or buildings.

Id: `7`

<a id="symbol-projectile-bombard-tower"></a>

## `projectile-bombard-tower`

- Kind: `value`
- Detail: ProjectileType value

Bombard Tower cannonballs.

Id: `3`

<a id="symbol-projectile-castle"></a>

## `projectile-castle`

- Kind: `value`
- Detail: ProjectileType value

Castle arrows.

Id: `1`

<a id="symbol-projectile-fortification"></a>

## `projectile-fortification`

- Kind: `value`
- Detail: ProjectileType value

Projectiles from Castles or towers.

Id: `6`

<a id="symbol-projectile-ship"></a>

## `projectile-ship`

- Kind: `value`
- Detail: ProjectileType value

Projectiles from any warship.

Id: `4`

<a id="symbol-projectile-siege"></a>

## `projectile-siege`

- Kind: `value`
- Detail: ProjectileType value

Projectiles from any ranged siege weapon, except scorpions.

Id: `5`

<a id="symbol-projectile-town-center"></a>

## `projectile-town-center`

- Kind: `value`
- Detail: ProjectileType value

Town Center arrows.

Id: `0`

<a id="symbol-projectile-watch-tower"></a>

## `projectile-watch-tower`

- Kind: `value`
- Detail: ProjectileType value

Watch Tower, Guard Tower, or Keep arrows.

Id: `2`

<a id="symbol-puru"></a>

## `puru`

- Kind: `value`
- Detail: Civ value

Puru (must define with a defconst first).

Id: `56`

<a id="symbol-qp-arabia"></a>

## `qp-arabia`

- Kind: `value`
- Detail: MapType value

Quick Play Arabia map.

Id: `190`

<a id="symbol-qp-arena"></a>

## `qp-arena`

- Kind: `value`
- Detail: MapType value

Quick Play Arena map.

Id: `195`

<a id="symbol-qp-black-forest"></a>

## `qp-black-forest`

- Kind: `value`
- Detail: MapType value

Quick Play Black Forest map.

Id: `196`

<a id="symbol-qp-fortified-clearing"></a>

## `qp-fortified-clearing`

- Kind: `value`
- Detail: MapType value

Quick Play Fortified Clearing map.

Id: `191`

<a id="symbol-qp-glade"></a>

## `qp-glade`

- Kind: `value`
- Detail: MapType value

Quick Play Glade map.

Id: `192`

<a id="symbol-qp-nomad"></a>

## `qp-nomad`

- Kind: `value`
- Detail: MapType value

Quick Play Nomad map.

Id: `193`

<a id="symbol-qp-runestones"></a>

## `qp-runestones`

- Kind: `value`
- Detail: MapType value

Quick Play Runestones map.

Id: `194`

<a id="symbol-rampart"></a>

## `rampart`

- Kind: `value`
- Detail: MapType value

Rampart map.

Id: `212`

<a id="symbol-random-map"></a>

## `random-map`

- Kind: `value`
- Detail: GameType value

Random Map game.

Id: `0`

<a id="symbol-random-number"></a>

## `random-number`

- Kind: `value`
- Detail: FactId value

The current random number value generated the last time the generate-random-number command was used. The corresponding fact command is random-number.

Id: `33`

<a id="symbol-random-resources"></a>

## `random-resources`

- Kind: `value`
- Detail: StartingResources value

Start with random amounts of each resource. DE only.

Id: `6`

<a id="symbol-ravines"></a>

## `ravines`

- Kind: `value`
- Detail: MapType value

Ravines map. Must be defined with a defconst.

Id: `125`

<a id="symbol-real-world-amazon"></a>

## `real-world-amazon`

- Kind: `value`
- Detail: MapType value

Amazon real world map.

Id: `88`

<a id="symbol-real-world-antarctica"></a>

## `real-world-antarctica`

- Kind: `value`
- Detail: MapType value

Antarctica real world map. Must be defined with a defconst.

Id: `132`

<a id="symbol-real-world-aral-sea"></a>

## `real-world-aral-sea`

- Kind: `value`
- Detail: MapType value

Aral Sea real world map. Must be defined with a defconst.

Id: `133`

<a id="symbol-real-world-australia"></a>

## `real-world-australia`

- Kind: `value`
- Detail: MapType value

Australia real world map. Must be defined with a defconst.

Id: `107`

<a id="symbol-real-world-black-sea"></a>

## `real-world-black-sea`

- Kind: `value`
- Detail: MapType value

Black Sea real world map. Must be defined with a defconst.

Id: `134`

<a id="symbol-real-world-bohemia"></a>

## `real-world-bohemia`

- Kind: `value`
- Detail: MapType value

Bohemia real world map.

Id: `94`

<a id="symbol-real-world-byzantium"></a>

## `real-world-byzantium`

- Kind: `value`
- Detail: MapType value

Byzantium real world map. Defined as 43 before DE.

Id: `58`

<a id="symbol-real-world-caribbean"></a>

## `real-world-caribbean`

- Kind: `value`
- Detail: MapType value

Central America real world map. Defined as 39 before DE.

Id: `54`

<a id="symbol-real-world-caucasus"></a>

## `real-world-caucasus`

- Kind: `value`
- Detail: MapType value

Caucasus real world map. Must be defined with a defconst.

Id: `135`

<a id="symbol-real-world-china"></a>

## `real-world-china`

- Kind: `value`
- Detail: MapType value

China real world map.

Id: `89`

<a id="symbol-real-world-earth"></a>

## `real-world-earth`

- Kind: `value`
- Detail: MapType value

Earth real world map.

Id: `95`

<a id="symbol-real-world-england"></a>

## `real-world-england`

- Kind: `value`
- Detail: MapType value

Britain real world map. Defined as 35 before DE.

Id: `50`

<a id="symbol-real-world-france"></a>

## `real-world-france`

- Kind: `value`
- Detail: MapType value

France real world map. Defined as 40 before DE.

Id: `55`

<a id="symbol-real-world-horn-of-africa"></a>

## `real-world-horn-of-africa`

- Kind: `value`
- Detail: MapType value

Horn of Africa real world map.

Id: `90`

<a id="symbol-real-world-india"></a>

## `real-world-india`

- Kind: `value`
- Detail: MapType value

India real world map.

Id: `91`

<a id="symbol-real-world-indochina"></a>

## `real-world-indochina`

- Kind: `value`
- Detail: MapType value

Indochina real world map. Must be defined with a defconst.

Id: `108`

<a id="symbol-real-world-indonesia"></a>

## `real-world-indonesia`

- Kind: `value`
- Detail: MapType value

Indonesia real world map. Must be defined with a defconst.

Id: `109`

<a id="symbol-real-world-italy"></a>

## `real-world-italy`

- Kind: `value`
- Detail: MapType value

Italy real world map. Defined as 38 before DE.

Id: `53`

<a id="symbol-real-world-jutland"></a>

## `real-world-jutland`

- Kind: `value`
- Detail: MapType value

Norse Lands real world map. Defined as 41 before DE.

Id: `56`

<a id="symbol-real-world-madagascar"></a>

## `real-world-madagascar`

- Kind: `value`
- Detail: MapType value

Madagascar real world map.

Id: `92`

<a id="symbol-real-world-malacca"></a>

## `real-world-malacca`

- Kind: `value`
- Detail: MapType value

Malacca real world map. Must be defined with a defconst.

Id: `110`

<a id="symbol-real-world-manchuria"></a>

## `real-world-manchuria`

- Kind: `value`
- Detail: MapType value

Manchuria real world map. Must be defined with a defconst.

Id: `197`

<a id="symbol-real-world-mideast"></a>

## `real-world-midEast`

- Kind: `value`
- Detail: MapType value

Mideast real world map. Notice the uppercase 'E'. Defined as 36 before DE.

Id: `51`

<a id="symbol-real-world-nippon"></a>

## `real-world-nippon`

- Kind: `value`
- Detail: MapType value

Sea of Japan (East Sea) real world map. Defined as 42 before DE.

Id: `57`

<a id="symbol-real-world-philippines"></a>

## `real-world-philippines`

- Kind: `value`
- Detail: MapType value

Philippines real world map. Must be defined with a defconst.

Id: `111`

<a id="symbol-real-world-siberia"></a>

## `real-world-siberia`

- Kind: `value`
- Detail: MapType value

Siberia real world map. Must be defined with a defconst.

Id: `136`

<a id="symbol-real-world-spain"></a>

## `real-world-spain`

- Kind: `value`
- Detail: MapType value

Australia map. Must be defined with a defconst.

Id: `49`

<a id="symbol-real-world-texas"></a>

## `real-world-texas`

- Kind: `value`
- Detail: MapType value

Texas real world map. Defined as 37 before DE.

Id: `52`

<a id="symbol-real-world-west-africa"></a>

## `real-world-west-africa`

- Kind: `value`
- Detail: MapType value

West Africa real world map.

Id: `93`

<a id="symbol-regicide"></a>

## `regicide`

- Kind: `value`
- Detail: GameType value

Regicide game.

Id: `1`

<a id="symbol-relic-class-"></a>

## `relic-class*`

- Kind: `value`
- Detail: ClassId value

Relic class.

Id: `942`

<a id="symbol-research-available"></a>

## `research-available`

- Kind: `value`
- Detail: ResearchState value

The age, technology, building (for age techs), and civilization requirements for the research have been met, but the player hasn't started researching the research yet. Techs can still be considered research-available even if the AI doesn'...

Id: `1`

<a id="symbol-research-complete"></a>

## `research-complete`

- Kind: `value`
- Detail: ResearchState value

The research has been completed.

Id: `3`

<a id="symbol-research-disabled"></a>

## `research-disabled`

- Kind: `value`
- Detail: ResearchState value

DE only. The research has been manually disabled, probably through a scenario trigger. If a tech is unavailable in a civ's tech tree, the status will be research-unavailable.

Id: `-1`

<a id="symbol-research-pending"></a>

## `research-pending`

- Kind: `value`
- Detail: ResearchState value

The research is currently being researched. Doesn't count queued techs.

Id: `2`

<a id="symbol-research-queued"></a>

## `research-queued`

- Kind: `value`
- Detail: ResearchState value

DE only. The research has been queued.

Id: `4`

<a id="symbol-research-unavailable"></a>

## `research-unavailable`

- Kind: `value`
- Detail: ResearchState value

The research is not available, either because the age or technology prerequisites haven't been met, the research is not available in the civ's tech tree, or building requirements haven't been met (for age techs only).

Id: `0`

<a id="symbol-resource-amount"></a>

## `resource-amount`

- Kind: `value`
- Detail: FactId value

The current stockpile amount of the given resource. The corresponding fact commands are up-resource-amount and up-allied-resource-amount.

Id: `34`

<a id="symbol-resource-percent"></a>

## `resource-percent`

- Kind: `value`
- Detail: FactId value

The current amount of the given resource * 100. The corresponding fact commands are up-resource-percent and up-allied-resource-amount.

Id: `38`

<a id="symbol-ring-fortress"></a>

## `ring-fortress`

- Kind: `value`
- Detail: MapType value

Ring Fortress map.

Id: `166`

<a id="symbol-river-divide"></a>

## `river-divide`

- Kind: `value`
- Detail: MapType value

River Divide map.

Id: `182`

<a id="symbol-rivers"></a>

## `rivers`

- Kind: `value`
- Detail: MapType value

Rivers map.

Id: `22`

<a id="symbol-romans"></a>

## `romans`

- Kind: `value`
- Detail: Civ value

Romans.

Id: `43`

<a id="symbol-runestones"></a>

## `runestones`

- Kind: `value`
- Detail: MapType value

Runestones map.

Id: `167`

<a id="symbol-s-"></a>

## `s:`

- Kind: `value`
- Detail: compareOp value

Treats the second compared parameter in the command as a <a href="urlPrefix/strategic-numbers/sn-index.html">Strategic Number</a> and compare to the value set by that strategic number. This prefix is required when comparing to the strategi...

<a id="symbol-s--"></a>

## `s:-`

- Kind: `value`
- Detail: mathOp value

Subtract the strategic number value of the second operand from the first operand.

DE id: `2`

<a id="symbol-s-"></a>

## `s:!=`

- Kind: `value`
- Detail: compareOp value

Not equal to the strategic number's value.

DE id: `11`

<a id="symbol-s-"></a>

## `s:*`

- Kind: `value`
- Detail: mathOp value

Multiply the first operand by the strategic number value of the second operand.

DE id: `3`

<a id="symbol-s-"></a>

## `s:/`

- Kind: `value`
- Detail: mathOp value

Divide the first operand by the strategic number value of the second operand. The quotient is rounded to the nearest integer.

DE id: `4`

<a id="symbol-s-"></a>

## `s:%*`

- Kind: `value`
- Detail: mathOp value

Treat the strategic number value of the second operand as a percentage and find that percentage of the first parameter, truncated (not rounded) to the nearest integer, i.e. (first operand * second operand / 100).

DE id: `10`

<a id="symbol-s-"></a>

## `s:%/`

- Kind: `value`
- Detail: mathOp value

Divide the first operand by the strategic number value of the second operand, and convert the quotient to a percent, truncated (not rounded) to the nearest integer, i.e. (first operand / second operand * 100).

DE id: `11`

<a id="symbol-s-"></a>

## `s:+`

- Kind: `value`
- Detail: mathOp value

Add the strategic number value of the second operand to the first operand.

DE id: `1`

<a id="symbol-s-"></a>

## `s:<`

- Kind: `value`
- Detail: compareOp value

Less than the strategic number's value.

DE id: `6`

<a id="symbol-s-"></a>

## `s:<=`

- Kind: `value`
- Detail: compareOp value

Less than or equal to the strategic number's value.

DE id: `7`

<a id="symbol-s-"></a>

## `s:=`

- Kind: `value`
- Detail: mathOp value

Set the first operand equal to the strategic number value of the second operand.

DE id: `0`

<a id="symbol-s-"></a>

## `s:==`

- Kind: `value`
- Detail: compareOp value

Equal to the strategic number's value. Note: one equals sign (=) is an assignment operator used in the mathOp operator. Always use "==" when you want to compare.

DE id: `10`

<a id="symbol-s-"></a>

## `s:>`

- Kind: `value`
- Detail: compareOp value

Greater than the strategic number's value.

DE id: `8`

<a id="symbol-s-"></a>

## `s:>=`

- Kind: `value`
- Detail: compareOp value

Greater than or equal to the strategic number's value.

DE id: `9`

<a id="symbol-s-max"></a>

## `s:max`

- Kind: `value`
- Detail: mathOp value

Store the largest value between the first operand and the strategic number value of the second operand.

DE id: `6`

<a id="symbol-s-min"></a>

## `s:min`

- Kind: `value`
- Detail: mathOp value

Store the smallest value between the first operand and the strategic number value of the second operand.

DE id: `5`

<a id="symbol-s-mod"></a>

## `s:mod`

- Kind: `value`
- Detail: mathOp value

Divide the first operand by the strategic number value of the second operand. Store the remainder instead of the quotient.

DE id: `7`

<a id="symbol-s-neg"></a>

## `s:neg`

- Kind: `value`
- Detail: mathOp value

Negate the strategic number value of the second operand and store the result in the first operand. If the strategic number is already negative, this will store its positive value.

DE id: `8`

<a id="symbol-s-z-"></a>

## `s:z/`

- Kind: `value`
- Detail: mathOp value

Divide the first operand by the strategic number value of the second operand. The quotient is truncated (rounded down) to the nearest integer.

DE id: `9`

<a id="symbol-sacred-springs"></a>

## `sacred-springs`

- Kind: `value`
- Detail: MapType value

Sacred Springs map.

Id: `173`

<a id="symbol-salt-marsh"></a>

## `salt-marsh`

- Kind: `value`
- Detail: MapType value

Salt Marsh map.

Id: `28`

<a id="symbol-sandbank"></a>

## `sandbank`

- Kind: `value`
- Detail: MapType value

Sandbank map.

Id: `115`

<a id="symbol-sandrift"></a>

## `sandrift`

- Kind: `value`
- Detail: MapType value

Sandrift map.

Id: `183`

<a id="symbol-saracen"></a>

## `saracen`

- Kind: `value`
- Detail: Civ value

Saracens

Id: `9`

<a id="symbol-sardis"></a>

## `sardis`

- Kind: `value`
- Detail: MapType value

Sardis map.

Id: `201`

<a id="symbol-scandanavia"></a>

## `scandanavia`

- Kind: `value`
- Detail: MapType value

Scandinavia map. Notice the name is mispelled.

Id: `25`

<a id="symbol-scenario"></a>

## `scenario`

- Kind: `value`
- Detail: GameType value

A custom scenario.

Id: `3`

<a id="symbol-scenario-map"></a>

## `scenario-map`

- Kind: `value`
- Detail: MapType value

Scenario map. A map created in the scenario editor.

Id: `-1`

<a id="symbol-score"></a>

## `score`

- Kind: `value`
- Detail: VictoryCondition value

Score victory. The player or team to first reach the score wins.

Id: `3`

<a id="symbol-scorpion-class"></a>

## `scorpion-class`

- Kind: `value`
- Detail: ClassId value

Scorpion class.

Id: `955`

<a id="symbol-scout-border"></a>

## `scout-border`

- Kind: `value`
- Detail: ScoutMethod value

Scouts the point on a border that is closest to position-self (the location of the player's oldest Town Center).

Id: `4`

<a id="symbol-scout-cavalry-class-"></a>

## `scout-cavalry-class*`

- Kind: `value`
- Detail: ClassId value

Scout Cavalry class. Includes scout cavalry, light cavalry, and hussar, although it doesn't include light cavalry or hussars (not scout cavalry) that are placed at the start of the game in scenarios.

Id: `947`

<a id="symbol-scout-center"></a>

## `scout-center`

- Kind: `value`
- Detail: ScoutMethod value

Scout around the center of the map.

Id: `0`

<a id="symbol-scout-corner"></a>

## `scout-corner`

- Kind: `value`
- Detail: ScoutMethod value

Scouts the location of the corner closest to position-self (the location of the player's oldest Town Center).

Id: `2`

<a id="symbol-scout-enemy"></a>

## `scout-enemy`

- Kind: `value`
- Detail: ScoutMethod value

This parameter will send the scout back to the target enemy's nearest building +/- 8 tiles in any direction at random, in order to better explore the target's town. If your ally finds the enemy town, you can target it for attacks, but not ...

Id: `3`

<a id="symbol-scout-flank"></a>

## `scout-flank`

- Kind: `value`
- Detail: ScoutMethod value

Scouts the expected position where the nearest enemy flank player should be, found by evaluating all of the scout-opposite points for all members of the team and picking the closest point.

Id: `6`

<a id="symbol-scout-mirror"></a>

## `scout-mirror`

- Kind: `value`
- Detail: ScoutMethod value

Scouts the expected position of the mirrored opponent on the opposite team, found by mirroring from position-self across the line that separates teams.

Id: `5`

<a id="symbol-scout-opposite"></a>

## `scout-opposite`

- Kind: `value`
- Detail: ScoutMethod value

Scouts the point on the opposite side of the map from position-self. It is found reflecting position-self across the center of the map.

Id: `1`

<a id="symbol-search-local"></a>

## `search-local`

- Kind: `value`
- Detail: SearchSource value

The list that stores the search results from up-find-local commands. This list only contains objects from the current (local) player. The list holds a maximum of 240 objects.

Id: `1`

<a id="symbol-search-order-asc"></a>

## `search-order-asc`

- Kind: `value`
- Detail: SearchOrder value

Sort the search results in ascending order.

Id: `1`

<a id="symbol-search-order-desc"></a>

## `search-order-desc`

- Kind: `value`
- Detail: SearchOrder value

Sort the search results in descending order.

Id: `2`

<a id="symbol-search-order-none"></a>

## `search-order-none`

- Kind: `value`
- Detail: SearchOrder value

Preserves the existing list order. Usually only used when removing duplicates from the search list.

Id: `0`

<a id="symbol-search-remote"></a>

## `search-remote`

- Kind: `value`
- Detail: SearchSource value

The list that stores the search results from up-find-remote commands. This list only contains objects from the focus-player. The list holds a maximum of 40 objects.

Id: `2`

<a id="symbol-seasons"></a>

## `seasons`

- Kind: `value`
- Detail: MapType value

Seasons map. Must be defined with a defconst.

Id: `43`

<a id="symbol-seize-the-mountain"></a>

## `seize-the-mountain`

- Kind: `value`
- Detail: MapType value

Seize the Mountain map.

Id: `151`

<a id="symbol-serengeti"></a>

## `serengeti`

- Kind: `value`
- Detail: MapType value

Serengeti map.

Id: `86`

<a id="symbol-sherwood-forest"></a>

## `sherwood-forest`

- Kind: `value`
- Detail: MapType value

Sherwood Forest map. Must be defined with a defconst.

Id: `44`

<a id="symbol-shipwreck"></a>

## `shipwreck`

- Kind: `value`
- Detail: MapType value

Shipwreck map. Must be defined with a defconst.

Id: `46`

<a id="symbol-shoals"></a>

## `shoals`

- Kind: `value`
- Detail: MapType value

Shoals map.

Id: `176`

<a id="symbol-shore-fish-class"></a>

## `shore-fish-class`

- Kind: `value`
- Detail: ClassId value

Shore Fish class.

Id: `933`

<a id="symbol-shrubland"></a>

## `shrubland`

- Kind: `value`
- Detail: MapType value

Shrubland map.

Id: `184`

<a id="symbol-shu"></a>

## `shu`

- Kind: `value`
- Detail: Civ value

Shu (must define with a defconst first).

Id: `49`

<a id="symbol-sicilians"></a>

## `sicilians`

- Kind: `value`
- Detail: Civ value

Sicilians.

Id: `37`

<a id="symbol-siege-weapon-class"></a>

## `siege-weapon-class`

- Kind: `value`
- Detail: ClassId value

Siege Weapons class. Doesn't include trebuchets, scorpions, or petards.

Id: `913`

<a id="symbol-slavic"></a>

## `slavic`

- Kind: `value`
- Detail: Civ value

Slavs. In WK, must define with a defconst before it can be used.

Id: `23`

<a id="symbol-small-map-small"></a>

## `small-map, small`

- Kind: `value`
- Detail: MapSize value

Small (3 player) map size. 144x144 tiles.

Id: `144`

<a id="symbol-socotra"></a>

## `socotra`

- Kind: `value`
- Detail: MapType value

Socotra map.

Id: `87`

<a id="symbol-soldier-count"></a>

## `soldier-count`

- Kind: `value`
- Detail: FactId value

The number of the player's land-based military units. The corresponding fact command is soldier-count.

Id: `13`

<a id="symbol-spanish"></a>

## `spanish`

- Kind: `value`
- Detail: Civ value

Spanish

Id: `14`

<a id="symbol-spartans"></a>

## `spartans`

- Kind: `value`
- Detail: Civ value

Spartans (must define with a defconst first).

Id: `48`

<a id="symbol-special-map-archipelago"></a>

## `special-map-archipelago`

- Kind: `value`
- Detail: MapType value

Archipelago special map.

Id: `97`

<a id="symbol-special-map-border-stones"></a>

## `special-map-border-stones`

- Kind: `value`
- Detail: MapType value

Border Stones special map.

Id: `119`

<a id="symbol-special-map-canyons"></a>

## `special-map-canyons`

- Kind: `value`
- Detail: MapType value

Canyons special map.

Id: `96`

<a id="symbol-special-map-enemy-islands"></a>

## `special-map-enemy-islands`

- Kind: `value`
- Detail: MapType value

Islands special map.

Id: `98`

<a id="symbol-special-map-far-out"></a>

## `special-map-far-out`

- Kind: `value`
- Detail: MapType value

Far Out special map.

Id: `99`

<a id="symbol-special-map-forest-breach"></a>

## `special-map-forest-breach`

- Kind: `value`
- Detail: MapType value

Forest Breach special map.

Id: `203`

<a id="symbol-special-map-front-line"></a>

## `special-map-front-line`

- Kind: `value`
- Detail: MapType value

Front Line special map.

Id: `100`

<a id="symbol-special-map-holy-line"></a>

## `special-map-holy-line`

- Kind: `value`
- Detail: MapType value

Holy Line special map.

Id: `118`

<a id="symbol-special-map-inner-circle"></a>

## `special-map-inner-circle`

- Kind: `value`
- Detail: MapType value

Inner Circle special map.

Id: `101`

<a id="symbol-special-map-journey-south"></a>

## `special-map-journey-south`

- Kind: `value`
- Detail: MapType value

Journey South special map. Must be defined with a defconst.

Id: `129`

<a id="symbol-special-map-jungle-islands"></a>

## `special-map-jungle-islands`

- Kind: `value`
- Detail: MapType value

Jungle Islands special map.

Id: `117`

<a id="symbol-special-map-jungle-lanes"></a>

## `special-map-jungle-lanes`

- Kind: `value`
- Detail: MapType value

Jungle Lanes special map.

Id: `121`

<a id="symbol-special-map-motherland"></a>

## `special-map-motherland`

- Kind: `value`
- Detail: MapType value

Motherland special map.

Id: `102`

<a id="symbol-special-map-open-plains"></a>

## `special-map-open-plains`

- Kind: `value`
- Detail: MapType value

Open Plains special map.

Id: `103`

<a id="symbol-special-map-ring-of-water"></a>

## `special-map-ring-of-water`

- Kind: `value`
- Detail: MapType value

Ring of Water special map.

Id: `104`

<a id="symbol-special-map-snake-forest"></a>

## `special-map-snake-forest`

- Kind: `value`
- Detail: MapType value

special map. Must be defined with a defconst.

Id: `130`

<a id="symbol-special-map-snake-pit"></a>

## `special-map-snake-pit`

- Kind: `value`
- Detail: MapType value

Snake Pit special map.

Id: `105`

<a id="symbol-special-map-sprawling-streams"></a>

## `special-map-sprawling-streams`

- Kind: `value`
- Detail: MapType value

Sprawling Streams special map. Must be defined with a defconst.

Id: `131`

<a id="symbol-special-map-swirling-river"></a>

## `special-map-swirling-river`

- Kind: `value`
- Detail: MapType value

Swirling River special map. Must be defined with a defconst.

Id: `127`

<a id="symbol-special-map-the-eye"></a>

## `special-map-the-eye`

- Kind: `value`
- Detail: MapType value

The Eye special map.

Id: `106`

<a id="symbol-special-map-twin-forests"></a>

## `special-map-twin-forests`

- Kind: `value`
- Detail: MapType value

Twin Forests special map. Must be defined with a defconst.

Id: `128`

<a id="symbol-special-map-yin-yang"></a>

## `special-map-yin-yang`

- Kind: `value`
- Detail: MapType value

Yin Yang special map.

Id: `120`

<a id="symbol-stance-aggressive"></a>

## `stance-aggressive`

- Kind: `value`
- Detail: AttackStance value

Aggressive Stance. Soldiers will attack all enemy objects in line of sight and chase them.

Id: `0`

<a id="symbol-stance-defensive"></a>

## `stance-defensive`

- Kind: `value`
- Detail: AttackStance value

Defensive Stance. Soldiers will attack most enemy objects in line of sight, but they will return to their original location if the enemy objects leave the area.

Id: `1`

<a id="symbol-stance-no-attack"></a>

## `stance-no-attack`

- Kind: `value`
- Detail: AttackStance value

No Attack Stance. Soldiers will only attack if ordered to target an object through DUC.

Id: `3`

<a id="symbol-stance-stand-ground"></a>

## `stance-stand-ground`

- Kind: `value`
- Detail: AttackStance value

Stand Ground Stance. Soldiers will only attack enemy objects if they can attack the unit from their current location.

Id: `2`

<a id="symbol-standard"></a>

## `standard`

- Kind: `value`
- Detail: VictoryCondition value

Standard victory. Team wins by defeating all enemies, capturing all relics, or defending a wonder.

Id: `0`

<a id="symbol-status-down"></a>

## `status-down`

- Kind: `value`
- Detail: ObjectStatus value

Objects that are currently in their dying animation but aren't completely dead yet. Does not include building rubble or dead units.

Id: `4`

<a id="symbol-status-gather"></a>

## `status-gather`

- Kind: `value`
- Detail: ObjectStatus value

Dead animals carrying food, fish, corpses.

Id: `5`

<a id="symbol-status-pending"></a>

## `status-pending`

- Kind: `value`
- Detail: ObjectStatus value

Incomplete buildings.

Id: `0`

<a id="symbol-status-ready"></a>

## `status-ready`

- Kind: `value`
- Detail: ObjectStatus value

Default. Most active objects. Also includes live animals, live trees.

Id: `2`

<a id="symbol-status-resource"></a>

## `status-resource`

- Kind: `value`
- Detail: ObjectStatus value

Some resources: berries, down trees, gold, and stone.

Id: `3`

<a id="symbol-steppe"></a>

## `steppe`

- Kind: `value`
- Detail: MapType value

Steppe map.

Id: `75`

<a id="symbol-stone"></a>

## `stone`

- Kind: `value`
- Detail: Commodity value

Stone

Id: `2`

<a id="symbol-stone-amount"></a>

## `stone-amount`

- Kind: `value`
- Detail: FactId value

The current stone amount. The corresponding fact command is stone-amount.

Id: `7`

<a id="symbol-stone-mine-class-"></a>

## `stone-mine-class*`

- Kind: `value`
- Detail: ClassId value

Stone Mine class.

Id: `908`

<a id="symbol-stone-wall"></a>

## `stone-wall`

- Kind: `value`
- Detail: WallId value

Stone Wall.

Id: `117`

<a id="symbol-stone-wall-line"></a>

## `stone-wall-line`

- Kind: `value`
- Detail: WallId value

Stone Wall line. In Return of Rome, it includes Medium Wall and Fortified Wall, but not Small Wall.

Id: `-399`

<a id="symbol-stonefront"></a>

## `stonefront`

- Kind: `value`
- Detail: MapType value

Stonefront map.

Id: `213`

<a id="symbol-stranded"></a>

## `stranded`

- Kind: `value`
- Detail: MapType value

Stranded map.

Id: `200`

<a id="symbol-sub-game-type-empire-wars"></a>

## `sub-game-type-empire-wars`

- Kind: `value`
- Detail: SubGameType value

Empire Wars sub-game type. Players start in Feudal Age with a pre-established town.

Id: `1`

<a id="symbol-sub-game-type-king-of-the-hill"></a>

## `sub-game-type-king-of-the-hill`

- Kind: `value`
- Detail: SubGameType value

King of the Hill sub-game type. There is a monument in the middle of the map that can grant victory if it is controlled by one player for a long enough time.

Id: `1`

<a id="symbol-sub-game-type-regicide"></a>

## `sub-game-type-regicide`

- Kind: `value`
- Detail: SubGameType value

Regicide sub-game type. Players start with a king, castle, and extra villagers and lose if their king is killed.

Id: `1`

<a id="symbol-sub-game-type-sudden-death"></a>

## `sub-game-type-sudden-death`

- Kind: `value`
- Detail: SubGameType value

Sudden Death sub-game type. Players are defeated if they lose all of their town centers.

Id: `1`

<a id="symbol-sudden-death"></a>

## `sudden-death`

- Kind: `value`
- Detail: GameType value

Sudden Death game.

Id: `11`

<a id="symbol-tatars"></a>

## `tatars`

- Kind: `value`
- Detail: Civ value

Tatars.

Id: `33`

<a id="symbol-team-glaciers"></a>

## `team-glaciers`

- Kind: `value`
- Detail: MapType value

Team Glaciers map. Must be defined with a defconst.

Id: `47`

<a id="symbol-team-islands"></a>

## `team-islands`

- Kind: `value`
- Detail: MapType value

Team Islands map.

Id: `23`

<a id="symbol-terrain-beach-not-navigable-"></a>

## `terrain-beach-not-navigable*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Non-navigable Beach terrain.

Id: `79`

<a id="symbol-terrain-beach-vegetation-white-"></a>

## `terrain-beach-vegetation-white*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. White Beach Vegetation terrain.

Id: `51`

<a id="symbol-terrain-beach-vegetation-"></a>

## `terrain-beach-vegetation*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Beach Vegetation terrain.

Id: `52`

<a id="symbol-terrain-beach-wet-gravel-not-navigable-"></a>

## `terrain-beach-wet-gravel-not-navigable*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Non-navigable Wet Gravel Beach terrain.

Id: `81`

<a id="symbol-terrain-beach-wet-gravel-"></a>

## `terrain-beach-wet-gravel*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Wet Gravel Beach terrain.

Id: `108`

<a id="symbol-terrain-beach-wet-rock-not-navigable-"></a>

## `terrain-beach-wet-rock-not-navigable*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Non-navigable Wet Rock Beach terrain.

Id: `82`

<a id="symbol-terrain-beach-wet-rock-"></a>

## `terrain-beach-wet-rock*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Wet Rock Beach terrain.

Id: `109`

<a id="symbol-terrain-beach-wet-sand-not-navigable-"></a>

## `terrain-beach-wet-sand-not-navigable*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Non-navigable Wet Sand Beach terrain.

Id: `80`

<a id="symbol-terrain-beach-wet-"></a>

## `terrain-beach-wet*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Wet Beach terrain.

Id: `107`

<a id="symbol-terrain-beach-white-"></a>

## `terrain-beach-white*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. White Beach terrain.

Id: `53`

<a id="symbol-terrain-black-walkable-"></a>

## `terrain-black-walkable*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Walkable Black terrain.

Id: `129`

<a id="symbol-terrain-black-"></a>

## `terrain-black*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Black terrain.

Id: `47`

<a id="symbol-terrain-class-"></a>

## `terrain-class*`

- Kind: `value`
- Detail: ClassId value

Terrain class. Map objects like mountains, bridges, and flowers.

Id: `914`

<a id="symbol-terrain-corruption-"></a>

## `terrain-corruption*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Corruption terrain.

Id: `69`

<a id="symbol-terrain-desert"></a>

## `terrain-desert`

- Kind: `value`
- Detail: Terrain value

Desert terrain.

Id: `14`

<a id="symbol-terrain-desert-cracked-"></a>

## `terrain-desert-cracked*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Desert cracked terrain.

Id: `45`

<a id="symbol-terrain-desert-quicksand-"></a>

## `terrain-desert-quicksand*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Desert quicksand terrain.

Id: `46`

<a id="symbol-terrain-dirt"></a>

## `terrain-dirt`

- Kind: `value`
- Detail: Terrain value

Dirt 1 terrain.

Id: `6`

<a id="symbol-terrain-dirt-mud-"></a>

## `terrain-dirt-mud*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Dirt Mud terrain.

Id: `76`

<a id="symbol-terrain-dirt-snow"></a>

## `terrain-dirt-snow`

- Kind: `value`
- Detail: Terrain value

Snow Dirt terrain. Obsolete in DE. In DE, use terrain-foundation-snow.

Id: `33`

<a id="symbol-terrain-dirt2"></a>

## `terrain-dirt2`

- Kind: `value`
- Detail: Terrain value

Dirt 2 terrain. This was replaced with Mangrove Shallows in the Rajas expansion. To use the old Dirt 2 terrain, use terrain-foundation instead.

Id: `11`

<a id="symbol-terrain-dirt3"></a>

## `terrain-dirt3`

- Kind: `value`
- Detail: Terrain value

Dirt 3 terrain.

Id: `3`

<a id="symbol-terrain-dirt4-"></a>

## `terrain-dirt4*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Dirt4 terrain.

Id: `42`

<a id="symbol-terrain-farm"></a>

## `terrain-farm`

- Kind: `value`
- Detail: Terrain value

Farm terrain. Looks like normal farms.

Id: `7`

<a id="symbol-terrain-farm-dead"></a>

## `terrain-farm-dead`

- Kind: `value`
- Detail: Terrain value

Dead Farm terrain. Looks like exhausted or destroyed farms.

Id: `8`

<a id="symbol-terrain-farm-rice-dead-"></a>

## `terrain-farm-rice-dead*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Dead Rice Farm terrain.

Id: `64`

<a id="symbol-terrain-farm-rice-"></a>

## `terrain-farm-rice*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Rice Farm terrain.

Id: `63`

<a id="symbol-terrain-farm-rice1-"></a>

## `terrain-farm-rice1*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Rice Farms that are 0% planted.

Id: `65`

<a id="symbol-terrain-farm-rice2-"></a>

## `terrain-farm-rice2*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Rice Farms that are 33% planted.

Id: `66`

<a id="symbol-terrain-farm-rice3-"></a>

## `terrain-farm-rice3*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Rice Farms that are 66% planted.

Id: `67`

<a id="symbol-terrain-farm1"></a>

## `terrain-farm1`

- Kind: `value`
- Detail: Terrain value

Farm 1 terrain. Farms that are 0% planted.

Id: `29`

<a id="symbol-terrain-farm2"></a>

## `terrain-farm2`

- Kind: `value`
- Detail: Terrain value

Farm 2 terrain. Farms that are 33% planted.

Id: `30`

<a id="symbol-terrain-farm3"></a>

## `terrain-farm3`

- Kind: `value`
- Detail: Terrain value

Farm 3 terrain. Farms that are 66% planted.

Id: `31`

<a id="symbol-terrain-forest"></a>

## `terrain-forest`

- Kind: `value`
- Detail: Terrain value

Forest terrain. Looks like Oak Forest.

Id: `10`

<a id="symbol-terrain-forest-acacia-"></a>

## `terrain-forest-acacia*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Acacia Forest terrain.

Id: `50`

<a id="symbol-terrain-forest-autumn-snow-"></a>

## `terrain-forest-autumn-snow*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Snow Autumn Forest terrain.

Id: `105`

<a id="symbol-terrain-forest-autumn-"></a>

## `terrain-forest-autumn*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Autumn Forest terrain.

Id: `104`

<a id="symbol-terrain-forest-bamboo"></a>

## `terrain-forest-bamboo`

- Kind: `value`
- Detail: Terrain value

Bamboo terrain.

Id: `18`

<a id="symbol-terrain-forest-baobab-"></a>

## `terrain-forest-baobab*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Baobab Forest terrain.

Id: `49`

<a id="symbol-terrain-forest-birch-"></a>

## `terrain-forest-birch*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Birch Forest terrain.

Id: `110`

<a id="symbol-terrain-forest-bush-"></a>

## `terrain-forest-bush*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Bush Forest terrain.

Id: `89`

<a id="symbol-terrain-forest-dead-"></a>

## `terrain-forest-dead*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Dead Forest terrain.

Id: `106`

<a id="symbol-terrain-forest-dragon-tree-"></a>

## `terrain-forest-dragon-tree*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Dragon tree forest terrain.

Id: `48`

<a id="symbol-terrain-forest-dry-south-american-"></a>

## `terrain-forest-dry-south-american*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Dry South American Forest terrain.

Id: `128`

<a id="symbol-terrain-forest-jungle"></a>

## `terrain-forest-jungle`

- Kind: `value`
- Detail: Terrain value

Jungle terrain.

Id: `17`

<a id="symbol-terrain-forest-lush-bamboo-"></a>

## `terrain-forest-lush-bamboo*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Lush Bamboo Forest terrain.

Id: `113`

<a id="symbol-terrain-forest-mangrove-"></a>

## `terrain-forest-mangrove*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Mangrove Forest terrain.

Id: `55`

<a id="symbol-terrain-forest-mediterranean-"></a>

## `terrain-forest-mediterranean*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Mediterranean Forest terrain.

Id: `88`

<a id="symbol-terrain-forest-oak"></a>

## `terrain-forest-oak`

- Kind: `value`
- Detail: Terrain value

Oak Forest terrain. Replaced with Oak Bush in DE. To use the old Oak Forest terrain in this expansion and later, use terrain-forest instead.

Id: `20`

<a id="symbol-terrain-forest-palm"></a>

## `terrain-forest-palm`

- Kind: `value`
- Detail: Terrain value

Palm Desert terrain.

Id: `13`

<a id="symbol-terrain-forest-palm-grass-"></a>

## `terrain-forest-palm-grass*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Palm Grass Forest terrain.

Id: `112`

<a id="symbol-terrain-forest-pine"></a>

## `terrain-forest-pine`

- Kind: `value`
- Detail: Terrain value

Pine Forest terrain.

Id: `19`

<a id="symbol-terrain-forest-rainforest-"></a>

## `terrain-forest-rainforest*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Rainforest Forest terrain.

Id: `56`

<a id="symbol-terrain-forest-reeds-beach-"></a>

## `terrain-forest-reeds-beach*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Reeds Forest terrain which is placed on Beach terrain.

Id: `91`

<a id="symbol-terrain-forest-reeds-shallows-"></a>

## `terrain-forest-reeds-shallows*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Reeds Forest terrain which is placed on Shallows terrain.

Id: `90`

<a id="symbol-terrain-forest-reeds-"></a>

## `terrain-forest-reeds*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Reeds Forest terrain which is placed on all terrains except Shallows and Beach.

Id: `92`

<a id="symbol-terrain-forest-snow"></a>

## `terrain-forest-snow`

- Kind: `value`
- Detail: Terrain value

Snow Pine Forest terrain.

Id: `21`

<a id="symbol-terrain-foundation"></a>

## `terrain-foundation`

- Kind: `value`
- Detail: Terrain value

Foundation terrain. Terrain placed under buildings when constructed. Looks like terrain-dirt2.

Id: `27`

<a id="symbol-terrain-foundation-snow"></a>

## `terrain-foundation-snow`

- Kind: `value`
- Detail: Terrain value

Snow Foundation terrain. Terrain placed under buildings constructed on snowy terrains. Looks like Snow Dirt.

Id: `36`

<a id="symbol-terrain-grass"></a>

## `terrain-grass`

- Kind: `value`
- Detail: Terrain value

Grass 1 terrain.

Id: `0`

<a id="symbol-terrain-grass-dry-"></a>

## `terrain-grass-dry*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Dry Grass terrain.

Id: `100`

<a id="symbol-terrain-grass-flowers1-"></a>

## `terrain-grass-flowers1*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Grass Flowers 1 terrain.

Id: `122`

<a id="symbol-terrain-grass-flowers2-"></a>

## `terrain-grass-flowers2*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Grass Flowers 2 terrain.

Id: `123`

<a id="symbol-terrain-grass-jungle-"></a>

## `terrain-grass-jungle*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Jungle Grass terrain.

Id: `60`

<a id="symbol-terrain-grass-old"></a>

## `terrain-grass-old`

- Kind: `value`
- Detail: Terrain value

Old grass terrain. Used as the base terrain for cliffs. Replaced with Baobab Forest in the African Kingdoms expansion.

Id: `16`

<a id="symbol-terrain-grass-rainforest-"></a>

## `terrain-grass-rainforest*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Rainforest Grass terrain.

Id: `83`

<a id="symbol-terrain-grass-snow"></a>

## `terrain-grass-snow`

- Kind: `value`
- Detail: Terrain value

Snow Grass terrain. Obsolete in DE.

Id: `34`

<a id="symbol-terrain-grass2"></a>

## `terrain-grass2`

- Kind: `value`
- Detail: Terrain value

Grass 2 terrain.

Id: `12`

<a id="symbol-terrain-grass3"></a>

## `terrain-grass3`

- Kind: `value`
- Detail: Terrain value

Grass 3 terrain.

Id: `9`

<a id="symbol-terrain-gravel-desert-"></a>

## `terrain-gravel-desert*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Desert Gravel terrain.

Id: `102`

<a id="symbol-terrain-gravel-"></a>

## `terrain-gravel*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Gravel terrain.

Id: `70`

<a id="symbol-terrain-ice"></a>

## `terrain-ice`

- Kind: `value`
- Detail: Terrain value

Ice terrain. This ice terrain is navigable by ships.

Id: `26`

<a id="symbol-terrain-ice-beach"></a>

## `terrain-ice-beach`

- Kind: `value`
- Detail: Terrain value

Ice Beach terrain. Ice terrain created on shorelines.

Id: `37`

<a id="symbol-terrain-ice-soft-"></a>

## `terrain-ice-soft*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Soft Ice terrain.

Id: `127`

<a id="symbol-terrain-ice2"></a>

## `terrain-ice2`

- Kind: `value`
- Detail: Terrain value

Other Ice terrain. This ice terrain is not navigable by ships.

Id: `35`

<a id="symbol-terrain-koh"></a>

## `terrain-koh`

- Kind: `value`
- Detail: Terrain value

Terrain placed under monuments in King of the Hill games.

Id: `40`

<a id="symbol-terrain-leaves"></a>

## `terrain-leaves`

- Kind: `value`
- Detail: Terrain value

Leaves terrain.

Id: `5`

<a id="symbol-terrain-pasture-dead-"></a>

## `terrain-pasture-dead*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Dead Pasture terrain.

Id: `118`

<a id="symbol-terrain-pasture-"></a>

## `terrain-pasture*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Pasture terrain.

Id: `117`

<a id="symbol-terrain-pasture1-"></a>

## `terrain-pasture1*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Pastures that are 0% planted.

Id: `119`

<a id="symbol-terrain-pasture2-"></a>

## `terrain-pasture2*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Pastures that are 33% planted.

Id: `120`

<a id="symbol-terrain-pasture3-"></a>

## `terrain-pasture3*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Pastures that are 66% planted.

Id: `121`

<a id="symbol-terrain-road"></a>

## `terrain-road`

- Kind: `value`
- Detail: Terrain value

Road terrain.

Id: `24`

<a id="symbol-terrain-road-broken"></a>

## `terrain-road-broken`

- Kind: `value`
- Detail: Terrain value

Broken Road terrain.

Id: `25`

<a id="symbol-terrain-road-fungus"></a>

## `terrain-road-fungus`

- Kind: `value`
- Detail: Terrain value

Fungus Road terrain. Obsolete in DE. In DE, use terrain-road-fungus-de.

Id: `39`

<a id="symbol-terrain-road-fungus-de-"></a>

## `terrain-road-fungus-de*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Road Fungus terrain. Replaces terrain-road-fungus terrain in DE.

Id: `75`

<a id="symbol-terrain-road-gravel-"></a>

## `terrain-road-gravel*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Gravel Road terrain.

Id: `78`

<a id="symbol-terrain-road-snow"></a>

## `terrain-road-snow`

- Kind: `value`
- Detail: Terrain value

Snow Road. Obsolete in DE. In DE, use terrain-foundation-snow

Id: `38`

<a id="symbol-terrain-savannah-dirt-"></a>

## `terrain-savannah-dirt*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Savannah Dirt terrain. Defconsted as terrain-unknown in UP.

Id: `41`

<a id="symbol-terrain-shallows"></a>

## `terrain-shallows`

- Kind: `value`
- Detail: Terrain value

Shallows terrain.

Id: `4`

<a id="symbol-terrain-shallows-azure-"></a>

## `terrain-shallows-azure*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Azure Shallows terrain.

Id: `59`

<a id="symbol-terrain-shallows-mangrove-"></a>

## `terrain-shallows-mangrove*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Mangrove Shallows terrain.

Id: `54`

<a id="symbol-terrain-shallows-yellow-"></a>

## `terrain-shallows-yellow*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Yellow Shallows terrain.

Id: `115`

<a id="symbol-terrain-snow"></a>

## `terrain-snow`

- Kind: `value`
- Detail: Terrain value

Snow terrain.

Id: `32`

<a id="symbol-terrain-snow-light-"></a>

## `terrain-snow-light*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Light Snow terrain.

Id: `73`

<a id="symbol-terrain-snow-soft-light-"></a>

## `terrain-snow-soft-light*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Light Soft Snow terrain.

Id: `125`

<a id="symbol-terrain-snow-soft-strong-"></a>

## `terrain-snow-soft-strong*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Strong Soft Snow terrain.

Id: `126`

<a id="symbol-terrain-snow-soft-"></a>

## `terrain-snow-soft*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Soft Snow terrain.

Id: `124`

<a id="symbol-terrain-snow-strong-"></a>

## `terrain-snow-strong*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Strong Snow terrain.

Id: `74`

<a id="symbol-terrain-swamp-bogland-"></a>

## `terrain-swamp-bogland*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Bogland Swamp terrain.

Id: `101`

<a id="symbol-terrain-swamp-shallows-"></a>

## `terrain-swamp-shallows*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Swamp Shallows terrain.

Id: `111`

<a id="symbol-terrain-underbrush-jungle-"></a>

## `terrain-underbrush-jungle*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Jungle Underbrush terrain.

Id: `77`

<a id="symbol-terrain-underbrush-leaves-"></a>

## `terrain-underbrush-leaves*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Leaves Underbrush terrain.

Id: `71`

<a id="symbol-terrain-underbrush-snow-"></a>

## `terrain-underbrush-snow*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Snow Underbrush terrain.

Id: `72`

<a id="symbol-terrain-water"></a>

## `terrain-water`

- Kind: `value`
- Detail: Terrain value

Shallow Water terrain.

Id: `1`

<a id="symbol-terrain-water-azure-"></a>

## `terrain-water-azure*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Azure Water terrain.

Id: `58`

<a id="symbol-terrain-water-beach"></a>

## `terrain-water-beach`

- Kind: `value`
- Detail: Terrain value

Beach terrain.

Id: `2`

<a id="symbol-terrain-water-bridge"></a>

## `terrain-water-bridge`

- Kind: `value`
- Detail: Terrain value

Walkable water terrain placed under bridges.

Id: `28`

<a id="symbol-terrain-water-brown-"></a>

## `terrain-water-brown*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Brown Water terrain.

Id: `96`

<a id="symbol-terrain-water-deep"></a>

## `terrain-water-deep`

- Kind: `value`
- Detail: Terrain value

Deep Water terrain.

Id: `22`

<a id="symbol-terrain-water-deep-ocean-"></a>

## `terrain-water-deep-ocean*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Deep Ocean Water terrain.

Id: `57`

<a id="symbol-terrain-water-green-"></a>

## `terrain-water-green*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Green Water terrain.

Id: `95`

<a id="symbol-terrain-water-medium"></a>

## `terrain-water-medium`

- Kind: `value`
- Detail: Terrain value

Medium Water terrain.

Id: `23`

<a id="symbol-terrain-water-old"></a>

## `terrain-water-old`

- Kind: `value`
- Detail: Terrain value

Old water terrain. Probably the Shoreless Water in the editor.

Id: `15`

<a id="symbol-terrain-water-weeds-"></a>

## `terrain-water-weeds*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Water Weeds terrain.

Id: `130`

<a id="symbol-terrain-water-yellow-deep-"></a>

## `terrain-water-yellow-deep*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Deep Yellow Water terrain.

Id: `116`

<a id="symbol-terrain-water-yellow-"></a>

## `terrain-water-yellow*`

- Kind: `value`
- Detail: Terrain value

DE only. Must be defined with a defconst. Yellow Water terrain.

Id: `114`

<a id="symbol-teutonic"></a>

## `teutonic`

- Kind: `value`
- Detail: Civ value

Teutons

Id: `4`

<a id="symbol-thames"></a>

## `thames`

- Kind: `value`
- Detail: MapType value

Thames map.

Id: `214`

<a id="symbol-the-majapahit-empire"></a>

## `the-majapahit-empire`

- Kind: `value`
- Detail: MapType value

The Majapahit Empire battle royale map.

Id: `146`

<a id="symbol-thracians"></a>

## `thracians`

- Kind: `value`
- Detail: Civ value

Thracians (must define with a defconst first).

Id: `55`

<a id="symbol-time-limit"></a>

## `time-limit`

- Kind: `value`
- Detail: VictoryCondition value

Time Limit victory. The team with the highest score at the time limit wins.

Id: `2`

<a id="symbol-timer-disabled"></a>

## `timer-disabled`

- Kind: `value`
- Detail: TimerState value

The timer is disabled.

Id: `0`

<a id="symbol-timer-running"></a>

## `timer-running`

- Kind: `value`
- Detail: TimerState value

The timer has been set, but it hasn't been triggered yet.

Id: `2`

<a id="symbol-timer-status"></a>

## `timer-status`

- Kind: `value`
- Detail: FactId value

The status of a timer, either timer-disabled, timer-running, or timer-triggered. The corresponding fact command is up-timer-status.

Id: `51`

<a id="symbol-timer-triggered"></a>

## `timer-triggered`

- Kind: `value`
- Detail: TimerState value

The timer has triggered, and it hasn't been disabled yet.

Id: `1`

<a id="symbol-tiny-map-tiny"></a>

## `tiny-map, tiny`

- Kind: `value`
- Detail: MapSize value

Tiny (2 player) map size. 120x120 tiles.

Id: `120`

<a id="symbol-tower-class"></a>

## `tower-class`

- Kind: `value`
- Detail: ClassId value

Tower class.

Id: `952`

<a id="symbol-trade-cart-class-"></a>

## `trade-cart-class*`

- Kind: `value`
- Detail: ClassId value

Trade Cart class.

Id: `919`

<a id="symbol-trade-cog-class-"></a>

## `trade-cog-class*`

- Kind: `value`
- Detail: ClassId value

Trade Cog class.

Id: `902`

<a id="symbol-transport-ship-class-"></a>

## `transport-ship-class*`

- Kind: `value`
- Detail: ClassId value

Transport Ship class.

Id: `920`

<a id="symbol-treaty-time"></a>

## `treaty-time`

- Kind: `value`
- Detail: FactId value

DE only. The amount of treaty time left, in seconds. There isn't a corresponding fact command, but you can also store the remaining treaty time with up-get-treaty-data.

Id: `54`

<a id="symbol-tree-class-"></a>

## `tree-class*`

- Kind: `value`
- Detail: ClassId value

Tree class.

Id: `915`

<a id="symbol-trigger"></a>

## `trigger`

- Kind: `value`
- Detail: EventType value

Trigger

Id: `0`

<a id="symbol-tupi"></a>

## `tupi`

- Kind: `value`
- Detail: Civ value

Tupi (must define with a defconst first).

Id: `59`

<a id="symbol-turbo-random-map"></a>

## `turbo-random-map`

- Kind: `value`
- Detail: GameType value

Turbo Random Map game.

Id: `8`

<a id="symbol-turkish"></a>

## `turkish`

- Kind: `value`
- Detail: Civ value

Turks

Id: `10`

<a id="symbol-ultra-high-resources"></a>

## `ultra-high-resources`

- Kind: `value`
- Detail: StartingResources value

Start with 20000W, 20000F, 10000G, and 5000S in random map games, the same as a Death match game. Other game modes may have different starting resources. DE only.

Id: `4`

<a id="symbol-unit-count"></a>

## `unit-count`

- Kind: `value`
- Detail: FactId value

The number of units the player has. The corresponding fact commands are unit-count and players-unit-count. There isn't a corresponding FactId for unit-count-total.

Id: `24`

<a id="symbol-unit-type-count"></a>

## `unit-type-count`

- Kind: `value`
- Detail: FactId value

The number of a given type of unit a player has, excluding units currently training. The corresponding fact commands are unit-type-count and players-unit-type-count.

Id: `25`

<a id="symbol-unit-type-count-total"></a>

## `unit-type-count-total`

- Kind: `value`
- Detail: FactId value

The number of a given type of unit a player has, including units currently training. The corresponding fact command is unit-type-count-total.

Id: `26`

<a id="symbol-unit-type-in-town"></a>

## `unit-type-in-town`

- Kind: `value`
- Detail: FactId value

The number of enemy units of the given type inside the AI's town. The corresponding fact command is up-unit-type-in-town.

Id: `45`

<a id="symbol-unpacked-trebuchet-class"></a>

## `unpacked-trebuchet-class`

- Kind: `value`
- Detail: ClassId value

Unpacked Trebuchet class.

Id: `954`

<a id="symbol-valley"></a>

## `valley`

- Kind: `value`
- Detail: MapType value

Valley map.

Id: `76`

<a id="symbol-vietnamese"></a>

## `vietnamese`

- Kind: `value`
- Detail: Civ value

Vietnamese. In WK, must define with a defconst before it can be used.

Id: `31`

<a id="symbol-viking"></a>

## `viking`

- Kind: `value`
- Detail: Civ value

Vikings

Id: `11`

<a id="symbol-villager-class"></a>

## `villager-class`

- Kind: `value`
- Detail: ClassId value

Villager class.

Id: `904`

<a id="symbol-villager-type-in-town"></a>

## `villager-type-in-town`

- Kind: `value`
- Detail: FactId value

The number of enemy villagers of the given type inside the AI's town. The corresponding fact command is up-villager-type-in-town.

Id: `46`

<a id="symbol-volcanic-island"></a>

## `volcanic-island`

- Kind: `value`
- Detail: MapType value

Volcanic Island map.

Id: `156`

<a id="symbol-vulpine"></a>

## `vulpine`

- Kind: `value`
- Detail: MapType value

Vulpine map.

Id: `215`

<a id="symbol-wade"></a>

## `wade`

- Kind: `value`
- Detail: MapType value

Wade map.

Id: `174`

<a id="symbol-wall-class"></a>

## `wall-class`

- Kind: `value`
- Detail: ClassId value

Wall class.

Id: `927`

<a id="symbol-warboat-count"></a>

## `warboat-count`

- Kind: `value`
- Detail: FactId value

The number of the player's warships, not including fishing ships, transport ships, or trade cogs. The corresponding fact command is warboat-count.

Id: `16`

<a id="symbol-warship-class"></a>

## `warship-class`

- Kind: `value`
- Detail: ClassId value

Warship class.

Id: `922`

<a id="symbol-watch-tower-line"></a>

## `watch-tower-line`

- Kind: `value`
- Detail: BuildingId value

Watch Tower line. Bugged. Won't include Guard Tower or Keep in counting commands. "watch-tower" by itself usually works in non-counting commands. In Return of Rome, it includes Watch Tower, Sentry Tower, Guard Tower, but not Ballista Tower.

Id: `-398`

<a id="symbol-water-nomad"></a>

## `water-nomad`

- Kind: `value`
- Detail: MapType value

Water Nomad map.

Id: `116`

<a id="symbol-wei"></a>

## `wei`

- Kind: `value`
- Detail: Civ value

Wei (must define with a defconst first).

Id: `51`

<a id="symbol-wolf-hill"></a>

## `wolf-hill`

- Kind: `value`
- Detail: MapType value

Wolf Hill map. Must be defined with a defconst.

Id: `126`

<a id="symbol-wonder-race"></a>

## `wonder-race`

- Kind: `value`
- Detail: GameType value

Wonder Race game.

Id: `6`

<a id="symbol-wood"></a>

## `wood`

- Kind: `value`
- Detail: Commodity value

Wood

Id: `1`

<a id="symbol-wood-amount"></a>

## `wood-amount`

- Kind: `value`
- Detail: FactId value

The current wood amount. The corresponding fact command is wood-amount.

Id: `6`

<a id="symbol-wu"></a>

## `wu`

- Kind: `value`
- Detail: Civ value

Wu (must define with a defconst first).

Id: `50`

<a id="symbol-yucatan"></a>

## `yucatan`

- Kind: `value`
- Detail: MapType value

Yucatan map.

Id: `27`

