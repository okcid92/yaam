# Yaam — AGENTS.md

## What this repo is

Documentation-only repo for **Yaam**, a Vibe Coding context management framework using the Model Context Protocol (MCP). No code, no build, no tests. The single source of truth is `README.md`.

## Language

All prose is in French. Keep new documentation entries in French.

## What matters

- `README.md` describes the framework spec, MCP tools, directory layout, and Debian install workflow. This is the primary artifact.
- The directory tree described in the README (`contexts/`, `features-specs/`, `issues/`, `AGENT.md`) is what Yaam **generates** when run inside a project — it is **not** present in this repo itself.
- There is no `.deb` packaging, build scripts, CI, or test setup in this repo. The framework binary is distributed separately.
- `roadmap.md` est la feuille de route dynamique du framework Yaam. L'agent coche les tâches au fur et à mesure avec `- [x]`.

## Workflow

- **Push après chaque modification :** tout commit doit être suivi d'un `git push` immédiat sur GitHub.
- **Questionner avant d'implémenter :** poser au moins 5 questions à l'utilisateur pour clarifier le besoin avant de coder ou modifier une feature.

## Conventions

- Preserve the existing French descriptions and example code blocks in `README.md`.
- Keep markdown clean: no unnecessary formatting, no emoji overuse (existing ones like 🧠 ☝️ are fine).
- The README is the *specification* — if it says something, trust it as the source of truth.
