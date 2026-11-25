# Tipi di sito, livelli e sezioni

Da leggere nelle fasi 2 (brief) e 6 (struttura). Ogni regola ha il livello della prova: **[Evidenza]** (studi, norme,
documentazione ufficiale), **[Prassi]** (consenso professionale senza un dato misurato), **[Opinione]** (parere di un autore).
Dove le prove mancano lo si dice: è lì che si rischia di inventare.

## 1. Il brief (fase 2)

Prima di qualsiasi direzione si scrive il brief in poche righe. I campi che solo il cliente sa si chiedono, non si inventano.

| Campo | Cosa scrivere | Esempio di risposta |
|---|---|---|
| Cliente | nome, attività, dove, da quando (solo se vero) | studio di consulenza del lavoro, Milano, dal 2004 |
| Pubblico | chi compra, che mestiere fa, come sceglie | titolari di aziende da 5-50 dipendenti, scelgono per passaparola |
| Tipo di sito | uno dei cinque della sezione 2 | servizio per generare contatti |
| Obiettivo e CTA principale | l'azione che conta, con verbo e oggetto | "Prenota una chiamata di 20 minuti" |
| Traffico e consapevolezza | da dove arriva la gente e quanto sa già (sezione 4) | ricerca del nome + passaparola: consapevole del prodotto |
| Livello di esperienza | sobrio e curato, immersivo o esperienziale (sezione 3), **con il motivo** | sobrio: il pubblico vuole capire in fretta e fidarsi |
| Piattaforma e limiti | WordPress con Elementor o codice; cosa questo limita | Elementor: niente scorrimento legato alla barra senza codice |
| Materiale vero | foto, video, logo vettoriale, testi del titolare, recensioni | foto della sede mancanti: da chiedere |

Il livello e il tipo di sito si scelgono dal cliente, mai dal gusto di chi progetta: un'agenzia creativa che vende la propria
immaginazione e un'azienda che vende affidabilità hanno bisogno di pagine opposte **[Prassi]**.

## 2. I cinque tipi di sito

| Tipo | Per chi | Cosa deve fare la home | CTA tipica |
|---|---|---|---|
| **Vetrina / istituzionale** | attività locali, aziende con traffico misto | orientare e dare fiducia: cosa fai, prove, chi c'è dietro, dove sei | "Chiama", "Contattaci", "Vieni a trovarci" |
| **Servizio per contatti** | professionisti, consulenze, prenotazioni | portare a una richiesta: risultato, prova, come funziona, prezzo o fascia | "Prenota una chiamata", "Chiedi un preventivo" |
| **Landing di prodotto** | un prodotto o un'offerta, traffico da campagne | costruire l'argomento quanto serve al livello di consapevolezza | "Ordina", "Prova gratis" |
| **E-commerce** | piccoli negozi online | far scegliere subito un ambito: categorie, più venduti, ricerca | "Vedi la collezione", "Aggiungi al carrello" |
| **Esperienziale / agenzia** | studi creativi, campagne, marchi che vendono immaginazione | farsi ricordare: un'esperienza che è essa stessa il portfolio | "Parliamo del tuo progetto", "Vedi i lavori" |

## 3. I livelli di esperienza

Il livello si sceglie nel brief, con il motivo, e decide quanto movimento e quanta costruzione servono. Non è fisso per chi
progetta: dipende dal cliente **[Prassi]**.

| Livello | Per chi | Cosa contiene | Piattaforma |
|---|---|---|---|
| **Sobrio e curato** | studi, professionisti, attività locali, aziende di servizi | apertura forte (caratteri grandi, foto o video vero), poche animazioni di risposta (hover, pressione), **nessun movimento sul titolo**, al massimo un momento leggero | Elementor o codice |
| **Immersivo** | marchi con una storia, prodotti, e-commerce curati | in più: scorrimento che racconta in una sezione (testo che si rivela, capitoli di foto, una sequenza fissata), un momento animato | codice, o Elementor con poco codice |
| **Esperienziale** | agenzie, studi creativi, campagne | storie allo scorrimento, oggetti e testi in movimento, transizioni di pagina | codice |

Il movimento rispetta sempre `prefers-reduced-motion` e le durate di `movimento-e-telefono.md`. NN/g vieta di animare logo,
slogan e titolo principale della home **[Evidenza]** ([NN/g, Homepage Design Principles](https://www.nngroup.com/articles/homepage-design-principles/)):
nel livello esperienziale si può fare un'eccezione motivata, mai negli altri due. Un sito esperienziale imposto a chi ha
bisogno di chiarezza è un fallimento quanto un sito piatto dato a chi vuole un'esperienza.

## 4. La lunghezza segue il livello di consapevolezza

Non esiste un ordine universale. I cinque livelli di consapevolezza di Eugene Schwartz (inconsapevole, consapevole del
problema, della soluzione, del prodotto, più consapevole) decidono quanto deve essere lunga la pagina: chi conosce già il
prodotto vuole offerta e pulsante; chi non sa di avere il problema ha bisogno di una pagina lunga che lo rispecchi, presenti
la soluzione, mostri perché la tua è migliore e dia un motivo per agire ora **[Opinione ben argomentata]**
([Copyhackers, Long pages](https://copyhackers.com/2014/07/long-pages/)). Il livello si ricava dal traffico: ricerca del
nome del marchio o retargeting = più consapevole; annuncio social a freddo = poco consapevole.

Nessun test pubblico recente confronta ordini di sezioni diversi per piccole imprese: le sequenze sotto sono **deduzioni**
dalle fonti, un punto di partenza e non una legge **[Prassi]**.

## 5. Ordine delle sezioni per tipo

| Tipo | Ordine di partenza | Perché |
|---|---|---|
| **Vetrina / istituzionale** | header (logo a sinistra, 4-6 voci, contatto) → hero (cosa, per chi, dove + "Chiama" o "Contattaci") → cosa offri (servizi o prodotti specifici, con link) → prove (recensioni con nome, foto dei lavori veri) → chi siamo breve (persone e foto vere) → come si lavora, dove siamo, orari, zona servita → CTA finale → footer con contatti completi e dati legali | traffico misto: orientare e dare fiducia |
| **Servizio per contatti** | hero con risultato per un pubblico preciso + CTA di prenotazione → prova subito sotto → problema riconosciuto → servizi o pacchetti con prezzo o "a partire da" → come funziona (3-4 passi) → chi sono → FAQ sulle obiezioni (prezzo, tempi, garanzie) → CTA finale con modulo breve e telefono | visitatore consapevole del problema o della soluzione |
| **Landing di prodotto, traffico freddo** | hero con beneficio + foto + prezzo e CTA → problema → prodotto come soluzione (dettagli, materiali, foto) → recensioni con foto → confronto e perché noi → garanzie, spedizioni, resi → FAQ → CTA ripetuta | bisogna costruire l'argomento da zero |
| **Landing di prodotto, traffico caldo** | offerta, prezzo, una prova forte, CTA | il visitatore ha già deciso |
| **Piccolo e-commerce** | header con ricerca e categorie visibili → hero statico con l'offerta o la categoria principale → categorie e più venduti → proposta di valore e prove (artigianalità, spedizione, resi) → storia breve del marchio → iscrizione newsletter nella pagina (non popup) → footer con servizio clienti e policy | far scegliere subito un ambito |
| **Esperienziale / agenzia** | apertura con il momento forte (oggetto, illustrazione o frase gigante) → manifesto breve che si rivela scorrendo → lavori selezionati grandi, con il nome del cliente → servizi come elenco o percorso, non schede → chi siamo con persone vere → contatto diretto (email, orari) | il sito è il primo lavoro che il visitatore giudica |

Fonti: Copyhackers e CXL per landing e servizi **[Opinione ben argomentata]**; Baymard per l'e-commerce **[Evidenza]**: il
32% delle home è mediocre o scarso; mostrare visivamente almeno il 40% dei tipi di prodotto; categorie e sottocategorie
popolari in home (il 62% non lo fa); ricerca visibile; niente overlay aggressivi per la newsletter (presenti nel 59%)
([Baymard, Homepage UX](https://baymard.com/blog/ecommerce-homepage-ux)). L'ordine esperienziale viene dall'archivio di
riferimenti di studi creativi (`ispirazione.md`) **[Opinione]**.

**Carosello in home** **[Evidenza]**: gli utenti vedono quasi solo la prima slide ([NN/g, Designing Effective Carousels](https://www.nngroup.com/articles/designing-effective-carousels/));
il 31% dei siti con carosello lo implementa male; alternativa migliore: sezioni statiche. Se proprio serve: al massimo
5 slide, posizione e totale visibili, 5-7 secondi per slide su desktop, pausa al passaggio del mouse, **nessuna rotazione
automatica su mobile** ([Baymard, Navigation Best Practices](https://baymard.com/blog/ecommerce-navigation-best-practice)).
Regola: hero statico più una sezione con 3-6 prodotti o servizi visibili insieme.

## 6. La prima schermata

Le prime due schermate raccolgono il 74% del tempo di visione (57% la prima, 81% le prime tre; NN/g 2018, 120 partecipanti)
**[Evidenza]** ([NN/g, Scrolling and Attention](https://www.nngroup.com/articles/scrolling-and-attention/)). La gente scorre
solo se capisce che sotto c'è altro: in un test NN/g del 2016 6 utenti su 8 non hanno capito che la pagina continuava
**[Evidenza]** ([NN/g, The Illusion of Completeness](https://www.nngroup.com/articles/illusion-of-completeness/)). La home deve
dire subito **chi sei** (nome e logo in alto a sinistra), **cosa fai** (una frase esplicita) e **perché scegliere te**, nelle
parole del pubblico **[Evidenza]** ([NN/g 2024](https://www.nngroup.com/articles/homepage-design-principles/)).

| Elemento | Regola | Livello |
|---|---|---|
| Titolo (H1) | cosa offri + per chi o dove + un risultato concreto; in pratica 6-12 parole, ma nessun dato fissa la lunghezza | [Evidenza] chiarezza; [Opinione] numero di parole |
| Sottotitolo | 1-2 righe che dicono come, dove, per chi | [Prassi] |
| CTA primaria | una sola, verbo + oggetto, visibile senza scorrere | [Evidenza] |
| CTA secondaria | al massimo una, più debole (contorno o link) | [Prassi] |
| Prova vicina | stelle Google con numero di recensioni, numero di clienti, un logo riconoscibile (solo se veri) | [Prassi] |
| Immagine | foto vera di prodotto, lavoro o persona; niente stock decorativo | [Evidenza] |
| Altezza | niente 100vh pieno; `min-height: 100svh` al massimo, con l'inizio della sezione successiva visibile | [Evidenza] + [Prassi] |
| Movimento | titolo, logo e slogan fermi (eccezione motivata solo nel livello esperienziale); niente video in autoplay né carosello | [Evidenza] |

La proposta di valore è la **tesi** che il resto della pagina dimostra; "la chiarezza batte l'originalità": se il lettore non
sa spiegarla a un amico in una frase, ha fallito **[Opinione ben argomentata]** ([CXL, Value Proposition Examples](https://www.cxl.com/blog/value-proposition-examples/)).

**Il momento visivo forte.** Chiarezza non vuol dire pagina vuota. L'apertura deve avere **un solo momento che si ricorda**:
caratteri giganti sopra o accanto a una foto vera, un oggetto del mestiere, un'illustrazione fatta apposta, un video del
titolare. Pochi colori usati in grande, non tanti colori piccoli **[Opinione]** (dai riferimenti in `ispirazione.md`).

**Lettura a F.** Si legge la prima riga, una seconda banda più corta, poi giù lungo il margine sinistro **[Evidenza]**
([NN/g, F-Shaped Pattern](https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/)): punti chiave nei primi due
paragrafi, prime due parole dei titoli che danno il senso, link che descrivono la destinazione.

## 7. Navigazione

- **Su desktop mai hamburger**: con la navigazione nascosta la trovabilità cala di oltre il 20% e i tempi crescono di
  almeno il 39% **[Evidenza]** ([NN/g, Hamburger Menus](https://www.nngroup.com/articles/hamburger-menus/)).
- Su telefono: voci visibili se sono 4-5 o meno, altrimenti navigazione combinata (alcune voci visibili più il menu) con un
  pulsante etichettato "Menu" **[Evidenza]** ([NN/g, Find navigation on mobile](https://www.nngroup.com/articles/find-navigation-mobile-even-hamburger/)).
- 4-6 voci con etichette concrete ("Servizi", "Lavori", "Prezzi", "Chi siamo", "Contatti") più un pulsante CTA a destra;
  su telefono la CTA (chiama, prenota) resta fuori dal menu **[Prassi]**. Il "massimo 7 voci" non ha supporto nelle fonti.
- La voce corrente va evidenziata (`aria-current="page"`): non farlo è "probabilmente l'errore più comune" **[Evidenza]**
  ([NN/g, Menu-Design Checklist](https://www.nngroup.com/articles/menu-design/)); breadcrumb sulle pagine interne.
- Menu a tendina con 300-500 ms di ritardo al passaggio del mouse; su telefono le categorie al primo livello **[Evidenza]**
  ([Baymard](https://baymard.com/blog/ecommerce-navigation-best-practice)).
- Header fisso solo se compatto e con **sfondo opaco**; la variante che ricompare scorrendo verso l'alto usa 300-400 ms
  **[Evidenza]** ([NN/g, Sticky Headers](https://www.nngroup.com/articles/sticky-headers/)). Un header leggero (a pillola,
  staccato dal bordo) è una scelta di carattere possibile, purché opaco e leggibile **[Opinione]**.

## 8. Chi siamo, contatti, footer

- **Chi siamo**: gli utenti cercano cosa fa l'azienda, dove si trova, chi c'è dietro e come raggiungerla; preferiscono foto di
  persone vere e recensioni bilanciate a testimonianze tutte positive **[Evidenza]** ([NN/g, About Us](https://www.nngroup.com/articles/about-us-information-on-websites/)).
  Come scriverlo: `conversione-e-testi.md`.
- **Contatti**: pagina dedicata con almeno telefono ed email, non solo un modulo; telefono mai nascosto; indirizzo completo;
  modulo di 3-5 campi come complemento; orari e tempi di risposta per ogni canale; "Contatti" nel menu e nel footer
  **[Evidenza]** ([NN/g, Contact Us Pages](https://www.nngroup.com/articles/contact-us-pages/)).
- **Footer**: sempre contatti, privacy e termini **[Evidenza]** ([NN/g, Footers](https://www.nngroup.com/articles/footers/)); in
  Italia anche P.IVA (in home), cookie policy, "Preferenze cookie" (vedi `seo-accessibilita-velocita-legale.md`). Solo fatti:
  niente slogan di chiusura **[Prassi]**.
- **Pagine servizio**: titolo con risultato, per chi è e per chi no, cosa include, processo, prezzo o fascia, prove di quel
  servizio, FAQ sulle obiezioni, CTA con modulo breve e telefono. Nessuna fonte primaria: è una deduzione **[Prassi]**.

## 9. Quando chiedere

Si chiede prima di costruire se mancano: obiettivo e CTA principale, il pubblico, la provenienza del traffico, il materiale
vero (foto, logo vettoriale, recensioni), i fatti (anni, prezzi, orari, zona). Il livello di esperienza si propone con il
motivo e si fa confermare quando il cliente non l'ha indicato.
