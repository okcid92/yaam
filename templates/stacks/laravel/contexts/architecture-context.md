# Contexte d'Architecture — Laravel

> Généré par Yaam — architecture spécifique Laravel.

## Stack

- **Framework** : Laravel
- **PHP** : >= 8.1
- **Base de données** : MySQL / PostgreSQL / SQLite
- **Queue** : Redis / Database
- **Cache** : Redis / File
- **Frontend** : Blade / Inertia / Livewire

## Structure

```
app/
├── Http/
│   ├── Controllers/
│   ├── Requests/
│   └── Middleware/
├── Models/
├── Services/
├── Actions/
└── Providers/
resources/
├── views/
└── js/
routes/
├── web.php
└── api.php
database/
└── migrations/
```

## Conventions

- Utiliser des `Service Providers` pour enregistrer les bindings.
- Events & Listeners pour la logique déterministe.
- Jobs pour les tâches asynchrones.
