# Standards de Code — Laravel

> Généré par Yaam — conventions spécifiques Laravel.

## Nommage

- **Controllers** : `PascalCase` (ex: `UserController`)
- **Models** : `PascalCase`, singulier (ex: `User`, `Post`)
- **Migrations** : `snake_case` daté (ex: `2024_01_01_000001_create_users_table`)
- **Tables** : `snake_case` pluriel (ex: `users`, `posts`)
- **Relations** : `camelCase` (ex: `userPosts()`)
- **Vues Blade** : `kebab-case` (ex: `user-profile.blade.php`)
- **Routes** : `kebab-case` (ex: `/user-profile`)

## Architecture

- Suivre le pattern MVC de Laravel.
- Business logic dans des `Actions` ou `Services` (pas dans les controllers).
- Utiliser les `Form Requests` pour la validation.
- Éviter les `Facades` dans le code métier ; préférer l'injection de dépendances.

## Commandes

```bash
php artisan make:controller UserController
php artisan make:model User -m
php artisan make:request StoreUserRequest
php artisan migrate
php artisan test
```

## Tests

- Utiliser PHPUnit / Pest.
- Nommer : `{NomDuTest}Test.php`
- Un fichier par classe testée.
