# Yaam — AGENTS.md

## What this repo is

Documentation + serveur MCP Python pour **Yaam**, un framework de gestion de contexte Vibe Coding avec le Model Context Protocol (MCP). La source de vérité est `README.md`.

## Language

All prose is in French. Keep new documentation entries in French.

## What matters

- `README.md` describes the framework spec, MCP tools, directory layout, and Debian install workflow. This is the primary artifact.
- The directory tree described in the README (`contexts/`, `features-specs/`, `issues/`, `AGENT.md`) is what Yaam **generates** when run inside a project — it is **not** present in this repo itself.
- `templates/` contient les fichiers markdown source que `yaam-server` utilise pour générer l'arborescence dans un projet cible.
- `yaam-server.py` est le serveur MCP en Python (dépendances dans `requirements.txt`). Point d'entrée : `python3 yaam-server.py [--project-path] [--verbose] [--dry-run]`.
- `pkg/` contient la structure du paquet Debian. `build-deb.sh` construit le `.deb` (output : `yaam_1.0.0_all.deb`).
- `roadmap.md` est la feuille de route dynamique du framework Yaam. L'agent coche les tâches au fur et à mesure avec `- [x]`.

## Workflow

- **Push après chaque modification :** tout commit doit être suivi d'un `git push` immédiat sur GitHub.
- **Questionner avant d'implémenter :** poser au moins 5 questions à l'utilisateur pour clarifier le besoin avant de coder ou modifier une feature.

## Conventions

- Preserve the existing French descriptions and example code blocks in `README.md`.
- Keep markdown clean: no unnecessary formatting, no emoji overuse (existing ones like 🧠 ☝️ are fine).
- The README is the *specification* — if it says something, trust it as the source of truth.
