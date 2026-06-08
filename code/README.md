# Code source du projet — Crew

Snapshot complet du code de l'application **Crew** (planification
d'équipe pour la restauration) figé au moment du dépôt du dossier
AFPA pour la soutenance DWWM.

## Pourquoi un snapshot ici ?

Le jury peut explorer le code directement dans ce dépôt sans avoir
besoin d'accéder à GitHub. Le code vivant continue d'évoluer sur :

- 🔗 **Repo canonique** : https://github.com/Vladimir08880888/crew
- 🌐 **Application en ligne** : https://crew-planner-hazel.vercel.app

## Contenu

| Dossier / fichier              | Description                                                  |
| ------------------------------ | ------------------------------------------------------------ |
| `crew/back/`                   | API Node.js + Express + mysql2 (sans ORM)                    |
| `crew/back/src/`               | Code source back : routes, controllers, validators, models, services |
| `crew/back/migrations/`        | 12 fichiers SQL versionnés (001 → 012)                       |
| `crew/back/Dockerfile`         | Image Docker pour le déploiement Fly.io (Node + MariaDB)     |
| `crew/back/fly.toml`           | Configuration Fly.io (région cdg, volume persistant)         |
| `crew/front/`                  | SPA React 18 + Vite                                          |
| `crew/front/src/`              | Code source front : pages, components, contexts, api, locales |
| `crew/front/vercel.json`       | Configuration Vercel (SPA rewrite)                           |
| `crew/annexes/`                | Documents de soutenance (justification scientifique, plan de tests, manuel, schéma BDD, screenshots) |
| `crew/CAHIER_DES_CHARGES.md`   | CDC complet, 11 sections                                     |
| `crew/SOUTENANCE.md`           | Trame de présentation de soutenance                          |
| `crew/README.md`               | README utilisateur du projet                                 |

## Ce qui est exclu du snapshot

- `node_modules/` (~150 MB) — restaurable via `npm install`
- `.git/` — historique conservé sur GitHub
- `dist/` — sortie de build, régénérable via `npm run build`
- `.env*` — secrets locaux (jamais commit, gitignored)

## Démarrage local

Pré-requis : Node.js 22, MariaDB 10.11.

```bash
cd crew/back
cp .env.example .env       # renseigner DB_PASSWORD + JWT_SECRET
npm install
npm run migrate
npm run seed               # données démo « Bistrot du Vieux Port »
npm run dev                # http://localhost:3000

# autre terminal
cd crew/front
echo "VITE_API_BASE=http://localhost:3000/api" > .env.local
npm install
npm run dev                # http://localhost:5173
```

Comptes de démo après seed — voir `crew/README.md`.
