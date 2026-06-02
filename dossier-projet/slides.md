---
marp: true
theme: default
size: 16:9
paginate: true
header: "Reminder Famille — Soutenance DWWM"
footer: "Vladimir Rodzaevskiy · AFPA Marseille 2026"
style: |
  section {
    background: linear-gradient(135deg, #f0f4ff 0%, #fce7f3 100%);
    color: #1e1b3a;
    font-family: -apple-system, 'Inter', sans-serif;
    padding: 60px 80px;
  }
  section.lead {
    background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 60%, #ec4899 100%);
    color: white;
    text-align: center;
  }
  section.lead h1 { font-size: 3em; margin-bottom: 0.3em; }
  section.lead h2 { font-weight: 300; opacity: 0.95; }
  h1 { color: #4f46e5; border-bottom: 3px solid #6366f1; padding-bottom: 12px; }
  h2 { color: #6366f1; }
  code { background: rgba(99,102,241,0.12); padding: 2px 6px; border-radius: 4px; }
  pre { background: #1e1b3a; color: #e6e6f0; border-radius: 8px; }
  table { font-size: 0.85em; }
  th { background: #6366f1; color: white; }
  blockquote { border-left: 4px solid #6366f1; padding-left: 16px; color: #6b7280; }
  .columns { display: grid; grid-template-columns: 1fr 1fr; gap: 30px; }
  .big { font-size: 2.5em; color: #6366f1; font-weight: 700; }
  .badge { display: inline-block; padding: 4px 12px; border-radius: 999px;
           background: #6366f1; color: white; font-size: 0.7em; font-weight: 600; }
---

<!-- _class: lead -->

# Reminder Famille

## Application web de gestion des tâches familiales

**Soutenance Titre Professionnel**
Développeur Web et Web Mobile

Vladimir Rodzaevskiy — AFPA Marseille 2026

---

# 1. Le constat

Une famille moderne gère **beaucoup** de tâches récurrentes :

- 💰 Échéances financières (loyer, factures, impôts)
- 🏥 Rendez-vous médicaux
- 🚗 Maintenance véhicule (CT, vidange)
- 🧹 Corvées domestiques
- 📚 Suivi scolaire des enfants

**Aujourd'hui, c'est dispersé** entre post-it, WhatsApp, mémoire d'un seul parent → charge mentale.

---

# 2. Les solutions existantes échouent

| Solution | Limitation |
|---|---|
| Todoist | Pensé entreprise, fonctions famille payantes (4€/mois/user) |
| Trello | Aucun modèle parent/enfant |
| Apple Reminders | iOS uniquement |
| Google Tasks | Pas de partage à plusieurs |
| Notion | Trop complexe, abonnement |

> **Hypothèse** : peut-on faire mieux avec des standards ouverts ?

---

# 3. Reminder Famille — la proposition

<div class="columns">
<div>

### 🎯 3 idées clés

1. Familles avec rôles **parent / enfant**
2. **Validation parent** quand enfant termine
3. **Notifications natives téléphone** via iCal — sans installer d'app

</div>
<div>

### 📦 Livré

- Application full-stack fonctionnelle
- Multi-utilisateurs, multi-familles
- Mobile + desktop
- Mode sombre intégré
- 100% gratuit, auto-hébergeable

</div>
</div>

---

# 4. Stack technique

<div class="columns">
<div>

### Front-end
- **React 18** + Vite 5
- **React Router 6**
- **Context API** (Auth, Family, Theme)
- **Chart.js** pour stats
- CSS pur (glassmorphism + dark mode)

</div>
<div>

### Back-end
- **Node.js 22** LTS
- **Express 4**
- **mysql2** (SQL préparé, sans ORM)
- **bcrypt + JWT** (HS256)
- **ical-generator** (RFC 5545)

</div>
</div>

**Base de données** : MariaDB 10.11 · 5 tables · 6 migrations versionnées

---

# 5. Architecture en couches

```
Browser (React + Vite)
        │ fetch JSON + JWT Bearer
        ▼
Express (Node.js 22)
   ├─ middleware : CORS, auth, rate-limit, family-access
   ├─ routes → controllers → validators → models
        │
        ▼
mysql2 (requêtes préparées)
        ▼
MariaDB 10.11 (ACID, FK strictes)
```

**Principe** : 1 entité = 1 fichier par couche → travail isolé + évolutif

---

# 6. Démonstration en direct ⭐

> *Passage à l'application*

**Scénario démo (12 étapes)** :

1. Login Marie (parent admin) → Dashboard parent
2. Création tâche assignée à Léo
3. Calendrier mensuel + stats
4. Page Famille → invite_code + reset password
5. Page Profil → QR code iCal → scan iPhone
6. Logout, login Léo (enfant) → Dashboard enfant
7. Léo termine tâche → status `pending_review`
8. Re-login Marie → carte orange « À valider » → approve

---

# 7. Mission 1 — Auth & Familles

**Périmètre** : inscription, connexion, gestion familles, rôles, validation membres

<div class="columns">
<div>

### Côté back
- JWT HS256 + bcrypt cost 10
- Middlewares composables :
  `authRequired` → `requireFamilyMember` → `requireAdmin`
- **Last-admin protection** sur suppression
- Reset MDP par admin (sans email)

</div>
<div>

### Côté front
- `AuthContext` global
- `ProtectedRoute` pour routes privées
- Persistance JWT en `localStorage`
- Réhydratation au reload via `/auth/me`

</div>
</div>

`28 / 57 scénarios de tests intégration` couvrent cette mission

---

# 8. Mission 2 — Tâches & Validation parent

**Workflow distinctif** : enfant termine → parent valide

```
[Enfant] click "Terminer" sur tâche assignée
            ↓
   POST /api/tasks/:id/complete
            ↓
   status passe à 'pending_review'
            ↓
[Parent] voit carte orange sur Dashboard
            ↓
   POST /api/tasks/:id/approve  ou  /reject
            ↓
   once → completed  |  récurrente → due_date avancée (DATE_ADD)
```

**21 scénarios de tests** valident ce flux + permissions enfant/parent

---

# 9. Mission 3 — Export iCal ⭐

### Le défi : notifier sur téléphone sans installer d'app

| Approche | Problème |
|---|---|
| App native | 2 stores, comptes développeur, mise à jour |
| Web Push | Limité iOS (PWA installée obligatoire) |
| Email / SMS | SMTP / coût / spam |

### ✅ Solution : standard **iCalendar (RFC 5545)**

`webcal://api/calendar/<token>` → l'iPhone/Android **poll automatiquement** ce flux → **VALARM** = notification système 1j avant

**Aucune app à installer. Fonctionne iOS + Android.**

---

# 10. Sécurité — OWASP Top 10

| Risque | Mesure |
|---|---|
| Injection SQL | 100% requêtes préparées (`?` placeholders) |
| XSS | React échappement automatique (jamais `dangerouslySetInnerHTML`) |
| CSRF | JWT en header (pas de cookie) |
| Auth brute force | Rate limit 5/15min + message générique |
| Cryptographic failures | bcrypt cost 10 + JWT HS256 |
| Broken access control | Middlewares composables + last-admin protection |

📄 Document détaillé : `dossier-projet/securite.md`

---

# 11. Conception BDD — 5 tables relationnelles

```
users ─┬──< families (created_by)
       ├──< family_members >──┐
       │                       │
       ├──< tasks ─────────────┤
       │   (assigned_to, completed_by)
       │                       │
       └──< task_comments      │
           (via tasks)         │
                  families ────┘
```

- **InnoDB** pour ACID + FK strictes
- **`ON DELETE CASCADE/SET NULL/RESTRICT`** selon sémantique
- **Index** sur user_id, family_id, due_date, status
- **ENUM MySQL** pour énumérations métier (catégorie, priorité, fréquence, statut, rôle)

---

# 12. Tests d'intégration — 57 / 57 ✅

```bash
$ bash tests/integration.sh
═══════════════════════════════════════
1. Authentification          11 ✓
2. Familles                  14 ✓
3. Tâches CRUD & perms       11 ✓
4. Validation parent         10 ✓
5. Export iCal                7 ✓
6. Statistiques               2 ✓
─────────────────────────────────
Résultats : 57 passés / 57 total
Tous les tests passent !
```

Script bash + `curl` + `jq` — réexécutable à chaque évolution

---

# 13. Le projet en chiffres

<div class="columns">
<div>

<div class="big">2 mois</div>
développement solo

<div class="big">~6000</div>
lignes de code

<div class="big">117</div>
fichiers versionnés

</div>
<div>

<div class="big">57</div>
tests d'intégration ✅

<div class="big">17</div>
captures auto-générées

<div class="big">8</div>
diagrammes UML/Merise

</div>
</div>

---

# 14. Choix discutés et évolutions

<div class="columns">
<div>

### ⚖️ Compromis assumés

- **Pas d'ORM** → SQL visible, plus de boilerplate mais maîtrise
- **Pas de TypeScript** → temps gagné, risques runtime
- **Pas de tests unitaires** → 57 d'intégration à la place
- **Node + MariaDB co-localisés** sur 1 machine Fly (free tier)

</div>
<div>

### 🚀 Évolutions identifiées

- Tests unitaires Vitest
- CI/CD GitHub Actions (auto-deploy sur push)
- Notifications email (Resend)
- Bot Telegram pour rappels temps réel
- PWA mode offline
- Séparation back / BDD sur 2 machines Fly

</div>
</div>

---

<!-- _class: lead -->

# Merci pour votre attention

🌐 **Application live** :
**reminder-famille.vercel.app**

💻 **GitHub** :
github.com/Vladimir08880888/reminder-famille
github.com/Vladimir08880888/vladimir-rodzaevski-dossiers-pros-DWWM

🎯 **Comptes démo** :
`marie@famille.fr` / `motdepasse123`

📖 **Code MIT** — auto-hébergeable

## Vos questions ?
