# -*- coding: utf-8 -*-
"""Manifest of generated pages. `slug` "" means project root (index.html),
anything else becomes `<slug>/index.html`."""

PAGES = [
    {
        "slug": "",
        "title": "Steuerkanzlei Schreiber · Braunschweig und Magdeburg",
        "description": "Steuerkanzlei Schreiber in Braunschweig und Magdeburg: Wir nehmen uns genügend Zeit für Sie. Der Mandant als Persönlichkeit steht im Vordergrund.",
        "content": "home.html",
    },
    {
        "slug": "leistungen",
        "title": "Leistungen · Steuerkanzlei Schreiber",
        "description": "Steuerliche Pflichten, Unterstützung von Entscheidungen, Durchsetzung Ihrer Rechte und Spezialgebiete wie Nachfolgeplanung: das Leistungsspektrum der Steuerkanzlei Schreiber.",
        "content": "leistungen.html",
    },
    {
        "slug": "wissen",
        # TODO: aus Navigation und Sitemap genommen, bis Quelle und Nutzungsrechte (mainfo.de) geklärt sind
        "sitemap": False,
        "title": "Wissen · Steuerkanzlei Schreiber",
        "description": "Kurze Erklärvideos zu Steuerfristen, Belegen und Steuerbescheiden von der Steuerkanzlei Schreiber.",
        "content": "wissen.html",
    },
    {
        "slug": "kanzlei",
        "title": "Kanzlei · Steuerkanzlei Schreiber",
        "description": "Die Steuerkanzlei Schreiber: Berufsleitbild, drei Generationen Verantwortung, Team und Kooperationspartner in Braunschweig und Magdeburg.",
        "content": "kanzlei.html",
    },
    {
        "slug": "kanzlei/geschichte",
        "title": "Geschichte · Steuerkanzlei Schreiber",
        "description": "Von Dr. Alfred Enke über Dr. Wolfgang Enke bis Frank Michael Schreiber: die Geschichte der Steuerkanzlei Schreiber in drei Generationen.",
        "content": "kanzlei-geschichte.html",
    },
    {
        "slug": "kanzlei/philosophie",
        "title": "Philosophie · Steuerkanzlei Schreiber",
        "description": "Der Mandant als Persönlichkeit steht im Vordergrund: die sechs Grundsätze der Steuerkanzlei Schreiber.",
        "content": "kanzlei-philosophie.html",
    },
    {
        "slug": "kanzlei/team",
        "title": "Team · Steuerkanzlei Schreiber",
        "description": "Die Mitarbeiterinnen und Mitarbeiter der Steuerkanzlei Schreiber in Braunschweig und Magdeburg, mit Zugehörigkeit und Schwerpunkten.",
        "content": "kanzlei-team.html",
    },
    {
        "slug": "karriere",
        "title": "Karriere · Steuerkanzlei Schreiber",
        "description": "Offene Stellen und Initiativbewerbung bei der Steuerkanzlei Schreiber in Braunschweig und Magdeburg.",
        "content": "karriere.html",
    },
    {
        "slug": "kontakt",
        "title": "Kontakt · Steuerkanzlei Schreiber",
        "description": "Kontaktieren Sie die Steuerkanzlei Schreiber in Braunschweig oder Magdeburg: Adresse, Telefon, E-Mail und Kontaktformular.",
        "content": "kontakt.html",
    },
    {
        "slug": "infobriefe",
        "title": "Infobriefe · Steuerkanzlei Schreiber",
        "description": "Inhalt der Mandantenschreiben der Steuerkanzlei Schreiber, nach Jahrgang und Monat.",
        "content": "infobriefe.html",
    },
    {
        "slug": "impressum",
        "title": "Impressum · Steuerkanzlei Schreiber",
        "description": "Impressum der Steuerkanzlei Schreiber gemäß § 5 TMG.",
        "content": "impressum.html",
    },
    {
        "slug": "datenschutz",
        "title": "Datenschutz · Steuerkanzlei Schreiber",
        "description": "Datenschutzerklärung der Steuerkanzlei Schreiber.",
        "content": "datenschutz.html",
    },
    {
        "slug": "faq",
        "title": "Häufige Fragen · Steuerkanzlei Schreiber",
        "description": "Antworten auf häufige Fragen zu Standorten, Leistungen und Kontakt der Steuerkanzlei Schreiber in Braunschweig und Magdeburg.",
        "content": "faq.html",
    },
]
