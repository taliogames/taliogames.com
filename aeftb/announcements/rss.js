// Variables Globales
let allNews = [];
let currentPage = 1;
const postsPerPage = 3;

async function loadRSS() {
    const container = document.getElementById('rss');
    
    // Busca el json en la misma carpeta donde está este script
    const jsonUrl = './news.json'; 

    try {
        const res = await fetch(jsonUrl + '?t=' + new Date().getTime());
        
        if (!res.ok) throw new Error('No se pudo cargar el archivo de noticias local.');
        
        const data = await res.json();

        if (!Array.isArray(data) || data.length === 0) {
            container.innerHTML = '<p>No announcements found.</p>';
            return;
        }

        allNews = data;
        renderPage(1);

    } catch (error) {
        console.error(error);
        container.innerHTML = `
            <div style="text-align:center; color: #ff6b6b;">
                <p>Could not load news.</p>
                <small>${error.message}</small>
            </div>`;
    }
}

function renderPage(page) {
    const container = document.getElementById('rss');
    container.innerHTML = '';
    currentPage = page;

    const start = (page - 1) * postsPerPage;
    const end = start + postsPerPage;
    const pageItems = allNews.slice(start, end);

    pageItems.forEach(news => {
        const div = document.createElement('div');
        div.className = 'rss-item';
        div.innerHTML = `
            <h1 class="rss-title"><a href="${news.link}" target="_blank">${news.title}</a></h1>
            <div class="rss-meta">Posted on ${news.pubDate}</div>
            <div class="rss-content">${news.content}</div>
            <div class="rss-footer">
                <a href="${news.link}" target="_blank" class="btn-steam">View on Steam</a>
            </div>
        `;
        container.appendChild(div);
    });

    renderPagination();
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

function renderPagination() {
    const paginationContainer = document.getElementById('pagination');
    paginationContainer.innerHTML = '';

    const totalPages = Math.ceil(allNews.length / postsPerPage);
    if (totalPages <= 1) return;

    for (let i = 1; i <= totalPages; i++) {
        const btn = document.createElement('span');
        btn.className = 'page-btn';
        if (i === currentPage) btn.classList.add('active');
        btn.textContent = i;
        btn.onclick = () => renderPage(i);
        paginationContainer.appendChild(btn);
    }
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', loadRSS);
} else {
    loadRSS();
}