# Checklist di consegna

Controllo finale prima di mostrare o consegnare. Sintesi del Front-End Checklist (386 regole, [GitHub](https://github.com/thedaviddias/Front-End-Checklist)),
delle web-quality-skills di Addy Osmani (Lighthouse indicativi: Performance ≥ 90, Accessibilità 100 più i controlli manuali,
Best Practices ≥ 95, SEO ≥ 95, [GitHub](https://github.com/addyosmani/web-quality-skills)), di Opquast ([Opquast](https://www.opquast.com/en/certification/web-qa/))
e delle Web Interface Guidelines di Vercel ([Vercel](https://vercel.com/design/guidelines)) **[Prassi]**. Un sito "premium"
non ha una definizione verificabile: in pratica è ciò che un template non fa.

Colonna "Chi lo copre": `slop` = `controllo_slop.py`, `tecnico` = `controllo_tecnico.py`, `estetico` = il controllo degli
otto punti di `SKILL.md`, `a mano` = da guardare.

| # | Area | Controlli con soglia | Chi lo copre |
|---|---|---|---|
| 1 | **Contenuto vero** | nessun testo segnaposto; nessuna testimonianza, cifra o logo inventati; recensioni con nome, data e fonte; link funzionanti; contatti verificati | a mano; `slop` (frasi generiche) |
| 2 | **Struttura** | prima schermata con chi, cosa, per chi, perché tu e una CTA; sezione successiva visibile; ordine scelto per tipo di sito e traffico; niente carosello nell'hero; voce di menu corrente evidenziata | `estetico`; a mano |
| 3 | **Conversione** | CTA con verbo e oggetto; una primaria per vista; modulo di 3-4 campi con etichette visibili; telefono cliccabile e più canali; prezzi o fasce; nessun dark pattern; eventi di contatto tracciati | `tecnico` (`tel`); a mano |
| 4 | **Segnali da IA** | conteggio delle co-occorrenze (`segnali-ia.md`); una sola mossa audace; palette e font motivati dal cliente; icone non predefinite o con etichetta; testi senza i segnali della seconda ondata | `slop`; a mano per i testi |
| 5 | **Qualità estetica** | gli otto punti (punto di vista, tipografia, colori trattenuti, gerarchia, immagini, movimento, telefono progettato, cose invisibili) su computer e telefono; confronto con l'archivio del gusto e con i riferimenti | `estetico` |
| 6 | **Accessibilità WCAG 2.2 AA** | testo 4,5:1, grande 3:1; bordi, icone e focus 3:1; focus visibile e mai coperto; tastiera senza trappole; bersagli ≥ 24 px o distanziati (obiettivo 44); `lang`; titoli in ordine; alt; reflow a 320 px; pausa oltre 5 s; `prefers-reduced-motion` | `tecnico` (`contrasto`, `bersagli`, `sbordamento`, `lang`, `h1`, `alt`, `movimento-ridotto`); a mano il resto |
| 7 | **Prestazioni** | LCP ≤ 2,5 s, INP ≤ 200 ms, CLS ≤ 0,1 al 75° percentile; immagine LCP nell'HTML con `fetchpriority="high"` e senza lazy; AVIF/WebP con `width` e `height`; font locali WOFF2, ≤ 2 famiglie; pagina sotto 1,5 MB; script di terzi rimandati | `tecnico` (`lcp-lazy`, `dimensioni-img`, `font-formato`); PageSpeed a mano |
| 8 | **Telefono** | bersagli 44-48 px; input ≥ 16 px; nessuno scorrimento orizzontale; testo corrente ≥ 16 px; zone sicure; hero in `svh`; prova su iPhone reale in Safari | `tecnico` (`viewport`, `bersagli`, `sbordamento`, `testi-piccoli`); a mano |
| 9 | **SEO e condivisione** | title e description unici; un H1; canonical; sitemap e robots; dati strutturati validati; Open Graph; nome, indirizzo e telefono identici al profilo Google; mappa dei redirect se è un redesign; contenuto leggibile senza JavaScript | `tecnico` (`title`, `description`, `h1`, `canonical`, `jsonld`, `og`, `senza-js`); a mano |
| 10 | **Sicurezza e affidabilità** | HTTPS; header di sicurezza; console senza errori; 404 utile; moduli provati fino alla ricezione dell'email; stati vuoto, errore e caricamento progettati | a mano; errori JS nel rapporto di `slop` |
| 11 | **Legale Italia/UE** | nessun cookie non tecnico né richiesta a terzi prima del consenso; banner con X, pulsanti di pari evidenza, opzioni su "no"; "Preferenze cookie" nel footer; Consent Mode v2 in ordine; P.IVA in home; privacy e cookie policy; chatbot dichiarato come IA; nessuna immagine IA realistica di persone o lavori del cliente | `tecnico` (`terzi-al-caricamento`, `piva`); a mano |
| 12 | **Consegna** | accessi, backup, guida d'uso, elenco di plugin e licenze (font compresi, con i file di licenza), Search Console e GA4 con eventi chiave, kit di marca (logo in varianti, palette, font, preset foto, guida di stile); note per rifare l'anteprima in Elementor | a mano |

Soglie dei punteggi automatici: `controllo_slop.py` ≥ 80 (o segnali rimasti tutti scelti e dichiarati); `controllo_tecnico.py`
0 errori, avvisi letti uno per uno e spiegati nel resoconto. Un punteggio pieno non dice che la pagina è bella: lo dice
solo il controllo estetico.
