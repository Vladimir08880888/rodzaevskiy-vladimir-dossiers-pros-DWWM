# Wireframes — Reminder Famille

> Représentations basse fidélité des écrans clés. Ces wireframes ont
> guidé l'implémentation initiale ; les **screenshots haute fidélité**
> définitifs sont disponibles dans
> [`reminder-famille/annexes/screenshots/`](https://github.com/Vladimir08880888/reminder-famille/tree/main/annexes/screenshots).

---

## 1. Page Login (mobile + desktop)

```
┌─────────────────────────────────────────────┐
│  🌓                                     [≡] │ ← navbar (toggle thème)
├─────────────────────────────────────────────┤
│                                             │
│              ╔═══════════════╗              │
│              ║ Reminder Famille            │
│              ║   Connexion   ║              │
│              ║               ║              │
│              ║  Email ____   ║              │
│              ║  ┌─────────┐  ║              │
│              ║  │         │  ║              │
│              ║  └─────────┘  ║              │
│              ║  Mot de passe ║              │
│              ║  ┌─────────┐  ║              │
│              ║  │ •••••   │  ║              │
│              ║  └─────────┘  ║              │
│              ║               ║              │
│              ║  [Se connecter] ←── primary  │
│              ║               ║              │
│              ║  Pas de compte ? S'inscrire  │
│              ╚═══════════════╝              │
│                                             │
│            (mesh gradient bg)               │
│                                             │
└─────────────────────────────────────────────┘
```

**Comportement** :
- Erreur sous chaque champ en rouge si validation HTML5 échoue
- Bouton désactivé pendant la requête (spinner)
- Toast top-right si 401 du back

---

## 2. Dashboard Parent (desktop)

```
┌───────────────────────────────────────────────────────────────┐
│ ⚡ Reminder │ Tâches  Familles  Calendrier  Stats │ 🌓  👤▾   │
├───────────────────────────────────────────────────────────────┤
│                                                               │
│  Bonjour Marie 👋                                             │
│                                                               │
│  ╭───────────╮  ╭───────────╮  ╭───────────╮  ╭───────────╮  │
│  │     5     │  │     1     │  │     2     │  │    12     │  │
│  │ En cours  │  │ En retard │  │À valider ⚠│  │Faites 30j │  │
│  ╰───────────╯  ╰───────────╯  ╰───────────╯  ╰───────────╯  │
│                                                               │
│  ⚠ 2 tâches à valider                                         │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │ Sortir poubelle (Léo, hier)         [Valider] [Rejeter] │  │
│  │ Ranger chambre  (Léo, avant-hier)   [Valider] [Rejeter] │  │
│  └─────────────────────────────────────────────────────────┘  │
│                                                               │
│  Par membre                                                   │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐           │
│  │  Marie       │ │  Paul        │ │  Léo (enfant)│           │
│  │  ▰▰▰▰▱  3/5  │ │  ▰▱▱▱▱  1/4  │ │  ▰▰▱▱▱  2/6  │           │
│  └──────────────┘ └──────────────┘ └──────────────┘           │
│                                                               │
│  Prochaines tâches                                            │
│  ● Demain   - Payer loyer (Marie)        [Voir]               │
│  ● Demain   - Sortir poubelle (Léo)      [Voir]               │
│  ● Dans 7j  - Rdv dentiste (Ana)         [Voir]               │
│                                                               │
└───────────────────────────────────────────────────────────────┘
```

---

## 3. Dashboard Enfant (mobile)

```
┌───────────────────────┐
│ ⚡ Reminder    🌓  👤 │
├───────────────────────┤
│                       │
│  Salut Léo 👋         │
│                       │
│  À faire aujourd'hui  │
│  ┌───────────────┐    │
│  │ ● Promener    │    │
│  │   le chien    │    │
│  │ [Terminer ✓]  │    │
│  └───────────────┘    │
│                       │
│  À faire bientôt      │
│  ┌───────────────┐    │
│  │ ● Sortir      │    │
│  │   poubelle    │    │
│  │   demain      │    │
│  └───────────────┘    │
│                       │
│  ┌───────────────┐    │
│  │ ● Devoir      │    │
│  │   maths       │    │
│  │   demain      │    │
│  └───────────────┘    │
│                       │
│  En attente parent    │
│  ┌───────────────┐    │
│  │ ⏳ Ranger      │    │
│  │   chambre     │    │
│  │   (validation)│    │
│  └───────────────┘    │
│                       │
└───────────────────────┘
   ↑ menu burger
```

---

## 4. Liste des tâches (desktop)

```
┌───────────────────────────────────────────────────────────────┐
│  Tâches                              [+ Nouvelle tâche]       │
├───────────────────────────────────────────────────────────────┤
│                                                               │
│  Filtres                                                      │
│  Catégorie [Toutes ▾]  Statut [Toutes ▾]  Famille [Toutes ▾]  │
│  Membre [Tous ▾]       Période [Tout ▾]                       │
│                                                               │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │ ● Sortir poubelle              ↳ Léo · weekly · Corvée  │  │
│  │   Lundi soir avant 21h                                   │  │
│  │   📅 Demain  |  ⬤ Medium  |  [✓ Terminer] [✏] [🗑]      │  │
│  └─────────────────────────────────────────────────────────┘  │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │ ● Payer loyer                ↳ Marie · monthly · Finances│  │
│  │   Virement avant le 5                                    │  │
│  │   📅 Dans 3 jours  |  ⬤ High  |  [✓ Terminer]            │  │
│  └─────────────────────────────────────────────────────────┘  │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │ ● Pilates (perso)              ↳ Marie · weekly · Santé  │  │
│  │   Cours du mardi                                         │  │
│  │   📅 Dans 2 jours  |  ⬤ Low                              │  │
│  └─────────────────────────────────────────────────────────┘  │
│                                                               │
│  ... (paginé si > 50 tâches)                                  │
│                                                               │
└───────────────────────────────────────────────────────────────┘
```

---

## 5. Formulaire de tâche (modal/page)

```
┌─────────────────────────────────────────┐
│  Nouvelle tâche                       ✕ │
├─────────────────────────────────────────┤
│                                         │
│  Titre *                                │
│  ┌───────────────────────────────────┐  │
│  │ Sortir la poubelle                │  │
│  └───────────────────────────────────┘  │
│                                         │
│  Description                            │
│  ┌───────────────────────────────────┐  │
│  │ Lundi soir avant 21h              │  │
│  │                                   │  │
│  └───────────────────────────────────┘  │
│                                         │
│  Catégorie *           Priorité *       │
│  [Corvée    ▾]         [Medium    ▾]    │
│                                         │
│  Fréquence *           Échéance *       │
│  [Weekly    ▾]         [29/05/2026 📅]  │
│                                         │
│  Famille (optionnel)                    │
│  [Famille Dupont      ▾]                │
│                                         │
│  Assigner à (si famille)                │
│  [Léo  ▾]                               │
│                                         │
│              [Annuler]  [Créer la tâche]│
└─────────────────────────────────────────┘
```

---

## 6. Détail famille (admin)

```
┌───────────────────────────────────────────────────────────────┐
│  Famille Dupont                          [✏ Renommer] [🗑]    │
├───────────────────────────────────────────────────────────────┤
│                                                               │
│  Code d'invitation                                            │
│  ╭─────────────────────────────╮                              │
│  │     ABC12345         📋     │  [🔄 Régénérer]              │
│  ╰─────────────────────────────╯                              │
│  Partager ce code avec les personnes à inviter                │
│                                                               │
│  Membres actifs (4)                                           │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │ 👤 Marie Dupont  · parent · ⭐ admin       [⚙] [🔑]      │  │
│  │ 👤 Paul Dupont   · parent                  [⚙] [🔑] [✕] │  │
│  │ 👤 Léo Dupont    · child                   [⚙] [🔑] [✕] │  │
│  │ 👤 Ana Dupont    · child                   [⚙] [🔑] [✕] │  │
│  └─────────────────────────────────────────────────────────┘  │
│                                                               │
│  Demandes en attente (1)                                      │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │ 👤 Sophie Bertrand                                       │  │
│  │   Valider en tant que : [Parent] [Enfant]   [Refuser]   │  │
│  └─────────────────────────────────────────────────────────┘  │
│                                                               │
└───────────────────────────────────────────────────────────────┘
```

---

## 7. Page Profil — Export iCal

```
┌───────────────────────────────────────────────────────────────┐
│  Mon profil                                                   │
├───────────────────────────────────────────────────────────────┤
│                                                               │
│  Marie Dupont                                                 │
│  marie@famille.fr                                             │
│  [Modifier] [Changer mot de passe]                            │
│                                                               │
│  ─────────────────────────────────────────────────────────    │
│                                                               │
│  📱 Synchroniser avec votre téléphone                         │
│                                                               │
│  Scannez ce QR avec votre iPhone ou Android :                 │
│                                                               │
│            ┌─────────────────┐                                │
│            │ ██▀▀ ▄▄█ ▄ █████│                                │
│            │ █▀▀  ▄ ▄ ▀▄ ▀▀█│   ← QR webcal://                │
│            │ ██▀▄▀▀▀█ █▄█ ▀█│                                 │
│            │ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀│                                 │
│            └─────────────────┘                                │
│                                                               │
│            [📱 Ouvrir dans Calendrier]                        │
│                                                               │
│  Sous-calendriers (couleurs différentes)                      │
│  ▶ Personnel uniquement       [QR] [Lien]                     │
│  ▶ Famille Dupont uniquement  [QR] [Lien]                     │
│                                                               │
└───────────────────────────────────────────────────────────────┘
```

---

## Versions responsive

Tous les écrans ont été pensés mobile-first puis enrichis pour desktop.

### Breakpoints

| Type | Largeur | Adaptations |
|---|---|---|
| Mobile | < 768px | Navbar → burger, cartes pleine largeur |
| Tablette | 768–1024px | 2 colonnes, navbar visible |
| Desktop | ≥ 1024px | 3-4 colonnes, sidebar fixe |

Voir les **screenshots définitifs** mobile (`12-mobile.png`,
`13-mobile-dashboard.png`) et desktop (`03-dashboard-parent.png` etc.)
dans `annexes/screenshots/` du projet.
