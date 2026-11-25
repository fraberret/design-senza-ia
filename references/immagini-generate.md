# Immagini generate

Quando usare un'immagine generata, come scrivere il prompt e come metterla nella pagina senza che sembri appiccicata.
Adattato da `visuals.md` di *unslop* di Damir Sokolovsky (github.com/heydamir/unslop, CC BY 4.0).

## Prima di tutto: serve davvero?

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

## Stili che funzionano

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

## Il prompt, in quest'ordine

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

## Oggetti da mettere nell'interfaccia

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

## Nella pagina

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
