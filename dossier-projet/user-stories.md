# User Stories — Reminder Famille

> Toutes les fonctionnalités exprimées du point de vue utilisateur.
> Format Connextra : **En tant que** … **je veux** … **afin de** …

---

## 🔓 Authentification

### US-01 — Création de compte
**En tant que** visiteur sans compte,
**je veux** pouvoir m'inscrire avec mon email, un mot de passe, mon prénom et nom,
**afin d'**accéder à l'application et créer mes premières tâches.

**Critères d'acceptation** :
- L'email est validé côté front (regex) et back (validators/auth)
- Le mot de passe doit faire au moins 8 caractères
- Si l'email est déjà pris, message clair : « Cet email est déjà utilisé »
- À la création réussie, je suis automatiquement connecté (JWT retourné)

---

### US-02 — Connexion
**En tant qu'**utilisateur enregistré,
**je veux** me connecter avec email et mot de passe,
**afin de** retrouver mes tâches et ma famille.

**Critères** :
- Mauvais identifiants → message générique « Identifiants incorrects »
  (pas de distinction email inconnu / mauvais mdp pour éviter l'énumération)
- Rate limit : 5 tentatives par 15 min en production
- Le token JWT est stocké en localStorage et inclus dans les requêtes suivantes

---

### US-03 — Changement de mot de passe
**En tant qu'**utilisateur connecté,
**je veux** changer mon mot de passe en fournissant l'ancien,
**afin de** sécuriser mon compte après une fuite suspectée.

**Critères** :
- Demande l'ancien mot de passe (re-vérification bcrypt)
- Nouveau mdp doit différer de l'ancien
- 8 caractères minimum

---

## 👨‍👩‍👧 Familles

### US-04 — Création d'une famille
**En tant qu'**utilisateur connecté,
**je veux** créer une famille en lui donnant un nom,
**afin de** pouvoir y inviter mes proches et partager des tâches.

**Critères** :
- Le créateur devient automatiquement `parent + admin`
- Un code d'invitation à 8 caractères alphanumériques est généré

---

### US-05 — Rejoindre une famille via code
**En tant qu'**utilisateur,
**je veux** rejoindre une famille existante en saisissant son code d'invitation,
**afin de** recevoir des tâches assignées par les parents.

**Critères** :
- Si le code n'existe pas → 404 avec message clair
- À la jointure, mon statut est `pending` jusqu'à validation par un admin
- Tant que `pending`, je ne vois pas les tâches de la famille

---

### US-06 — Validation des nouveaux membres
**En tant qu'**admin d'une famille,
**je veux** valider ou refuser les demandes de jointure,
**afin de** garder le contrôle sur qui accède aux tâches familiales.

**Critères** :
- Liste des demandes `pending` visible sur la page Famille
- À la validation, je choisis explicitement le rôle (parent ou child)
- Le membre validé reçoit le statut `active`

---

### US-07 — Régénération du code d'invitation
**En tant qu'**admin,
**je veux** régénérer le code d'invitation,
**afin d'**invalider l'ancien si je soupçonne qu'il a fuité.

**Critères** :
- Action accessible depuis la page détail de la famille
- Le nouveau code remplace l'ancien immédiatement
- Les membres déjà dans la famille ne sont pas affectés

---

### US-08 — Réinitialisation MDP d'un membre
**En tant qu'**admin,
**je veux** réinitialiser le mot de passe d'un membre de la famille
(typiquement un enfant qui l'a oublié),
**afin de** lui redonner accès sans passer par un email.

**Critères** :
- Génère un mot de passe temporaire affiché une seule fois
- L'admin communique ce mdp au membre concerné (oralement)
- Action interdite sur soi-même (utiliser la page Profil)

---

### US-09 — Quitter une famille
**En tant que** membre,
**je veux** pouvoir quitter une famille,
**afin de** ne plus en faire partie si je le décide.

**Critères** :
- Confirmation obligatoire (modal)
- Si je suis le dernier admin : refus avec message
  « Désignez un autre admin avant de quitter »

---

## 📋 Tâches personnelles

### US-10 — Création tâche personnelle
**En tant qu'**utilisateur,
**je veux** créer une tâche pour moi-même (sans famille),
**afin de** suivre mes obligations personnelles.

**Critères** :
- Champs : titre, description (optionnel), catégorie, priorité, fréquence, échéance
- 7 catégories disponibles, 3 priorités, 5 fréquences
- Si `frequency != once`, la tâche est récurrente

---

### US-11 — Complétion tâche personnelle
**En tant que** propriétaire d'une tâche,
**je veux** marquer ma tâche comme terminée,
**afin de** l'archiver et libérer mon dashboard.

**Critères** :
- Tâche `once` → statut `completed`, ne réapparaît plus dans le calendrier
- Tâche récurrente → l'échéance avance automatiquement
  (ex: hebdomadaire → +7 jours), statut reste `pending`

---

## 📋 Tâches familiales

### US-12 — Création tâche familiale par parent
**En tant que** parent,
**je veux** créer une tâche pour la famille en l'assignant éventuellement
à un membre précis,
**afin d'**organiser les corvées et obligations partagées.

**Critères** :
- Seul un parent peut créer une tâche familiale (sinon 403)
- Le champ `assigned_to` est optionnel
- Visible par tous les membres actifs de la famille

---

### US-13 — Modification/Suppression tâche familiale
**En tant que** parent,
**je veux** pouvoir modifier ou supprimer toute tâche familiale,
**afin de** corriger des erreurs ou retirer une tâche obsolète.

**Critères** :
- Enfant qui tente de modifier/supprimer → 403
- Modification du titre, échéance, priorité, fréquence, assigné

---

### US-14 — Complétion par enfant (validation requise)
**En tant qu'**enfant,
**je veux** marquer comme terminée une tâche qui m'est assignée,
**afin de** prévenir mes parents que c'est fait.

**Critères** :
- Tâche passe en `pending_review` (et non `completed`)
- Un parent doit valider ou rejeter ensuite
- Je vois bien le statut « En attente de validation »

---

### US-15 — Validation par parent
**En tant que** parent,
**je veux** valider ou rejeter une tâche terminée par un enfant,
**afin de** confirmer le travail bien fait, ou redemander si nécessaire.

**Critères** :
- Card orange en haut du Dashboard parent : « 2 tâches à valider »
- Si validation : tâche `once` → completed ; tâche récurrente → avancée
- Si rejet : retour `pending`, l'enfant voit qu'elle est à refaire

---

### US-16 — Commentaires sur tâche
**En tant que** membre d'une famille,
**je veux** ajouter des commentaires sur une tâche familiale,
**afin de** communiquer avec les autres membres (« j'ai utilisé le dernier sac »).

**Critères** :
- Tout membre actif de la famille peut commenter
- Suppression : auteur du commentaire ou parent

---

## 📊 Visualisation

### US-17 — Dashboard adaptatif
**En tant qu'**utilisateur,
**je veux** un dashboard qui s'adapte à mon rôle,
**afin d'**avoir directement les infos qui me concernent.

**Critères** :
- Parent : stats globales + breakdown par membre + tâches à valider
- Enfant : ses tâches assignées (par priorité), pas de stats famille
- Tâches en retard mises en avant en rouge

---

### US-18 — Calendrier mensuel
**En tant qu'**utilisateur,
**je veux** voir mes tâches dans un calendrier mensuel,
**afin de** visualiser ma charge sur le mois.

**Critères** :
- Navigation mois précédent/suivant
- Points colorés par priorité sur chaque jour
- Clic sur un jour → liste des tâches

---

### US-19 — Statistiques avec graphiques
**En tant que** parent,
**je veux** voir des stats sur les tâches familiales,
**afin de** suivre l'équilibre de la charge entre membres.

**Critères** :
- 3 graphiques : répartition par catégorie, par membre, évolution 30 jours
- Chart.js, responsive

---

## 📱 Notifications

### US-20 — Export iCal pour téléphone
**En tant qu'**utilisateur,
**je veux** synchroniser mes échéances avec le calendrier de mon téléphone,
**afin de** recevoir des notifications natives sans installer d'application.

**Critères** :
- Page Profil affiche un QR code `webcal://`
- Scan du QR avec iPhone → bouton « Ouvrir dans Calendrier »
- Le téléphone poll automatiquement le flux et déclenche des alarmes 1j avant

---

### US-21 — Flux iCal filtrés
**En tant qu'**utilisateur,
**je veux** pouvoir m'abonner à des sous-calendriers (perso seulement,
ou une famille spécifique),
**afin d'**avoir des calendriers séparés (couleurs différentes) sur mon téléphone.

**Critères** :
- 3 URLs disponibles : global, perso uniquement, par famille
- Chaque flux a un nom et une couleur distincte

---

## 🎨 Confort d'utilisation

### US-22 — Mode sombre
**En tant qu'**utilisateur,
**je veux** basculer entre mode clair et mode sombre,
**afin de** réduire la fatigue oculaire en soirée.

**Critères** :
- Toggle dans la navbar
- Choix sauvegardé en localStorage
- Respect par défaut de `prefers-color-scheme` du système

---

### US-23 — Interface responsive
**En tant qu'**utilisateur mobile,
**je veux** que l'interface s'adapte à mon écran,
**afin de** consulter mes tâches dans le bus ou les transports.

**Critères** :
- Breakpoints : mobile (< 768px), tablette (768–1024px), desktop (> 1024px)
- Navbar se transforme en menu hamburger sur mobile
- Toutes les actions accessibles au doigt (cibles ≥ 44px)

---

## 📊 Synthèse

| Catégorie | Nombre d'US |
|---|---|
| Authentification | 3 |
| Familles | 6 |
| Tâches personnelles | 2 |
| Tâches familiales | 5 |
| Visualisation | 3 |
| Notifications | 2 |
| Confort | 2 |
| **Total** | **23 user stories** |

Toutes les user stories ci-dessus sont **livrées et testées**
(57 scénarios d'intégration dans `tests/integration.sh`).
