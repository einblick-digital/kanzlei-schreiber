# -*- coding: utf-8 -*-
"""Shared header/footer HTML for every page. Uses __TOKEN__ placeholders
(replaced via str.replace in build.py) instead of str.format(), since the
embedded JSON-LD block contains literal curly braces."""

SITE_URL = "https://www.kanzlei-schreiber.de"

SCHEMA_JSON = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "AccountingService",
      "@id": "__SITE_URL__/#braunschweig",
      "name": "Steuerkanzlei Schreiber · Kanzlei Braunschweig",
      "url": "__SITE_URL__",
      "telephone": "+49-531-333347",
      "faxNumber": "+49-531-331095",
      "email": "steuerkanzlei-bs@t-online.de",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Gaußstraße 32",
        "postalCode": "38106",
        "addressLocality": "Braunschweig",
        "addressCountry": "DE"
      },
      "founder": { "@type": "Person", "name": "Frank Michael Schreiber" }
    },
    {
      "@type": "AccountingService",
      "@id": "__SITE_URL__/#magdeburg",
      "name": "Steuerkanzlei Schreiber · Kanzlei Magdeburg",
      "url": "__SITE_URL__",
      "telephone": "+49-391-7332640",
      "faxNumber": "+49-391-7332050",
      "email": "steuerkanzlei-md@t-online.de",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Liebknechtstraße 50",
        "postalCode": "39108",
        "addressLocality": "Magdeburg",
        "addressCountry": "DE"
      },
      "founder": { "@type": "Person", "name": "Frank Michael Schreiber" }
    }
  ]
}"""

HEAD = """<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
<meta name="description" content="__DESCRIPTION__">
<link rel="canonical" href="__CANONICAL__">
<link rel="stylesheet" href="/css/tokens.css?v=46">
<link rel="stylesheet" href="/css/styles.css?v=46">
<script type="application/ld+json">__SCHEMA_JSON__</script>
<script src="https://unpkg.com/lucide@latest" defer></script>
<script src="/script.js?v=8" defer></script>
</head>
<body>
"""

HEADER = """
<header class="site-header">
  <div class="site-header__bar">
    <a href="/" class="site-header__logo"><img src="/assets/Steuerkanzlei Schreiber Logo Blau Grau.svg" alt="Steuerkanzlei Schreiber"></a>
    <button type="button" class="nav-toggle" id="navToggle" aria-expanded="false" aria-controls="siteNav" aria-label="Menü öffnen">
      <i data-lucide="menu"></i>
    </button>
    <nav class="site-nav" id="siteNav">
      <div class="site-nav__item has-dropdown">
        <a href="/kanzlei/">Kanzlei</a>
        <div class="site-nav__dropdown">
          <a href="/kanzlei/geschichte/">Geschichte</a>
          <a href="/kanzlei/philosophie/">Philosophie</a>
        </div>
      </div>
      <a href="/leistungen/">Leistungen</a>
      <a href="/wissen/">Wissen</a>
      <a href="/karriere/" class="is-accent">Karriere</a>
      <a href="/kanzlei/team/">Team</a>
    </nav>
    <a href="/kontakt/" class="site-header__cta btn btn--primary btn--sm">Kontakt</a>
  </div>
</header>

<main id="top">
"""

FOOTER = """
</main>

<footer class="site-footer">
  <div class="container site-footer__grid">
    <div>
      <div class="site-footer__brand">Steuerkanzlei Schreiber</div>
      <div style="font:var(--text-body-sm)">Gaußstraße 32, 38106 Braunschweig<br>Liebknechtstraße 50, 39108 Magdeburg</div>
      <div class="site-footer__social">
        <a href="https://www.instagram.com/kanzlei.schreiber/" target="_blank" rel="noopener" aria-label="Instagram"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg></a>
        <a href="https://www.linkedin.com/company/steuerkanzlei-schreiber/" target="_blank" rel="noopener" aria-label="LinkedIn"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg></a>
      </div>
    </div>
    <div class="site-footer__col">
      <a href="/kanzlei/">Kanzlei</a>
      <a href="/leistungen/">Leistungen</a>
      <a href="/wissen/">Wissen</a>
      <a href="/karriere/">Karriere</a>
      <a href="/kanzlei/team/">Team</a>
    </div>
    <div class="site-footer__col">
      <a href="/kontakt/">Kontakt</a>
      <a href="/faq/">FAQ</a>
      <a href="/impressum/">Impressum</a>
      <a href="/datenschutz/">Datenschutz</a>
    </div>
    <div class="site-footer__col">
      <a href="tel:+4953133347">Braunschweig: (05 31) 33 33 47</a>
      <a href="tel:+493917332640">Magdeburg: (03 91) 7 33 26 40</a>
    </div>
  </div>
  <div class="container site-footer__bottom">© 2026 Steuerkanzlei Schreiber · Mitglied der Steuerberaterkammer Niedersachsen</div>
</footer>

</body>
</html>
"""
