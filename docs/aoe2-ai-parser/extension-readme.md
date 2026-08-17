# AOE2 AI Parser

VS Code and Cursor support for Age of Empires II: Definitive Edition AI
scripts. Install the extension, open a folder containing `.ai` and `.per` files,
and use the AoE2 command palette actions for linting and package reports.

## Features

- Syntax highlighting for `.per` and `.ai` files.
- Registry-backed completion, hover, and signature help for commands,
  strategic numbers, objects, techs, classes, DUC actions, operators, and other
  values.
- Semantic coloring that distinguishes actions, facts, strategic numbers,
  objects, techs, values, and local constants.
- Optional `AOE2 AI Parser Dark`, `AOE2 AI Parser Light`, and
  `AOE2 AiScript Classic` themes. The classic theme is based on the original
  extension's TextMate scopes instead of parser-specific semantic tokens.
- Go to definition for local `defconst` declarations, `.ai` load targets, and
  generated local Markdown reference docs.
- Package-aware diagnostics from the bundled parser/linter.
- Command palette actions for linting/formatting the current file, current AI,
  current folder, recursive folder, and generated package reports.
- Compact package graph output for reachable `.per` loads and `.xs` includes.
- Quick fixes and diagnostic documentation actions for common validator
  diagnostics.

## Requirements

The extension bundles the AOE2 AI Parser validator and reference data, so users do
not need to clone the tooling repository for normal editor diagnostics.

Python must be available. Configure `aoe2_AiScript.pythonPath` if `python` is
not on PATH.

Contributors can set `aoe2_AiScript.labPath` to a local AOE2 AI Parser
checkout to test parser or reference-data changes without repackaging the
extension.

## Commands

- `AoE2: Lint Current File`
- `AoE2: Lint Current AI`
- `AoE2: Lint Current Folder`
- `AoE2: Lint Recursive Folder`
- `AoE2: Generate Package Report`
- `AoE2: Open Latest Package Report`
- `AoE2: AutoFormat Current File`
- `AoE2: AutoFormat Current AI`
- `AoE2: AutoFormat Current Folder`
- `AoE2: AutoFormat Recursive Folder`
- `AoE2: Format Then Lint Current File`
- `AoE2: Format Then Lint Current AI`
- `AoE2: Format Then Lint Current Folder`
- `AoE2: Format Then Lint Recursive Folder`
- `AoE2: Open Symbol Docs Preview`
- `AoE2: Open Diagnostic Docs Preview`

## Theme

For the most distinct parser token colors, choose `AOE2 AI Parser Dark` or
`AOE2 AI Parser Light` from `Preferences: Color Theme`. To stay closer to the
original AoE2 AiScript extension coloring model, choose `AOE2 AiScript Classic`;
it colors the original TextMate scopes and leaves semantic highlighting off.

## Settings

- `aoe2_AiScript.useLabLinter`: use bundled AOE2 AI Parser diagnostics.
- `aoe2_AiScript.usePackageLint`: prefer package-aware live diagnostics.
  Default is `false` because large AI packages can make live open/save
  diagnostics CPU-heavy. Use explicit current-AI, current-folder, or
  recursive-folder lint commands for manual validation.
- `aoe2_AiScript.packageFailLevel`: minimum package-lint severity surfaced by
  package commands and package-aware diagnostics (`error`, `warning`, or
  `info`). Default is `info`.
- `aoe2_AiScript.labPath`: optional development checkout override.
- `aoe2_AiScript.pythonPath`: Python executable.
- `aoe2_AiScript.updateErrorsWhen`: validate on save, on change, or never.
- `aoe2_AiScript.formatOnSave`: run `AoE2: AutoFormat` during save. Default
  is `false`.
- `aoe2_AiScript.formatMaxLineLength`: comment wrapping limit for AutoFormat,
  from 40 to 255. Default is 255.
- `aoe2_AiScript.formatChat`: allow AutoFormat to touch `chat-to-all` and
  `chat-to-player` lines. Default is `false`.
- `aoe2_AiScript.enableSemanticColors`: enable parser-specific semantic colors
  for commands, facts, strategic numbers, objects, techs, values, and local
  constants. Default is `false` so users keep their normal editor theme colors.
- `aoe2_AiScript.semanticColors.*`: direct color settings for parser semantic
  categories such as action, fact, strategicNumber, object, tech, value, and
  localConstant. These apply when semantic colors are enabled.

`Lint Current File` validates only the active file. `Lint Current AI` resolves
which nearby `.ai` root reaches the active `.per` through load directives, then
validates that selected AI root plus reachable `.per` loads. If exactly one AI
reaches the active file, it is selected automatically; if the file is shared by
multiple AIs, the extension asks which root to use. If no AI load graph reaches
the active file, the command stops instead of guessing from nearby `.ai` files.
`Lint Current Folder` validates `.ai` roots directly inside the active file's
folder only. `Lint Recursive Folder` validates every `.ai` root below that
folder.
Folder lint, current-AI lint, and package-report commands write a Markdown
summary under `.tmp/lint-package/` and open it in a side Markdown Preview when
the linter finishes.
The output panel also starts with a `Lint trace` tree that shows the input path,
resolved `.ai` roots, root `.per` files, every reachable `.per`, included
`.xs` files, and load/include edges so users can confirm exactly what was
validated. Package and folder lint commands also stream a simpler live trace
while linting is still running.

`AoE2: AutoFormat Current File` formats the active `.per` or `.ai` file. It
enforces final newlines for `.per`, keeps `.ai` entry files empty, wraps long
comments, promotes overlong inline comments above code, normalizes load path
separators to the dominant style in the file, and splits multiple same-line
expressions into separate lines. Chat lines are skipped unless `formatChat` is
enabled.
`AoE2: AutoFormat Current AI` uses the same current-AI load-graph resolution
and formats the selected `.ai` root plus reachable `.per` loads. `AutoFormat Current Folder` formats direct
`.ai`/`.per` children only. `AutoFormat Recursive Folder` formats every
`.ai`/`.per` below the active file's folder. The `Format Then Lint` commands
run the corresponding formatter first and then lint the same scope when
formatting succeeds.

For local symbol docs, VS Code's built-in definition gesture is `Ctrl+Click`.
Cursor also supports its own side-definition gestures such as `Ctrl+Alt+Click`.
Use the hover link, right-click `AoE2: Open Symbol Docs Preview`, or the command
palette action when you want rendered Markdown Preview beside the script.

Reviewed findings can be suppressed inline with comments:

```lisp
; aoe2-ai-parser-disable-next-line repeat-chat
(chat-to-all "debug")
```

Diagnostics expose a quick fix named `Suppress <code> on this line`, which
inserts `; aoe2-ai-parser-disable-line <code>`.

Parser-specific semantic colors are off by default. Enable
`aoe2_AiScript.enableSemanticColors` if you want those token categories colored
separately from your normal theme.
You can then customize the colors directly through extension settings:

```json
{
  "aoe2_AiScript.semanticColors.theme": "auto",
  "aoe2_AiScript.semanticColors.byTheme": {
    "Dark": {
      "action": "#5DADEC",
      "fact": "#C69CFF",
      "strategicNumber": "#4CC2FF",
      "localConstant": "#57D68D"
    },
    "Light": {
      "action": "#0550AE",
      "fact": "#6F42C1",
      "strategicNumber": "#0A7EA4",
      "localConstant": "#116329"
    },
    "Custom": {
      "action": "#569CD6",
      "fact": "#C586C0",
      "strategicNumber": "#4BA3FF",
      "localConstant": "#7EE787"
    }
  }
}
```

Run `AoE2: Write Semantic Color Settings` from the command palette to write the
`Dark`, `Light`, and `Custom` presets into user `settings.json` for editing.
The command also removes legacy native editor color blocks from user/workspace
settings. The `auto` selector uses `Light` for light-named editor themes and
`Dark` otherwise; set it to `custom` to force the custom preset.

## Attribution

This extension is based on the open source AoE2 AiScript extension by Jvinniec:

https://github.com/Jvinniec/aoe2-aiscript

It keeps the original GPL-3.0-or-later license. AOE2 AI Parser adds the local
reference registry, parser/linter integration, package validator diagnostics,
generated documentation navigation, semantic coloring, and marketplace-friendly
bundled validator runtime.
