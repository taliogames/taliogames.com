---
layout: default
title: Announcements
---

<h1>TEKO Announcements</h1>

<div id="rss">
    <p style="text-align:center; padding: 20px;">Loading updates from Steam...</p>
</div>

<style>
    /* Estilo para cada noticia */
    .rss-item {
        background: rgba(255, 255, 255, 0.05); /* Fondo sutil para separar posts */
        padding: 20px;
        margin-bottom: 40px;
        border-radius: 8px;
        border: 1px solid rgba(255,255,255,0.1);
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    .rss-title {
        margin-top: 0;
        margin-bottom: 5px;
        font-size: 1.8em;
    }
    
    .rss-title a {
        text-decoration: none;
        color: #159957; /* Color del tema Cayman (verde) */
    }

    .rss-meta {
        font-size: 0.85em;
        color: #888;
        margin-bottom: 20px;
        border-bottom: 1px solid #ddd;
        padding-bottom: 10px;
    }

    /* --- ESTILOS CORRECTIVOS PARA EL CONTENIDO DE STEAM --- */
    .rss-content {
        line-height: 1.6;
        font-size: 1rem;
        overflow-wrap: break-word; /* Evita que textos largos rompan el móvil */
    }

    /* IMÁGENES: Que nunca se salgan del ancho y se centren si son pequeñas */
    .rss-content img {
        max-width: 100%;
        height: auto !important; /* Forza la proporción correcta */
        display: block;
        margin: 15px 0;
        border-radius: 4px;
    }

    /* VIDEOS (YouTube/Steam): Responsivos */
    .rss-content iframe {
        max-width: 100%;
        width: 100%;
        aspect-ratio: 16 / 9; /* Mantiene formato video */
        border: none;
    }

    /* Listas y citas */
    .rss-content ul, .rss-content ol {
        padding-left: 20px;
        margin-bottom: 15px;
    }
    
    .rss-content blockquote {
        border-left: 4px solid #159957;
        margin: 15px 0;
        padding-left: 15px;
        color: #555;
        background: #f9f9f9;
        padding: 10px;
    }

    /* Botón final */
    .rss-footer {
        margin-top: 20px;
        text-align: right;
    }

    .btn-steam {
        display: inline-block;
        padding: 8px 18px;
        background-color: #2a475e; /* Azul Steam */
        color: #fff !important;
        text-decoration: none;
        border-radius: 4px;
        font-size: 0.9em;
        transition: background 0.3s;
    }
    .btn-steam:hover {
        background-color: #66c0f4;
    }
</style>

<script src="/taliogames.com/TEKO/Announcements/rss.js"></script>
