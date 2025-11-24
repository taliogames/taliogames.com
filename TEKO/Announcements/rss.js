async function loadRSS() {
    const container = document.getElementById('rss');
    if (!container) return;

    // Usamos el enlace en inglés/US como pediste, a través del proxy
    const feedUrl = 'https://store.steampowered.com/feeds/news/app/3835670/?cc=US&l=english';
    const proxyUrl = 'https://api.allorigins.win/get?url=' + encodeURIComponent(feedUrl);

    try {
        const res = await fetch(proxyUrl);
        if (!res.ok) throw new Error('Error de conexión');
        
        const data = await res.json();
        if (!data.contents) throw new Error('Sin contenido');

        const parser = new DOMParser();
        const xml = parser.parseFromString(data.contents, 'application/xml');
        const items = xml.querySelectorAll('item');

        container.innerHTML = ''; // Limpiar mensaje de carga

        if (items.length === 0) {
            container.innerHTML = '<p>No announcements found.</p>';
            return;
        }

        items.forEach(item => {
            const title = item.querySelector('title')?.textContent || 'No Title';
            const link = item.querySelector('link')?.textContent || '#';
            const pubDateRaw = item.querySelector('pubDate')?.textContent;
            
            // Formatear fecha
            let pubDate = '';
            if (pubDateRaw) {
                const dateObj = new Date(pubDateRaw);
                pubDate = dateObj.toLocaleDateString('en-US', { 
                    year: 'numeric', month: 'long', day: 'numeric' 
                });
            }

            // Obtener contenido HTML completo
            const contentEncoded = item.getElementsByTagName('content:encoded')[0] || 
                                   item.getElementsByTagNameNS('*', 'encoded')[0];
            const description = item.querySelector('description');
            
            let content = contentEncoded ? contentEncoded.textContent : (description ? description.textContent : '');

            // --- LIMPIEZA DE FORMATO (Opcional pero recomendado) ---
            // 1. Eliminar etiquetas <br> excesivas al inicio/final si las hubiera
            content = content.replace(/^(<br\s*\/?>)+|(<br\s*\/?>)+$/gi, '');
            // 2. A veces Steam usa enlaces a imágenes HTTP que dan warnings, no es crítico pero bueno saberlo.

            const div = document.createElement('div');
            div.className = 'rss-item';
            div.innerHTML = `
                <h2 class="rss-title"><a href="${link}" target="_blank">${title}</a></h2>
                <div class="rss-meta">Posted on ${pubDate}</div>
                <div class="rss-content">${content}</div>
                <div class="rss-footer">
                    <a href="${link}" target="_blank" class="btn-steam">View on Steam</a>
                </div>
            `;
            container.appendChild(div);
        });

    } catch (error) {
        console.error(error);
        container.innerHTML = '<p>Could not load news feed.</p>';
    }
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', loadRSS);
} else {
    loadRSS();
}
