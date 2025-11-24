// Variables Globales para manejar el estado
let allNews = [];       // Aquí guardaremos todas las noticias limpias
let currentPage = 1;    // Página actual
const postsPerPage = 3; // Cuántos posts por página

async function loadRSS() {
    const container = document.getElementById('rss');
    const paginationContainer = document.getElementById('pagination');
    
    if (!container) return;

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

        if (items.length === 0) {
            container.innerHTML = '<p>No announcements found.</p>';
            return;
        }

        // 1. PROCESAMOS TODAS LAS NOTICIAS PRIMERO Y LAS GUARDAMOS EN EL ARRAY
        allNews = Array.from(items).map(item => {
            const title = item.querySelector('title')?.textContent || 'No Title';
            const link = item.querySelector('link')?.textContent || '#';
            const pubDateRaw = item.querySelector('pubDate')?.textContent;
            
            // Fecha
            let pubDate = '';
            if (pubDateRaw) {
                const dateObj = new Date(pubDateRaw);
                pubDate = dateObj.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' });
            }

            // Contenido
            const contentEncoded = item.getElementsByTagName('content:encoded')[0] || 
                                   item.getElementsByTagNameNS('*', 'encoded')[0];
            const description = item.querySelector('description');
            
            let content = contentEncoded ? contentEncoded.textContent : (description ? description.textContent : '');
            
            // Limpieza básica
            content = content.replace(/^(<br\s*\/?>)+|(<br\s*\/?>)+$/gi, '');

            return { title, link, pubDate, content };
        });

        // 2. INICIAMOS LA VISTA EN LA PÁGINA 1
        renderPage(1);

    } catch (error) {
        console.error(error);
        container.innerHTML = '<p>Could not load news feed.</p>';
    }
}

// Función para mostrar una página específica
function renderPage(page) {
    const container = document.getElementById('rss');
    container.innerHTML = ''; // Limpiar noticias anteriores
    
    currentPage = page;

    // Calcular índices
    const start = (page - 1) * postsPerPage;
    const end = start + postsPerPage;
    
    // Obtener solo las noticias de esta página
    const pageItems = allNews.slice(start, end);

    // Renderizar noticias
    pageItems.forEach(news => {
        const div = document.createElement('div');
        div.className = 'rss-item';
        div.innerHTML = `
            <h2 class="rss-title"><a href="${news.link}" target="_blank">${news.title}</a></h2>
            <div class="rss-meta">Posted on ${news.pubDate}</div>
            <div class="rss-content">${news.content}</div>
            <div class="rss-footer">
                <a href="${news.link}" target="_blank" class="btn-steam">View on Steam</a>
            </div>
        `;
        container.appendChild(div);
    });

    // Actualizar los botones de paginación
    renderPagination();
    
    // Hacer scroll suave hacia arriba al cambiar de página
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Función para dibujar los botones de números (1, 2, 3...)
function renderPagination() {
    const paginationContainer = document.getElementById('pagination');
    paginationContainer.innerHTML = '';

    const totalPages = Math.ceil(allNews.length / postsPerPage);

    if (totalPages <= 1) return; // No mostrar botones si solo hay 1 página

    for (let i = 1; i <= totalPages; i++) {
        const btn = document.createElement('span');
        btn.className = 'page-btn';
        if (i === currentPage) btn.classList.add('active');
        btn.textContent = i;
        
        // Al hacer click, ir a esa página
        btn.onclick = () => renderPage(i);
        
        paginationContainer.appendChild(btn);
    }
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', loadRSS);
} else {
    loadRSS();
}
