# 🧠 Yaam (💡 Intelligence / Sagesse)

**Yaam** est un framework de gestion de contexte minimaliste et ultra-léger conçu pour le *Vibe Coding*. Propulsé par le **Model Context Protocol (MCP)** d'Anthropic, Yaam permet à vos agents IA (comme **OpenCode**) de comprendre l'état de votre projet, de respecter vos standards d'architecture, et de mettre à jour la roadmap de manière **100% autonome et bidirectionnelle**, sans friction et directement depuis le chat.

Contrairement aux usines à gaz de gestion de mémoire à long terme (bases de données vectorielles complexes, configurations lourdes), Yaam adopte une approche **Markdown-First** et **Git-friendly**. Tout votre contexte est stocké localement dans votre projet et évolue au rythme de vos commits.

---

## 🚀 Fonctionnalités Clés

- **Initialisation Intelligente (`yaam-init`) :** Lancé directement au sein d'OpenCode, Yaam scanne votre dossier. S'il détecte un `README.md` existant, l'IA vous propose de générer intelligemment tout le contexte du projet à partir de celui-ci et de quelques questions rapides.
- **Auto-Mise à Jour du Progrès (Automatic Progress) :** Grâce aux outils MCP dédiés, l'agent IA coche les tâches terminées, ajoute de nouvelles sous-tâches s'il rencontre des imprévus, et tient un journal de bord historique horodaté de ses modifications dans `progress-tracer.md`.
- **Architecture Découpée (Context Splitting) :** Fini le gaspillage de tokens système en injectant tout l'historique ou d'immenses fichiers de prompt. L'IA pioche chirurgicalement ce dont elle a besoin (règles d'UI, standards de code, spécifications d'une fonctionnalité précise).
- **Package Natif Debian :** Distribué sous forme de paquet `.deb`, Yaam s'installe globalement sur votre système Linux et s'intègre en une ligne de configuration à vos outils d'IA.

---

## 📁 L'Arborescence Yaam

Lorsqu'il est initialisé à la racine d'une application (Laravel, Next.js, React Native, etc.), Yaam génère la structure suivante :

```text
mon-projet/
├── contexts/
│   ├── ai-workflow-rules.md     # Règles de comportement de l'IA (Directives Vibe Coding)
│   ├── architecture-context.md  # Choix techniques, configuration BDD, structure globale
│   ├── code-standards.md        # Conventions de nommage, clean code, typage
│   ├── progress-tracer.md       # LE COEUR : Roadmap dynamique et Journal historique
│   ├── project-overview.md      # Description macro du projet et objectifs métiers
│   └── ui-context.md            # Charte graphique, palettes, composants UI réutilisables
├── features-specs/
│   └── TEMPLATE.md              # Modèle vide pour documenter une nouvelle fonctionnalité
├── issues/
│   └── TEMPLATE.md              # Modèle standardisé pour décrire un bug ou une régression
└── AGENT.md                     # Directives système impératives lues par l'IA au démarrage
```

## 🛠️ Outils MCP Exposés à l'IA

Le serveur MCP `yaam-server` met à disposition de votre agent une boîte à outils chirurgicale :

- `check_yaam_status` : Analyse le dossier pour savoir si le framework est en place ou s'il faut lancer la phase interactive.
- `setup_yaam_framework` : Génère l'arborescence complète basée sur vos besoins techniques.
- `get_project_status` : Permet à l'IA de lire la feuille de route avant de coder.
- `add_tracer_task` : Permet à l'IA d'ajouter une tâche non cochée au tracker de progression.
- `complete_tracer_task` : Permet à l'IA de remplacer un `- [ ]` par un `- [x]` dès qu'une fonctionnalité est implémentée et testée.
- `log_progress_note` : Ajoute une note horodatée dans le Journal Historique de modification.

## 📦 Installation (Debian / Ubuntu / Mint)

### 1. Installation du paquet

Téléchargez le dernier fichier `.deb` depuis les releases (ou via votre dépôt APT personnalisé) et installez-le :

```bash
sudo dpkg -i yaam_1.0.0_all.deb
# Installe les dépendances nécessaires si besoin
sudo apt-get install -f
```

### 2. Configuration d'OpenCode

Ajoutez le serveur MCP Yaam de manière globale dans votre fichier de configuration `~/.opencode.json` :

```json
{
  "mcp": {
    "servers": {
      "yaam": {
        "command": "/usr/bin/yaam-server"
      }
    }
  }
}
```

## 🏎️ Le Workflow En Action

Ouvrez votre projet (contenant idéalement un premier `README.md`) et lancez votre agent :

```bash
opencode
```

Tapez simplement dans le chat de l'agent :

```bash
yaam-init
```

L'IA détecte l'absence du framework, analyse votre README, et vous pose des questions ciblées dans le chat (Nom du projet, stack, contraintes).

Une fois votre accord donné, l'arborescence est créée. L'IA lit `AGENT.md` qui lui donne l'obligation absolue de s'auto-gérer.

Vous donnez vos consignes de code ("Build l'UI de la page de profil"). L'IA code, teste, et utilise les outils MCP en arrière-plan pour mettre à jour votre fichier `progress-tracer.md` en temps réel.

## 📄 Licence

Ce projet est sous licence MIT. Développé avec 🧠 pour rendre le vibe coding plus structuré, plus rapide et plus intelligent.