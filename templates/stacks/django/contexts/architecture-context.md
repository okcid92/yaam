# Contexte d'Architecture — Django

> Généré par Yaam — architecture spécifique Django.

## Stack

- **Framework** : Django
- **Langage** : Python >= 3.11
- **Base de données** : PostgreSQL
- **Cache** : Redis
- **File storage** : S3 / MinIO
- **Task queue** : Celery + Redis
- **API** : Django REST Framework

## Structure

```
project/
├── apps/
│   ├── users/
│   ├── blog/
│   └── api/
├── config/
│   ├── settings/
│   ├── urls.py
│   └── wsgi.py
├── static/
├── media/
└── templates/
```

## Conventions

- Apps Django autonomes avec leur propre `models.py`, `views.py`, `tests.py`.
- Settings par environnement (base, dev, prod).
- Utiliser `django-environ` pour les variables d'environnement.
