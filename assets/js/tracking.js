(function () {
  const sendGA = (name, params={}) => {
    if (typeof gtag === 'function') gtag('event', name, params);
  };

  const tg = document.getElementById('tg-btn');
  if (tg) {
    tg.addEventListener('click', () => {
      // GA4 custom event
      sendGA('tg_click', {
        event_category: 'engagement',
        event_label: 't.me/astana_gb'
      });
      // Google Ads conversion (set your ID/label)
      sendGA('conversion', {
        send_to: 'AW-123456789/ABCDEF12345', // TODO: replace with real send_to
        value: 0,
        currency: 'KZT'
      });
    });
  }

  // Safety: track any other links to this TG URL across the page
  document.addEventListener('click', (e) => {
    const a = e.target.closest('a[href]');
    if (!a) return;
    const url = a.getAttribute('href') || '';
    if (url.includes('t.me/astana_gb')) {
      sendGA('tg_click', { event_category: 'engagement', event_label: url });
    }
  });
})();
