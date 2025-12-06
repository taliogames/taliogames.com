import requests
import json
import xml.etree.ElementTree as ET
from datetime import datetime
import os

# Configuración de Apps
APPS = [
    {
        "name": "Teko",
        "rss_url": "https://store.steampowered.com/feeds/news/app/3835670/?cc=US&l=english",
        "output_file": "teko/announcements/news.json"
    },
    {
        "name": "AEFTB",
        "rss_url": "https://store.steampowered.com/feeds/news/app/3157360/?cc=US&l=english",
        "output_file": "aeftb/announcements/news.json"
    }
]

def fetch_news():
    for app in APPS:
        try:
            print(f"--- Procesando {app['name']} ---")
            # 1. Obtener el XML de Steam
            response = requests.get(app['rss_url'], timeout=10)
            response.raise_for_status()
            
            # 2. Parsear XML
            root = ET.fromstring(response.content)
            channel = root.find('channel')
            items = channel.findall('item')
            
            news_list = []
            
            for item in items:
                # Extraer datos básicos
                title = item.find('title').text if item.find('title') is not None else 'No Title'
                link = item.find('link').text if item.find('link') is not None else '#'
                pub_date_raw = item.find('pubDate').text if item.find('pubDate') is not None else ''
                
                # Formatear fecha
                pub_date_display = ""
                if pub_date_raw:
                    try:
                        dt = datetime.strptime(pub_date_raw, "%a, %d %b %Y %H:%M:%S %z")
                        pub_date_display = dt.strftime("%B %d, %Y")
                    except:
                        pub_date_display = pub_date_raw

                # Extraer contenido
                content = ""
                encoded = item.find('{http://purl.org/rss/1.0/modules/content/}encoded')
                description = item.find('description')
                
                if encoded is not None and encoded.text:
                    content = encoded.text
                elif description is not None and description.text:
                    content = description.text
                
                if content:
                    content = content.strip()

                news_list.append({
                    'title': title,
                    'link': link,
                    'pubDate': pub_date_display,
                    'content': content
                })

            # 3. Guardar como JSON
            os.makedirs(os.path.dirname(app['output_file']), exist_ok=True)
            
            with open(app['output_file'], 'w', encoding='utf-8') as f:
                json.dump(news_list, f, ensure_ascii=False, indent=2)
                
            print(f"Éxito: Se guardaron {len(news_list)} noticias en {app['output_file']}")

        except Exception as e:
            print(f"Error actualizando noticias de {app['name']}: {e}")

if __name__ == "__main__":
    fetch_news()