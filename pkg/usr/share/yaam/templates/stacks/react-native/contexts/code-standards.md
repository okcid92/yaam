# Standards de Code — React Native

> Généré par Yaam — conventions spécifiques React Native.

## Nommage

- **Composants** : `PascalCase` (ex: `UserProfileCard`)
- **Fichiers** : `kebab-case` (ex: `user-profile-card.tsx`)
- **Hooks** : `camelCase`, préfixé `use` (ex: `useUserProfile`)
- **Navigators** : `PascalCase` (ex: `AppNavigator`, `AuthStack`)
- **Styles** : `StyleSheet.create()` ou `camelCase` pour les propriétés

## Architecture

- Screens dans `screens/`, composants réutilisables dans `components/`.
- Navigation avec React Navigation (Stack, Tab, Drawer).
- State management : React Context + useReducer / Zustand.
- Appels API dans des services séparés.

## Commandes

```bash
npx expo start
npx expo run:ios
npx expo run:android
npx expo test
npm run lint
```

## Tests

- Jest + React Native Testing Library.
- Fichiers : `{nom}.test.tsx` à côté du composant.
- Tester les comportements, pas l'implémentation.
