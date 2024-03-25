var staticCacheName = 'djangopwa-v1';

self.addEventListener('install', function (event) {
  event.waitUntil(
    caches.open(staticCacheName).then(function (cache) {
      return cache.addAll([
        '/',
        '/kayscrochetapp/static/images/background.png',
        '/kayscrochetapp/static/images/HaveAGoodDay.png',
        '/kayscrochetapp/static/images/icon-192x192.png',
        '/kayscrochetapp/static/images/icon-256x256.png',
        '/kayscrochetapp/static/images/icon-384x384.png',
        '/kayscrochetapp/static/images/icon-512x512.png',
        '/kayscrochetapp/static/style.css',
      ]);
    }).catch(function (error) {
      console.error('Error during installation:', error);
    })
  );
});

self.addEventListener('fetch', function (event) {
  var requestUrl = new URL(event.request.url);

  if (requestUrl.origin === location.origin) {
    if (requestUrl.pathname === '/') {
      event.respondWith(
        caches.match(PWA_APP_START_URL).then(function (response) {
          return response || fetch(PWA_APP_START_URL);
        })
      );
      return;
    }
    // Handle other static assets explicitly
    if (requestUrl.pathname.startsWith('/kayscrochetapp/static/')) {
      event.respondWith(
        caches.match(event.request).then(function (response) {
          return response || fetch(event.request);
        }).catch(function (error) {
          console.error('Error during fetch:', error);
        })
      );
      return;
    }
  }

  // Cache images dynamically
  if (requestUrl.origin === 'https://s3.amazonaws.com' && requestUrl.pathname.startsWith('/kayscrochetbucket/items_images/')) {
    event.respondWith(
      caches.open(staticCacheName).then(function (cache) {
        return fetch(event.request).then(function (networkResponse) {
          cache.put(event.request, networkResponse.clone());
          return networkResponse;
        }).catch(function () {
          return cache.match(event.request);
        });
      })
    );
    return;
  }

  event.respondWith(
    fetch(event.request).catch(function () {
      return caches.match(event.request);
    })
  );
});