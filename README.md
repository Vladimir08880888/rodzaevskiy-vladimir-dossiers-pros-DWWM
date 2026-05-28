# Vladimir Rodzaevskiy — Dossiers Professionnels DWWM

Repository centralisant les documents officiels pour la soutenance du
Titre Professionnel **Développeur Web et Web Mobile** (AFPA Marseille, 2026).

> 🎯 **Pour le jury** : tous les documents sont disponibles en **PDF** prêts
> à imprimer, et en Markdown rendus directement sur GitHub.

---

## 📑 Documents

### 📘 Dossier Professionnel (DP)
> *Document personnel : compétences validées par 3 exemples par activité-type.*

| Format | Lien |
|---|---|
| 📄 PDF | [`dossier-professionnel/DP.pdf`](./dossier-professionnel/DP.pdf) |
| 📝 Markdown | [`dossier-professionnel/DP.md`](./dossier-professionnel/DP.md) |

Contenu :
- Présentation du parcours (2 Masters, 13 ans en restauration/casino,
  reconversion vers développement web)
- **AT1 — Développer la partie front-end** : 3 exemples détaillés
- **AT2 — Développer la partie back-end** : 3 exemples détaillés
- Projet professionnel à 6-12 mois et 1-3 ans

### 📗 Dossier de Projet
> *Document technique sur l'application Reminder Famille (15 sections).*

| Format | Lien |
|---|---|
| 📄 PDF | [`dossier-projet/dossier-projet.pdf`](./dossier-projet/dossier-projet.pdf) |
| 📝 Markdown | [`dossier-projet/dossier-projet.md`](./dossier-projet/dossier-projet.md) |

### 🎤 Slides de soutenance

| Format | Usage | Lien |
|---|---|---|
| 📄 PDF | À projeter | [`dossier-projet/slides.pdf`](./dossier-projet/slides.pdf) |
| 🌐 HTML | Interactif | [`dossier-projet/slides.html`](./dossier-projet/slides.html) |
| 📊 PPTX | Editable (Canva/PowerPoint) | [`dossier-projet/slides.pptx`](./dossier-projet/slides.pptx) |
| 📝 Source | Markdown Marp | [`dossier-projet/slides.md`](./dossier-projet/slides.md) |

15 slides au format 16:9 — environ 12-15 minutes de présentation.

### 📚 Documents annexes (PDF + Markdown)

| Document | PDF | Markdown |
|---|---|---|
| API REST (30+ endpoints) | [`api-documentation.pdf`](./dossier-projet/api-documentation.pdf) | [`api-documentation.md`](./dossier-projet/api-documentation.md) |
| Sécurité (OWASP Top 10) | [`securite.pdf`](./dossier-projet/securite.pdf) | [`securite.md`](./dossier-projet/securite.md) |
| User stories (23 stories) | [`user-stories.pdf`](./dossier-projet/user-stories.pdf) | [`user-stories.md`](./dossier-projet/user-stories.md) |
| Charte graphique | [`charte-graphique.pdf`](./dossier-projet/maquettes/charte-graphique.pdf) | [`charte-graphique.md`](./dossier-projet/maquettes/charte-graphique.md) |
| Wireframes (7 écrans) | [`wireframes.pdf`](./dossier-projet/maquettes/wireframes.pdf) | [`wireframes.md`](./dossier-projet/maquettes/wireframes.md) |

### 🗂️ Diagrammes (Mermaid, rendus natifs sur GitHub)

| Diagramme | Type | Fichier |
|---|---|---|
| Packages | UML | [`packages.mmd`](./dossier-projet/diagrammes/packages.mmd) |
| Use cases (28 cas, 6 acteurs) | UML | [`use-cases.mmd`](./dossier-projet/diagrammes/use-cases.mmd) |
| MCD | Merise | [`mcd.mmd`](./dossier-projet/diagrammes/mcd.mmd) |
| MLD | Merise | [`mld.mmd`](./dossier-projet/diagrammes/mld.mmd) |
| Activité — Authentification | UML | [`activite-auth.mmd`](./dossier-projet/diagrammes/activite-auth.mmd) |
| Activité — Validation parent | UML | [`activite-validation-parent.mmd`](./dossier-projet/diagrammes/activite-validation-parent.mmd) |
| Séquence — Abonnement iCal | UML | [`sequence-ical.mmd`](./dossier-projet/diagrammes/sequence-ical.mmd) |
| Séquence — CRUD tâche | UML | [`sequence-task-crud.mmd`](./dossier-projet/diagrammes/sequence-task-crud.mmd) |

---

## 💻 Projet présenté

### Reminder Famille
> Application web full-stack de gestion des tâches familiales.
> React 18 + Vite (front) / Node.js + Express + mysql2 (back) / MariaDB 10.11.

🔗 **Code source** : https://github.com/Vladimir08880888/reminder-famille

🎯 **Démo locale** : `marie@famille.fr` / `motdepasse123` (après `npm run seed`)

Fonctionnalités clés :
- Familles avec rôles **parent / enfant** + workflow de validation parent
- Tâches récurrentes (daily / weekly / monthly / yearly) avec avancement auto
- **Export iCal** natif (notifications iPhone & Android sans application)
- Statistiques (Chart.js), calendrier mensuel, commentaires sur tâches
- Mode sombre, responsive mobile/tablette/desktop
- **57 tests d'intégration** automatisés (100% PASS)

---

## 📅 Soutenance

- **Formation** : Développeur Web et Web Mobile — RNCP 37674, niveau 5
- **Centre** : AFPA Marseille
- **Candidat** : Vladimir Rodzaevskiy (né le 31 mai 1982)
- **Période projet** : 2 mois (avril–mai 2026)

---

## 📜 Licence

Code source sous licence **MIT** — voir
[`reminder-famille/LICENSE`](https://github.com/Vladimir08880888/reminder-famille/blob/main/LICENSE).
