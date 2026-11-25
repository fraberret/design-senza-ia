# Direzione e costruzione

Come si passa dall'analisi a un design che sembra fatto da qualcuno che conosce il cliente.

## 1. L'inventario del materiale vero (prima di qualsiasi stile)

Elenca cosa esiste davvero, con il percorso del file o l'URL. Ogni voce vuota è una cosa da chiedere al cliente, non da
inventare.

| Materiale | Dove si trova di solito | Se manca |
|---|---|---|
| Logo (vettoriale) | sito, documenti, insegna | usare il PNG del sito e chiedere l'originale |
| Colori del marchio | logo, sito, insegna, brochure, divise, packaging | misurati con analizza_sito.py |
| Font del marchio | logo, brochure, sito vecchio | scegliere un font con lo stesso carattere (condensato, serif, geometrico...) |
| Foto della sede, delle persone, del lavoro | sito, scheda Google, social | foto sostitutive dello stesso fotografo + lista di scatti |
| Schermate o foto del prodotto | sito, brochure, video | chiedere le versioni attuali |
| Video | YouTube/Vimeo del cliente | - |
| Testi e frasi del titolare | sito, social, brochure, chi siamo | le sue parole valgono più delle nostre |
| Fatti: anni, sede, orari, prezzi, nomi, numeri | sito, registro imprese, scheda Google | mai inventati: si chiedono |
| Recensioni vere | Google, Facebook, Trustpilot | nessuna sezione recensioni |
| Elementi riconoscibili del sito vecchio | icone, illustrazioni, slogan, struttura | decidere cosa tenere ridisegnato: il cliente ci è affezionato |

## 2. Capire il cliente

Scrivi in 5 righe: cosa vende, a chi (età, mestiere, come compra), dove, perché lo scelgono invece dei concorrenti, e il tono
giusto (serio, caldo, tecnico, artigianale). Il tono viene dal pubblico, non dal gusto: commercialisti e consulenti vogliono
affidabilità e chiarezza; un bar vuole calore e foto; un artigiano vuole materia e mani.

### Quanto cambiare (decidilo dopo l'analisi, prima delle direzioni)

Leggi con onestà l'analisi e il punteggio del sito attuale:
- **Molti segnali** (colore, caratteri, icone, testi, struttura): rifacimento completo, con le tre direzioni qui sotto.
- **Pochi segnali**, su un sito che nel complesso è disegnato: **ritocco**. Si correggono solo i segnali trovati e si tengono
  marchio, colori, caratteri e impaginazione. Le idee più grandi (una foto vera in apertura, una sezione che manca) vanno nel
  resoconto come proposte, non nella pagina.
- **Nessun segnale**: dillo chiaramente e proponi al massimo due o tre ritocchi precisi, con i valori. Si applicano solo se
  l'utente è d'accordo. Non si cambia un sito buono solo per farlo diverso.

Se il cliente ha chiesto un sito nuovo, il rifacimento resta, ma il livello dice quanto del vecchio tenere.

## 3. Le tre direzioni

Prepara **tre direzioni** diverse tra loro, ognuna ancorata a un elemento vero del cliente. Mai tre varianti dello stesso
template. Ogni direzione si scrive prima in **cinque righe**, ricavate da cosa fa il cliente e per chi, mai da cosa va di
moda:

- **Attività.** Cosa fa e per chi, in una frase semplice.
- **Carattere.** Due o tre parole concrete, come `preciso, paziente, di quartiere` o `caldo, artigianale, un po' ironico`.
  Vietate *pulito, moderno, elegante, minimal, premium, innovativo*: descrivono qualsiasi modello.
- **Mondo.** Il luogo o la materia a cui appartiene l'attività: lo studio con i faldoni, l'officina, il laboratorio, il
  cuoio, la carta della brochure. Il mondo decide la tinta dei neutri, il colore d'accento e le immagini.
- **Momenti.** Uno o due punti della pagina dove si concentrano colore, materia e cura (una foto vera grande, il video del
  titolare, un oggetto del mestiere, una tabella fatta bene). Tutto il resto (menu, pulsanti, testi) resta tranquillo.
  Il "look da IA" spalma colore ed effetti dappertutto; un sito curato li tiene per uno o due momenti.
- **Firma.** **Un solo** dettaglio che solo questo cliente avrebbe, usato sempre uguale e solo dove serve (i bollini del sito
  vecchio ridisegnati, una sottolineatura fatta a mano, l'orario scritto come sul cartello del negozio). Uno, non cinque.

Poi, per ogni direzione: font (con il motivo), colori (dal marchio), come è fatta l'apertura, come sono composte le sezioni,
cosa la rende diversa dai concorrenti. Scegli e scrivi perché.

*Le cinque righe, i livelli di intervento, la prova dello scambio di nome e le regole di finitura sono adattati da unslop
di Damir Sokolovsky (github.com/heydamir/unslop, CC BY 4.0).*

Fonti di una direzione autentica (esempi, non un menu da cui pescare):
- **La carta del cliente**: brochure, biglietti, insegna, moduli, packaging. Un'azienda con una brochure anni '90 arancione e
  blu ha già un linguaggio: colori pieni, condensato in grassetto, riquadri netti.
- **Il prodotto**: l'interfaccia vera del software (i suoi colori e pulsanti), la materia (cuoio, legno, pietra), il luogo.
- **Il mestiere**: lo scadenzario di uno studio, il listino di un'officina, il menù di un ristorante, la cartella clinica.
  Le forme del lavoro vero sono più credibili di qualsiasi scheda.
- **Il territorio**: il quartiere, la città, i materiali locali (con misura, senza cartoline).
- **Il titolare**: la sua voce, la sua firma, la sua storia, se il cliente è una persona.

Direzioni da evitare come scorciatoia: "minimal moderno", "SaaS scuro", "editoriale crema con serif corsivo", "bento":
sono la media, non una direzione.

## 4. Regole di costruzione

Ogni regola ha il suo perché: è quello che decide nei casi non previsti.

- **Prima il contenuto, poi la forma.** Scrivi la pagina come testo (titoli, paragrafi, dati) e solo dopo scegli la forma di
  ogni sezione in base a cosa contiene: una lista resta lista, una tabella resta tabella, tre cose diverse non diventano tre
  schede uguali.
- **Una composizione diversa per sezione.** Mai due sezioni vicine con la stessa impaginazione. Varia anche la densità.
- **Un segnale scelto, non arrivato.** Un'etichetta sopra un titolo, una griglia di schede, un'icona colorata si possono usare
  se c'è un motivo (scrivilo nella guida di stile); il controllo li accetta con `--accetta`.
- **Colore pieno del marchio, non gradienti.** Un colore dominante, un accento; niente aloni, vetri, ombre colorate.
- **Tipografia con carattere.** Un font da display legato al marchio, un font da testo leggibile; salti di dimensione netti;
  testi mai sotto 15 px.
- **Icone disegnate per il cliente**, coerenti tra loro, nel colore del testo; meglio poche e utili. Un elemento del sito
  vecchio a cui il cliente tiene (i bollini, la mascotte) si ridisegna, non si trasforma nel cliché "icona in cerchio".
- **Foto vere sopra tutto.** Senza foto, il materiale del cliente (video, schermate, documenti, firma) e la tipografia.
- **Movimento quasi zero.** Contenuto visibile subito; hover discreti solo su ciò che si clicca; al massimo un momento curato.
- **Testi del cliente.** Frasi che un concorrente non potrebbe firmare; pulsanti con verbo e oggetto; niente numeri inventati.
- **Imperfezioni volute.** Un sito umano ha parti asimmetriche, una sezione più fitta, un dettaglio specifico (un orario
  particolare, una nota del titolare). Non tutto allineato al millimetro con lo stesso respiro.
- **Finitura precisa.** Le imperfezioni volute stanno nella composizione, non nei dettagli:
  - spazi da una scala di passi (multipli di 4 o 8), cose uguali con spazi uguali, più spazio tra i gruppi che dentro un
    gruppo (il controllo li riporta nella riga "Finitura");
  - raggi annidati: il raggio interno è quello esterno meno lo spazio tra i due, mai sotto 4 px;
  - gerarchia dei titoli con dimensione e colore più che col peso; spaziatura delle lettere 0 sotto i 16 px, negativa solo
    sui titoli grandi;
  - numeri in un solo formato in tutta la pagina (`1.250 €` ovunque, non `1250€` accanto a `€ 1.250,00`);
  - ombre neutre e piccole, mai colorate; filetti sottili invece di bordi accesi;
  - niente punti esclamativi né punti finali su titoli, pulsanti ed etichette;
  - transizioni solo su colore, fondo, bordo, opacità e trasformazioni, con una sola curva e durate brevi (120-200 ms per il
    passaggio del mouse); mai animare larghezza, altezza o margini.
- **Immagini generate**, solo quando per un momento non ci sono foto vere: segui `immagini-generate.md`. Non sostituiscono
  le foto del cliente, che restano da chiedere.

## 5. Dopo la costruzione

1. `controllo_slop.py` sulla pagina: leggi `controllo.md`, correggi, ripeti fino alla soglia (80) o finché i segnali
   rimasti sono tutti scelti e dichiarati.
2. Guarda le schermate (`computer-NN.jpg`, `telefono-NN.jpg`) come le guarderebbe il cliente: a colpo d'occhio sembra un
   modello? Se sì, il punteggio non basta: torna alla direzione.
3. **Prova dello scambio di nome.** Metti il nome di un concorrente al posto di quello del cliente: la pagina regge lo
   stesso? Se sì, la direzione è debole. Rinforzala nei testi (fatti e parole del cliente), nel momento principale e nella
   firma, non aggiungendo decorazioni.
4. Controlli tecnici: nessuno sbordamento, un solo H1, contrasti calcolati (testi ≥ 4,5:1, grandi ≥ 3:1), testi ≥ 15 px.
5. Confronta con i concorrenti (stesso metro): il nuovo sito deve avere un punteggio IA più alto di tutti e un aspetto
   riconoscibile.
