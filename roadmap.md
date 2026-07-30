# 🗺️ Roadmap Yaam

> Roadmap dynamique — l'agent IA coche au fur et à mesure de l'avancement.

---

## Phase 1 — Fondations du Framework

### 1.1 Serveur MCP `yaam-server`
- [x] Implémenter le binaire `yaam-server` (Python)
- [x] Implémenter l'outil MCP `check_yaam_status`
- [x] Implémenter l'outil MCP `setup_yaam_framework`
- [x] Implémenter l'outil MCP `get_project_status`
- [x] Implémenter l'outil MCP `add_tracer_task`
- [x] Implémenter l'outil MCP `complete_tracer_task`
- [x] Implémenter l'outil MCP `log_progress_note`
- [x] Gérer les erreurs (pas de README, projet déjà initialisé, etc.)
- [x] Logger les appels MCP pour débogage

### 1.2 Génération de l'arborescence
- [x] Créer les templates markdown pour `contexts/` :
  - [x] `contexts/ai-workflow-rules.md`
  - [x] `contexts/architecture-context.md`
  - [x] `contexts/code-standards.md`
  - [x] `contexts/progress-tracer.md`
  - [x] `contexts/project-overview.md`
  - [x] `contexts/ui-context.md`
- [x] Créer le template `features-specs/TEMPLATE.md`
- [x] Créer le template `issues/TEMPLATE.md`
- [x] Créer `AGENT.md` (directives impératives pour l'IA)
- [ ] Implémenter la logique `setup_yaam_framework` qui écrit ces fichiers

### 1.3 Initialisation intelligente (`yaam-init`)
- [x] Scanner le projet cible pour détecter un `README.md` existant
- [x] Analyser le README pour extraire nom, stack technique, contraintes
- [ ] Poser des questions de clarification à l'utilisateur dans le chat
- [x] Générer l'arborescence adaptée aux réponses

---

## Phase 2 — Distribution & Installation

### 2.1 Paquet Debian
- [ ] Créer la structure `DEBIAN/control`, `DEBIAN/postinst`
- [ ] Empaqueter `yaam-server` dans `/usr/bin/yaam-server`
- [ ] Générer le `.deb` (`dpkg-deb --build`)
- [ ] Tester l'installation avec `dpkg -i` et `apt-get install -f`

### 2.2 Configuration OpenCode
- [ ] Documenter la configuration MCP dans `~/.opencode.json`
- [ ] Option : proposer une commande `yaam-configure` pour auto-ajouter le serveur

---

## Phase 3 — Auto-gestion & Résilience

### 3.1 Mise à jour automatique du progrès
- [ ] `add_tracer_task` : ajouter une tâche non cochée dans `progress-tracer.md`
- [ ] `complete_tracer_task` : cocher une tâche (`- [ ]` → `- [x]`)
- [ ] `log_progress_note` : horodater une note dans le journal historique
- [ ] `get_project_status` : retourner l'état courant de la roadmap

### 3.2 Robustesse
- [ ] Détecter et signaler les fichiers verrouillés / permissions insuffisantes
- [ ] Éviter les doubles initialisations (ne pas écraser un projet déjà Yaam)
- [ ] Mode dry-run pour prévisualiser les modifications

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

| Date | Tâche |
|------|-------|
| 2026-07-30 | Templates contextuels markdown (×9) |
| 2026-07-30 | Serveur MCP yaam-server (Python) + 6 outils MCP |
| 2026-07-30 | Init intelligente yaam_init (scan README, détection stack, script standalone) |
