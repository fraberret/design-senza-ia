---
name: design-senza-ia
description: >-
  Processo completo e autonomo per rifare o creare un sito, una landing page, una home o una grafica che NON sembri fatta con
  l'intelligenza artificiale ("AI slop"): analizza da sola il sito esistente (schermate, colori misurati, font, contenuti,
  contatti, video), capisce attività e pubblico, trova e cattura i concorrenti principali con il loro punteggio,
  fa l'inventario del materiale vero, sceglie una direzione motivata dal cliente, costruisce e poi verifica la pagina con uno
  script che conta i segnali da IA (etichette sopra i titoli, schede identiche, icone in cerchi colorati, comparse allo
  scorrimento, gradienti, font predefiniti, testi generici) con punteggio e correzioni. Usala ogni volta che l'utente dà
  l'URL di un sito da rifare, chiede un'anteprima, una home, una landing page, un restyling o una grafica per un cliente,
  dice che un design "sembra fatto con l'IA", "è generico", "è un template", "è AI slop", o chiede di analizzare
  concorrenti o il design di un sito, anche se non nomina questa skill.
---

# Design senza aspetto da IA

Il look "fatto con l'IA" non è un font o un colore: è la somma di tante scelte predefinite, non decise, tutte insieme
(etichetta sopra il titolo, tre schede con l'icona nel cerchio, fondo crema, parola arancione nel titolo, comparsa dal basso,
stesso arrotondamento ovunque...). Il modello, senza vincoli, produce la media dei siti che ha visto. La cura non è un elenco
di divieti, perché vietare un segnale sposta il modello sul successivo: è **partire dal materiale vero del cliente**,
**decidere ogni scelta con un motivo**, e **misurare** il risultato.

Questa skill lavora in modo autonomo dall'URL al risultato verificato. Chiedi all'utente solo ciò che solo lui sa
(vedi "Quando chiedere").

**Prima di cominciare**, se nella cartella della skill c'è `locale.md`, leggilo: contiene le convenzioni dell'utente
(cartelle di lavoro, dove sta la guida di stile, strumenti). Vale più delle indicazioni generiche di questo file.

## Strumenti

Gli script stanno in `scripts/` e si lanciano sempre con il lanciatore, che trova da solo un Python con Playwright:

```bash
S=~/.claude/skills/design-senza-ia/scripts
$S/py.sh analizza_sito.py <url> --out <cartella>/analisi [--pagine 6]
$S/py.sh cattura_concorrenti.py <url1> <url2> ... --out <cartella>/analisi [--etichetta concorrenti]
$S/py.sh controllo_slop.py <url o file.html> --out <cartella>/controllo-vN [--accetta id1,id2] [--soglia 80]
```

Gli script girano in un browser invisibile, uno alla volta, e impiegano da 1 a 5 minuti: lanciali in primo piano con un
timeout lungo, o in background se il Mac è lento. Una pagina che usa moduli JavaScript va servita da un server locale
(`python3 -m http.server`), non aperta come `file://`.

Riferimenti da leggere quando servono:
- `references/catalogo-segnali.md`: tutti i segnali, perché nascono, cosa fare al loro posto. Leggilo prima di costruire.
- `references/direzione-e-costruzione.md`: inventario, quanto cambiare, tre direzioni in cinque righe, regole di
  costruzione e di finitura, controlli finali. Leggilo prima della fase 4.
- `references/concorrenti-e-strumenti.md`: come trovare i concorrenti, cosa ricavarne, Chrome ed estensione Design.md.
- `references/immagini-generate.md`: quando serve un'immagine generata, il prompt, come fonderla con la pagina.

## Il processo

### Fase 1. Analisi del sito (autonoma)

1. Crea la cartella di lavoro (quella indicata in `locale.md`, se c'è; altrimenti chiedi una volta).
2. `analizza_sito.py <url> --out <cartella>/analisi`. Leggi `analisi.md`, guarda i pezzi `schermate/home-computer-NN.jpg` e
   `home-telefono-*.jpg`, scorri `testi/`.
3. Scrivi in `analisi/sintesi.md`: cosa vende, a chi, dove, da quanto, cosa c'è di riconoscibile (icone, slogan, mascotte,
   video, colori, una firma), cosa non funziona, cosa il titolare evidentemente tiene a mostrare. Il sito vecchio è anche un
   indizio dei gusti del cliente: un sito pieno e colorato dice che un design vuoto e grigio verrà bocciato.
4. Lancia `controllo_slop.py` anche sul sito attuale e decidi **quanto cambiare** (rifacimento, ritocco o pochi ritocchi:
   `references/direzione-e-costruzione.md`, "Quanto cambiare"). Scrivilo nella sintesi.

### Fase 2. Concorrenti (autonoma)

1. Trova 4-8 concorrenti e, se utile, 2-4 riferimenti del settore (`references/concorrenti-e-strumenti.md`).
2. `cattura_concorrenti.py ... --out <cartella>/analisi`. Leggi `concorrenti.md` e guarda il foglio.
3. Annota nella sintesi: la media del settore (da non copiare), il migliore e perché, lo spazio libero per il cliente,
   il punteggio IA più alto da battere.

### Fase 3. Inventario del materiale vero

Compila la tabella di `references/direzione-e-costruzione.md` sezione 1: logo, colori, font, foto, video, testi, fatti,
recensioni, elementi del sito vecchio. Copia il materiale utile in `<cartella>/materiale/`. Quello che manca diventa la lista
"da chiedere al cliente" del resoconto; nel frattempo niente di inventato (numeri, recensioni, persone, date).

### Fase 4. Direzione

Prepara tre direzioni ancorate al materiale vero (sezione 3 del riferimento), ognuna in cinque righe: attività, carattere
(senza "pulito, moderno, elegante, premium"), mondo, momenti, una sola firma. Scegli la più adatta al pubblico e al
cliente e scrivi il motivo. Se l'utente ha chiesto piena autonomia, scegli e dichiaralo; altrimenti mostra le tre
direzioni in un messaggio breve con la tua raccomandazione e aspetta. Registra la direzione nella guida di stile del cliente
(dove dice `locale.md`, altrimenti un file `guida-di-stile.md` nella cartella di lavoro) prima di scrivere codice: le
cinque righe, font, colori, regole, cose bocciate.

### Fase 5. Costruzione

Segui le regole della sezione 4 del riferimento. In breve: contenuto prima della forma, una composizione diversa per sezione,
colori pieni del marchio, colore ricco solo nei momenti e il resto tranquillo, tipografia con carattere, icone disegnate
per il cliente e nel colore del testo, foto vere, movimento quasi zero, testi del cliente, finitura precisa (scala di spazi,
raggi annidati, niente ombre colorate). Le immagini generate solo per un momento senza foto, con
`references/immagini-generate.md`. Font caricati dal sito (non da Google) quando la privacy conta. Ogni versione è un
file nuovo (`<cliente>-home-vN.html`), le precedenti restano.

### Fase 6. Controllo e correzione (autonoma, in ciclo)

1. `controllo_slop.py <pagina> --out <cartella>/controllo-vN`. Leggi `controllo.md`.
2. Correggi ogni segnale non scelto. Quelli scelti di proposito vanno in `--accetta` e il motivo nella guida di stile.
3. Ripeti finché il punteggio è almeno 80 (o la soglia concordata) e più alto di tutti i concorrenti.
4. Guarda sempre le schermate del controllo: il punteggio misura le forme, non il gusto. Se a colpo d'occhio sembra un
   modello, torna alla fase 4. Il punteggio è tarato su siti di attività e servizi: i siti di prodotti tech (Linear,
   Stripe) usano di proposito molti di questi schemi e prendono punteggi bassi senza essere fatti con l'IA.
5. **Prova dello scambio di nome**: con il nome di un concorrente al posto del cliente, la pagina reggerebbe? Se sì,
   rinforza testi, momento e firma.
6. Leggi la riga "Finitura" (spaziature senza scala, lettere strette sui testi piccoli): non toglie punti, ma va sistemata.
7. Controlli tecnici: niente sbordamenti, un solo H1, testi ≥ 15 px, contrasti calcolati (≥ 4,5:1 testi, ≥ 3:1 grandi),
   prova a 1440, 900, 390 e 360 px, con JavaScript spento e con il movimento ridotto.

### Fase 7. Resoconto

Scrivi all'utente, in italiano semplice:
- dove si apre la pagina e come (doppio clic o server);
- la direzione scelta e perché, in due righe;
- punteggio IA della nuova pagina contro sito vecchio e concorrenti (una piccola tabella);
- cosa hai controllato e corretto;
- cosa manca dal cliente (foto, logo originale, testi, conferme) e ogni elemento sostitutivo usato.

## Quando chiedere

Chiedi solo quello che solo l'utente sa: la cartella di lavoro se non è ovvia, una direzione quando non ha dato piena
autonomia, un riferimento visivo dopo **due bocciature** della stessa versione (non tentare una terza volta alla cieca),
e i dati del cliente che non si trovano online, e il permesso prima di generare immagini a pagamento. Tutto il resto
(analisi, ricerche, concorrenti, controlli) lo fai da solo.

## Regole fisse

- Niente dati inventati (numeri, recensioni, persone, date, loghi di clienti); per i siti reali i contatti veri del cliente
  si usano così come sono.
- Una persona in foto non si presenta come il cliente senza conferma.
- Contrasti calcolati e controllo a larghezza di telefono prima di mostrare qualsiasi pagina o grafica.
