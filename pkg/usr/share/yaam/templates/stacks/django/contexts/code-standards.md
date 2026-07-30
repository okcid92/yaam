# Standards de Code — Django

> Généré par Yaam — conventions spécifiques Django / Python.

## Nommage

- **Models** : `PascalCase`, singulier (ex: `User`, `BlogPost`)
- **Vues** : `PascalCase` (ex: `UserListView`)
- **Forms** : `PascalCase` (ex: `UserRegistrationForm`)
- **URLs** : `snake_case` (ex: `user-profile/`)
- **Fonctions** : `snake_case`
- **Fichiers Python** : `snake_case.py`

## Architecture

- Suivre le pattern MVT de Django.
- Business logic dans des `services.py` ou `utils.py`.
- Utiliser les Class-Based Views sauf pour les cas simples.
- Sérialisation avec Django REST Framework (si API).

## Commandes

```bash
python manage.py runserver
python manage.py test
python manage.py makemigrations
python manage.py migrate
ruff check .
```

## Tests

- Utiliser pytest-django.
- Fichiers : `test_{module}.py` dans chaque app.
- Un fichier par modèle ou vue.
