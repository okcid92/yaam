# Standards de Code — Next.js

> Généré par Yaam — conventions spécifiques Next.js / React.

## Nommage

- **Composants** : `PascalCase` (ex: `UserProfile`)
- **Fichiers** : `kebab-case` (ex: `user-profile.tsx`)
- **Fonctions/ hooks** : `camelCase` (ex: `useUserProfile`)
- **Constantes** : `UPPER_SNAKE_CASE`
- **Types/ interfaces** : `PascalCase`, préfixé `I` optionnel

## Architecture

- `app/` router (App Router) par défaut.
- Composants serveur par défaut, `'use client'` quand nécessaire.
- Logique métier dans des `lib/` ou `utils/`.
- Appels API via des `server actions` ou `route handlers`.

## Commandes

```bash
npm run dev
npm run build
npm run lint
npm run test
npm run typecheck
```

## Tests

- Vitest + Testing Library.
- Fichiers : `{nom}.test.tsx` à côté du composant.
- Tests d'intégration avec `msw` pour les appels API.
