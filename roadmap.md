```

```

# 🗺️ Roadmap Yaam

> Roadmap dynamique — l'agent IA coche au fur et à mesure de l'avancement.

---

## Phase 1 — Fondations du Framework

### 1.1 Serveur MCP `yaam-server`

- [X] Implémenter le binaire `yaam-server` (Python)
- [X] Implémenter l'outil MCP `check_yaam_status`
- [X] Implémenter l'outil MCP `setup_yaam_framework`
- [X] Implémenter l'outil MCP `get_project_status`
- [X] Implémenter l'outil MCP `add_tracer_task`
- [X] Implémenter l'outil MCP `complete_tracer_task`
- [X] Implémenter l'outil MCP `log_progress_note`
- [X] Gérer les erreurs (pas de README, projet déjà initialisé, etc.)
- [X] Logger les appels MCP pour débogage

### 1.2 Génération de l'arborescence

- [X] Créer les templates markdown pour `contexts/` :
  - [X] `contexts/ai-workflow-rules.md`
  - [X] `contexts/architecture-context.md`
  - [X] `contexts/code-standards.md`
  - [X] `contexts/progress-tracer.md`
  - [X] `contexts/project-overview.md`
  - [X] `contexts/ui-context.md`
- [X] Créer le template `features-specs/TEMPLATE.md`
- [X] Créer le template `issues/TEMPLATE.md`
- [X] Créer `AGENT.md` (directives impératives pour l'IA)
- [X] Implémenter la logique `setup_yaam_framework` qui écrit ces fichiers

### 1.3 Initialisation intelligente (`yaam-init`)

- [X] Scanner le projet cible pour détecter un `README.md` existant
- [X] Analyser le README pour extraire nom, stack technique, contraintes
- [X] Poser des questions de clarification à l'utilisateur dans le chat *(via IA — l'outil `yaam_init` fournit les données, l'IA questionne dans le chat avant d'appeler `setup_yaam_framework`)*
- [X] Générer l'arborescence adaptée aux réponses

---

## Phase 2 — Distribution & Installation

### 2.1 Paquet Debian

- [X] Créer la structure `DEBIAN/control`, `DEBIAN/postinst`, `DEBIAN/postrm`
- [X] Templates embarqués dans `/usr/share/yaam/templates/`
- [X] `yaam-server` installé dans `/usr/bin/yaam-server`
- [X] `yaam-init` installé dans `/usr/bin/yaam-init`
- [X] Script `build-deb.sh` pour générer le `.deb`
- [X] Générer le `.deb` (`dpkg-deb --build`) — testé et validé
- [X] Tester l'installation complète avec `dpkg -i` et `apt-get install -f`

### 2.2 Configuration OpenCode

- [X] Auto-configuration dans `~/.opencode.json` via `postinst`
- [X] Nettoyage de la config via `postrm`
- [X] Documentation de la configuration dans `README.md`

---

## Phase 3 — Auto-gestion & Résilience

### 3.1 Mise à jour automatique du progrès

- [X] `add_tracer_task` : ajouter une tâche non cochée dans `progress-tracer.md`
- [X] `complete_tracer_task` : cocher une tâche (`- [ ]` → `- [x]`)
- [X] `log_progress_note` : horodater une note dans le journal historique
- [X] `get_project_status` : retourner l'état courant de la roadmap

### 3.2 Robustesse

- [x] Détecter et signaler les fichiers verrouillés / permissions insuffisantes
- [x] Éviter les doubles initialisations (ne pas écraser un projet déjà Yaam)
- [x] Mode dry-run pour prévisualiser les modifications
- [x] Tests pytest (15 tests, tous passent)

---

## Phase 4 — Écosystème & Itérations

### 4.1 Intégration continue

- [ ] Configurer une CI pour builder le `.deb` automatiquement
- [ ] Publier les releases sur GitHub

### 4.2 Templates avancés

- [ ] Proposer des templates par stack (Laravel, Next.js, React Native, Django)
- [ ] Option : template vide vs template pré-rempli

### 4.3 Feedback & améliorations

- [ ] Tester le workflow complet sur un vrai projet
- [ ] Itérer sur le prompt `AGENT.md` pour améliorer l'auto-gestion
- [ ] Documenter les retours d'expérience

---

## 🏁 Étapes validées

| Date       | Tâche                                                                         |
| ---------- | ------------------------------------------------------------------------------ |
| 2026-07-30 | Templates contextuels markdown (×9)                                           |
| 2026-07-30 | Serveur MCP yaam-server (Python) + 6 outils MCP                                |
| 2026-07-30 | Init intelligente yaam_init (scan README, détection stack, script standalone) |
| 2026-07-30 | Packaging .deb (control, postinst, postrm, .desktop, build-deb.sh) |
| 2026-07-30 | Phase 3 — Robustesse (double init, permissions, dry-run, tests pytest) |
