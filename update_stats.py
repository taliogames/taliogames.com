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

patch_name = data.get('patch_name', 'PATCH -')

def build_html_table(rows, has_header=False, bold_col_indices=[]):
    """
    Función auxiliar para construir tablas HTML limpias y centradas.
    rows: lista de listas (datos).
    has_header: si True, la primera fila usa <th> y fondo oscuro.
    bold_col_indices: lista de índices de columnas (0, 1, etc.) que siempre deben ser negritas.
    """
    html = "<div style=\"display: flex; justify-content: center; margin: 20px 0;\">\n"
    html += "  <table style=\"width: max-content; margin: 0; box-shadow: 0 4px 8px rgba(0,0,0,0.2);\">\n"
    
    if not rows:
        return html + "</table></div>"

    # Procesar encabezado si tiene
    start_idx = 0
    if has_header:
        header_row = rows[0]
        html += "    <thead><tr>\n"
        for i, val in enumerate(header_row):
            html += f"      <th style=\"text-align: center; padding: 10px 30px;\"><strong>{val}</strong></th>\n"
        html += "    </tr></thead>\n"
        start_idx = 1
        
    html += "    <tbody>\n"
    for r in range(start_idx, len(rows)):
        row = rows[r]
        html += "      <tr>\n"
        for c, val in enumerate(row):
            # Formatear el valor: poner en negrita si pertenece a una columna especificada en bold_col_indices
            cell_val = f"<strong>{val}</strong>" if c in bold_col_indices else val
            html += f"        <td style=\"text-align: center; padding: 10px 30px;\">{cell_val}</td>\n"
        html += "      </tr>\n"
    html += "    </tbody>\n"
    html += "  </table>\n</div>\n"
    return html

# ---------------------------------------------------------
# Construcción del HTML final combinando todas las secciones
# ---------------------------------------------------------

html_output = f"<h2 style=\"text-align: center;\">{patch_name}</h2>\n\n"

# 1. Tabla principal (Runs, Won, Lost, Winrate)
# La creamos manualmente porque no viene de un array 2D
html_output += (
    "<div style=\"display: flex; justify-content: center; margin: 20px 0;\">\n"
    "  <table style=\"width: max-content; margin: 0; box-shadow: 0 4px 8px rgba(0,0,0,0.2);\">\n"
    "    <tbody>\n"
    f"      <tr><td style=\"text-align: center; padding: 10px 30px;\"><strong>Runs</strong></td><td style=\"text-align: center; padding: 10px 30px;\">{data.get('runs', 0)}</td></tr>\n"
    f"      <tr><td style=\"text-align: center; padding: 10px 30px;\"><strong>Won</strong></td><td style=\"text-align: center; padding: 10px 30px;\">{data.get('won', 0)}</td></tr>\n"
    f"      <tr><td style=\"text-align: center; padding: 10px 30px;\"><strong>Lost</strong></td><td style=\"text-align: center; padding: 10px 30px;\">{data.get('lost', 0)}</td></tr>\n"
    f"      <tr><td style=\"text-align: center; padding: 10px 30px;\"><strong>Winrate</strong></td><td style=\"text-align: center; padding: 10px 30px;\">{data.get('winrate', '0%')}</td></tr>\n"
    "    </tbody>\n"
    "  </table>\n"
    "</div>\n"
)

# 2. Runs by difficulty (K7:O12) - Con encabezado, primera columna negrita (col 0)
html_output += "<div style=\"height: 20px;\"></div>\n"
html_output += "<h2 style=\"text-align: center;\">Runs by difficulty</h2>\n"
html_output += build_html_table(data.get('diff_table', []), has_header=True, bold_col_indices=[0])

# 3. Averages (B7:C24) - Sin encabezado, primera columna negrita (col 0)
html_output += "<div style=\"height: 20px;\"></div>\n"
html_output += "<h2 style=\"text-align: center;\">Averages</h2>\n"
html_output += build_html_table(data.get('avg_table', []), has_header=False, bold_col_indices=[0])

# 4. Averages when winning (E7:F24) - Sin encabezado, primera columna negrita (col 0)
html_output += "<div style=\"height: 20px;\"></div>\n"
html_output += "<h2 style=\"text-align: center;\">Averages when winning</h2>\n"
html_output += build_html_table(data.get('avg_win_table', []), has_header=False, bold_col_indices=[0])

# 5. Averages when losing (H7:I24) - Sin encabezado, primera columna negrita (col 0)
html_output += "<div style=\"height: 20px;\"></div>\n"
html_output += "<h2 style=\"text-align: center;\">Averages when losing</h2>\n"
html_output += build_html_table(data.get('avg_lose_table', []), has_header=False, bold_col_indices=[0])

# 6. Defeats by round (K15:M38) - Con encabezado, primera columna negrita (col 0)
html_output += "<div style=\"height: 20px;\"></div>\n"
html_output += "<h2 style=\"text-align: center;\">Defeats by round</h2>\n"
html_output += build_html_table(data.get('defeats_table', []), has_header=True, bold_col_indices=[0])

try:
    with open(FILE_PATH, "r", encoding="utf-8") as file:
        content = file.read()

    new_content = re.sub(
        r"<!-- STATS_START -->.*?<!-- STATS_END -->",
        f"<!-- STATS_START -->\n{html_output}\n<!-- STATS_END -->",
        content,
        flags=re.DOTALL
    )

    with open(FILE_PATH, "w", encoding="utf-8") as file:
        file.write(new_content)
        
    print("runs.md actualizado exitosamente con todas las tablas HTML.")
except Exception as e:
    print(f"Error modificando el archivo Markdown: {e}")
    sys.exit(1)