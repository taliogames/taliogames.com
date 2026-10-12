import requests
import re
import sys

# 1. Reemplaza con la URL de tu Web App de Google Apps Script
URL = "https://script.google.com/macros/s/AKfycbzUPJSGk3kyRRgGt38DlWPjLP5SF0HkNk6b07anPPB7HTaqoN7FznAKfGBcWlcUB3vi/exec"

# 2. Ajusta la ruta exacta hacia tu archivo runs.md dentro del repositorio
FILE_PATH = "teko/wiki/stats/runs/runs.md"

try:
    response = requests.get(URL)
    data = response.json()
except Exception as e:
    print(f"Error obteniendo los datos de Google Sheets: {e}")
    sys.exit(1)

# Construir la tabla en formato Markdown
table_md = f"""| Métrica | Valor |
| :--- | :---: |
| **Runs** | {data.get('runs', 0)} |
| **Won** | {data.get('won', 0)} |
| **Lost** | {data.get('lost', 0)} |
| **Winrate** | {data.get('winrate', '0%')} |"""

try:
    with open(FILE_PATH, "r", encoding="utf-8") as file:
        content = file.read()

    # Reemplazar el contenido entre los marcadores
    new_content = re.sub(
        r"<!-- STATS_START -->.*?<!-- STATS_END -->",
        f"<!-- STATS_START -->\n{table_md}\n<!-- STATS_END -->",
        content,
        flags=re.DOTALL
    )

    with open(FILE_PATH, "w", encoding="utf-8") as file:
        file.write(new_content)
        
    print("runs.md actualizado exitosamente.")
except Exception as e:
    print(f"Error modificando el archivo Markdown: {e}")
    sys.exit(1)