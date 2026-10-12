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

# Construir el HTML del título y la tabla sin la primera fila (Métrica/Valor)
# Mantenemos la fila de alineación (| :--- | :---: |) porque Markdown la exige para renderizar la tabla,
# pero en Jekyll, al no tener encabezados con texto, suele ocultarlos o dejarlos invisibles.
table_md = (
    f"<h2 style=\"text-align: center;\">{patch_name}</h2>\n\n"
    "| | |\n"
    "| :--- | :---: |\n"
    f"| **Runs** | {data.get('runs', 0)} |\n"
    f"| **Won** | {data.get('won', 0)} |\n"
    f"| **Lost** | {data.get('lost', 0)} |\n"
    f"| **Winrate** | {data.get('winrate', '0%')} |"
)

try:
    with open(FILE_PATH, "r", encoding="utf-8") as file:
        content = file.read()

    # Agregamos los reemplazos con saltos de línea
    new_content = re.sub(
        r"<!-- STATS_START -->.*?<!-- STATS_END -->",
        f"<!-- STATS_START -->\n\n{table_md}\n\n<!-- STATS_END -->",
        content,
        flags=re.DOTALL
    )

    with open(FILE_PATH, "w", encoding="utf-8") as file:
        file.write(new_content)
        
    print("runs.md actualizado exitosamente.")
except Exception as e:
    print(f"Error modificando el archivo Markdown: {e}")
    sys.exit(1)