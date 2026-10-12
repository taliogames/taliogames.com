import requests
import re
import sys

# 1. Tu URL de la Web App de Google Apps Script
URL = "https://script.google.com/macros/s/AKfycbzUPJSGk3kyRRgGt38DlWPjLP5SF0HkNk6b07anPPB7HTaqoN7FznAKfGBcWlcUB3vi/exec"

# 2. La ruta exacta hacia tu archivo runs.md dentro del repositorio
FILE_PATH = "teko/wiki/stats/runs.md"

try:
    response = requests.get(URL)
    data = response.json()
except Exception as e:
    print(f"Error obteniendo los datos de Google Sheets: {e}")
    sys.exit(1)

# Obtener el nombre del parche (si está vacío, usamos un texto por defecto)
patch_name = data.get('patch_name', 'PATCH -')

# Construimos la tabla en HTML puro. 
# display: flex centra la tabla en la página.
# width: max-content anula el "width: 100%" de tu CSS.
# padding da ese espacio lindo (aire) dentro de las celdas.
table_html = (
    f"<h2 style=\"text-align: center;\">{patch_name}</h2>\n\n"
    "<div style=\"display: flex; justify-content: center; margin: 20px 0;\">\n"
    "  <table style=\"width: max-content; margin: 0; box-shadow: 0 4px 8px rgba(0,0,0,0.2);\">\n"
    "    <tbody>\n"
    f"      <tr><td style=\"text-align: center; padding: 10px 30px;\"><strong>Runs</strong></td><td style=\"text-align: center; padding: 10px 30px;\">{data.get('runs', 0)}</td></tr>\n"
    f"      <tr><td style=\"text-align: center; padding: 10px 30px;\"><strong>Won</strong></td><td style=\"text-align: center; padding: 10px 30px;\">{data.get('won', 0)}</td></tr>\n"
    f"      <tr><td style=\"text-align: center; padding: 10px 30px;\"><strong>Lost</strong></td><td style=\"text-align: center; padding: 10px 30px;\">{data.get('lost', 0)}</td></tr>\n"
    f"      <tr><td style=\"text-align: center; padding: 10px 30px;\"><strong>Winrate</strong></td><td style=\"text-align: center; padding: 10px 30px;\">{data.get('winrate', '0%')}</td></tr>\n"
    "    </tbody>\n"
    "  </table>\n"
    "</div>"
)

try:
    with open(FILE_PATH, "r", encoding="utf-8") as file:
        content = file.read()

    # Reemplazamos el contenido en runs.md
    new_content = re.sub(
        r"<!-- STATS_START -->.*?<!-- STATS_END -->",
        f"<!-- STATS_START -->\n{table_html}\n<!-- STATS_END -->",
        content,
        flags=re.DOTALL
    )

    with open(FILE_PATH, "w", encoding="utf-8") as file:
        file.write(new_content)
        
    print("runs.md actualizado exitosamente con tabla HTML.")
except Exception as e:
    print(f"Error modificando el archivo Markdown: {e}")
    sys.exit(1)