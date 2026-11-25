"""Controllo dei segnali di design "fatto con l'IA" su una pagina vera.

Uso: scripts/py.sh controllo_slop.py <url o file.html> --out <cartella> [--soglia 80]

Apre la pagina in Chromium (1440 e 390), la scorre e conta i segnali del catalogo
(references/catalogo-segnali.md). Ogni segnale ha un peso: il punteggio parte da 100
e scende. Scrive controllo.md (da leggere), controllo.json e le schermate.
Il punteggio non è un giudizio estetico: misura quante scelte "di default" restano.
Un segnale scelto di proposito si tiene e si dichiara nella guida di stile (--accetta id1,id2).
"""
import argparse
import json
import os
import sys

from playwright.sync_api import sync_playwright

sys.path.insert(0, os.path.dirname(__file__))
import comune as C  # noqa: E402

# id: (peso, gravità, titolo, cosa fare)
SEGNALI = {
    "etichette-sopra-titoli": (8, "alta", "Etichetta maiuscola spaziata sopra i titoli (eyebrow)",
        "Toglila quasi ovunque: il titolo deve bastare. Al massimo una in pagina, con un'informazione vera (una data, un luogo)."),
    "pillola-hero": (6, "alta", "Pillola o badge sopra il titolo d'apertura",
        "Togli la pillola. Se c'è una notizia vera, scrivila come frase nel sottotitolo."),
    "parola-colorata-h1": (6, "alta", "Una parola del titolo principale in colore o gradiente",
        "Titolo in un solo colore; l'enfasi la dà la frase, non la tinta."),
    "testo-gradiente": (7, "alta", "Testo riempito con un gradiente",
        "Tinta piatta."),
    "griglia-schede-uguali": (7, "alta", "Griglie di schede identiche (stessa misura, stessa struttura)",
        "Lascia che il contenuto decida forma e numero: elenco, tabella, testo lungo, una scheda grande e due piccole, foto."),
    "icona-in-cerchio": (8, "alta", "Icona dentro un cerchio o quadrato colorato sopra/accanto al titolo di una scheda",
        "Niente contenitore colorato: icona nel colore del testo, una foto vera, un numero vero, o nessuna icona."),
    "elenco-spunte": (5, "media", "Elenco con spunte o icone uguali davanti a ogni voce",
        "Elenco semplice, oppure frasi con il dato concreto; la spunta solo in tabelle di confronto vere."),
    "comparsa-scorrimento": (6, "media", "Comparsa dal basso uguale su tutte le sezioni allo scorrimento",
        "Contenuto subito visibile. Il movimento solo dove comunica (un cambio di stato, un'azione)."),
    "solleva-hover": (4, "media", "Schede o pulsanti che si sollevano al passaggio del mouse",
        "Feedback sobrio (colore, sottolineatura) e solo su ciò che è cliccabile."),
    "raggio-uniforme": (5, "media", "Lo stesso arrotondamento su quasi tutti i riquadri",
        "Due o tre valori con un motivo (pulsanti, foto, contenitori), anche angoli vivi dove serve rigore."),
    "bordo-e-ombra": (4, "media", "Bordo sottile e ombra larga sulla stessa scheda",
        "Scegli una sola soluzione per staccare: bordo, ombra o fondo."),
    "vetro": (6, "media", "Effetto vetro: sfocatura dietro o riquadri semitrasparenti con bordo chiaro",
        "Fondo pieno."),
    "aloni-decorativi": (6, "media", "Aloni, macchie sfumate o cerchi decorativi senza contenuto",
        "Togli. Il fondo lo fanno foto vere, colore pieno o tipografia."),
    "gradiente-fondo": (4, "media", "Fondi a gradiente su sezioni grandi",
        "Colore pieno del marchio; un gradiente solo se è del marchio."),
    "numeri-decorativi": (4, "media", "Numeri decorativi 01/02/03 o 'Passo 1'",
        "Ordine dato dai verbi o dal contenuto; numeri solo se la sequenza è il contenuto."),
    "spazi-uniformi": (5, "media", "Tutte le sezioni con lo stesso margine verticale",
        "Ritmo: sezioni dense accanto a sezioni ariose, secondo il contenuto."),
    "struttura-ripetuta": (5, "media", "Sezioni consecutive con la stessa struttura",
        "Ogni sezione con una composizione diversa, scelta per quel contenuto."),
    "tutto-centrato": (3, "bassa", "Molti titoli centrati",
        "Allineamento a sinistra su una griglia; il centrato solo per un momento voluto."),
    "font-default": (5, "media", "Font predefiniti della generazione IA",
        "Font scelto dal marchio o dal settore, con un motivo scritto nella guida di stile."),
    "frasi-generiche": (5, "media", "Frasi e pulsanti generici o da marketing",
        "Frasi con il dato specifico del cliente; pulsanti con verbo e oggetto ('Richiedi la demo')."),
    "trattini-lunghi": (3, "bassa", "Trattini lunghi (—) frequenti nel testo",
        "Punto, virgola o due frasi."),
    "chat-finta": (5, "media", "Interfaccia finta (chat, terminale, finestre con tre pallini)",
        "Schermate vere del prodotto, oppure niente."),
    "zero-foto": (8, "alta", "Nessuna fotografia vera nella pagina",
        "Foto del cliente (sede, persone, lavoro, prodotto); finché mancano, segnalarlo nel report."),
    "piede-quattro-colonne": (2, "bassa", "Piè di pagina a 4 colonne di link standard",
        "Piè di pagina costruito sui contenuti veri: indirizzo, orari, chi risponde."),
    "statistiche-contatore": (4, "media", "Numeri che contano da zero o fila di statistiche",
        "Numeri veri in una frase, con la fonte."),
    # dai segnali di unslop (heydamir/unslop, CC BY 4.0), adattati
    "ombre-colorate": (5, "media", "Ombre o bagliori colorati (glow) intorno a schede, pulsanti o immagini",
        "Ombre neutre, piccole e morbide, oppure nessuna: lo stacco lo danno il fondo e un filetto."),
    "maiuscolo-spaziato": (4, "media", "Molte etichette brevi in maiuscolo con lettere spaziate (non solo sopra i titoli)",
        "Maiuscole normali (prima lettera maiuscola) e spaziatura normale; il maiuscolo solo se è del marchio."),
    "titoli-pesanti": (3, "bassa", "Titoli in grassetto 800-900 senza che lo chieda il marchio",
        "Gerarchia con dimensione e colore, peso 400-600. Se il marchio è davvero pesante (insegna, brochure), accettalo e scrivilo."),
    "esclamativi": (3, "bassa", "Punti esclamativi in titoli, pulsanti ed etichette",
        "Frasi affermative semplici: l'entusiasmo lo danno i fatti, non la punteggiatura."),
    "punto-su-etichette": (2, "bassa", "Punto finale su molti titoli brevi e pulsanti (\"Fatto bene.\", \"Semplice. Veloce.\")",
        "Niente punto su titoli, pulsanti ed etichette; il punto resta nei paragrafi. Se è uno stile scelto (editoriale), accettalo."),
}
# Spaziature senza scala e lettere strette sui testi piccoli NON entrano nel punteggio: provati il 25/11/2026,
# scattano anche su siti fatti da studi (Linear, Stripe) e su siti vecchi fatti a mano. Sono difetti di finitura,
# non segni da IA: compaiono come informazione nella riga "Finitura" di controllo.md.

BANALI = ["scopri di più", "scopri", "inizia ora", "inizia subito", "get started", "learn more", "start now",
          "soluzioni innovative", "a 360 gradi", "all'avanguardia", "su misura per te", "il partner ideale",
          "potenzia", "sblocca", "trasforma il tuo", "porta il tuo business", "eccellenza", "seamless",
          "next level", "cutting-edge", "game changer", "in pochi clic", "tutto ciò di cui hai bisogno",
          "la soluzione completa", "semplice. veloce", "non è solo", "unlock", "supercharge", "empower"]
FONT_DEFAULT = ["inter", "roboto", "open sans", "lato", "montserrat", "poppins", "space grotesk", "geist",
                "instrument serif", "plus jakarta sans", "dm sans", "manrope", "outfit", "sora", "urbanist"]

JS = r"""
(args) => {
  const [BANALI, FONT_DEFAULT] = args;
  const vis = e => { const r = e.getBoundingClientRect(); const s = getComputedStyle(e);
    return r.width > 2 && r.height > 2 && s.visibility !== 'hidden' && s.display !== 'none'; };
  const testo = e => (e.innerText || '').replace(/\s+/g, ' ').trim();
  const dove = e => { let p = []; let x = e; for (let i = 0; i < 3 && x && x !== document.body; i++) {
    let s = x.tagName.toLowerCase(); if (x.id) s += '#' + x.id; else if (x.classList.length) s += '.' + [...x.classList].slice(0, 2).join('.');
    p.unshift(s); x = x.parentElement; } return p.join(' > '); };
  const T = {}; const add = (id, e, nota) => { (T[id] = T[id] || []).push({ dove: e ? dove(e) : '', testo: e ? testo(e).slice(0, 70) : '', nota: nota || '' }); };
  const bg = e => getComputedStyle(e).backgroundColor;
  const pieno = c => c && c !== 'rgba(0, 0, 0, 0)' && c !== 'transparent';
  const tuttiVis = [...document.querySelectorAll('body *')].filter(vis);

  // etichette sopra i titoli: testo corto maiuscolo spaziato subito prima di un h1-h3
  document.querySelectorAll('h1,h2,h3').forEach(h => {
    if (!vis(h)) return; let p = h.previousElementSibling;
    if (!p) { const par = h.parentElement; p = par && par.previousElementSibling; }
    if (!p || !vis(p)) return;
    // un'etichetta sta sopra il titolo: se sta accanto (un bollino, un'icona a sinistra) non è un eyebrow
    const rp = p.getBoundingClientRect(), rh = h.getBoundingClientRect();
    if (rp.bottom > rh.top + 4) return;
    const s = getComputedStyle(p); const t = testo(p);
    const maiusc = s.textTransform === 'uppercase' || (t && t === t.toUpperCase() && /[A-ZÀ-Ü]/.test(t));
    const spaz = parseFloat(s.letterSpacing) > 0.5;
    if (t && t.length < 60 && parseFloat(s.fontSize) <= 17 && (maiusc || spaz)) add('etichette-sopra-titoli', p);
    const r = parseFloat(s.borderTopLeftRadius);
    if (h.tagName === 'H1' && t && t.length < 60 && (pieno(s.backgroundColor) || s.borderTopWidth !== '0px') && r >= 10) add('pillola-hero', p);
  });

  // parola colorata o gradiente nel titolo principale
  document.querySelectorAll('h1,h2').forEach(h => { if (!vis(h)) return; const c = getComputedStyle(h).color;
    h.querySelectorAll('span,em,strong,b,i,mark').forEach(s => { const cs = getComputedStyle(s);
      if (cs.color !== c && testo(s).length > 1) add('parola-colorata-h1', s, h.tagName); }); });
  tuttiVis.forEach(e => { const s = getComputedStyle(e);
    if ((s.webkitBackgroundClip === 'text' || s.backgroundClip === 'text') && s.backgroundImage.includes('gradient')) add('testo-gradiente', e); });

  // griglie di schede uguali e icone in cerchio
  const gruppi = new Set();
  tuttiVis.forEach(p => { const figli = [...p.children].filter(vis); if (figli.length < 3) return;
    if (figli.every(f => f.tagName === 'DETAILS' || f.tagName === 'TR' || f.tagName === 'OPTION')) return;
    const ws = figli.map(f => Math.round(f.getBoundingClientRect().width)); const hs = figli.map(f => Math.round(f.getBoundingClientRect().height));
    const firma = f => [...f.children].map(c => c.tagName).join(',');
    const ugW = ws.every(w => Math.abs(w - ws[0]) <= ws[0] * 0.04 && w > 150 && w < window.innerWidth * 0.5);
    const box = figli.every(f => { const s = getComputedStyle(f); return pieno(s.backgroundColor) || s.borderTopWidth !== '0px' || s.boxShadow !== 'none'; });
    const ugF = figli.every(f => firma(f) === firma(figli[0]));
    // una griglia ha elementi affiancati: un elenco verticale (uno sotto l'altro) non conta
    const tops = figli.map(f => Math.round(f.getBoundingClientRect().top));
    const affiancati = tops.some((t, i) => tops.some((u, j) => i !== j && Math.abs(t - u) <= 4));
    if (ugW && box && ugF && affiancati && !gruppi.has(p)) { gruppi.add(p); add('griglia-schede-uguali', p, figli.length + ' schede da ' + ws[0] + 'px'); }
  });
  let icone = 0; const visti = new Set();
  tuttiVis.forEach(e => { const r = e.getBoundingClientRect(); const s = getComputedStyle(e);
    if (r.width < 28 || r.width > 120 || Math.abs(r.width - r.height) > 6) return;
    const rad = parseFloat(s.borderTopLeftRadius); if (!(pieno(s.backgroundColor) && rad >= r.width * 0.18)) return;
    if (!e.querySelector('svg,img,i,use')) return;
    const sch = e.closest('article,li,a,div'); if (!sch || visti.has(sch.parentElement)) return;
    if (sch.querySelector('h2,h3,h4,strong,b')) { visti.add(sch.parentElement); icone++; if (icone <= 8) add('icona-in-cerchio', e); } });

  // elenchi con spunte
  document.querySelectorAll('ul,ol').forEach(u => { const li = [...u.children].filter(x => x.tagName === 'LI' && vis(x));
    if (li.length >= 3 && li.every(x => x.firstElementChild && /svg|img|i/i.test(x.firstElementChild.tagName))) {
      const forme = new Set(li.map(x => x.firstElementChild.outerHTML.replace(/\s+/g, ' ')));
      if (forme.size <= 2) add('elenco-spunte', u); } });

  // raggi, bordo+ombra, vetro, aloni, gradienti
  const raggi = {}; tuttiVis.forEach(e => { const s = getComputedStyle(e); const r = e.getBoundingClientRect();
    const boxato = pieno(s.backgroundColor) || s.borderTopWidth !== '0px' || s.boxShadow !== 'none' || e.tagName === 'IMG';
    if (boxato && r.width > 60 && r.height > 30) { const v = s.borderTopLeftRadius; if (v !== '0px' && parseFloat(v) < 100) raggi[v] = (raggi[v] || 0) + 1;
      if (s.borderTopWidth !== '0px' && s.boxShadow !== 'none' && parseFloat(s.borderTopWidth) <= 1.5 && r.width > 200) add('bordo-e-ombra', e); }
    if (s.backdropFilter && s.backdropFilter !== 'none') add('vetro', e);
    const m = s.backgroundColor.match(/rgba\((\d+), (\d+), (\d+), ([\d.]+)\)/);
    if (m && parseFloat(m[4]) > 0.03 && parseFloat(m[4]) < 0.25 && s.borderTopWidth !== '0px' && r.width > 120) add('vetro', e, 'fondo semitrasparente');
    if ((s.filter.includes('blur') && r.width > 150) || (parseFloat(s.borderTopLeftRadius) >= r.width * 0.45 && r.width > 140 && !testo(e) && !e.querySelector('img,svg,video'))) add('aloni-decorativi', e);
    if (s.backgroundImage.includes('radial-gradient') && r.width > 300) add('aloni-decorativi', e, 'gradiente radiale');
    if (s.backgroundImage.includes('linear-gradient') && r.width > window.innerWidth * 0.6 && r.height > 200) add('gradiente-fondo', e); });
  // pseudo-elementi ::before/::after usati come aloni o forme
  tuttiVis.forEach(e => { ['::before', '::after'].forEach(ps => { const s = getComputedStyle(e, ps);
    if (s.content === 'none' || s.content === 'normal') return; const w = parseFloat(s.width), h = parseFloat(s.height);
    if (w > 150 && h > 150 && (s.backgroundImage.includes('gradient') || s.filter.includes('blur') || parseFloat(s.borderTopLeftRadius) >= w * 0.45)) add('aloni-decorativi', e, ps); }); });
  const tr = Object.values(raggi).reduce((a, b) => a + b, 0); const top = Object.entries(raggi).sort((a, b) => b[1] - a[1])[0];
  if (tr >= 12 && top && top[1] / tr > 0.6) add('raggio-uniforme', null, top[0] + ' su ' + top[1] + ' riquadri di ' + tr);

  // numeri decorativi
  tuttiVis.forEach(e => { if (e.children.length) return; const t = testo(e);
    if (/^(0\d|passo \d+|step \d+|fase \d+)$/i.test(t)) add('numeri-decorativi', e); });
  document.querySelectorAll('ol,li').forEach(e => { const s = getComputedStyle(e, '::before');
    if (s.content && /counter|"0\d|Passo|Step/i.test(s.content)) add('numeri-decorativi', e, 'contatore CSS'); });

  // sezioni: spazi e strutture
  let sezioni = [...document.querySelectorAll('main > section, body > section, main > div > section, section')].filter(s => vis(s) && s.getBoundingClientRect().height > 250);
  sezioni = sezioni.filter(s => !sezioni.some(o => o !== s && o.contains(s)));
  const padd = sezioni.map(s => Math.round(parseFloat(getComputedStyle(s).paddingTop)));
  if (padd.length >= 5) { const c = {}; padd.forEach(p => c[p] = (c[p] || 0) + 1); const m = Math.max(...Object.values(c));
    if (m / padd.length >= 0.7) add('spazi-uniformi', null, m + ' sezioni su ' + padd.length + ' con lo stesso margine'); }
  const firmaSez = s => { let w = s; for (let k = 0; k < 4; k++) { const g = [...w.children].filter(vis); if (g.length === 1) w = g[0]; else break; }
    const g = [...w.children].filter(vis); if (g.length < 2) return null;
    const sub = g.map(x => { const c = [...x.children].filter(vis); return Math.round(x.getBoundingClientRect().width / 80) + '/' + c.length + (x.querySelector('img,video,picture') ? 'i' : ''); });
    return g.length + ':' + sub.join('-'); };
  for (let i = 1; i < sezioni.length; i++) { const a = firmaSez(sezioni[i]), b = firmaSez(sezioni[i - 1]); if (a && a === b) add('struttura-ripetuta', sezioni[i], 'come la sezione precedente'); }
  const centr = [...document.querySelectorAll('h1,h2')].filter(vis); const nc = centr.filter(h => getComputedStyle(h).textAlign === 'center').length;
  if (centr.length >= 4 && nc / centr.length > 0.6) add('tutto-centrato', null, nc + ' titoli su ' + centr.length);

  // font
  const font = {}; tuttiVis.forEach(e => { if (!testo(e) || e.children.length > 3) return; const f = getComputedStyle(e).fontFamily.split(',')[0].replace(/["']/g, '').trim().toLowerCase(); font[f] = (font[f] || 0) + 1; });
  Object.keys(font).forEach(f => { if (FONT_DEFAULT.some(d => f === d || f.startsWith(d + ' '))) add('font-default', null, f + ' (' + font[f] + ' elementi)'); });

  // testi
  const corpo = testo(document.body).toLowerCase();
  BANALI.forEach(b => { const n = corpo.split(b).length - 1; if (n) add('frasi-generiche', null, '"' + b + '" ×' + n); });
  const trattini = (document.body.innerText.match(/ — |—/g) || []).length; if (trattini >= 3) add('trattini-lunghi', null, trattini + ' trattini lunghi');

  // interfacce finte, foto, piè di pagina, contatori
  tuttiVis.forEach(e => { const c = (e.className && e.className.baseVal === undefined ? e.className : '') + ' ' + (e.id || '');
    if (/\b(chat|terminal|terminale|mockup|fake-ui)\b/i.test(c) && e.getBoundingClientRect().width > 250) add('chat-finta', e); });
  const foto = [...document.images].filter(i => vis(i) && i.naturalWidth >= 400 && !/logo|icon|icona/i.test(i.src + i.alt + i.className));
  if (foto.length === 0) add('zero-foto', null, 'nessuna immagine ≥ 400 px oltre a logo e icone');
  const piede = document.querySelector('footer'); if (piede) { const colonne = [...piede.querySelectorAll('ul')].filter(vis).length; if (colonne >= 3) add('piede-quattro-colonne', piede, colonne + ' colonne di link'); }
  document.querySelectorAll('[data-count],[data-counter],[data-m-count],.counter,.count-up').forEach(e => add('statistiche-contatore', e));

  // ombre e bagliori colorati: colore dell'ombra saturo e sfocatura ampia
  const saturo = c => { const m = c.match(/rgba?\((\d+),\s*(\d+),\s*(\d+)(?:,\s*([\d.]+))?\)/); if (!m) return false;
    const [r, g, b] = [+m[1], +m[2], +m[3]]; const a = m[4] === undefined ? 1 : +m[4];
    return a >= 0.12 && Math.max(r, g, b) - Math.min(r, g, b) >= 60; };
  tuttiVis.forEach(e => { const s = getComputedStyle(e); const sh = s.boxShadow + ' ' + (s.filter.includes('drop-shadow') ? s.filter : '');
    if (sh.includes('none') && !s.filter.includes('drop-shadow')) return;
    const pezzi = sh.split(/,(?![^(]*\))/);
    if (pezzi.some(p => { const col = (p.match(/rgba?\([^)]*\)/) || [])[0]; const px = (p.replace(/rgba?\([^)]*\)/, '').match(/-?[\d.]+px/g) || []).map(parseFloat);
      return col && saturo(col) && (px[2] || 0) >= 10 && !p.includes('inset'); })) add('ombre-colorate', e); });

  // etichette brevi in maiuscolo spaziato in tutta la pagina (menu ed etichette sopra i titoli esclusi)
  const giaEyebrow = new Set((T['etichette-sopra-titoli'] || []).map(x => x.dove + x.testo));
  let maiusc = 0; tuttiVis.forEach(e => { if (e.children.length > 1 || e.closest('nav') || giaEyebrow.has(dove(e) + testo(e).slice(0, 70))) return; const t = testo(e); const s = getComputedStyle(e);
    if (t && t.length >= 3 && t.length < 40 && s.textTransform === 'uppercase' && parseFloat(s.letterSpacing) >= 1 && parseFloat(s.fontSize) <= 15) {
      maiusc++; if (maiusc <= 6) add('maiuscolo-spaziato', e); } });
  if (maiusc > 0 && maiusc < 4) delete T['maiuscolo-spaziato'];

  // scala degli spazi: valori interi diversi di padding e gap su contenitori e riquadri
  const spazi = {}; tuttiVis.forEach(e => { const r = e.getBoundingClientRect(); if (r.width < 40 || r.height < 20) return; const s = getComputedStyle(e);
    [s.paddingTop, s.paddingBottom, s.paddingLeft, s.paddingRight, s.rowGap, s.columnGap].forEach(v => { const n = parseFloat(v);
      if (n > 2 && n < 200 && Math.abs(n - Math.round(n)) < 0.01) spazi[n] = (spazi[n] || 0) + 1; }); });
  const valori = Object.keys(spazi).map(Number); const strani = valori.filter(n => n >= 5 && n % 2 && n % 5).sort((a, b) => a - b);

  // titoli pesanti e lettere strette sui testi piccoli
  const pes = [...document.querySelectorAll('h1,h2,h3')].filter(vis).filter(h => parseInt(getComputedStyle(h).fontWeight) >= 800);
  if (pes.length >= 2) add('titoli-pesanti', pes[0], pes.length + ' titoli a ' + getComputedStyle(pes[0]).fontWeight);
  let strette = 0; tuttiVis.forEach(e => { if (e.children.length || testo(e).length < 4) return; const s = getComputedStyle(e);
    if (parseFloat(s.fontSize) < 16 && parseFloat(s.letterSpacing) < -0.1) strette++; });

  // punteggiatura: esclamativi e punti su titoli brevi e pulsanti
  const corti = [...document.querySelectorAll('h1,h2,h3,h4,button,a,label,strong,figcaption')].filter(vis).filter(e => { const t = testo(e); return t && t.length < 120; });
  const escl = corti.filter(e => testo(e).includes('!')); if (escl.length >= 2) escl.slice(0, 5).forEach(e => add('esclamativi', e));
  const conPunto = [...document.querySelectorAll('h1,h2,h3,button,a[class*=btn],a[class*=button],.button')].filter(vis)
    .filter(e => { const t = testo(e); return t.length > 2 && t.length < 70 && /[^.]\.$/.test(t); });
  if (conPunto.length >= 3) conPunto.slice(0, 5).forEach(e => add('punto-su-etichette', e));
  const finitura = { spazi_diversi: valori.length, spazi_strani: strani.slice(0, 10), lettere_strette_piccoli: strette };
  return { T, n_sezioni: sezioni.length, font, foto: foto.length, finitura };
}
"""

JS_NASCOSTI = r"""
() => { const out = []; document.querySelectorAll('section *, main *').forEach(e => { const r = e.getBoundingClientRect();
  if (r.top > innerHeight * 1.2 && r.width > 100 && r.height > 40) { const s = getComputedStyle(e);
    if (parseFloat(s.opacity) < 0.2 || (s.transform !== 'none' && s.transform.includes('matrix') && parseFloat(s.opacity) < 1)) out.push(e); } });
  return out.length; }
"""

JS_HOVER = r"""
() => { let n = 0; const sel = []; for (const sh of document.styleSheets) { let rules; try { rules = sh.cssRules; } catch (e) { continue; }
  const giro = rs => { for (const r of rs) { if (r.cssRules && !r.selectorText) giro(r.cssRules);
    if (r.selectorText && r.selectorText.includes(':hover') && r.style && /translate|scale/.test(r.style.transform || '')) { n++; sel.push(r.selectorText.slice(0, 80)); } } };
  giro(rules); } return { n, sel: sel.slice(0, 6) }; }
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pagina")
    ap.add_argument("--out", required=True)
    ap.add_argument("--accetta", default="", help="id di segnali scelti di proposito, separati da virgola")
    ap.add_argument("--soglia", type=int, default=80)
    a = ap.parse_args()
    url = C.url_da_argomento(a.pagina)
    out = os.path.abspath(os.path.expanduser(a.out))
    os.makedirs(out, exist_ok=True)
    accettati = {x.strip() for x in a.accetta.split(",") if x.strip()}

    with sync_playwright() as p:
        b = p.chromium.launch(headless=True)
        ctx, pg, errori = C.apri(b, url, attesa=1500)
        nascosti = pg.evaluate(JS_NASCOSTI)  # prima di scorrere: cosa aspetta di comparire
        hover = pg.evaluate(JS_HOVER)
        C.scorri_tutta(pg)
        r = pg.evaluate(JS, [C_BANALI(), FONT_DEFAULT])
        intera = C.schermata_intera(pg, os.path.join(out, "computer-intera.png"))
        C.tagli(intera, os.path.join(out, "computer"))
        tecnici = pg.evaluate("""() => ({ sborda: document.documentElement.scrollWidth - innerWidth, h1: document.querySelectorAll('h1').length,
            piccoli: [...document.querySelectorAll('p,li,a,span,small,label,dd,dt,td')].filter(e => e.offsetParent && e.innerText && e.innerText.trim() && parseFloat(getComputedStyle(e).fontSize) < 15).length })""")
        ctx.close()
        ctx, pm, err_m = C.apri(b, url, 390, 844, mobile=True, attesa=1200)
        C.scorri_tutta(pm)
        mob = C.schermata_intera(pm, os.path.join(out, "telefono-intera.png"))
        C.tagli(mob, os.path.join(out, "telefono"), altezza_taglio=2600, larghezza_max=420)
        sborda_m = pm.evaluate("document.documentElement.scrollWidth - innerWidth")
        ctx.close()
        b.close()

    T = r["T"]
    if nascosti >= 3:
        T.setdefault("comparsa-scorrimento", []).append({"dove": "", "testo": "", "nota": f"{nascosti} elementi invisibili finché non si scorre"})
    if hover["n"] >= 2:
        T.setdefault("solleva-hover", []).append({"dove": "", "testo": "", "nota": f"{hover['n']} regole: " + "; ".join(hover["sel"][:3])})

    righe, punteggio, trovati = [], 100, []
    for sid, (peso, grav, titolo, rimedio) in SEGNALI.items():
        occ = T.get(sid, [])
        if not occ:
            continue
        # le etichette e le parole colorate pesano di più quando sono tante
        molt = 1.0
        if sid in ("etichette-sopra-titoli", "griglia-schede-uguali", "struttura-ripetuta") and len(occ) >= 3:
            molt = 1.5
        if sid == "etichette-sopra-titoli" and len(occ) == 1:
            molt = 0.3
        sottratti = 0 if sid in accettati else round(peso * molt)
        punteggio -= sottratti
        trovati.append({"id": sid, "gravita": grav, "titolo": titolo, "occorrenze": len(occ), "punti": sottratti,
                        "rimedio": rimedio, "esempi": occ[:5], "accettato": sid in accettati})
    punteggio = max(0, punteggio)
    trovati.sort(key=lambda x: -x["punti"])

    esito = "SUPERATO" if punteggio >= a.soglia else "DA RIVEDERE"
    righe = [f"# Controllo segnali IA: {a.pagina}", "",
             f"**Punteggio: {punteggio}/100 · {esito}** (soglia {a.soglia}). 100 = nessun segnale di default rilevato.", "",
             f"Sezioni: {r['n_sezioni']} · foto vere ≥ 400 px: {r['foto']} · font: {', '.join(list(r['font'])[:5])}",
             f"Tecnico: sborda di {tecnici['sborda']}px su computer e {sborda_m}px su telefono · H1: {tecnici['h1']} · testi sotto 15 px: {tecnici['piccoli']} · errori JS: {len(errori) + len(err_m)}",
             f"Finitura (non nel punteggio): {r['finitura']['spazi_diversi']} valori di spaziatura diversi"
             + (f", valori dispari strani: {', '.join(str(x) for x in r['finitura']['spazi_strani'])} px" if r['finitura']['spazi_strani'] else "")
             + f" · testi sotto 16 px con lettere strette: {r['finitura']['lettere_strette_piccoli']}."
             " Meglio una scala di passi (multipli di 4 o 8) e spaziatura 0 sui testi piccoli.", ""]
    if not trovati:
        righe.append("Nessun segnale rilevato. Guardare comunque le schermate: lo script non vede tutto.")
    for t in trovati:
        stato = " (accettato, scelto di proposito)" if t["accettato"] else ""
        righe += [f"## {t['titolo']}{stato}", f"*{t['gravita']} · {t['occorrenze']} volte · −{t['punti']}* · id `{t['id']}`", "",
                  f"**Cosa fare:** {t['rimedio']}", ""]
        for e in t["esempi"]:
            pezzi = [x for x in (e.get("dove"), e.get("testo") and f"\"{e['testo']}\"", e.get("nota")) if x]
            righe.append("- " + " · ".join(pezzi))
        righe.append("")
    righe += ["---", "Limiti: lo script misura forme e ripetizioni, non il gusto. Un segnale scelto con un motivo si tiene:",
              "passarlo con --accetta e scrivere il motivo nella guida di stile. Rileggere sempre le schermate (computer-NN.jpg, telefono-NN.jpg)."]
    with open(os.path.join(out, "controllo.md"), "w") as f:
        f.write("\n".join(righe))
    C.scrivi_json(os.path.join(out, "controllo.json"), {"pagina": a.pagina, "punteggio": punteggio, "esito": esito,
                                                         "segnali": trovati, "tecnico": tecnici, "sborda_telefono": sborda_m,
                                                         "finitura": r["finitura"]})
    print(f"{punteggio}/100 {esito} · {len(trovati)} tipi di segnale · {out}/controllo.md")


def C_BANALI():
    return BANALI


if __name__ == "__main__":
    main()
