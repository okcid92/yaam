# 🧠 Comment ça marche — Yaam

## En une phrase

Yaam est un petit serveur MCP qui ajoute de la **mémoire de contexte** à votre agent IA (OpenCode). Il lit, écrit et met à jour des fichiers markdown dans votre projet.

## Le flux

```
Vous : "yaam-init"
  → L'agent appelle yaam_init (scan README, détection stack)
  → L'agent appelle setup_yaam_framework (génère l'arborescence)

Vous : "Ajoute une page de connexion"
  → L'agent consulte contexts/project-overview.md
  → L'agent code
  → L'agent utilise complete_tracer_task pour cocher la tâche
```

## Ce qu'il y a dans le repo

| Fichier | Rôle |
|---------|------|
| `yaam-server.py` | Le serveur MCP en Python. Point d'entrée. |
| `yaam-init` | Script shell pour scanner un projet en CLI. |
| `templates/` | Les fichiers markdown générés dans le projet cible. |
| `pkg/` | Structure pour construire le paquet .deb Debian. |
| `build-deb.sh` | Construit `yaam_1.0.0_all.deb`. |
| `tests/` | Tests pytest (15 tests). |
| `roadmap.md` | Roadmap du framework Yaam lui-même. |
| `AGENTS.md` | Instructions pour l'agent OpenCode. |
| `requirements.txt` | Dépendance : `mcp>=2.0`. |

## Comment l'installer

```bash
# Depuis le .deb
sudo dpkg -i yaam_1.0.0_all.deb
sudo apt-get install -f

# Ou depuis les sources
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 yaam-server.py
```

## Les 6 outils MCP

1. **check_yaam_status** — Vérifie si Yaam est installé dans le projet.
2. **setup_yaam_framework** — Génère l'arborescence contexts/, features-specs/, issues/, AGENT.md.
3. **get_project_status** — Lit progress-tracer.md (roadmap + journal).
4. **add_tracer_task** — Ajoute une tâche `- [ ]` dans le tracker.
5. **complete_tracer_task** — Coche `- [x]` une tâche + horodate.
6. **log_progress_note** — Ajoute une note horodatée dans le journal.
7. **yaam_init** — Scanne le README et détecte nom, stack, description.

## L'arborescence générée

```
mon-projet/
├── contexts/
│   ├── ai-workflow-rules.md
│   ├── architecture-context.md
│   ├── code-standards.md
│   ├── progress-tracer.md      ← Roadmap + journal (mis à jour par l'IA)
│   ├── project-overview.md
│   └── ui-context.md
├── features-specs/TEMPLATE.md
├── issues/TEMPLATE.md
└── AGENT.md                    ← Directives impératives pour l'IA
```

## Comment l'utiliser

1. Installez le paquet `.deb` ou lancez `yaam-server.py`.
2. Configurez OpenCode (`~/.opencode.json`) — le postinst le fait automatiquement.
3. Ouvrez votre projet avec OpenCode.
4. Tapez **"yaam-init"** dans le chat.
5. L'IA scanne votre README, pose des questions, génère l'arborescence.
6. Donnez des instructions de code — l'IA met à jour la roadmap toute seule.
