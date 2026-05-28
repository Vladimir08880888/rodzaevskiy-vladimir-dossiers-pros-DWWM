# Charte graphique — Reminder Famille

> Identité visuelle de l'application. Les valeurs sont définies une seule fois
> dans `front/src/styles/variables.css` et consommées via custom properties
> CSS, garantissant la cohérence visuelle sur l'ensemble de l'interface.

---

## 🎨 Palette de couleurs

### Couleurs primaires

| Variable | Hex | Usage |
|---|---|---|
| `--primary` | `#6366f1` (indigo 500) | Boutons d'action, liens, focus |
| `--primary-hover` | `#4f46e5` | État survol |
| `--primary-grad` | `linear-gradient(135deg, #6366f1 → #8b5cf6 → #ec4899)` | Branding, header, CTAs majeurs |

**Justification** : l'indigo et le violet inspirent la confiance, la sérénité
et la modernité — adaptés à un usage familial quotidien. Le dégradé
indigo→violet→rose ajoute une touche chaleureuse et différencie
visuellement le produit des solutions corporate (Notion, Todoist).

### Couleurs sémantiques (statuts)

| Variable | Hex | Sens |
|---|---|---|
| `--success` | `#10b981` (emerald) | Tâche terminée, validation réussie |
| `--warning` | `#f59e0b` (amber) | Tâche en attente de validation parent |
| `--danger` | `#ef4444` (red) | Erreur, suppression, retard |
| `--info` | `#0ea5e9` (sky) | Notification informative |

### Couleurs des priorités

| Variable | Hex | Priorité |
|---|---|---|
| `--priority-high` | `#ef4444` | high — urgent |
| `--priority-medium` | `#f59e0b` | medium — important |
| `--priority-low` | `#10b981` | low — quand on a le temps |

### Couleurs par catégorie de tâche

| Variable | Hex | Catégorie |
|---|---|---|
| `--cat-Santé` | `#ec4899` (pink) | Santé |
| `--cat-Finances` | `#f59e0b` (amber) | Finances |
| `--cat-Administratif` | `#6366f1` (indigo) | Administratif |
| `--cat-Véhicule` | `#10b981` (emerald) | Véhicule |
| `--cat-Logement` | `#8b5cf6` (purple) | Logement |
| `--cat-Corvée` | `#06b6d4` (cyan) | Corvée |
| `--cat-Autre` | `#6b7280` (gray) | Autre |

**Justification** : palette HSL équirépartie sur le cercle chromatique
pour garantir une distinction visuelle nette même pour utilisateurs
daltoniens (testée avec simulateur Color Oracle).

### Surface (glassmorphism)

| Variable | Valeur | Usage |
|---|---|---|
| `--glass` | `rgba(255,255,255,0.55)` | Cartes, panneaux flottants |
| `--glass-strong` | `rgba(255,255,255,0.75)` | Modals, navbar |
| `--glass-border` | `rgba(255,255,255,0.5)` | Bordures translucides |
| `--blur-md` | `blur(18px) saturate(180%)` | Effet flou d'arrière-plan |

**Justification** : tendance glassmorphism (iOS, Windows 11) — apporte
de la profondeur et permet à un arrière-plan dégradé d'enrichir
l'interface sans surcharger.

### Mode sombre (dark theme)

Activé via `data-theme="dark"` sur `<html>`. Toutes les variables sont
re-définies (bg, glass, primary, shadows). Préférence sauvegardée en
`localStorage` et synchronisée avec `prefers-color-scheme`.

| Variable | Light | Dark |
|---|---|---|
| `--bg-base` | `#f0f4ff` | `#08081a` |
| `--text` | `#1e1b3a` | `#e6e6f0` |
| `--primary` | `#6366f1` | `#818cf8` |

---

## ✍️ Typographie

### Police principale (UI)

```css
--font-base:
  -apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI',
  Roboto, sans-serif;
```

**Stratégie** : *system font stack*. Aucun fichier `.woff2` à télécharger
→ performance maximale (0 KB de font), rendu natif optimisé par chaque OS.

- **Inter** comme premier choix après les polices système : design moderne,
  excellent rendu des caractères latins étendus (accents français), conçue
  pour le numérique par Rasmus Andersson.

### Police monospace (code)

```css
--font-mono:
  'JetBrains Mono', 'Fira Code', ui-monospace, SFMono-Regular,
  Menlo, monospace;
```

Utilisée pour : badges de code, IDs visibles, codes d'invitation famille.

### Échelle typographique

| Élément | Taille | Poids |
|---|---|---|
| H1 (titres pages) | `1.875rem` (30px) | 700 |
| H2 (sections) | `1.5rem` (24px) | 600 |
| H3 (sous-sections) | `1.25rem` (20px) | 600 |
| Texte courant | `1rem` (16px) | 400 |
| Labels formulaires | `0.875rem` (14px) | 500 |
| Texte secondaire | `0.875rem` (14px) | 400, `--text-muted` |
| Petit / badges | `0.75rem` (12px) | 500 |

**Justification** : ratio 1.25 (major third) — proportions harmoniques,
hiérarchie visuelle claire.

---

## 📐 Spacing & layout

### Échelle d'espacement (multiples de 4px)

`4px → 8px → 12px → 16px → 24px → 32px → 48px → 64px`

### Rayons de bordure

| Variable | Valeur | Usage |
|---|---|---|
| `--r-xs` | `6px` | Inputs, petits badges |
| `--r-sm` | `10px` | Boutons |
| `--r-md` | `14px` | Cartes standard |
| `--r-lg` | `20px` | Panneaux principaux |
| `--r-xl` | `28px` | Modals |
| `--r-full` | `9999px` | Pills, avatars |

### Largeur container

```css
--container-w: 1180px; /* contenu principal centré */
--nav-h: 64px;         /* hauteur navbar fixe */
```

---

## ⚡ Animations

### Easings

| Variable | Courbe | Usage |
|---|---|---|
| `--ease` | `cubic-bezier(0.4, 0, 0.2, 1)` | Standard Material |
| `--ease-bounce` | `cubic-bezier(0.34, 1.56, 0.64, 1)` | Pop d'apparition |

### Durées

| Variable | Durée | Usage |
|---|---|---|
| `--t-fast` | `120ms` | Hover, focus |
| `--t-base` | `220ms` | Transitions standard |
| `--t-slow` | `400ms` | Apparitions de modal |

### Accessibilité

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

Respect du paramètre OS « réduire les animations ».

---

## 🖼️ Iconographie

**Lucide Icons** (`lucide-react` — fork moderne de Feather Icons)

- Style : outline, stroke uniforme `2px`
- Cohérence visuelle parfaite avec la typographie
- Tree-shaking : seules les icônes utilisées sont incluses dans le bundle

---

## 🎯 Principes de design

1. **Glassmorphism subtil** — translucidité + flou pour profondeur,
   sans rendre l'interface illisible.
2. **Hiérarchie par la couleur** — chaque catégorie de tâche est
   identifiable instantanément à sa couleur.
3. **Contraste WCAG AA** vérifié sur tous les textes (ratio ≥ 4.5).
4. **Mobile-first** — toutes les pages sont d'abord conçues pour
   smartphone (375px) puis enrichies pour desktop (≥ 1024px).
5. **Mode sombre natif** — pas une simple inversion mais un thème
   complet retravaillé pour le confort visuel.

---

## 📦 Implémentation

Tous les choix ci-dessus sont matérialisés dans un seul fichier source :
[`front/src/styles/variables.css`](https://github.com/Vladimir08880888/reminder-famille/blob/main/front/src/styles/variables.css)

Aucune valeur magique en dur dans les composants — toutes les couleurs,
espacements, durées sont récupérés via `var(--…)`. Cela permet de changer
l'identité visuelle entière en modifiant ce seul fichier.
