# Contexte d'Architecture — React Native

> Généré par Yaam — architecture spécifique React Native.

## Stack

- **Framework** : React Native (Expo / CLI)
- **Langage** : TypeScript
- **Navigation** : React Navigation
- **State** : Zustand / React Context
- **API** : React Query / tRPC
- **Storage** : AsyncStorage / MMKV
- **UI** : NativeWind / Styled Components

## Structure

```
src/
├── app/
├── screens/
├── components/
│   ├── ui/
│   └── shared/
├── navigation/
├── services/
├── hooks/
├── stores/
├── types/
└── utils/
```

## Conventions

- Expo Router (file-based routing) si Expo.
- Éviter les dépendances natives excessives.
- Hooks personnalisés pour la logique réutilisable.
- Validation des entrées avec Zod.
