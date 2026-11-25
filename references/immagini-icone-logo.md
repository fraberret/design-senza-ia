# Immagini, icone e logo

Da leggere nella fase 7 (asset). Livelli: **[Evidenza]**, **[Prassi]**, **[Opinione]**. La parte sulle immagini generate è
adattata da `visuals.md` di *unslop* di Damir Sokolovsky (github.com/heydamir/unslop, CC BY 4.0); le regole su foto di
repertorio, pesi e loghi di terzi da TasteSkill 2.5.1 (MIT); la disciplina delle icone da UI/UX Pro Max (MIT).

## 1. Fotografia: un contenuto, non un abbellimento

**Ordine di preferenza [Prassi su base di evidenza NN/g]**: foto vere commissionate (persone, luogo, mani al lavoro,
prodotto in uso); foto vere del cliente rifinite con un trattamento unico; repertorio scelto con criterio e trattato; IA solo
per usi non documentali. Ogni foto risponde a "che informazione dà?", altrimenti si toglie
([NN/g, Photos as Web Content](https://www.nngroup.com/articles/photos-as-web-content/)). Le persone guardano le foto di
persone vere e di prodotti e saltano quelle di repertorio **[Evidenza]**.

**Repertorio [Prassi]** (TasteSkill): solo per dettagli (mani, attrezzi, materiali, un processo), mai per apertura, stanze,
vetrine, prodotti o persone, e al massimo 1 foto su 3.

**Senza foto del cliente** lo si dice nel resoconto e si propone, in ordine: mezza giornata con un fotografo locale; una
mattina di scatti col telefono; prodotti su un solo fondo. Lista scatti minima: vetrina di fronte, la stanza dalla porta, il
banco o il tavolo di lavoro, tre prodotti su una superficie, mani al lavoro, un dettaglio; obiettivo 1x, luce di finestra,
niente flash né filtri, orizzontale e verticale **[Prassi]** (TasteSkill). Il brief per il fotografo contiene contesto,
obiettivi, lista degli scatti costruita sugli usi reali, mood (palette, luce, tono), luogo e **immagini di riferimento**
([Milanote](https://milanote.com/templates/photography/photoshoot-brief)). Un solo preset di colore per tutto il set, stessa
temperatura di luce, proporzioni fisse per ruolo (hero 16:9 desktop e 4:5 telefono, schede 4:5 o 1:1, ritratti 4:5)
**[Prassi]**.

**Tecnica [Evidenza]**: l'immagine più grande della prima schermata (l'LCP) sta nell'HTML iniziale, non inserita via
JavaScript né come sfondo CSS, con `fetchpriority="high"` (al massimo 1-2) e **mai in lazy-load**, in AVIF o WebP alla
dimensione mostrata, dallo stesso dominio ([web.dev, Optimize LCP](https://web.dev/articles/optimize-lcp)); `srcset` con
descrittori `w` e `sizes` scritto sul layout reale, `<picture>` per tagli diversi su telefono
([MDN, Responsive images](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Responsive_images)); AVIF è Baseline dal
gennaio 2024 ([web-features](https://web-platform-dx.github.io/web-features-explorer/features/avif)).

| Regola | Valore | Livello |
|---|---|---|
| Dimensioni | `width` e `height` sempre (o `aspect-ratio`) | [Prassi] |
| Sotto la piega | `loading="lazy"` e `decoding="async"`; come `<img>`, non come sfondo CSS | [Prassi] |
| Larghezze esportate | 3-4 per foto (480, 800, 1200, 1600-2000 px), mai oltre 2x la larghezza mostrata | [Prassi] |
| Pesi | hero sotto 400 KB (meglio 150-200), ogni altra foto sotto 250 KB, immagini della pagina sotto 2.400 KB | [Prassi] (TasteSkill, Front-End Checklist) |
| Origine | segnare da dove viene ogni immagine (`data-source="cliente|commissionata|repertorio|generata|segnaposto"`) per il resoconto | [Prassi] |

**Testo alternativo** **[Evidenza]**, albero decisionale W3C: decorativa o già descritta dal testo vicino → `alt=""`; dentro
un link o un pulsante → descrive la destinazione; logo unico contenuto di un link → "Home – Nome azienda"
([W3C WAI, alt Decision Tree](https://www.w3.org/WAI/tutorials/images/decision-tree/)).

## 2. Immagini generate con IA

**La legge [Evidenza, norma]**: dal **2 agosto 2026** l'art. 50 dell'AI Act obbliga chi pubblica un **deepfake** (immagine
generata o manipolata che somiglia a persone, oggetti, luoghi o eventi esistenti e apparirebbe falsamente autentica) a
dichiararlo in modo visibile alla prima esposizione; il watermark invisibile non basta; per opere evidentemente artistiche
basta una dichiarazione discreta; sanzioni fino a 15 milioni di euro o al 3% del fatturato
([Commissione UE, FAQ art. 50](https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act)).
L'editing standard è escluso ([code of practice](https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content)).

**Regola**: **mai IA realistica per persone (team, testimonial, clienti), sede, lavori fatti o prodotti venduti**: sarebbe un
deepfake da etichettare e prima ancora una promessa falsa. IA accettabile per texture e fondi, oggetti generici non attribuiti
al cliente, illustrazioni chiaramente stilizzate, mockup interni, ritocco di foto vere **[Prassi]**. Le immagini IA non
riconosciute come tali non hanno ridotto la fiducia in un test NN/g: il problema è di veridicità e di legge, non di estetica
**[Evidenza]** ([NN/g, AI-Generated Images](https://nngroup.com/articles/ai-generated-images)). Segnali da controllare a
ingrandimento 100%: mani che impugnano oggetti, scritte e loghi storpiati, ombre e riflessi incoerenti, luce troppo uniforme,
pelle senza pori, sfondi impossibili, estetica "troppo cinematografica" **[Evidenza]**
([Euronews](https://www.euronews.com/2025/02/16/ai-slop-is-flooding-the-internet-this-is-how-can-you-tell-if-an-image-is-artificially-gene);
[Kellogg Insight](https://insight.kellogg.northwestern.edu/article/ai-photos-identification)). Per Merchant Center Google
chiede i metadati IPTC `TrainedAlgorithmicMedia` ([Google](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content)).

### Prima di tutto: serve davvero?

1. **Le foto vere vincono sempre.** Sede, persone, lavoro, prodotto: se esistono si usano; se mancano si chiedono al
   cliente. Un'immagine generata non prende mai il posto di una persona o di un luogo reale del cliente, e non si presenta
   come tale.
2. **Dove ha senso:** il momento principale di una pagina che non ha foto (servizi immateriali, software, consulenza), uno
   sfondo d'apertura, un oggetto del mestiere da mettere accanto a un riquadro (un faldone, una busta, un pacco, un
   portafoglio), una pagina vuota o di errore.
3. **Dove non serve:** pannelli, aree riservate, pagine di servizio. Lì il momento lo fa il contenuto (una tabella fatta
   bene, un numero vero, una schermata reale).
4. **Scrivi il soggetto in una frase** partendo dal "mondo" e dal "carattere" della direzione. Se non sta in una frase, non è
   ancora chiaro. Esempi della forma, da non riusare: uno studio che tiene la contabilità → *una scrivania di legno con un
   faldone aperto e una lampada accesa, luce di fine giornata*; un laboratorio di cuoio → *una pelle conciata stesa su un
   bancone, con gli attrezzi in fila, luce da finestra*.

Da evitare a meno che l'attività non parli proprio di quello: macchie lucide, sfere, nebulose, cromature liquide, cubi che
fluttuano, circuiti al neon, ologrammi, cervelli luminosi, robot, razzi, cristalli.

### Stili che funzionano

Uno per pagina, scelto per il carattere della direzione:
- **Foto cinematografica di un oggetto**: una cosa vera, luce netta, fondo semplice. Per attività serie e affidabili.
- **Illustrazione dipinta di un paesaggio o di un ambiente**, con cielo o spazio libero per il testo. Per attività calde e
  umane.
- **3D morbido**: un oggetto o una piccola scena con materiali opachi e luce gentile. Per attività giocose o amichevoli.
- **Oggetto del prodotto in studio**: il prodotto vero ricostruito con i materiali giusti, da mettere dentro l'interfaccia.
- **Incisione o stampa a un colore**, solo se tutta la pagina vive in quel mondo (carta tinta, caratteri coerenti).
  Su una pagina moderna normale sembra un filtro.

Cosa fallisce di solito: chiedere grana, carta o texture nel prompt (i modelli ci mettono una scacchiera finissima: la
texture si aggiunge nel codice), più soggetti o collage, astrazioni lucide viola e blu.

### Il prompt, in quest'ordine

1. **Soggetto**: la frase, concreta e fisica.
2. **Ambiente**: dove si trova, semplice.
3. **Luce e colori**: in armonia con la pagina. Scrivi il **colore esatto del fondo della pagina** (es. `#f4efe6`), così i
   bordi si possono fondere, e la direzione della luce.
4. **Stile**: uno solo, tra quelli sopra.
5. **Composizione**: dove sta il soggetto per lasciare spazio al testo ("soggetto nella metà destra, metà sinistra calma e
   vuota"). Per uno sfondo d'apertura chiedi 16:9 o più largo e tieni calmo anche il quinto inferiore.
6. **Esclusioni**: niente testo, lettere, loghi, interfacce, filigrane.
7. **Formato**: le proporzioni dello spazio nella pagina, al doppio della misura a schermo.

Prima di generare, mostra all'utente il prompt e lo strumento (può costare). Genera una volta, giudica il risultato contro la
frase e la tavolozza, e se non va **cambia il prompt** invece di rigenerare uguale. Dopo due tentativi falliti, chiedi un
riferimento visivo.

### Oggetti da mettere nell'interfaccia

- Un oggetto solo, luce da studio, su fondo del colore esatto della pagina, con un'ombra di contatto morbida e nient'altro.
- Chiedi l'angolo che serve ("inclinato di 20 gradi, visto un po' dall'alto").
- Se puoi, scontornalo; altrimenti fondilo con una maschera nel colore della pagina. Attenzione: lo scontorno automatico
  mangia le zone scure vicine al colore del fondo (uno schermo nero spento): chiedi lo schermo in un colore piatto di
  contrasto.
- Mettilo a cavallo del bordo di un riquadro, appena ruotato, con un'ombra neutra: così sta nello stesso spazio della
  pagina.
- Testi, loghi e scritte piccole i modelli li sbagliano: si rimettono sopra nel codice (HTML sopra l'immagine) o si
  correggono dopo. Mai lasciare un logo del cliente ridisegnato male.
- Tutto dentro un'immagine racconta la stessa storia: se la tabella accanto mostra la fattura 142 di un cliente, l'oggetto
  mostra lo stesso numero.

### Nella pagina

- WebP o AVIF al doppio della misura a schermo, con un `alt` vero che dice cosa si vede; dimensioni fisse, così la pagina
  non salta; priorità alta se è in apertura.
- **I bordi si fondono con la pagina.** Un rettangolo netto con un fondo di colore diverso è un segnale da IA. Se i colori
  non coincidono, sfuma con una maschera (`mask-image: radial-gradient(closest-side, #000 70%, transparent)`) o con un
  velo nel colore della pagina.
- Ferma, oppure un solo movimento lento e coerente con il soggetto. Niente parallasse.
- Un trattamento nel codice (bicromia nei colori della pagina) può farla sembrare nata lì: solo se sta nel carattere, mai
  come decorazione in più.
- Senza uno strumento per generare: lascia lo spazio vuoto della misura giusta (un fondo appena diverso, senza scritte), metti
  il prompt nel resoconto e di' che file serve. Mai un riquadro con scritto "immagine qui" in una pagina da mostrare.

## 3. Illustrazione ed elementi grafici dalla firma

Un sistema illustrativo funziona se ha regole scritte su forme, spessore delle linee, raggi e prospettiva, un solo stile, e
nasce dalla ricerca sul marchio **[Prassi]** ([Smashing Magazine](https://www.smashingmagazine.com/2019/12/brand-illustration-systems-visual-identity/);
[Toptal](https://www.toptal.com/designers/brand/brand-illustration-system)). Per un piccolo cliente basta un **kit firma di
3-5 elementi derivati dal suo mondo** (un motivo dal logo o da un materiale, una forma per ritagliare le foto, un segno
grafico, una texture), ognuno con regole d'uso **[Prassi]**: per un laboratorio di cuoio cuciture, grana e impunture; per
uno studio i bollini o i moduli che usa davvero. Il test: se l'elemento potrebbe stare sul sito di un concorrente qualunque,
non è una firma. Da evitare: macchie sfocate, gradienti mesh viola-blu, illustrazioni "corporate memphis", sfondi a griglia o
a puntini senza motivo. Personaggi illustrati fatti apposta (come fanno alcuni studi creativi) sono una firma forte, ma
richiedono un illustratore o un lavoro dedicato: non si improvvisano con un generatore **[Opinione]**.

## 4. Icone su misura

- Quasi sempre con un'etichetta visibile: pochissime icone sono universali (casa, stampa, lente); cuore e stella vengono
  fraintesi; se non trovi un'icona adatta in 5 secondi, non comunica quel concetto **[Evidenza]**
  ([NN/g, Icon Usability](https://www.nngroup.com/articles/icon-usability/)).
- Costruzione **[Prassi]**: tela 24×24, area viva 20×20, tratto 2 px (o 1,5 costante), almeno 1 px dal bordo, terminazioni e
  raggi costanti, SVG con `viewBox="0 0 24 24"`, `fill="none"`, `stroke="currentColor"`; niente scalature a misure
  arbitrarie ([Tabler, Design guide](https://docs.tabler.io/icons/design-guide); [Material, System icons](https://material.io/design/iconography/system-icons.html)).
- Disciplina **[Prassi]** (UI/UX Pro Max): un solo set e un solo stile per livello (non pieno e contorno mischiati); misure come
  token (16/20/24); allineate alla linea di base del testo; contrasto 3:1 se portano significato; mai emoji come icone
  strutturali; mai PNG per le icone.
- **Lucide è il set predefinito di shadcn/ui** ([shadcn changelog](https://ui.shadcn.com/docs/changelog/2024-11-icons)): Lucide
  in un quadratino colorato sopra ogni titolo legge come sito generato (inferenza, non dato). Regola: niente icone su elenchi
  di servizi o concetti astratti ("qualità"); sì per azioni note (carrello, ricerca, telefono, WhatsApp, mappa) e
  caratteristiche concrete (misure, materiale, consegna); set alternativo (Phosphor, Iconoir, Tabler) o set modificato in
  modo coerente; meglio ancora icone ridisegnate dagli elementi che il cliente ha già (bollini, pittogrammi del sito vecchio)
  **[Prassi]**.
- Accessibilità: icona decorativa con `aria-hidden="true"`, icona sola in un pulsante con `aria-label` sul pulsante.

**Loghi di terzi [Prassi]** (TasteSkill): se la pagina nomina uno strumento (WhatsApp, un software, un gestionale) si usa il
suo logo vero nei suoi colori, mai un disegno simile; fonti con licenza: gilbarbara/logos e simple-icons (CC0), vscode-icons
(MIT, tipi di file); uso nominativo, con la riga "I nomi e i loghi dei prodotti sono marchi dei rispettivi proprietari". Il
logo del cliente non si ricolora né si ridisegna senza richiesta.

## 5. Logo (solo su richiesta)

**Processo [Prassi]** (David Airey): ricerca, strategia, design, implementazione, con lo schizzo al centro: prima di
disegnare si capisce il cliente ([Airey, Identity Designed](https://www.davidairey.com/samples/identity_designed_the_process_free.pdf)).

**Ritocco o rifacimento.** L'equità visiva va protetta: Cracker Barrel nell'agosto 2025 ha ritirato il nuovo logo dopo circa
una settimana, con circa 100 milioni di dollari di valore di borsa bruciati, come Gap nel 2010 **[Evidenza]**
([Kellogg Insight](https://insight.kellogg.northwestern.edu/article/when-a-rebrand-meets-backlash)). Regola **[Prassi]**: se il
marchio è riconoscibile, **ritocco** (tenere forma, colore principale e segno distintivo; ripulire geometria e versioni
piccole); **rifacimento** solo se il logo è illeggibile, simile a un concorrente o il posizionamento cambia davvero. Il
wordmark è la scelta più sicura per un'attività locale, il marchio combinato è il default per una PMI (il simbolo fa da
favicon e avatar); un wordmark va almeno personalizzato, non solo digitato in un font scaricabile. Test a 16 e 32 px, in
negativo, su foto, e nella tecnica di stampa del cliente (per esempio impressione a caldo a un colore).

**Consegne [Prassi]**: SVG in versione orizzontale, impilata, solo simbolo, monocromo nero e bianco; PNG trasparenti 2x;
area di rispetto e misura minima; palette in HEX, RGB, CMYK; font con licenza; immagine Open Graph 1200×630 (convenzione);
file sorgente. **Favicon** **[Prassi]** (Evil Martians 2026): `favicon.ico` 32×32 alla radice, `icon.svg` con variante per
tema scuro dentro l'SVG, `apple-touch-icon.png` 180×180 con il logo a 140×140; manifest solo per le PWA
([Evil Martians, How to Favicon](https://evilmartians.com/chronicles/how-to-favicon-in-six-files-that-fit-most-needs)); per
Google, quadrata, più grande di 48×48 e con URL stabile ([Google, Favicon](https://developers.google.com/search/docs/appearance/favicon-in-search)).
Prima di consegnare un logo: ricerca di anteriorità su EUIPO/TMview e UIBM e ricerca per immagine inversa, dicendo al cliente
che non è un parere legale.

**Coerenza.** Affiancare sito, ultimi 9 post e un materiale stampato: se sembrano tre aziende, il sistema non c'è
([Ocus](https://www.ocus.com/resources/brand-photography-guidelines)). Le regole decise vanno nella guida di stile del cliente.
