# Contexte d'Architecture — Next.js

> Généré par Yaam — architecture spécifique Next.js.

## Stack

- **Framework** : Next.js (App Router)
- **Langage** : TypeScript
- **Base de données** : PostgreSQL via Prisma / Drizzle
- **UI** : Tailwind CSS / shadcn/ui
- **Auth** : NextAuth.js / Clerk
- **API** : Route handlers / Server Actions

## Structure

```
src/
├── app/
│   ├── (marketing)/
│   ├── (dashboard)/
│   └── api/
├── components/
│   ├── ui/
│   └── shared/
├── lib/
├── types/
└── styles/
```

## Conventions

- Server Components par défaut.
- Client Components uniquement pour l'interactivité.
- Les appels DB dans les Server Components ou Server Actions.
- Validation avec Zod.
