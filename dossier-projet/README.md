# Dossier de Projet — Crew

> Application de planification d'équipe pour la restauration. Projet
> de fin de formation **Développeur Web et Web Mobile** (La Plateforme Formation, Marseille, 2026).

**Démo en production** : https://crew-planner-hazel.vercel.app
**Code source** : https://github.com/Vladimir08880888/crew

---

## Documents

| Fichier                            | Contenu                                            |
| ---------------------------------- | -------------------------------------------------- |
| `cahier-des-charges.md`            | Cahier des charges (stack, métier, schéma, API, sécurité, déploiement, évolutions v2). |
| `README-projet.md`                 | README du dépôt code (lien rapide).                |
| `annexes/JUSTIFICATION_SCIENTIFIQUE.md` | Synthèse des références peer-reviewed qui sous-tendent le solver (12 sources, INRS, NIOSH, Convention HCR, OR economics). |
| `annexes/MANUEL_UTILISATEUR.md`    | Guide manager + équipier (synchronisation iCal, FAQ). |
| `annexes/PLAN_DE_TESTS.md`         | Plan de tests détaillé — 9 blocs initiaux + 7 blocs v2 (solver enrichi). Bilan d'exécution Playwright. |
| `annexes/SCHEMA_BDD.md`            | MCD / MLD au format Mermaid + règles d'intégrité. |
| `annexes/screenshots/`             | 17 captures d'écran (web + mobile, FR + EN, démo + édition). |

## Stack technique

- **Front** : React 18 + Vite, i18next (FR/EN), Chart.js, drag-and-drop natif.
- **Back** : Node.js 22 + Express 4, mysql2, bcrypt, JWT.
- **DB** : MariaDB 10.11.
- **Deploy** : Vercel (front) + Fly.io (back + DB conteneurisée).

## Périmètre fonctionnel

- Authentification (inscription / connexion / changement de mot de
  passe / réinitialisation par admin).
- Gestion d'équipe (création, code d'invitation, approbation des
  membres, rôles, polyvalence multi-postes).
- Planning hebdomadaire (création / édition / drag-and-drop / clone
  semaine / clear semaine).
- Smart planner — solver respectant la Convention HCR, optimisant
  la couverture et la masse salariale.
- Statistiques (heures planifiées vs cible, couverture par poste,
  graphiques Chart.js).
- Calendrier natif (iCal feed personnel, sans application
  supplémentaire à installer).

## Évolutions v2 incluses

Les migrations 006 à 012 introduisent :

1. Profils nommés (Apprenti → Référent) avec poids normalisés [0;1].
2. Paramètres d'établissement éditables par le manager (coefficients,
   capacité, idéaux par poste, taux horaires).
3. Jours d'ouverture configurables.
4. Densité prévue par (jour, service) — grille 7×2 dans le Smart Planner.
5. Conformité Convention HCR appliquée comme contrainte dure.
6. Polyvalence (multi-skill matrix par équipier).
7. Optimisation cost-aware — masse salariale prévisionnelle exposée
   dans l'UI.
8. Alertes science-based — fatigue (KC & Terwiesch 2009), non-conformités
   HCR (Matre et al. 2021), Service Health Score composite.

Voir `cahier-des-charges.md` section 11 pour le détail des migrations
et `annexes/JUSTIFICATION_SCIENTIFIQUE.md` pour la traçabilité
académique de chaque choix de modélisation.
