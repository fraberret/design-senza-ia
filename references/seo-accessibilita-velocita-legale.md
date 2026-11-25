# SEO, accessibilità, velocità e leggi

Requisiti dal primo abbozzo, non rifiniture. Livelli: **[Evidenza]**, **[Prassi]**, **[Opinione]**. La colonna "Verifica" dice
quale controllo di `scripts/controllo_tecnico.py` copre la regola (id) o se va guardata **a mano**.

## 1. SEO tecnica e on-page

Le regole non sono cambiate: contenuto originale per le persone, pagine scansionabili e indicizzabili, niente spam. Il
rischio reale per un piccolo sito sono tre abitudini: pagine "servizio + città" clonate (doorway), blog riempito di articoli
generici in serie (scaled content abuse), metadati generati e mai riletti **[Evidenza]**
([Google, Spam policies](https://developers.google.com/search/docs/essentials/spam-policies); [Google, generative AI content](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content)).

| Area | Regola | Livello | Verifica |
|---|---|---|---|
| Indicizzazione | Googlebot non bloccato, risposta 200, contenuto nell'HTML iniziale; ambiente di prova con `noindex` o password, tolto al lancio | [Evidenza] ([Google](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)) | `senza-js` (contenuto senza JavaScript); il resto a mano |
| Mobile | Google indicizza con lo smartphone: contenuti, dati strutturati, title e link anche nella versione mobile | [Evidenza] ([Google](https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing)) | a mano |
| robots.txt | blocca la scansione, non l'indicizzazione: per escludere serve `noindex` su una pagina non bloccata | [Evidenza] ([Google](https://developers.google.com/search/docs/crawling-indexing/robots/intro)) | a mano |
| Canonical | autoreferenziale su ogni pagina; redirect, sitemap e link interni puntano allo stesso URL | [Evidenza] ([Google](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)) | `canonical` |
| Sitemap | solo URL canonici, 200, indicizzabili; in robots.txt e in Search Console | [Prassi] | a mano |
| URL | brevi, minuscoli, con trattini; HTTPS con un solo redirect | [Prassi] | a mano |
| Pagine eliminate | 404 o 410 se non c'è sostituto; niente redirect di massa alla home (soft 404) | [Evidenza] ([Google](https://developers.google.com/search/docs/crawling-indexing/http-network-errors)) | a mano |
| Title e description | unici e descrittivi; Google non fissa lunghezze; 30-60 e 70-160 caratteri sono convenzioni degli strumenti | [Evidenza] + [Prassi] ([Google, Title links](https://developers.google.com/search/docs/appearance/title-link)) | `title`, `description` (avviso) |
| Titoli | un H1 visibile coerente con il title, H2 e H3 in ordine; più H1 non sono un problema per Google ma lo sono per accessibilità e lettura | [Evidenza] ([Google, SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)) | `h1`; ordine a mano |
| Link | solo `<a href>`; testo che descrive la destinazione | [Evidenza] ([Google](https://developers.google.com/search/docs/crawling-indexing/links-crawlable)) | a mano |
| Condivisione | `og:title`, `og:description`, `og:image` 1200×630, `og:url`, `twitter:card`: per WhatsApp e social, non per il ranking | [Prassi] | `og` |
| Favicon | quadrata, > 48×48 px, URL stabile | [Evidenza] ([Google](https://developers.google.com/search/docs/appearance/favicon-in-search)) | a mano |

**Dati strutturati 2026 [Prassi su documentazione Google]**: FAQ e HowTo non sono più nella galleria; nessun markup speciale
serve per AI Overviews e AI Mode; le recensioni dell'azienda su se stessa non danno stelline dal 2019
([Google, Search gallery](https://developers.google.com/search/docs/appearance/structured-data/search-gallery); [Google, AI features](https://developers.google.com/search/docs/appearance/ai-features)).
Pacchetto minimo: `Organization` o il sottotipo `LocalBusiness` più specifico (`ProfessionalService`, `HealthAndBeautyBusiness`…)
con nome, URL, logo, indirizzo, telefono, orari, coordinate e `sameAs` verso il profilo Google e i social; `WebSite` sulla
home; `BreadcrumbList` sulle pagine interne; `VideoObject` dove c'è un video; per l'e-commerce `Product` con prezzo,
disponibilità, spedizione e resi coerenti con Merchant Center. Verifica: `jsonld` (si legge, tipi elencati); validazione a
mano con Rich Results Test e Schema Markup Validator.

**Contenuti ed E-E-A-T [Prassi]**: contenuto "non-commodity", cioè **ciò che un modello di IA non potrebbe facilmente creare**
([Google, AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)): Chi siamo con
persone e foto vere, P.IVA e sede nel footer, casi con numeri, recensioni vere, prezzi o fasce, foto del lavoro reale. Una
pagina forte per ogni servizio; pagine località solo per sedi reali o zone servite con contenuto davvero diverso.

**SEO locale [Evidenza + Prassi]**: per Google contano pertinenza, distanza e notorietà ([Google Business Profile Help](https://support.google.com/business/answer/7091));
la categoria primaria del profilo è il primo fattore secondo il sondaggio Whitespark 2026 **[Opinione di esperti]**
([Whitespark](https://whitespark.ca/local-search-ranking-factors/)). Lato sito: nome, indirizzo e telefono in testo nel footer
di ogni pagina, identici al profilo Google; pagina contatti con mappa caricata al clic e indicazioni; `LocalBusiness` con gli
stessi dati; link "Lascia una recensione". Verifica: `tel` (numeri cliccabili), il resto a mano.

**Risposte dell'IA**: per Google GEO e AEO "sono SEO"; non servono llms.txt, copie in Markdown, chunking né markup speciali
**[Evidenza, posizione ufficiale]** ([Search Central Blog, maggio 2026](https://developers.google.com/search/blog/2026/05/a-new-resource-for-optimizing)).
Osservato: solo il 38% delle citazioni negli AI Overviews viene da pagine in top 10 e YouTube è il dominio più citato
([Ahrefs, marzo 2026](https://ahrefs.com/blog/ai-overview-citations-top-10/)): pagine che rispondono a sotto-domande precise
(prezzi, tempi, zone, procedure) e video dei servizi principali **[Prassi]**.

**Redesign senza perdere posizioni [Evidenza]**: mappa vecchio-nuovo per ogni URL, redirect 301/308 senza catene mantenuti
almeno un anno, nuova sitemap, canonical autoreferenziali, link interni aggiornati, "qualche settimana o più" di
fluttuazioni ([Google, Site move](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes)).
Prima: crawl del vecchio, 16 mesi da Search Console, landing organiche da GA4. Al lancio: via `noindex`, redirect testati,
sitemap inviata, conversioni attive. Dopo 2-8 settimane: rapporti Pagine e Prestazioni, 404 da coprire.

## 2. Accessibilità: WCAG 2.2 AA

| Criterio | Regola | Verifica |
|---|---|---|
| 1.4.3 contrasto | testo 4,5:1, testo grande (≥ 24 px o ≥ 18,66 px grassetto) 3:1, senza arrotondamenti | `contrasto` ("a occhio" sopra foto e gradienti) |
| 1.4.11 contrasto non testuale | bordi dei campi, icone funzionali, focus 3:1 | a mano |
| 2.5.8 bersagli | ≥ 24×24 px, o distanziati (cerchio di 24 px che non tocca altri bersagli), esclusi i link nel testo; obiettivo 44 | `bersagli` |
| 1.4.10 reflow | a 320 px nessuno scorrimento orizzontale | `sbordamento` (360, 390, 1440); 320 a mano |
| 3.1.1 lingua | `lang="it"` | `lang` |
| 1.1.1 alternative | alt significativi, `alt=""` per le decorative | `alt` |
| 1.3.1 titoli | H1-H2-H3 reali e in ordine | `h1`; ordine a mano |
| 2.4.11 focus non coperto | il focus non finisce sotto header fissi, banner cookie, chat | a mano (tastiera) |
| 2.4.7 focus visibile | sempre, mai tolto | a mano |
| 2.1.1 tastiera | tutto usabile da tastiera, senza trappole (menu mobile!) | a mano |
| 2.2.2 pausa | ciò che si muove da solo oltre 5 s ha una pausa | a mano |
| 2.3.3 movimento | `prefers-reduced-motion` rispettato | `movimento-ridotto` |
| 2.5.7 trascinamento | ogni trascinamento ha un'alternativa a clic | a mano |
| 3.2.6 aiuto coerente | aiuto e contatti nello stesso ordine su tutte le pagine | a mano |
| 3.3.7 dati ridondanti | non far reinserire dati già dati | a mano |
| 1.2 media | sottotitoli ai video | a mano |

Fonti **[Evidenza, norma]**: [W3C, What's New in WCAG 2.2](https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/);
[WCAG 2.2](https://www.w3.org/TR/WCAG22/). Il WebAIM Million 2026 trova errori rilevabili sul 95,9% delle home più visitate
(contrasto basso nell'83,9%, alt mancanti nel 53,1%) e "l'assenza di errori rilevati non significa che la pagina sia
accessibile" **[Evidenza]** ([WebAIM Million](https://webaim.org/projects/million/)). Processo **[Prassi]**: script
automatici, giro completo con la tastiera (Tab, Maiusc+Tab, Invio, Esc), zoom al 200%, finestra a 320 px, lettore di
schermo (VoiceOver) su home e modulo. Punti critici tipici di Elementor: header fisso e banner che coprono il focus, icone
social e puntini dei caroselli sotto i 24 px, caroselli senza pausa, menu mobile che intrappola il focus, titoli scelti per
stile e non per gerarchia, testo su foto.

**European Accessibility Act**: in Italia D.Lgs. 82/2022, efficace dal 28 giugno 2025; **le microimprese che forniscono
servizi (meno di 10 persone e fatturato o bilancio fino a 2 milioni) sono escluse**; sanzioni 5.000-40.000 €
**[Evidenza, fonti secondarie]** ([PMI.it](https://www.pmi.it/impresa/normativa/503995/european-accessibility-act-accessibilita-continua.html);
[AgID](https://www.agid.gov.it/index.php/it/notizie/european-accessibility-act-eaa-pubblicate-le-linee-guida-agid-sullaccessibilita-dei-servizi)).
Clienti sopra le soglie con e-commerce o prenotazioni online: obbligati. Per tutti, WCAG 2.2 AA è lo standard di qualità.

## 3. Velocità: Core Web Vitals

Soglie "buone": **LCP ≤ 2,5 s, INP ≤ 200 ms, CLS ≤ 0,1** al 75° percentile delle visite reali, mobile e desktop separati;
"scarse" oltre 4 s, 500 ms, 0,25 **[Evidenza]** ([web.dev, Web Vitals](https://web.dev/articles/vitals)). Lighthouse non misura
INP: i dati di laboratorio non sostituiscono quelli reali (CrUX, PageSpeed Insights, Search Console). I Core Web Vitals
entrano nel ranking ma "non garantiscono" le prime posizioni: la velocità si vende per esperienza e conversione
([Google, Page experience](https://developers.google.com/search/docs/appearance/page-experience)).

| Leva | Regola | Verifica |
|---|---|---|
| Immagine LCP | nell'HTML, `fetchpriority="high"`, mai lazy, AVIF/WebP | `lcp-lazy` |
| Dimensioni | `width`/`height` su ogni immagine (CLS) | `dimensioni-img` |
| Font | locali, WOFF2, ≤ 2 famiglie, ≤ 4 file | `font-formato`, `terzi-al-caricamento` |
| Script | niente script sincroni nell'`<head>`; terzi (chat, pixel, widget) dopo consenso e interazione | `terzi-al-caricamento`; a mano |
| Server | TTFB (circa il 40% dell'LCP) ridotto con cache, CDN e meno redirect | a mano (PageSpeed) |
| Peso | HTML, CSS e JS critici sotto 150-200 KB compressi; hero sotto 150-200 KB; pagina sotto 1,5 MB | a mano [Prassi] |

Fonti: [web.dev, Optimize LCP](https://web.dev/articles/optimize-lcp) **[Evidenza]**; [Front-End Checklist](https://github.com/thedaviddias/Front-End-Checklist)
**[Prassi]**. In Elementor **[Prassi]**: contenitori Flexbox, immagine dell'hero come widget e non come sfondo, niente slider
nell'hero, cache del server più CDN, chat, mappe e video caricati solo al clic ([Elementor Help](https://elementor.com/help/what-are-performance-experiments)).

## 4. Privacy e obblighi in Italia

| Regola | Fonte | Verifica |
|---|---|---|
| Al primo accesso solo cookie tecnici; scorrimento non è consenso; cookie wall vietati | [Garante, linee guida cookie 2021](https://www.garanteprivacy.it/home/docweb/-/docweb-display/print/9677876) [Evidenza, norma] | `terzi-al-caricamento` (richieste prima di qualsiasi clic) |
| Banner con **X che chiude rifiutando**, "Accetta tutti", scelte per finalità tutte su "no", pulsanti di **pari dimensione, enfasi e colore**; non riproposto prima di 6 mesi | Garante [Evidenza, norma] | a mano |
| Link "Preferenze cookie" nel footer | Garante | a mano |
| Analytics senza consenso solo con IP mascherato, dati aggregati, nessun incrocio | Garante | a mano |
| Google Ads/GA4: Consent Mode v2 con il default prima di ogni altro comando; in Italia la modalità base (nessun tag prima del consenso) è la più prudente | [Google, Consent mode](https://developers.google.com/tag-platform/security/guides/consent) [Evidenza] | a mano |
| Font, YouTube, Maps: nessuna chiamata a terzi prima del consenso; anteprima statica che carica al clic (migliora anche LCP e INP) | [IHK, Google Fonts](https://www.ihk.de/bergische/recht-und-steuern/wettbewerbsrecht/google-fonts-5646176) [Evidenza] + [Prassi] | `terzi-al-caricamento` |
| **P.IVA nella home** di ogni titolare di partita IVA, anche per un sito solo promozionale; sanzioni 250-2.000 € circa | [Brocardi, art. 35 DPR 633/72](https://www.brocardi.it/testo-unico-iva/titolo-ii/art35.html) [Evidenza, norma] | `piva` |
| Footer: ragione sociale, indirizzo, P.IVA (società: REA e capitale, non verificato), privacy, cookie policy, preferenze cookie, email o PEC | [Prassi] | a mano |
| Modulo: link all'informativa; casella separata e non spuntata solo per marketing | [Prassi] (inferenza dal GDPR) | a mano |
| Chatbot: dire che è un'IA all'apertura (AI Act art. 50, dal 2 agosto 2026); nessun caricamento prima del consenso se usa cookie di terzi | [Goodwin](https://www.goodwinlaw.com/en/insights/publications/2026/08/alerts-technology-dpc-eu-ai-act-transparency-obligations-now-in-force) [Evidenza] | a mano |
| Immagini IA realistiche di persone, sede, lavori del cliente: vietate (vedi `immagini-icone-logo.md`) | AI Act art. 50 | a mano |
| Prezzi: sconto con il prezzo più basso dei 30 giorni precedenti; niente dark pattern (vedi `conversione-e-testi.md`) | [Direttiva 2019/2161](https://eur-lex.europa.eu/eli/dir/2019/2161/oj) | a mano |

## 5. Dove le prove mancano

Non sono stati letti il testo integrale del D.Lgs. 82/2022 né le linee guida AgID 2026 (non è chiaro se richiedano WCAG 2.1
o 2.2), né l'art. 2250 c.c., né pronunce italiane su Google Fonts, YouTube o la modalità avanzata di Consent Mode; il Digital
Fairness Act è una proposta. Mancano dati italiani su recensioni, canali di contatto e conversioni. Non si inventa ciò che
manca: si dice al cliente che è da verificare.
