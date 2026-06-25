# Vladimir Rodzaevskiy — Dossiers Professionnels DWWM

Repository centralisant les documents officiels pour la soutenance du
Titre Professionnel **Développeur Web et Web Mobile** (AFPA Marseille, 2026).

> 🎯 **Pour le jury** : tous les documents sont disponibles en Markdown
> rendus directement sur GitHub. Les PDF imprimables sont générés à la
> demande depuis les sources Markdown.

---

## 📑 Documents

### 📘 Dossier Professionnel (DP)
> *Document personnel : compétences validées par 3 exemples par activité-type.*

| Format     | Lien                                                       |
| ---------- | ---------------------------------------------------------- |
| 📝 Markdown | [`dossier-professionnel/DP.md`](./dossier-professionnel/DP.md) |
| 📄 PDF     | [`dossier-professionnel/DP.pdf`](./dossier-professionnel/DP.pdf) |

Contenu :
- Présentation du parcours (2 Masters, 13 ans en restauration/casino,
  reconversion vers développement web)
- **AT1 — Développer la partie front-end** : 3 exemples détaillés
- **AT2 — Développer la partie back-end** : 3 exemples détaillés
- Projet professionnel à 6-12 mois et 1-3 ans

### 📗 Dossier de Projet — Crew

> *Application de planification d'équipe pour la restauration. Sept
> évolutions v2 (migrations 006-012) intégrant solver enrichi,
> conformité Convention HCR, polyvalence multi-skill et optimisation
> économique cost-aware.*

| Document                              | Lien                                                                         |
| ------------------------------------- | ---------------------------------------------------------------------------- |
| Cahier des charges                    | [`dossier-projet/cahier-des-charges.md`](./dossier-projet/cahier-des-charges.md) |
| Justification scientifique (12 réfs)  | [`dossier-projet/annexes/JUSTIFICATION_SCIENTIFIQUE.md`](./dossier-projet/annexes/JUSTIFICATION_SCIENTIFIQUE.md) |
| Plan de tests (Playwright)            | [`dossier-projet/annexes/PLAN_DE_TESTS.md`](./dossier-projet/annexes/PLAN_DE_TESTS.md) |
| Manuel utilisateur                    | [`dossier-projet/annexes/MANUEL_UTILISATEUR.md`](./dossier-projet/annexes/MANUEL_UTILISATEUR.md) |
| Schéma BDD (Mermaid ERD)              | [`dossier-projet/annexes/SCHEMA_BDD.md`](./dossier-projet/annexes/SCHEMA_BDD.md) |
| 17 captures d'écran                   | [`dossier-projet/annexes/screenshots/`](./dossier-projet/annexes/screenshots/) |

### 💻 Code source — snapshot

Le code complet de Crew est intégré dans le dépôt pour permettre au
jury d'explorer le code sans accès externe :

| Dossier                       | Lien                                                          |
| ----------------------------- | ------------------------------------------------------------- |
| Snapshot complet du code      | [`code/crew/`](./code/crew/) (10 MB, sans node_modules)        |
| Back-end Node.js + Express    | [`code/crew/back/`](./code/crew/back/)                         |
| Front-end React + Vite        | [`code/crew/front/`](./code/crew/front/)                       |
| 12 migrations SQL versionnées | [`code/crew/back/migrations/`](./code/crew/back/migrations/)   |

---

## 💻 Projet présenté

### Crew — Planification d'équipe intelligente
> Application web full-stack pour la planification de services
> d'équipe (restauration, hôtellerie, retail). Smart planner sous
> contrainte Convention HCR, polyvalence multi-postes, optimisation
> de la masse salariale, alertes science-based.

🌐 **Application en ligne** : https://crew-planner-hazel.vercel.app
🔗 **Code source** : https://github.com/Vladimir08880888/crew

🎯 **Comptes démo** (sur l'équipe « Bistrot du Vieux Port ») :
- `julien.patron@bistrot.fr / motdepasse123` — patron (admin)
- `sophie.manager@bistrot.fr / motdepasse123` — manager salle
- `ahmed.chef@bistrot.fr / motdepasse123` — chef cuisine
- `elena.serveuse@bistrot.fr / motdepasse123` — serveuse
- `clara.commis@bistrot.fr / motdepasse123` — apprentie

Stack : React 18 + Vite (front) / Node.js 22 + Express + mysql2 (back) /
MariaDB 10.11 / Vercel + Fly.io.

Fonctionnalités clés :
- 5 profils d'équipiers (Apprenti → Référent) avec poids normalisés [0;1]
- Smart Planner — solver greedy avec contraintes Convention HCR dures
- Polyvalence multi-postes (Jordan & Graves 1995, théorème de la chaîne courte)
- Optimisation cost-aware — masse salariale prévisionnelle exposée
- Alertes science-based — surcharge KC & Terwiesch 2009, non-conformité HCR, Service Health Score
- iCal natif (synchronisation calendrier téléphone sans application)
- i18n FR + EN, mode sombre, responsive mobile/desktop
- 60+ tests automatisés Playwright (PASS)

---

## 📅 Soutenance

- **Formation** : Développeur Web et Web Mobile — RNCP 37674, niveau 5
- **Centre** : AFPA Marseille La Treille
- **Candidat** : Vladimir Rodzaevskiy
- **Période projet** : avril – juin 2026

---

## 📜 Licence

Code source sous licence **MIT** — voir
[`crew/LICENSE`](https://github.com/Vladimir08880888/crew/blob/main/LICENSE).
