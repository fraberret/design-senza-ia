---
name: design-senza-ia
description: >-
  Progetta siti belli e specifici per il cliente, che non sembrano fatti con l'IA e sono corretti per SEO, accessibilità,
  velocità e leggi italiane: home, landing page, siti vetrina e istituzionali, siti di servizio, e-commerce, siti
  esperienziali per agenzie, restyling, anteprime HTML, grafiche e loghi su richiesta. Dal brief (tipo di sito, obiettivo,
  livello di esperienza sobrio, immersivo o esperienziale) all'analisi del sito e dei concorrenti, ai riferimenti, a tre
  direzioni, alla costruzione e a tre controlli con script (segnali da IA, qualità estetica, tecnico e legale). Non è legato
  alla piattaforma: dice cosa si rifà in Elementor e cosa solo in codice. Usala ogni volta che l'utente dà
  l'URL di un sito da rifare, chiede un sito, una home, una landing, un e-commerce, un'anteprima, un restyling, un logo o
  una grafica per un cliente, dice che un design "sembra fatto con l'IA", "è generico", "è un template", "è brutto", o
  chiede di analizzare concorrenti o riferimenti, anche se non nomina questa skill.
---

# Design dei siti senza aspetto da IA

Un sito eccellente non si riconosce dallo stile alla moda: dice subito chi sei, cosa fai, per chi e perché tu; ordina le
sezioni in base a quanto il visitatore sa già; mostra prove vere; ha un sistema visivo piccolo e motivato dal cliente; ha
**un momento visivo forte** che si ricorda; rispetta soglie tecniche misurate. Il look "fatto con l'IA" è la somma di scelte
predefinite non decise: la cura non è una lista di divieti (vietato un segnale, il modello passa al successivo) ma **partire
dal materiale vero del cliente, decidere ogni scelta con un motivo e misurare**. Togliere i difetti non basta: una pagina che
passa tutti i controlli ma è anonima ha fallito.

Lavora in modo autonomo dall'URL al risultato verificato; chiedi solo ciò che solo l'utente o il cliente sanno.

## Strumenti

```bash
S=~/.claude/skills/design-senza-ia/scripts
$S/py.sh analizza_sito.py <url> --out <cartella>/analisi [--pagine 6]
$S/py.sh cattura_concorrenti.py <url1> <url2> ... --out <cartella>/analisi [--etichetta concorrenti|riferimenti]
$S/py.sh cattura_scorrimento.py <url> --out <cartella>/riferimenti/<sito> [--fotogrammi 12] [--webgpu]
$S/py.sh controllo_slop.py <url o file.html> --out <cartella>/controllo-vN [--accetta id1,id2] [--soglia 80]
$S/py.sh controllo_tecnico.py <url o file.html> --out <cartella>/tecnico-vN
```

Browser invisibile, uno script alla volta (1-5 minuti ciascuno): in primo piano con un timeout lungo, o in background. Una
pagina con moduli JavaScript si serve da un server locale (`python3 -m http.server`). Test degli script:
`$S/py.sh tests/test_<nome>.py`.

## Le fasi

**1. Contesto.** Se nella cartella della skill c'è `locale.md`, leggilo per primo: convenzioni dell'utente (cartelle,
guida di stile, strumenti) che valgono più di questo file. Se c'è `locale/gusto.md` (archivio del gusto: riferimenti
approvati, tratti comuni, bocciature con la causa), leggilo e guarda le catture. Leggi la guida di stile del cliente se
esiste.

**2. Brief.** Scrivi in poche righe i campi di `references/tipi-di-sito-e-sezioni.md` §1: cliente, pubblico, **tipo di
sito**, obiettivo e CTA principale, traffico e consapevolezza, **livello di esperienza con il motivo**, piattaforma e limiti,
materiale vero. Quello che manca e solo il cliente sa, chiedilo.

**3. Analisi.** `analizza_sito.py` sul sito attuale (leggi `analisi.md`, guarda le schermate); `controllo_slop.py` e
`controllo_tecnico.py` anche sul sito vecchio (argomenti per la proposta); 4-8 concorrenti con `cattura_concorrenti.py`
(`references/concorrenti-e-strumenti.md`); inventario del materiale vero e "quanto cambiare"
(`references/direzione-e-costruzione.md` §1-2). Scrivi la sintesi: media del settore, il migliore e perché, spazio libero.

**4. Riferimenti.** L'archivio del gusto, poi 6-10 riferimenti da gallerie e dai migliori del settore
(`references/ispirazione.md`), scelti per tipo di sito e livello. Per ognuno: cosa si prende e cosa si lascia, mai la
pagina intera. Per i siti con movimento, `cattura_scorrimento.py`. Annota i tratti comuni.

**5. Direzione.** Tre direzioni diverse, ognuna in cinque righe (attività, carattere, mondo, momenti, firma:
`references/direzione-e-costruzione.md` §3) più il piccolo sistema (`references/sistema-visivo.md` §1): 4-6 colori con nome
e ruolo, 1-2 caratteri non predefiniti con il motivo, scala, raggi, movimento per il livello, **una sola mossa audace**, il
momento visivo forte dell'apertura, i riferimenti usati. Verifica: "con un altro cliente dello stesso settore arriverei allo
stesso piano?"; se sì, cambia. Mostra le tre direzioni con la tua raccomandazione e aspetta la scelta, salvo piena
autonomia. Registra la direzione scelta nella guida di stile prima di scrivere codice.

**6. Struttura e testi.** Ordine delle sezioni dal tipo di sito e dal traffico, prima schermata, navigazione
(`references/tipi-di-sito-e-sezioni.md`); testi con i fatti del cliente, CTA con verbo e oggetto, prove vere, moduli corti,
niente segnali di testo della seconda ondata (`references/conversione-e-testi.md`). Scrivi prima la pagina come testo, poi
scegli la forma di ogni sezione.

**7. Asset.** Foto vere prima di tutto; immagini generate solo per momenti senza foto, mai realistiche su persone, sede,
lavori o prodotti del cliente; icone disegnate o ridisegnate su una griglia comune; elementi grafici dalla firma; logo solo
su richiesta, con il suo processo (`references/immagini-icone-logo.md`).

**8. Costruzione.** Anteprima HTML in un file nuovo per versione (`<cliente>-home-vN.html`; le precedenti restano), con le
regole di `references/sistema-visivo.md` e `references/movimento-e-telefono.md` (movimento secondo il livello, telefono
progettato a parte) e SEO, accessibilità, velocità e privacy dentro dal primo file
(`references/seo-accessibilita-velocita-legale.md`): font locali WOFF2, video e mappe al clic, `lang`, un H1, meta, JSON-LD,
`prefers-reduced-motion`.

**9. Tre controlli, prima di mostrare qualsiasi cosa.**
1. **Segnali da IA**: `controllo_slop.py`, punteggio ≥ 80 e più alto dei concorrenti, e nessun "aspetto da IA" nella riga
   delle co-occorrenze per gruppo; i segnali scelti di proposito vanno in
   `--accetta` con il motivo nella guida di stile (`references/segnali-ia.md`; il gusto del committente e le scelte motivate
   vincono sul conteggio). Rileggi i testi contro la seconda ondata.
2. **Qualità estetica**: guarda le schermate su computer e telefono e giudica gli **otto punti**:
   - *punto di vista*: si riconosce una direzione; prova dello scambio di nome (con il nome di un concorrente reggerebbe?);
   - *tipografia*: caratteri con carattere, salti di scala netti, misura 45-75 caratteri, niente di predefinito;
   - *colori trattenuti*: pochi colori usati in grande; niente arcobaleno, niente pagina grigia con un accento minuscolo;
   - *gerarchia*: test della sfocatura, al massimo 3 livelli e 2 elementi grandi per schermata, non tutto con lo stesso peso;
   - *immagini*: vere, grandi, con un momento visivo forte in apertura;
   - *movimento*: quello del livello scelto, un momento curato, nulla che distrae;
   - *telefono*: composizione propria, CTA nel pollice, niente di rimpicciolito;
   - *cose invisibili*: stati (hover, focus, errore, invio), microcopy, alt, 404, prestazioni.
   Poi confronta con l'archivio del gusto e con i riferimenti scelti: se a colpo d'occhio la pagina è più debole, torna
   alla fase 5. Un punteggio pieno non dice che la pagina è bella.
3. **Tecnico e legale**: `controllo_tecnico.py` con 0 errori; gli avvisi letti uno per uno; i controlli "a mano" di
   `references/checklist-consegna.md` (tastiera, focus coperto, banner cookie, P.IVA, contrasti "a occhio" sopra le foto).

**10. Resoconto e consegna.** In italiano semplice: dove si apre e come; brief, direzione e motivo in due righe; punteggi
(slop contro sito vecchio e concorrenti, tecnico); cosa hai controllato e corretto; cosa manca dal cliente e ogni segnaposto
usato; **cosa si rifà in Elementor** (vedi sotto). Dopo il giudizio dell'utente, registralo nella guida di stile e, se esiste,
in `locale/gusto.md`.

## I livelli di esperienza

| Livello | Per chi | Movimento | Piattaforma |
|---|---|---|---|
| Sobrio e curato | studi, professionisti, attività locali | apertura forte ferma; hover e pressione; al massimo un momento leggero; titolo mai animato | Elementor o codice |
| Immersivo | marchi con una storia, prodotti, e-commerce curati | in più un momento di scorrimento in una sezione sua | codice o Elementor con poco codice |
| Esperienziale | agenzie, studi creativi, campagne | storie allo scorrimento, oggetti e testi in movimento, transizioni | codice |

Il livello dipende dal cliente, mai da chi progetta; sempre con `prefers-reduced-motion` (`references/movimento-e-telefono.md`).

## Rifare l'anteprima in Elementor

Nel resoconto, per ogni parte della pagina, una di tre etichette **[Prassi; nomi delle funzioni 2026 non verificati]**:
- **Nativo**: contenitori Flexbox, colori e caratteri globali, caratteri caricati in locale (Custom Fonts), header fisso,
  hover, moduli semplici, immagine dell'hero come widget (non come sfondo), video al clic.
- **Poco codice**: CSS personalizzato per elemento, un momento leggero (frase che si accende, foto che si sviluppa) in un
  widget HTML, `prefers-reduced-motion`, JSON-LD, anteprime statiche di mappe e video.
- **Solo codice**: momenti legati alla barra di scorrimento con GSAP, sezioni fissate a capitoli, transizioni di pagina,
  3D e WebGL, tutto il livello esperienziale.
Evita le animazioni d'ingresso di Elementor su ogni sezione: sono il segnale `comparsa-scorrimento`.

## Quando chiedere

Solo ciò che solo l'utente o il cliente sanno: la cartella di lavoro se non è ovvia; i campi del brief che non si trovano;
la scelta tra le tre direzioni (salvo piena autonomia); il livello di esperienza se non è chiaro dal cliente; il permesso
prima di generare immagini a pagamento; **un riferimento visivo dopo due bocciature** della stessa parte (non una terza
prova alla cieca); il logo, solo se lo chiede l'utente. Tutto il resto (analisi, ricerche, riferimenti, controlli) da sola.

## Regole fisse

- Niente dati inventati: numeri, recensioni, persone, date, loghi di clienti. I contatti veri del cliente si usano così come
  sono. Una persona in foto non si presenta come il cliente senza conferma.
- Nessuna immagine IA realistica di persone, sede, lavori o prodotti del cliente (AI Act art. 50).
- Nessuna richiesta a terzi (font, YouTube, mappe, analisi) prima del consenso; P.IVA in home; niente dark pattern.
- Contrasti calcolati (testo 4,5:1, grande 3:1, bordi e focus 3:1) e controllo a larghezza di telefono prima di mostrare.
- Animazioni d'interfaccia mai oltre 500 ms; `prefers-reduced-motion` sempre; contenuto leggibile senza JavaScript.
- Ogni versione in un file nuovo; il giudizio dell'utente si registra nella guida di stile.
