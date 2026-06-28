#!/usr/bin/env bash
# Reconstruit les 3 livrables PDF du dossier DWWM.
#
# Dépendances (macOS) :
#   - pandoc            (brew install pandoc)
#   - Google Chrome     (rendu HTML -> PDF, moteur Skia)
#   - python-docx       (pip install python-docx)  pour le DP officiel
#   - LibreOffice       (soffice — export DP_rempli.docx -> PDF, 28 pages,
#                        MÊME moteur que le build d'origine ; NE PAS utiliser
#                        Pages, qui re-paginé à 36 pages et gonfle le fichier)
#
# Usage : ./build-pdf.sh
set -euo pipefail
cd "$(dirname "$0")"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

md2pdf() { # <source.md> <titre> <sortie.pdf>
  pandoc "$1" -f gfm -t html5 -s --syntax-highlighting kate \
    --metadata title="$2" --metadata lang=fr \
    --include-in-header dossier-projet/_pdf_style.html \
    -o /tmp/_dwwm_build.html
  "$CHROME" --headless --disable-gpu --no-pdf-header-footer \
    --print-to-pdf="$3" "file:///tmp/_dwwm_build.html"
}

# 1. Dossier de projet (cahier des charges) ------------------------------
md2pdf dossier-projet/cahier-des-charges.md \
  "Crew — Dossier de projet (Cahier des charges)" \
  dossier-projet/dossier-projet.pdf

# 2. DP détaillé (markdown) ----------------------------------------------
md2pdf dossier-professionnel/DP.md \
  "Dossier Professionnel — Vladimir Rodzaevskiy" \
  dossier-professionnel/DP.pdf

# 3. DP officiel (gabarit Ministère) : docx -> PDF via LibreOffice -------
#    (le docx est édité directement via python-docx ; fill_dp_template.py
#     nécessite le gabarit source, absent de ce dépôt — on exporte le docx
#     tel quel. LibreOffice reproduit la pagination d'origine : 28 pages.)
soffice --headless --convert-to pdf \
  --outdir dossier-professionnel dossier-professionnel/DP_rempli.docx

# 4. Copies livrables (noms exigés par le centre) ------------------------
cp dossier-projet/dossier-projet.pdf      rodzaevskiy-vladimir-dossier-projet.pdf
cp dossier-professionnel/DP_rempli.pdf    rodzaevskiy-vladimir-dossier-pro.pdf
echo "✓ PDFs reconstruits."
