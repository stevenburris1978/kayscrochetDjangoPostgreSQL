self.addEventListener('install', function (event) {
    event.waitUntil(
        caches.open('cache-1').then(function (cache) {
            return cache.addAll([
                '/',
                '/kayscrochetapp/static/**',
                '/media/**',
                'https://s3.amazonaws.com/your-bucket-name/items_images/**',
            ]);
        }).catch(function (error) {
            console.error('Error during cache installation:', error);
        })
    );
});

self.addEventListener('fetch', async function (event) {
    event.respondWith(
        (async function () {
            try {
                // Try to fetch the resource from the network
                const fetchResponse = await fetch(event.request);

                // If the fetch was successful, cache the response
                const cache = await caches.open('cache-1');
                cache.put(event.request, fetchResponse.clone());

                return fetchResponse;
            } catch (error) {
                console.error('Error during fetch:', error);

                // If the fetch failed (e.g., due to no internet connection),
                // try to respond with a cached version if available
                const cachedResponse = await caches.match(event.request);
                if (cachedResponse) {
                    return cachedResponse;
                }
            }
        })()
    );
});


