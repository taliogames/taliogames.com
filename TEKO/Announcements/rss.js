async function loadRSS() {
    console.log("Iniciando carga de RSS...");
    const container = document.getElementById('rss');
    
    // Verificación de seguridad por si el DOM no está listo
    if (!container) {
        console.error("No se encontró el contenedor #rss");
        return;
    }

    try {
        // Usamos allorigins para saltar la restricción CORS
        // URL del feed: https://store.steampowered.com/feeds/news/app/3835670
        const feedUrl = 'https://store.steampowered.com/feeds/news/app/3835670';
        const proxyUrl = 'https://api.allorigins.win/get?url=' + encodeURIComponent(feedUrl);

        console.log("Consultando URL:", proxyUrl);
        const res = await fetch(proxyUrl);
        
        if (!res.ok) throw new Error(`Error de red: ${res.status}`);
        
        const data = await res.json();
        
        if (!data.contents) {
            throw new Error('El proxy no devolvió contenido.');
        }

        const parser = new DOMParser();
        const xml = parser.parseFromString(data.contents, 'application/xml');
        const items = xml.querySelectorAll('item');

        console.log(`Se encontraron ${items.length} noticias.`);

        container.innerHTML = ''; // Limpiar mensaje de "Cargando..."

        if (items.length === 0) {
            container.innerHTML = '<p>No hay noticias recientes publicadas en Steam.</p>';
            return;
        }

        items.forEach(item => {
            const title = item.querySelector('title')?.textContent || 'Sin título';
            const link = item.querySelector('link')?.textContent || '#';
            const pubDateRaw = item.querySelector('pubDate')?.textContent;
            
            // Formatear fecha
            let pubDate = '';
            if (pubDateRaw) {
                const dateObj = new Date(pubDateRaw);
                if (!isNaN(dateObj)) {
                    pubDate = dateObj.toLocaleDateString('es-ES', { year: 'numeric', month: 'long', day: 'numeric' });
                }
            }

            // Priorizar content:encoded (HTML completo) sobre description
            const contentEncoded = item.getElementsByTagName('content:encoded')[0] || 
                                   item.getElementsByTagNameNS('*', 'encoded')[0];
            const description = item.querySelector('description');
            
            let content = '';
            if (contentEncoded && contentEncoded.textContent.trim() !== '') {
                content = contentEncoded.textContent;
            } else if (description) {
                content = description.textContent;
            }

            // Construir HTML
            const div = document.createElement('div');
            div.className = 'rss-item';
            div.innerHTML = `
                <h2>${title}</h2>
                ${pubDate ? `<p class="rss-date">${pubDate}</p>` : ''}
                <div class="rss-content">${content}</div>
                <br>
                <a href="${link}" target="_blank" class="btn-steam">Leer en Steam</a>
            `;
            container.appendChild(div);
        });

    } catch (error) {
        console.error('Error cargando RSS:', error);
        if (container) {
            container.innerHTML = `<p style="color:red;">Error al cargar noticias: ${error.message}. <br>Revisa la consola (F12) para más detalles.</p>`;
        }
    }
}

// Ejecutar cuando el contenido esté cargado
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', loadRSS);
} else {
    loadRSS();
}
