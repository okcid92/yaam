# Standards de Code

> Généré par Yaam — conventions à suivre dans tout le projet.

## Nommage

- **Variables / fonctions** : `camelCase`
- **Classes / composants** : `PascalCase`
- **Fichiers** : `kebab-case`
- **Constantes** : `UPPER_SNAKE_CASE`
- **Bases de données** : `snake_case`

## Typage

- Privilégier le typage explicite.
- Éviter `any` / types implicites.
- Exporter les interfaces partagées.

## Structure de fichier

```
1. Imports (externes → internes → relatifs)
2. Types / Interfaces
3. Logique principale
4. Exports
```

## Tests

- Un fichier de test par module.
- Nommer : `[module].test.[ext]`
- Coverage minimal attendu : 80 %

## CSS / Style

- Utiliser [Tailwind / CSS Modules / Styled Components / etc.]
- Éviter les styles inline.
- Points de rupture standard : sm (640), md (768), lg (1024), xl (1280).
