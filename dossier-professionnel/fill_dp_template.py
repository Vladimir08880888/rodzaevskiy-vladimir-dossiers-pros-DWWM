#!/usr/bin/env python3
"""
Remplit le modèle officiel AFPA "Dossier Professionnel" avec les
informations de Vladimir Rodzaevskiy pour le titre DWWM.

Source : /home/vladimir/Documents/Dossier Professionnel/1-Dossier_professionnel_*.docx
Sortie : /home/vladimir/vladimir-rodzaevski-dossiers-pros-DWWM/
                    dossier-professionnel/DP_AFPA_rempli.docx
"""
from copy import deepcopy
from pathlib import Path
from docx import Document
from docx.oxml.ns import qn

SRC = Path("/home/vladimir/Documents/Dossier Professionnel/"
           "1-Dossier_professionnel_version_traitement_de_texte_11_09_2017.docx")
DST = Path("/home/vladimir/vladimir-rodzaevski-dossiers-pros-DWWM/"
           "dossier-professionnel/DP_AFPA_rempli.docx")

# ────────────────────────────────────────────────────────────────────────
# DONNÉES PERSONNELLES
# ────────────────────────────────────────────────────────────────────────
PERSONAL = {
    "Nom de naissance":  "RODZAEVSKIY",
    "Nom d’usage":       "RODZAEVSKIY",
    "Prénom":            "Vladimir",
    "Adresse":           "[à compléter par le candidat]",
}

TITRE_PRO = "Développeur Web et Web Mobile (DWWM) — RNCP 37674, niveau 5"

# ────────────────────────────────────────────────────────────────────────
# AT1 — DÉVELOPPER LA PARTIE FRONT-END
# ────────────────────────────────────────────────────────────────────────
AT1_INTITULE = "Développer la partie front-end d'une application web ou web mobile sécurisée"

AT1_EX_INTITULE = "Application Crew — planification d'équipe React 18 complète"

AT1_TASKS = (
    "Dans le cadre du projet de fin de formation Crew (gestion "
    "de tâches familiales avec rôles parent/enfant), j'ai réalisé l'intégralité "
    "de la partie front-end de l'application. J'ai notamment :\n\n"
    "• maquetté l'interface en mobile-first puis enrichi pour tablette et desktop "
    "(breakpoints 768px et 1024px), avec 13 pages : Login, Register, Dashboard "
    "(parent et enfant), TasksList, TaskForm, CalendarView, Stats, Families, "
    "FamilyCreate/Join/Detail, Profile, NotFound ;\n\n"
    "• mis en place le routage avec React Router 6 (routes publiques et "
    "protégées via un composant ProtectedRoute qui redirige vers /login quand "
    "l'utilisateur n'est pas authentifié) ;\n\n"
    "• développé un système d'état global avec 5 contextes React superposés "
    "(AuthContext, FamilyContext, ThemeContext, ToastContext, ConfirmContext) "
    "exposés via des hooks personnalisés (useAuth, useFamily, useTheme…) ;\n\n"
    "• créé un calendrier mensuel responsive sans bibliothèque externe — "
    "manipulation native de l'API Date pour construire la grille (lundi en tête, "
    "cellules carrées via aspect-ratio CSS) ;\n\n"
    "• intégré 3 graphiques Chart.js (répartition par catégorie, par membre, "
    "évolution 30 jours) sur la page Statistiques ;\n\n"
    "• développé la page Profil qui génère 3 QR codes webcal:// (calendrier "
    "global, personnel, par famille) pour permettre l'abonnement iCal depuis "
    "iPhone et Android en un seul scan ;\n\n"
    "• implémenté un thème clair/sombre complet avec persistance en localStorage "
    "et respect de prefers-color-scheme."
)

AT1_MOYENS = (
    "Stack technique :\n"
    "  • React 18.3 + Vite 5 (HMR, build ESM)\n"
    "  • React Router 6.26\n"
    "  • Chart.js + react-chartjs-2 (graphiques accessibles)\n"
    "  • lucide-react (icônes vectorielles outline)\n"
    "  • qrcode (génération canvas) pour QR webcal\n"
    "  • CSS pur avec custom properties (variables.css) — pas de framework, "
    "approche glassmorphism + dark mode natif\n\n"
    "Outils :\n"
    "  • Visual Studio Code\n"
    "  • Git + GitHub\n"
    "  • Firefox + Chromium (DevTools, accessibility audit, responsive mode)\n"
    "  • Postman et curl pour tester les appels API\n\n"
    "Bonnes pratiques :\n"
    "  • Validation HTML5 systématique (required, type, autoComplete)\n"
    "  • Labels associés (htmlFor + id), aria-invalid, aria-describedby\n"
    "  • Focus visible, prefers-reduced-motion respecté\n"
    "  • Contraste WCAG AA vérifié sur tous les textes (ratio ≥ 4.5)"
)

AT1_AVEC_QUI = (
    "Projet réalisé en solo dans le cadre de la formation AFPA DWWM. "
    "Échanges réguliers avec :\n"
    "  • le formateur référent AFPA Marseille pour cadrage technique et "
    "validation des choix d'architecture ;\n"
    "  • la promotion DWWM pour partage d'expérience et code reviews informelles ;\n"
    "  • la communauté open source (forums Stack Overflow, documentation MDN, "
    "documentation React et Vite) pour la résolution de problèmes techniques."
)

AT1_NOM_ENTREPRISE = ("AFPA Marseille — projet de fin de formation "
                       "« Crew »")
AT1_SERVICE = "Formation DWWM, plateau pédagogique"
AT1_PERIODE_DU = "Avril 2026"
AT1_PERIODE_AU = "Mai 2026"

AT1_INFOS_COMPL = (
    "Application déployée en ligne :\n"
    "https://crew-planner-hazel.vercel.app\n\n"
    "Code source public sous licence MIT :\n"
    "https://github.com/Vladimir08880888/crew\n\n"
    "Documents complémentaires (annexes) :\n"
    "  • DP détaillé (3 exemples Front documentés ligne par ligne) : DP.pdf\n"
    "  • Dossier de Projet complet (20 pages) : dossier-projet.pdf\n"
    "  • Charte graphique : maquettes/charte-graphique.pdf\n"
    "  • Wireframes basse fidélité : maquettes/wireframes.pdf\n"
    "  • 17 captures d'écran de l'interface livrée\n\n"
    "Repo centralisé pour le jury : \n"
    "https://github.com/Vladimir08880888/vladimir-rodzaevski-dossiers-pros-DWWM"
)

# ────────────────────────────────────────────────────────────────────────
# AT2 — DÉVELOPPER LA PARTIE BACK-END
# ────────────────────────────────────────────────────────────────────────
AT2_INTITULE = "Développer la partie back-end d'une application web ou web mobile sécurisée"

AT2_EX_INTITULE = "Application Crew — API Node.js/Express sécurisée"

AT2_TASKS = (
    "Pour le même projet Crew, j'ai conçu et développé l'intégralité "
    "de la partie back-end : conception de la base de données, API REST "
    "sécurisée, et logique métier de l'application multi-utilisateurs.\n\n"
    "Conception de la base de données (Merise) :\n"
    "• MCD avec 5 entités (User, Family, FamilyMember, Task, TaskComment) ;\n"
    "• MLD avec clé primaire composite sur family_members (relation many-to-many) ;\n"
    "• MPD matérialisé par 6 fichiers de migrations SQL versionnés ;\n"
    "• stratégies de suppression (ON DELETE CASCADE / SET NULL / RESTRICT) "
    "réfléchies selon la sémantique de chaque relation.\n\n"
    "Développement de l'API REST (Express) :\n"
    "• 30+ endpoints documentés couvrant authentification, familles, tâches, "
    "statistiques, export iCal et commentaires ;\n"
    "• architecture en couches strictes : routes → middleware → controllers "
    "→ validators → models ;\n"
    "• authentification JWT (HS256, durée 7 jours) avec mot de passe haché "
    "via bcrypt (coût 10) ;\n"
    "• système de middlewares composables : authRequired → "
    "requireFamilyMember → requireAdmin ;\n"
    "• validation systématique côté serveur (validators retournent HttpError 400 "
    "avec détails par champ) ;\n"
    "• gestion d'erreurs centralisée — les stack traces ne sont jamais "
    "renvoyées au client ;\n"
    "• génération de flux iCalendar (RFC 5545) avec VALARM pour notifications "
    "natives sur téléphone, sans application à installer ;\n"
    "• 3 endpoints iCal différents (global, personnel, par famille) avec "
    "authentification spéciale par token URL.\n\n"
    "Logique métier sensible :\n"
    "• workflow de validation parent : tâche assignée à un enfant passe en "
    "pending_review, parent peut approuver (→ completed ou avance la date "
    "si récurrente via DATE_ADD SQL) ou rejeter (→ retour pending) ;\n"
    "• last-admin protection : vérification countAdmins ≥ 2 avant retrait "
    "ou départ de famille ;\n"
    "• récurrence native SQL (DATE_ADD INTERVAL) — pas de cron, pas de table "
    "supplémentaire."
)

AT2_MOYENS = (
    "Stack technique :\n"
    "  • Node.js 22 LTS + Express 4.19\n"
    "  • mysql2 3.11 (driver avec prepared statements natifs, sans ORM)\n"
    "  • MariaDB 10.11 (moteur InnoDB pour ACID + FK strictes)\n"
    "  • jsonwebtoken 9.0 (signature JWT HS256)\n"
    "  • bcrypt 5.1 (hachage des mots de passe)\n"
    "  • ical-generator 7.2 (génération RFC 5545 + VALARM)\n"
    "  • express-rate-limit 7.5 (anti brute-force sur /auth/login)\n"
    "  • cors 2.8 (CORS restreint au front configuré)\n"
    "  • dotenv 16.4 (variables d'environnement)\n\n"
    "Outils :\n"
    "  • Visual Studio Code\n"
    "  • Git + GitHub\n"
    "  • curl + jq pour tests manuels API\n"
    "  • MariaDB CLI pour debugging SQL\n"
    "  • Postman pour exploration d'API\n\n"
    "Sécurité (OWASP Top 10) :\n"
    "  • 100 % requêtes préparées (vérifié par grep — aucune concaténation)\n"
    "  • Pas de cookie session (JWT en Authorization Bearer) → CSRF impossible\n"
    "  • CORS limité au FRONT_ORIGIN configuré\n"
    "  • Variables sensibles (.env, JWT_SECRET, DB_PASSWORD) gitignored\n\n"
    "Tests :\n"
    "  • Suite de 57 scénarios d'intégration en bash + curl (tests/integration.sh) "
    "qui couvre auth, familles, tâches, validation parent, iCal, statistiques. "
    "100 % PASS."
)

AT2_AVEC_QUI = (
    "Projet réalisé en solo dans le cadre de la formation AFPA DWWM. "
    "Mêmes interlocuteurs que pour l'AT1 :\n"
    "  • formateur référent AFPA Marseille pour validation des choix d'architecture "
    "et des décisions de sécurité ;\n"
    "  • promotion DWWM pour partage et entraide ;\n"
    "  • documentation officielle Node.js, Express, MariaDB, OWASP."
)

AT2_NOM_ENTREPRISE = AT1_NOM_ENTREPRISE
AT2_SERVICE = AT1_SERVICE
AT2_PERIODE_DU = AT1_PERIODE_DU
AT2_PERIODE_AU = AT1_PERIODE_AU

AT2_INFOS_COMPL = (
    "Application déployée en ligne :\n"
    "https://crew-planner-hazel.vercel.app\n\n"
    "Code source public sous licence MIT :\n"
    "https://github.com/Vladimir08880888/crew\n\n"
    "Documents complémentaires (annexes) :\n"
    "  • DP détaillé (3 exemples Back documentés ligne par ligne) : DP.pdf\n"
    "  • Dossier de Projet complet (20 pages) : dossier-projet.pdf\n"
    "  • Documentation API (30+ endpoints) : api-documentation.pdf\n"
    "  • Document Sécurité OWASP avec extraits défensifs : securite.pdf\n"
    "  • 8 diagrammes UML/Merise : packages, use cases, MCD, MLD, "
    "activité (auth, validation), séquence (iCal, CRUD)\n"
    "  • Suite de tests d'intégration (57 scénarios PASS) : "
    "tests/integration.sh\n\n"
    "Repo centralisé pour le jury : \n"
    "https://github.com/Vladimir08880888/vladimir-rodzaevski-dossiers-pros-DWWM"
)

# ────────────────────────────────────────────────────────────────────────
# DIPLÔMES
# ────────────────────────────────────────────────────────────────────────
DIPLOMES = [
    # (Intitulé, Autorité ou organisme, Date)
    ("Master 2 Économie et Gestion d'Entreprise",
     "Université d'État (Moscou, Russie)",
     "2004"),
    ("Master 2 Commerce International",
     "Université française",
     "2012"),
    ("Titre Professionnel Développeur Web et Web Mobile",
     "AFPA Marseille (en cours)",
     "2026"),
]

# ────────────────────────────────────────────────────────────────────────
# UTILITAIRES python-docx
# ────────────────────────────────────────────────────────────────────────

def set_cell_text(cell, text, *, bold=False, preserve_first_run=True):
    """
    Vide une cellule de tableau et y écrit `text` (multi-lignes acceptées
    via '\n'). Préserve le style du premier run quand possible.
    """
    # supprimer tous les paragraphes existants sauf le premier
    paras = cell.paragraphs
    for p in paras[1:]:
        p._element.getparent().remove(p._element)
    p = cell.paragraphs[0]
    # supprimer tous les runs existants
    for r in list(p.runs):
        r._element.getparent().remove(r._element)
    # écrire ligne par ligne
    lines = text.split('\n')
    run = p.add_run(lines[0])
    if bold:
        run.bold = True
    for line in lines[1:]:
        p.add_run().add_break()
        p.add_run(line)


def fill_example_table(table, intitule_at, intitule_ex,
                       tasks, moyens, avec_qui,
                       nom_ent, service, periode_du, periode_au,
                       infos_compl=""):
    """
    Remplit un tableau « exemple de pratique professionnelle ».
    Structure du tableau (33 rows) :
      row 0 : Activité-type | (n°) | (intitulé)
      row 1 : Exemple n° X  |       | (intitulé)
      row 2-3 : ligne séparatrice
      row 4 : « 1. Décrivez … » + zones de saisie en dessous
      row 10 : « 2. Précisez les moyens utilisés »
      row 16 : « 3. Avec qui avez-vous travaillé »
      row 22 : « 4. Contexte »
      row 24 : « Nom de l'entreprise … » | (à remplir)
      row 25 : « Chantier, atelier, service » | (à remplir)
      row 26 : « Période d'exercice  Du : Cliquez ici  au : Cliquez ici »
      row 29 : « 5. Informations complémentaires »
    Note: chaque section a plusieurs rows vides en dessous pour la saisie ;
    on cible la première row libre après chaque titre.
    """
    rows = table._tbl.tr_lst

    def cell_tcs_at(row_idx):
        # Find ALL <w:tc> including those wrapped by <w:sdt>/<w:sdtContent>
        return rows[row_idx].xpath('.//w:tc')

    # row 0 — Activité-type : 3ème colonne = intitulé
    tcs = cell_tcs_at(0)
    if len(tcs) >= 3:
        # remplacer le texte « Cliquez ici … » dans la 3ème cellule
        set_cell_in_tc(tcs[-1], intitule_at, bold=True)

    # row 1 — Exemple n°X : 2ème ou 3ème colonne
    tcs = cell_tcs_at(1)
    if len(tcs) >= 2:
        set_cell_in_tc(tcs[-1], intitule_ex, bold=True)

    # Section 1 : « 1. Décrivez les tâches » → écrire dans rows 5-9
    # (les rows 5, 6, 7, 8, 9 sont des cellules vides pour la saisie)
    set_section_content(rows, start_row=5, end_row=9, text=tasks)

    # Section 2 : « 2. Précisez les moyens » → rows 11-15
    set_section_content(rows, start_row=11, end_row=15, text=moyens)

    # Section 3 : « 3. Avec qui avez-vous travaillé » → rows 17-21
    set_section_content(rows, start_row=17, end_row=21, text=avec_qui)

    # Section 4 : Contexte — rows 24, 25, 26
    # row 24 : "Nom de l'entreprise" | (à remplir)
    tcs = cell_tcs_at(24)
    if len(tcs) >= 2:
        set_cell_in_tc(tcs[-1], nom_ent)
    # row 25 : "Chantier, atelier, service" | (à remplir)
    tcs = cell_tcs_at(25)
    if len(tcs) >= 2:
        set_cell_in_tc(tcs[-1], service)
    # row 26 : "Période d'exercice  Du : ... au : ..."
    # Cellule monobloc : on réécrit toute la ligne
    tcs = cell_tcs_at(26)
    if tcs:
        set_cell_in_tc(tcs[0],
                       f"Période d'exercice    Du : {periode_du}    au : {periode_au}")

    # Section 5 : Informations complémentaires → rows 30-32
    if infos_compl:
        set_section_content(rows, start_row=30, end_row=32, text=infos_compl)


def set_section_content(rows, start_row, end_row, text):
    """
    Écrit `text` dans la première cellule libre disponible entre
    start_row et end_row du tableau (cellules pour saisie utilisateur).
    """
    for r in range(start_row, end_row + 1):
        if r >= len(rows):
            break
        tcs = rows[r].xpath('.//w:tc')
        if not tcs:
            continue
        # prendre la première cellule de la row
        set_cell_in_tc(tcs[0], text)
        return


def set_cell_in_tc(tc, text, *, bold=False):
    """
    Remplit une cellule (élément <w:tc>) avec `text`.

    Stratégie : tout vider (paragraphes, SDT, runs) puis créer un seul
    paragraphe propre avec le texte voulu. Cela écrase aussi les
    « content controls » (SDT) Word qui contiennent souvent du texte
    placeholder du genre « Cliquez ici … ».
    """
    from docx.oxml import OxmlElement

    # 1. Supprimer TOUS les enfants directs sauf <w:tcPr> (propriétés)
    for child in list(tc):
        if child.tag == qn('w:tcPr'):
            continue
        tc.remove(child)

    # 2. Créer un seul paragraphe propre
    p = OxmlElement('w:p')
    tc.append(p)

    # 3. Ajouter le texte (multi-lignes via <w:br>)
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if i > 0:
            br_r = OxmlElement('w:r')
            br = OxmlElement('w:br')
            br_r.append(br)
            p.append(br_r)
        r = OxmlElement('w:r')
        if bold:
            rpr = OxmlElement('w:rPr')
            b = OxmlElement('w:b')
            rpr.append(b)
            r.append(rpr)
        t = OxmlElement('w:t')
        t.text = line
        t.set(qn('xml:space'), 'preserve')
        r.append(t)
        p.append(r)


def fill_header_table(doc):
    """Table 0 — nom, prénom, adresse.

    Structure de chaque ligne :
      col 0 : libellé ("Nom de naissance")
      col 1 : cellule de saisie (vide)
      col 2 : SDT avec placeholder "Entrez votre nom de naissance ici."

    On remplit col 1 avec la valeur, ET on vide col 2 pour ne pas avoir
    à la fois la valeur et le placeholder côte à côte.
    """
    t = doc.tables[0]
    rows = t._tbl.tr_lst
    fields = [
        (1, PERSONAL["Nom de naissance"]),
        (2, PERSONAL["Nom d’usage"]),
        (3, PERSONAL["Prénom"]),
        (4, PERSONAL["Adresse"]),
    ]
    for row_idx, value in fields:
        tcs = rows[row_idx].xpath('.//w:tc')
        if len(tcs) >= 2:
            set_cell_in_tc(tcs[1], value)
        # Vider le placeholder SDT en col 2 si présent
        if len(tcs) >= 3:
            set_cell_in_tc(tcs[2], '')


def fill_titre_pro(doc):
    """Table 1 — titre professionnel visé + modalité (Parcours coché)."""
    t = doc.tables[1]
    rows = t._tbl.tr_lst
    # row 0 = Titre professionnel visé (libellé)
    # row 1 ou 2 = champ de saisie pour le titre
    # row 6 = ☐ Parcours de formation
    # row 7 = ☐ VAE
    # On écrit le titre dans la première row libre après row 0
    # Row 2 contient le placeholder "Cliquez ici pour entrer l'intitulé…"
    # On l'écrase directement (et au passage, row 1 reste vide pour
    # l'aération du document)
    if len(rows) > 2:
        tcs = rows[2].xpath('.//w:tc')
        if tcs:
            set_cell_in_tc(tcs[0], TITRE_PRO, bold=True)

    # Cocher la case « Parcours de formation » :
    # row 6 = ☐ | Parcours de formation
    # row 7 = ☐ | VAE
    # On remplace le ☐ par ☒ dans la cellule 0 de row 6.
    if len(rows) > 6:
        tcs = rows[6].xpath('.//w:tc')
        if tcs:
            set_cell_in_tc(tcs[0], '☒', bold=True)


def fill_diplomes(doc):
    """Table 7 — Titres, diplômes, CQP."""
    t = doc.tables[7]
    rows = t._tbl.tr_lst
    # row 3 = ligne d'entête (Intitulé | Autorité | Date)
    # rows 4+ = lignes à remplir
    for i, (intitule, autorite, date) in enumerate(DIPLOMES):
        row_idx = 4 + i
        if row_idx >= len(rows):
            break
        tcs = rows[row_idx].xpath('.//w:tc')
        if len(tcs) >= 3:
            set_cell_in_tc(tcs[0], intitule)
            set_cell_in_tc(tcs[1], autorite)
            set_cell_in_tc(tcs[2], date)


def fill_declaration(doc):
    """Paragraphes (pas tableau) pour la déclaration sur l'honneur.

    Ces paragraphes sont en dehors des tableaux. On les modifie via
    doc.paragraphs.
    """
    for p in doc.paragraphs:
        txt = p.text
        if 'Je soussigné' in txt:
            # remplacer [prénom et nom] par le vrai nom
            for r in p.runs:
                if '[prénom et nom]' in r.text:
                    r.text = r.text.replace('[prénom et nom]',
                                            'Vladimir RODZAEVSKIY')
        elif txt.startswith('Fait à'):
            # remplir Fait à Marseille le ...
            for r in p.runs:
                if r.text.strip() == 'Fait à':
                    r.text = 'Fait à Marseille le [date à compléter par le candidat]'


def remove_excess_page_breaks(doc):
    """Supprime les paragraphes-saut-de-page entre AT1↔AT2 et AT2↔Titres.

    Le modèle force un PAGE_BREAK entre chaque AT pour qu'ils commencent
    sur une nouvelle page. Mais avec du contenu dense (notre cas), cela
    crée des pages quasi vides. On laisse Word/LibreOffice gérer le flux
    naturel.
    """
    from lxml import etree
    body = doc.element.body
    children = list(body)

    # On veut supprimer les paragraphes-saut-de-page qui se trouvent
    # juste avant des tables AT2, Titres-diplômes, Déclaration, etc.
    # Repérage par contenu de la table suivante.
    targets_following = (
        'Activité-type',          # AT2 (AT3 déjà supprimé)
        'Titres, diplômes',       # Table 7 (devenue 6 après suppression AT3)
        # Pas pour Déclaration / Documents / Annexes : on garde leur séparation
    )
    seen_first_at = False

    for i, child in enumerate(children):
        tag = etree.QName(child).localname
        if tag != 'tbl':
            continue
        first_text = ''.join(child.xpath('.//w:t/text()'))[:60]
        if not any(t in first_text for t in targets_following):
            continue
        if 'Activité-type' in first_text and not seen_first_at:
            # première Activité-type rencontrée = AT1, on ne touche pas
            seen_first_at = True
            continue
        # Chercher le paragraphe précédent qui contient un PAGE_BREAK
        prev = child.getprevious()
        while prev is not None:
            if etree.QName(prev).localname == 'p' and prev.xpath('.//w:br[@w:type="page"]'):
                prev.getparent().remove(prev)
                break
            prev = prev.getprevious()


def remove_at3_section(doc):
    """Supprime la table AT3 (Activité-type 3) + son saut de page précédent.

    Recherche par contenu : la table dont la première cellule contient
    « Activité-type » avec le numéro 3 ou son intitulé non-applicable.
    """
    body = doc.element.body

    # Identifier la table AT3 (et son saut de page précédent)
    target_table = None
    for child in body:
        from lxml import etree
        if etree.QName(child).localname != 'tbl':
            continue
        first_text = ''.join(child.xpath('.//w:t/text()'))[:60]
        # AT3 contient « Activité-type » et le numéro 3 (du sdt comboBox)
        # ou notre marqueur « Non applicable »
        if 'Activité-type' in first_text and ('3' in first_text or 'Non applicable' in first_text):
            # Vérifier que c'est bien AT3 (pas AT1 ou AT2)
            if 'front-end' not in first_text and 'back-end' not in first_text:
                target_table = child
                break

    if target_table is None:
        return  # rien à faire

    # Trouver le paragraphe juste avant la table (qui contient le PAGE_BREAK)
    prev_para = target_table.getprevious()
    while prev_para is not None and etree.QName(prev_para).localname != 'p':
        prev_para = prev_para.getprevious()

    # Supprimer la table
    target_table.getparent().remove(target_table)

    # Supprimer le saut de page précédent s'il en contient un
    if prev_para is not None and prev_para.xpath('.//w:br[@w:type="page"]'):
        prev_para.getparent().remove(prev_para)


def fill_sommaire(doc):
    """Table 3 — Sommaire.

    On remplit les intitulés AT1/AT2 + exemples. AT3 et AT4 marqués
    « Non applicable » (DWWM = 2 AT seulement). Les numéros de page
    réels seront déterminés au moment de l'impression — on laisse
    des indicateurs approximatifs.
    """
    t = doc.tables[3]
    rows = t._tbl.tr_lst

    def write_cell(row_idx, col_idx, text):
        if row_idx >= len(rows):
            return
        tcs = rows[row_idx].xpath('.//w:tc')
        if col_idx >= len(tcs):
            return
        set_cell_in_tc(tcs[col_idx], text)

    # AT1
    write_cell(2, 0, AT1_INTITULE)
    write_cell(3, 1, AT1_EX_INTITULE)
    write_cell(4, 1, "—")
    write_cell(5, 1, "—")

    # AT2
    write_cell(7, 0, AT2_INTITULE)
    write_cell(8, 1, AT2_EX_INTITULE)
    write_cell(9, 1, "—")
    write_cell(10, 1, "—")

    # AT3 + AT4 — non applicables (DWWM ne comporte que 2 AT)
    # On les marque dans le sommaire ; les tables physiques AT3/AT4
    # sont supprimées (cf. remove_at3_section + le fait qu'il n'y a
    # pas de table AT4 dans le modèle).
    write_cell(12, 0, "Non applicable (DWWM ne comporte que 2 AT)")
    write_cell(13, 1, "—")
    write_cell(14, 1, "—")
    write_cell(15, 1, "—")

    write_cell(17, 0, "Non applicable")
    write_cell(18, 1, "—")
    write_cell(19, 1, "—")
    write_cell(20, 1, "—")


def fill_documents_illustrant(doc):
    """Table 9 — Documents illustrant la pratique professionnelle (facultatif).

    On y liste les annexes disponibles dans le repo GitHub : code source,
    diagrammes, screenshots, tests, etc.
    """
    if len(doc.tables) < 10:
        return
    t = doc.tables[9]
    rows = t._tbl.tr_lst
    # row 3 = "Intitulé" + placeholder "Cliquez ici…"
    # rows 4+ = à remplir
    documents = [
        "Code source du projet Crew — "
            "github.com/Vladimir08880888/crew",
        "Repo centralisé des dossiers AFPA — "
            "github.com/Vladimir08880888/vladimir-rodzaevski-dossiers-pros-DWWM",
        "Dossier de Projet complet (20 pages, 15 sections) — "
            "dossier-projet/dossier-projet.pdf",
        "Dossier Professionnel détaillé (3 exemples par AT) — "
            "dossier-professionnel/DP.pdf",
        "Cahier des charges (sections 1-11, évolutions v2) — "
            "dossier-projet/cahier-des-charges.md",
        "Justification scientifique (12 références peer-reviewed) — "
            "dossier-projet/annexes/JUSTIFICATION_SCIENTIFIQUE.md",
        "Schéma BDD (Mermaid ERD) — "
            "dossier-projet/annexes/SCHEMA_BDD.md",
        "Manuel utilisateur (manager + équipier) — "
            "dossier-projet/annexes/MANUEL_UTILISATEUR.md",
        "17 captures d'écran haute résolution — "
            "dossier-projet/annexes/screenshots/",
        "Plan de tests (60+ scénarios Playwright) — "
            "dossier-projet/annexes/PLAN_DE_TESTS.md",
        "Trame de soutenance — "
            "dossier-projet/soutenance.md",
    ]
    for i, doc_str in enumerate(documents):
        row_idx = 3 + i
        if row_idx >= len(rows):
            break
        tcs = rows[row_idx].xpath('.//w:tc')
        if not tcs:
            continue
        set_cell_in_tc(tcs[0], doc_str)

# ────────────────────────────────────────────────────────────────────────
# MAIN
# ────────────────────────────────────────────────────────────────────────

def main():
    if not SRC.exists():
        raise SystemExit(f"Source introuvable : {SRC}")
    DST.parent.mkdir(parents=True, exist_ok=True)

    doc = Document(str(SRC))

    fill_header_table(doc)
    fill_titre_pro(doc)

    # AT1 → Table 4
    fill_example_table(
        doc.tables[4],
        intitule_at=AT1_INTITULE,
        intitule_ex=AT1_EX_INTITULE,
        tasks=AT1_TASKS,
        moyens=AT1_MOYENS,
        avec_qui=AT1_AVEC_QUI,
        nom_ent=AT1_NOM_ENTREPRISE,
        service=AT1_SERVICE,
        periode_du=AT1_PERIODE_DU,
        periode_au=AT1_PERIODE_AU,
        infos_compl=AT1_INFOS_COMPL,
    )

    # AT2 → Table 5
    fill_example_table(
        doc.tables[5],
        intitule_at=AT2_INTITULE,
        intitule_ex=AT2_EX_INTITULE,
        tasks=AT2_TASKS,
        moyens=AT2_MOYENS,
        avec_qui=AT2_AVEC_QUI,
        nom_ent=AT2_NOM_ENTREPRISE,
        service=AT2_SERVICE,
        periode_du=AT2_PERIODE_DU,
        periode_au=AT2_PERIODE_AU,
        infos_compl=AT2_INFOS_COMPL,
    )

    # AT3 → laissée en place temporairement pour stabilité d'indexation
    # (sera supprimée à la toute fin).

    fill_sommaire(doc)
    fill_diplomes(doc)
    fill_declaration(doc)
    fill_documents_illustrant(doc)

    # En dernier — supprimer la table AT3 (DWWM = 2 AT seulement).
    # Doit être après tous les fills pour que les indices doc.tables[N]
    # restent stables.
    remove_at3_section(doc)

    # Supprimer aussi les sauts de page « extra » entre AT1↔AT2 et
    # AT2↔Titres-diplômes pour éviter les pages vides.
    remove_excess_page_breaks(doc)

    doc.save(str(DST))
    print(f"✓ Généré : {DST}")
    print(f"  Taille  : {DST.stat().st_size:,} octets")


if __name__ == '__main__':
    main()
