---
layout: default
title: TEKO Announcements
---

<h1>TEKO Announcements</h1>

<div id="rss">
    <p style="text-align:center; padding: 20px;">Loading updates from Steam...</p>
</div>

<div id="pagination"></div>

<style>
    /* --- ESTILOS DE NOTICIAS (IGUAL QUE ANTES) --- */
    .rss-item {
        background: rgba(255, 255, 255, 0.05);
        padding: 20px;
        margin-bottom: 40px;
        border-radius: 8px;
        border: 1px solid rgba(255,255,255,0.1);
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .rss-title { margin-top: 0; margin-bottom: 5px; font-size: 1.8em; }
    .rss-title a { text-decoration: none; color: #159957; }
    .rss-meta { font-size: 0.85em; color: #888; margin-bottom: 20px; border-bottom: 1px solid #ddd; padding-bottom: 10px; }
    .rss-content { line-height: 1.6; font-size: 1rem; overflow-wrap: break-word; }
    .rss-content img { max-width: 100%; height: auto !important; display: block; margin: 15px 0; border-radius: 4px; }
    .rss-content iframe { max-width: 100%; width: 100%; aspect-ratio: 16 / 9; border: none; }
    .rss-content ul, .rss-content ol { padding-left: 20px; margin-bottom: 15px; }
    .rss-content blockquote { border-left: 4px solid #159957; margin: 15px 0; padding-left: 15px; color: #555; background: #f9f9f9; padding: 10px; }
    .rss-content img[src*="youtube_16x9_placeholder.gif"] {
        display: none !important;
    }
    .rss-footer { margin-top: 20px; text-align: right; }
    .btn-steam { display: inline-block; padding: 8px 18px; background-color: #2a475e; color: #fff !important; text-decoration: none; border-radius: 4px; font-size: 0.9em; transition: background 0.3s; }
    .btn-steam:hover { background-color: #66c0f4; }

    /* --- NUEVOS ESTILOS PARA PAGINACIÓN --- */
    #pagination {
        text-align: center;
        margin-top: 30px;
        margin-bottom: 50px;
    }
    
    .page-btn {
        display: inline-block;
        margin: 0 5px;
        padding: 8px 16px;
        background: #f0f0f0;
        color: #333;
        border-radius: 4px;
        cursor: pointer;
        user-select: none;
        transition: background 0.2s;
        border: 1px solid #ccc;
    }

    .page-btn:hover {
        background: #e0e0e0;
    }

    .page-btn.active {
        background: #159957; /* Color verde del tema */
        color: white;
        border-color: #159957;
        font-weight: bold;
    }
</style>

<script src="/taliogames.com/teko/announcements/rss.js"></script>
