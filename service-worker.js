JavaScript
const CACHE_NAME = 'horacios-curiacios-v1';
// Arquivos que serão salvos em cache
const urlsToCache = [
  '/',
  '/tabuleiro.html',
  '/style.css', // Se você separar seu CSS
  '/script.js', // Se você separar seu JS
  '/images/icon-192.png',
  '/images/icon-512.png',
  'https://cdn.jsdelivr.net/npm/chart.js'
];

// Instala o Service Worker e salva os arquivos no cache
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log('Cache aberto');
        return cache.addAll(urlsToCache);
      })
  );
});

// Intercepta as requisições e serve os arquivos do cache se estiverem disponíveis
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        // Se encontrar no cache, retorna. Senão, busca na rede.
        return response || fetch(event.request);
      })
  );
});
