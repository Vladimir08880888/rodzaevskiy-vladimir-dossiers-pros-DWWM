#!/usr/bin/env bash
# Reconstruit les 3 livrables PDF du dossier DWWM.
#
# Dépendances (macOS) :
#   - pandoc            (brew install pandoc)
#   - Google Chrome     (rendu HTML -> PDF, moteur Skia)
#   - python-docx       (pip install python-docx)  pour le DP officiel
#   - Pages             (export DP_rempli.docx -> PDF, conserve le gabarit)
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

# 3. DP officiel (gabarit Ministère) : docx -> PDF via Pages -------------
#    (le docx est édité directement ; le script fill_dp_template.py nécessite
#     le gabarit source, absent de ce dépôt — on exporte donc le docx tel quel.)
osascript <<APPLESCRIPT
tell application "Pages"
  set d to open POSIX file "$PWD/dossier-professionnel/DP_rempli.docx"
  delay 2
  export d to POSIX file "$PWD/dossier-professionnel/DP_rempli.pdf" as PDF
  delay 1
  close d saving no
  quit
end tell
APPLESCRIPT

# 4. Copies livrables (noms exigés par le centre) ------------------------
cp dossier-projet/dossier-projet.pdf      rodzaevskiy-vladimir-dossier-projet.pdf
cp dossier-professionnel/DP_rempli.pdf    rodzaevskiy-vladimir-dossier-pro.pdf
echo "✓ PDFs reconstruits."
