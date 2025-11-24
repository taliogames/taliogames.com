async function loadRSS() {
    const url = 'https://api.allorigins.win/get?url=' + encodeURIComponent('https://store.steampowered.com/feeds/news/app/3835670');

    const res = await fetch(url);
    const data = await res.json();

    const parser = new DOMParser();
    const xml = parser.parseFromString(data.contents, 'application/xml');

    const items = xml.querySelectorAll('item');
    const container = document.getElementById('rss');

    items.forEach(i => {
        const title = i.querySelector('title').textContent;
        const desc = i.querySelector('description').textContent;
        const link = i.querySelector('link').textContent;

        const div = document.createElement('div');
        div.innerHTML = `
            <h2>${title}</h2>
            <div>${desc}</div>
            <a href="${link}" target="_blank">Ver en Steam</a>
            <hr>
        `;
        container.appendChild(div);
    });
}

loadRSS();
