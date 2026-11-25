# Segnali "fatto con l'IA"

Adattato e ampliato da *Signs of AI design* (github.com/febbhav/signs-of-ai-design, licenza CC BY-SA 4.0) e dalle guide di
Anthropic ("Improving frontend design through Skills"), Sailop, 925 Studios, Noqode, TeneX, Build to Launch, Rottoways,
Regards, Blusteak (ricerca del 24/11/2026). Integrato il 25/11/2026 con alcuni segnali di *unslop* di Damir Sokolovsky
(github.com/heydamir/unslop, CC BY 4.0). Aggiornato il 25/11/2026 con la seconda ondata elencata dalla skill
`frontend-design` di Anthropic (Apache 2.0), la ricerca "Sito web eccellente dalla A alla Z" e alcuni divieti di TasteSkill
2.5.1 (MIT). Questo file resta sotto CC BY-SA 4.0.

**Il principio.** I segnali pesano **in combinazione**: un'etichetta sopra un titolo da sola non è un problema; etichetta +
schede identiche + icone in cerchi + comparse allo scorrimento + gradiente sì ([Sitepeel](https://sitepeel.dev/free-tools/ai-slop-checker/))
**[Opinione convergente]**. Il controllo conta le co-occorrenze, non vieta un elemento. E **vincono il gusto del committente
(l'archivio del gusto, se esiste) e le scelte motivate**: un segnale scelto per un motivo legato al cliente e scritto nella
guida di stile si accetta (`controllo_slop.py --accetta`). Una lista nera da sola non basta: ogni default di buon gusto
diventa il segnale successivo.

**Come leggerlo.** Nessun segnale è vietato da solo: quasi tutti sono nati da designer umani. Il "look da IA" è la somma di
tante scelte predefinite, non decise, tutte insieme. Un segnale è grave quando arriva col modello e non ha un motivo legato
al cliente. Tra parentesi l'id usato da `controllo_slop.py` (dove c'è).

## Indice
1. Struttura della pagina · 2. Apertura (hero) · 3. Schede e superfici · 4. Colore · 5. Tipografia · 6. Icone e immagini ·
7. Movimento · 8. Contenuti e testi · 9. Fiducia, prezzi, piè di pagina · 10. Seconda ondata · 11. Co-occorrenze ·
12. Perché succede

## 1. Struttura della pagina
- **Ordine fisso**: apertura, fascia loghi, tre schede, recensioni, numeri, prezzi, domande, fascia finale, piè di pagina. È anche
  la scaletta umana standard: il segnale è zero deviazioni. *Al suo posto:* l'ordine lo decide la storia del cliente (cosa
  vende, a chi, perché fidarsi, come si comincia); sezioni tolte se non c'è materiale vero.
- **Sezioni con la stessa struttura una dopo l'altra** (`struttura-ripetuta`): titolo, frase, griglia; titolo, frase, griglia.
  *Al suo posto:* composizioni diverse per contenuti diversi (elenco, tabella, testo lungo, foto grande, citazione).
- **Spazi tutti uguali** (`spazi-uniformi`): stesso margine in ogni sezione, sei schermate per poche parole. *Al suo posto:*
  ritmo; parti dense (tabelle, elenchi, orari) accanto a parti ariose.
- **Tutto centrato** (`tutto-centrato`). *Al suo posto:* griglia allineata a sinistra; il centrato è un momento.
- **Etichetta maiuscola spaziata sopra ogni titolo** (`etichette-sopra-titoli`, "eyebrow", "kicker"): il segnale più
  riconoscibile del 2025-26. *Al suo posto:* nessuna; il titolo deve bastare. Al massimo una, con un dato vero.
- **Numeri 01/02/03, "Passo 1"** (`numeri-decorativi`). *Al suo posto:* verbi ("Ci chiami", "Ti mostriamo", "Installiamo")
  o nessun numero; numeri solo se l'ordine è il contenuto.

## 2. Apertura (hero)
- **La formula**: pillola o etichetta, titolo enorme centrato, sottotitolo grigio di una riga, pulsante pieno + pulsante vuoto,
  alone sfumato dietro (`pillola-hero`, `aloni-decorativi`). *Al suo posto:* la cosa vera (foto del luogo/persone/prodotto,
  schermata reale, video vero, un dato utile) e un titolo che dice cosa si fa e per chi.
- **Una parola del titolo colorata o in gradiente** (`parola-colorata-h1`, `testo-gradiente`). *Al suo posto:* un colore.
- **Titolo serif corsivo enorme** (Instrument Serif, Playfair) su un'azienda che non è editoriale.
- **Finestra finta di terminale o chat con tre pallini** come immagine (`chat-finta`).

## 3. Schede e superfici
- **Tre (o sei) schede identiche** con icona in alto, titolino, due righe (`griglia-schede-uguali`). *Al suo posto:* il numero
  e la forma li decide il contenuto: un elenco con descrizioni, una tabella, una scheda grande e due piccole, una foto per voce.
- **Griglia bento**: nata per sfuggire alle tre schede, ormai è lo stesso riflesso.
- **Icona in un cerchio o quadrato colorato** sopra il titolo della scheda (`icona-in-cerchio`). *Al suo posto:* icona nel
  colore del testo e più piccola, foto, numero vero, oppure niente.
- **Stesso arrotondamento ovunque** (`raggio-uniforme`, "rounded-2xl"). *Al suo posto:* due o tre valori con un motivo, anche
  angoli vivi.
- **Bordo sottile + ombra larga sulla stessa scheda** (`bordo-e-ombra`). *Al suo posto:* una sola soluzione.
- **Schede dentro schede**, tutto incorniciato. *Al suo posto:* gerarchia con spazio, filetti, dimensione del testo.
- **Vetro** (`vetro`): sfocature e riquadri semitrasparenti con bordo chiaro dove non c'è niente sotto da far vedere.
- **Striscia colorata a sinistra** su schede normali (è roba da avvisi).
- **Ombre e bagliori colorati** (`ombre-colorate`): alone viola o del colore del marchio intorno a pulsanti, schede, emoji.
  *Al suo posto:* ombre neutre, piccole e morbide; lo stacco lo danno il fondo e un filetto sottile.
- **Tutto a pillola**: ricerca, pulsanti, schede, etichette, tutti arrotondati al massimo. *Al suo posto:* raggio in base
  alla misura, con i raggi annidati (interno = esterno meno lo spazio tra i due).

## 4. Colore
- **Gradiente viola/indaco** (Tailwind indigo-500 #6366F1, violet-500 #8B5CF6), bottoni e titoli in gradiente.
- **Seconda ondata**: fondo crema/pesca con accento arancione o ambra, oppure verde smeraldo (#10B981) quando il viola è vietato.
- **Neon su quasi nero con ombre colorate** (stile "Linear" copiato).
- **Gradienti di fondo grandi** (`gradiente-fondo`), **aloni radiali** (`aloni-decorativi`).
- **Tavolozza timida**: quattro colori spenti tutti con lo stesso peso. *Al suo posto:* colori del marchio o del luogo, uno
  dominante e un accento netto, usati pieni.
- **Tutto evidenziato**: accento su ogni titolo, icona, bordo e pulsante, così niente spicca. *Al suo posto:* l'accento sulle
  poche cose che contano (l'azione principale, un dato, la selezione); il colore ricco nei "momenti" della direzione
  (uno o due), il resto tranquillo.
- **Cinque sfumature quasi uguali** dello stesso colore per i testi. *Al suo posto:* tre ruoli di testo (principale,
  secondario, attenuato) da una sola scala di neutri.

## 5. Tipografia
- **Font predefiniti** (`font-default`): Inter, Roboto, Open Sans, Lato, Montserrat, Poppins, Space Grotesk, Geist, DM Sans,
  Plus Jakarta Sans, Manrope, Outfit, Sora, Urbanist, Instrument Serif. Il problema non è il font: è il font non scelto.
  *Al suo posto:* font derivato dal marchio (il logo, l'insegna, la brochure, il periodo dell'azienda) o dal settore, con il
  motivo scritto.
- **Una famiglia, un peso, gradini troppo vicini**: gerarchia piatta. *Al suo posto:* scala con salti netti.
- **Monospace per "fare tecnologico"** su chi non fa software per sviluppatori.
- **Titoli in grassetto 800-900** (`titoli-pesanti`) senza che lo chieda il marchio. *Al suo posto:* gerarchia con
  dimensione e colore. Un marchio davvero pesante (insegna, brochure in condensato nero) è un motivo: si accetta.
- **Etichette brevi in maiuscolo spaziato** sparse in pagina (`maiuscolo-spaziato`), oltre a quelle sopra i titoli.
  *Al suo posto:* maiuscola solo all'inizio, spaziatura normale.
- **Lettere strette sui testi piccoli** e **numeri in formati diversi** (`1250€` accanto a `€ 1.250,00`): difetti di
  finitura, non segni da IA (li fanno anche ottimi studi). Il controllo li riporta nella riga "Finitura", fuori dal
  punteggio. *Al suo posto:* spaziatura 0 sotto i 16 px, un formato solo per i numeri.

## 6. Icone e immagini
- **Le solite icone sottili** (Lucide: scintille per l'IA, fulmine per "veloce", scudo per "sicuro", spunta, freccia su ogni
  pulsante). **Emoji come icone.**
- **Elenco con spunte uguali** davanti a ogni voce (`elenco-spunte`).
- **Nessuna foto vera** (`zero-foto`): solo icone, forme, illustrazioni 3D lisce, ritratti generati, stock da ufficio perfetto.
  *Al suo posto:* foto del cliente; finché mancano, poche foto sostitutive dello stesso fotografo e una lista di scatti da fare.
- **Cerchi concentrici, macchie, forme decorative** senza contenuto (`aloni-decorativi`).
- **Robot, cervelli luminosi, circuiti, ologrammi** per tutto ciò che riguarda l'IA. *Al suo posto:* quello che l'IA
  produce davvero per il cliente (un documento, una risposta, un risultato).
- **Immagine che non si fonde con la pagina**: rettangolo netto con un fondo di colore diverso. *Al suo posto:* fondo
  dell'immagine uguale alla pagina, o bordi sfumati (vedi `immagini-icone-logo.md`).
- **Scritte, pulsanti o loghi dentro un'immagine generata.** *Al suo posto:* immagine pulita, testo vero nella pagina.
- **Un'immagine in ogni sezione.** *Al suo posto:* un'immagine dove aiuta, di solito il momento principale.

## 7. Movimento
- **Comparsa dal basso uguale su tutto allo scorrimento** (`comparsa-scorrimento`).
- **Schede che si sollevano al passaggio del mouse** anche se non portano da nessuna parte (`solleva-hover`).
- **Numeri che contano da zero** (`statistiche-contatore`), titoli che si scrivono lettera per lettera, gradienti animati,
  rimbalzi elastici, puntini che lampeggiano.
- **Transizioni "su tutto"** (`transition: all`) e ingrandimenti al passaggio del mouse; elementi che fluttuano o fanno
  parallasse.
- **Schede che si inclinano o seguono il puntatore, pulsanti "magnetici", luce che segue il cursore, fila di loghi che
  scorre, scritte che si rimescolano** (TasteSkill).
- *Al suo posto:* il movimento solo dove dice qualcosa (stato, azione, gerarchia); un solo momento curato, non dieci effetti
  (`movimento-e-telefono.md`).

## 8. Contenuti e testi
- **Frasi buone per chiunque** (`frasi-generiche`): "soluzioni innovative", "a 360 gradi", "il partner ideale",
  "porta il tuo business al livello successivo", "Scopri di più", "Inizia ora".
- **Tricolon** ("Semplice. Veloce. Sicuro."), "non è solo X, è Y", domanda retorica con risposta, trattini lunghi
  (`trattini-lunghi`), parole di virtù su sé stessi.
- **Punti esclamativi** (`esclamativi`) in titoli e pulsanti ("Contattaci!") e **punto finale su titoli brevi e
  pulsanti** (`punto-su-etichette`, "Fatto bene."). Il secondo può essere uno stile editoriale scelto: allora si accetta.
- **Titolo di benvenuto** ("Benvenuto nel futuro della tua azienda 👋"). *Al suo posto:* cosa si fa, per chi.
- **"Scelto da oltre 1.000 aziende", cinque stelline senza fonte**: si chiede se è vero; se lo è, si scrive preciso e con
  la fonte, altrimenti si toglie.
- **Numeri, recensioni, loghi di clienti inventati**. **Interfacce finte**.
- **Seconda ondata dei testi**: dettagli inventati per sembrare concreti, striscia di numeri sotto l'hero, titoli "X. Y.",
  contrapposizioni "non X ma Y" e sostituti, parole di virtù, battuta secca a fine paragrafo, storia d'origine a stampo,
  testimonianze levigate (elenco completo in `conversione-e-testi.md`). Lo script non li conta: si controllano leggendo.
- *Al suo posto:* fatti del cliente (anni, sede, orari, nomi, prodotti veri, prezzi), parole del cliente, frasi che non
  potrebbe dire un concorrente.

## 9. Fiducia, prezzi, piè di pagina
- Muro di recensioni con nomi solo di battesimo e avatar generati; fascia "Ci hanno scelto" con loghi grigi; tre piani prezzi
  con "Più scelto" al centro; piè di pagina a quattro colonne Prodotto/Azienda/Risorse/Legale (`piede-quattro-colonne`);
  domande a fisarmonica. Sono standard anche per gli umani: pesano solo insieme agli altri segnali.

## 10. Seconda ondata (cosa arriva quando si vieta la prima)
Vietare un segnale sposta il modello sul successivo: niente viola → crema e arancione; niente Inter → Space Grotesk,
Geist, Instrument Serif; niente tre schede → bento; niente gradiente → aloni radiali. Per questo la cura non è una lista di
divieti ma **partire dal materiale vero del cliente** e decidere ogni cosa con un motivo.

C'è anche l'aspetto "da modello pulito": tolti i segnali, resta una pagina grigia, Inter, testo bianco e il vecchio colore
del marchio su un pulsante. Non è IA, ma è il default di chi non ha deciso niente. Si riconosce con la **prova dello
scambio di nome**: se con il nome di un concorrente la pagina regge lo stesso, manca la direzione.

## 11. Co-occorrenze: quando i segnali diventano un aspetto

| Gruppo | Segnali da contare | id dello script |
|---|---|---|
| Tipografia | font predefinito unico; serif sottile da "buon gusto" con una parola in corsivo o colorata nel titolo; etichette in monospace; etichetta maiuscola spaziata sopra ogni titolo | `font-default`, `parola-colorata-h1`, `etichette-mono`, `etichette-sopra-titoli`, `maiuscolo-spaziato` |
| Colore | gradiente viola-indaco o testo in gradiente; aloni sfocati; vetro decorativo; crema + serif + terracotta; quasi nero + un accento acido | `gradiente-fondo`, `testo-gradiente`, `aloni-decorativi`, `vetro`, `crema-terracotta` |
| Layout | hero centrato + pillola + due pulsanti + fila di loghi + tre schede; schede identiche con icona nel quadratino; stesso raggio e stessa ombra ovunque; schede dentro schede; numero grande con statistiche; 01/02/03 senza sequenza | `pillola-hero`, `griglia-schede-uguali`, `icona-in-cerchio`, `raggio-uniforme`, `bordo-e-ombra`, `numeri-decorativi` |
| Dettagli | "→" su ogni link; trattini lunghi e puntini mediani nelle meta; emoji come icone | `freccia-su-link`, `trattini-lunghi`, `puntini-mediani` |
| Movimento | comparsa dal basso su ogni sezione; hover su ogni scheda; contatori | `comparsa-scorrimento`, `solleva-hover`, `statistiche-contatore` |
| Contenuto | testi generici; testimonianze senza nome; numeri e loghi inventati; link morti | `frasi-generiche`; il resto a mano |

`controllo_slop.py` conta i segnali trovati per gruppo e scrive in `controllo.md` se insieme fanno un aspetto da IA
(tre o più nello stesso gruppo, o quattro gruppi toccati); il conteggio è informativo e non cambia il punteggio. I segnali
di contenuto non visibili allo script (testimonianze inventate, link morti) si aggiungono a mano.

Fonte della tabella: ricerca "Sito web eccellente dalla A alla Z", sezione sui segnali, che riprende
[anthropics/skills, frontend-design](https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md)
**[Opinione convergente]**. Lettura: uno o due segnali da gruppi diversi sono normali; tre o più dello stesso gruppo, o
quattro gruppi toccati, sono un aspetto da IA. I segnali "non finito o inventato" (testimonianze di nessuno, numeri inventati,
link morti) costano più fiducia di quelli estetici e sono i primi che un cliente nota.

**La seconda ondata, in dettaglio** (frontend-design di Anthropic, 2026): fondo crema vicino a **#F4F1EA** con serif display
ad alto contrasto e accento terracotta; quasi nero con un solo accento verde acido o vermiglione; layout "da giornale" con
filetti, raggio zero e colonne dense; schede arrotondate identiche con la stessa ombra `rgba(0,0,0,.1)`; etichetta maiuscola
spaziata sopra ogni titolo; meta uniti da puntini mediani (`·`); "→" aggiunto a link e pulsanti; una sola parola accentata nel
titolo; monospace per le piccole etichette; numero grande con statistiche nell'hero; marcatori 01/02/03 su contenuti che non
sono una sequenza; dissolvenza e salita su ogni sezione e hover su ogni scheda.

## 12. Perché succede
Il modello, senza vincoli, produce la mediana dei siti visti in addestramento (Tailwind, shadcn/ui, Lucide, Framer Motion,
migliaia di tutorial uguali). I siti generati tornano negli esempi e rinforzano la media. Il prompt da solo non basta
("non usare il viola" funziona una volta): serve un sistema di decisioni scritto (guida di stile) e un controllo a fine lavoro.
