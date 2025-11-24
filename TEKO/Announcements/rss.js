async function loadRSS() {
    // Usamos allorigins para evitar problemas de CORS (Cross-Origin Resource Sharing)
    const url = 'https://api.allorigins.win/get?url=' + encodeURIComponent('https://store.steampowered.com/feeds/news/app/3835670');

    try {
        const res = await fetch(url);
        const data = await res.json();

        if (!data.contents) {
            throw new Error('No se pudo obtener el contenido del feed.');
        }

        const parser = new DOMParser();
        const xml = parser.parseFromString(data.contents, 'application/xml');

        const items = xml.querySelectorAll('item');
        const container = document.getElementById('rss');

        // Limpiamos el contenedor (y mostramos mensaje si no hay noticias)
        container.innerHTML = '';
        if (items.length === 0) {
            container.innerHTML = '<p>No hay noticias recientes.</p>';
            return;
        }

        items.forEach(item => {
            // Extraer título y enlace
            const title = item.querySelector('title') ? item.querySelector('title').textContent : 'Sin título';
            const link = item.querySelector('link') ? item.querySelector('link').textContent : '#';
            
            // Extraer fecha y formatearla
            const pubDateRaw = item.querySelector('pubDate') ? item.querySelector('pubDate').textContent : '';
            const pubDate = pubDateRaw ? new Date(pubDateRaw).toLocaleDateString('es-ES', { year: 'numeric', month: 'long', day: 'numeric' }) : '';

            // LÓGICA IMPORTANTE: Buscar contenido completo
            // content:encoded suele tener el HTML completo del anuncio.
            // description a veces es solo un resumen o texto plano.
            let content = '';
            
            // Intentamos buscar la etiqueta 'content:encoded'
            const contentEncoded = item.getElementsByTagName('content:encoded')[0] || 
                                   item.getElementsByTagNameNS('*', 'encoded')[0]; // Soporte para namespaces

            const description = item.querySelector('description');

            if (contentEncoded) {
                content = contentEncoded.textContent;
            } else if (description) {
                content = description.textContent;
            }

            // Crear el elemento HTML
            const div = document.createElement('div');
            div.className = 'rss-item';
            div.innerHTML = `
                <h2>${title}</h2>
                <p><small>Publicado el: ${pubDate}</small></p>
                <div class="rss-content">${content}</div>
                <br>
                <a href="${link}" target="_blank" style="display:inline-block; padding:8px 16px; background:#1b2838; color:white; text-decoration:none; border-radius:4px;">Ver en Steam</a>
                <hr style="margin: 30px 0;">
            `;
            container.appendChild(div);
        });

    } catch (error) {
        console.error('Error cargando el RSS:', error);
        const container = document.getElementById('rss');
        if (container) container.innerHTML = '<p>Hubo un error al cargar las noticias de Steam. Por favor, intenta más tarde.</p>';
    }
}

loadRSS();
