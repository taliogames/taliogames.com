import requests
import re
import sys

# 1. Tu URL de la Web App de Google Apps Script
URL = "https://script.google.com/macros/s/AKfycbzUPJSGk3kyRRgGt38DlWPjLP5SF0HkNk6b07anPPB7HTaqoN7FznAKfGBcWlcUB3vi/exec"

# 2. Las rutas hacia tus archivos Markdown
FILE_PATH_RUNS = "teko/wiki/stats/runs.md"
FILE_PATH_CARDS = "teko/wiki/stats/cards.md"
FILE_PATH_POCKETS = "teko/wiki/stats/pockets.md"

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
    """
    html = "<div style=\"display: flex; justify-content: center; margin: 20px 0;\">\n"
    # Añadido "max-width: 100%;" para evitar que la tabla desborde en móviles
    html += "  <table style=\"width: max-content; max-width: 100%; margin: 0; box-shadow: 0 4px 8px rgba(0,0,0,0.2);\">\n"
    
    if not rows:
        return html + "</table></div>"

    start_idx = 0
    if has_header:
        header_row = rows[0]
        html += "    <thead><tr>\n"
        for i, val in enumerate(header_row):
            # Límite de ancho y salto de línea automático solo para la primera columna (i == 0)
            extra_style = " max-width: 250px; white-space: normal; word-wrap: break-word;" if i == 0 else ""
            html += f"      <th style=\"text-align: center; padding: 10px 30px;{extra_style}\"><strong>{val}</strong></th>\n"
        html += "    </tr></thead>\n"
        start_idx = 1
        
    html += "    <tbody>\n"
    for r in range(start_idx, len(rows)):
        row = rows[r]
        html += "      <tr>\n"
        for c, val in enumerate(row):
            cell_val = f"<strong>{val}</strong>" if c in bold_col_indices else val
            # Límite de ancho y salto de línea automático solo para la primera columna (c == 0)
            extra_style = " max-width: 250px; white-space: normal; word-wrap: break-word;" if c == 0 else ""
            html += f"        <td style=\"text-align: center; padding: 10px 30px;{extra_style}\">{cell_val}</td>\n"
        html += "      </tr>\n"
    html += "    </tbody>\n"
    html += "  </table>\n</div>\n"
    return html

def update_markdown_file(file_path, html_content):
    """
    Función auxiliar para leer, reemplazar y guardar un archivo Markdown.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        new_content = re.sub(
            r"<!-- STATS_START -->.*?<!-- STATS_END -->",
            f"<!-- STATS_START -->\n{html_content}\n<!-- STATS_END -->",
            content,
            flags=re.DOTALL
        )

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(new_content)
            
        print(f"{file_path} actualizado exitosamente.")
    except Exception as e:
        print(f"Error modificando el archivo {file_path}: {e}")
        sys.exit(1)


# =========================================================
# CONSTRUCCIÓN PARA RUNS.MD
# =========================================================
html_runs = f"<h2 style=\"text-align: center;\">{patch_name}</h2>\n\n"

# 1. Tabla principal
html_runs += (
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

# Tablas restantes
html_runs += "<div style=\"height: 20px;\"></div>\n<h2 style=\"text-align: center;\">Runs by difficulty</h2>\n"
html_runs += build_html_table(data.get('diff_table', []), has_header=True, bold_col_indices=[0])

html_runs += "<div style=\"height: 20px;\"></div>\n<h2 style=\"text-align: center;\">Averages</h2>\n"
html_runs += build_html_table(data.get('avg_table', []), has_header=False, bold_col_indices=[0])

html_runs += "<div style=\"height: 20px;\"></div>\n<h2 style=\"text-align: center;\">Averages when winning</h2>\n"
html_runs += build_html_table(data.get('avg_win_table', []), has_header=False, bold_col_indices=[0])

html_runs += "<div style=\"height: 20px;\"></div>\n<h2 style=\"text-align: center;\">Averages when losing</h2>\n"
html_runs += build_html_table(data.get('avg_lose_table', []), has_header=False, bold_col_indices=[0])

html_runs += "<div style=\"height: 20px;\"></div>\n<h2 style=\"text-align: center;\">Defeats by round</h2>\n"
html_runs += build_html_table(data.get('defeats_table', []), has_header=True, bold_col_indices=[0])


# =========================================================
# CONSTRUCCIÓN PARA CARDS.MD
# =========================================================
html_cards = f"<h2 style=\"text-align: center;\">{patch_name}</h2>\n\n"

# 1. TOP 10 highest winrate Cards
html_cards += "<div style=\"height: 20px;\"></div>\n<h2 style=\"text-align: center;\">TOP 10 highest winrate Cards</h2>\n"
html_cards += build_html_table(data.get('cards_top_winrate', []), has_header=True, bold_col_indices=[0])

# 2. TOP 10 lowest winrate Cards
html_cards += "<div style=\"height: 20px;\"></div>\n<h2 style=\"text-align: center;\">TOP 10 lowest winrate Cards</h2>\n"
html_cards += build_html_table(data.get('cards_low_winrate', []), has_header=True, bold_col_indices=[0])

# 3. TOP 50 most played Cards
html_cards += "<div style=\"height: 20px;\"></div>\n<h2 style=\"text-align: center;\">TOP 50 most played Cards</h2>\n"
html_cards += build_html_table(data.get('cards_most_played', []), has_header=True, bold_col_indices=[0])


# =========================================================
# CONSTRUCCIÓN PARA POCKETS.MD
# =========================================================
html_pockets = f"<h2 style=\"text-align: center;\">{patch_name}</h2>\n\n"

# 1. TOP 5 highest winrate Pockets
html_pockets += "<div style=\"height: 20px;\"></div>\n<h2 style=\"text-align: center;\">TOP 5 highest winrate Pockets</h2>\n"
html_pockets += build_html_table(data.get('pockets_top_winrate', []), has_header=True, bold_col_indices=[0])

# 2. TOP 5 lowest winrate Pockets
html_pockets += "<div style=\"height: 20px;\"></div>\n<h2 style=\"text-align: center;\">TOP 5 lowest winrate Pockets</h2>\n"
html_pockets += build_html_table(data.get('pockets_low_winrate', []), has_header=True, bold_col_indices=[0])

# 3. Most played Pockets (Dinámica)
html_pockets += "<div style=\"height: 20px;\"></div>\n<h2 style=\"text-align: center;\">Most played Pockets</h2>\n"
html_pockets += build_html_table(data.get('pockets_most_played', []), has_header=True, bold_col_indices=[0])

# 4. Winrate by difficulty for each Pocket (Dinámica)
html_pockets += "<div style=\"height: 20px;\"></div>\n<h2 style=\"text-align: center;\">Winrate by difficulty for each Pocket</h2>\n"
html_pockets += build_html_table(data.get('pockets_diff_table', []), has_header=True, bold_col_indices=[0])


# =========================================================
# ACTUALIZAR ARCHIVOS
# =========================================================
update_markdown_file(FILE_PATH_RUNS, html_runs)
update_markdown_file(FILE_PATH_CARDS, html_cards)
update_markdown_file(FILE_PATH_POCKETS, html_pockets)