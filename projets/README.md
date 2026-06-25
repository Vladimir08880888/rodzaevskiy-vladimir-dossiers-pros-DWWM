# Projets

## Crew — Planification d'équipe intelligente

Application full-stack de planification de services pour la
restauration. Projet de fin de formation DWWM, développé en solo
sur 3 mois.

- 🔗 **Code source** : https://github.com/Vladimir08880888/crew
- 🌐 **Démo en ligne** : https://crew-planner-hazel.vercel.app
- 📖 [Cahier des charges](https://github.com/Vladimir08880888/crew/blob/main/CAHIER_DES_CHARGES.md)
- 📋 [README](https://github.com/Vladimir08880888/crew/blob/main/README.md)
- 🧪 [Plan de tests](https://github.com/Vladimir08880888/crew/blob/main/annexes/PLAN_DE_TESTS.md) — 60+ scénarios Playwright
- 📚 [Justification scientifique](https://github.com/Vladimir08880888/crew/blob/main/annexes/JUSTIFICATION_SCIENTIFIQUE.md) — 12 références peer-reviewed

### Stack
- **Front** : React 18, Vite, React Router, i18next (FR/EN), Chart.js, drag-and-drop natif, CSS pur
- **Back** : Node.js 22, Express 4, mysql2 (SQL préparé, sans ORM)
- **BDD** : MariaDB 10.11
- **Sécurité** : bcrypt + JWT, rate-limit, prepared statements, helmet, CORS strict
- **Standards** : iCal (RFC 5545) pour la synchronisation calendrier natif sans application
- **Déploiement** : Vercel (front) + Fly.io (back + DB conteneurisée)

### Fonctionnalités clés
- 5 profils d'équipiers (Apprenti → Référent) avec poids normalisés [0;1]
- Smart Planner — solver greedy avec contraintes Convention HCR (48 h/sem, 11 h/jour cuisinier)
- Polyvalence multi-postes (théorème de la chaîne courte, Jordan & Graves 1995)
- Optimisation cost-aware — masse salariale prévisionnelle exposée dans l'UI
- Alertes science-based (KC & Terwiesch 2009 surcharge, Matre 2021 fatigue, Service Health Score composite)
- 12 migrations SQL versionnées
