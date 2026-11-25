# Conversione e testi

Da leggere nella fase 6 (struttura e testi) e nel controllo finale. Livelli: **[Evidenza]**, **[Prassi]**, **[Opinione]**.
Le regole di scrittura vengono anche da TasteSkill 2.5.1 (`copy-tells.md`, `copy-moves.md`, licenza MIT), tradotte e
adattate all'italiano.

## 1. CTA: il testo conta più del colore

- **Verbo + oggetto concreto**, parola chiave all'inizio ("Prenota la prima seduta", "Chiedi un preventivo per il tetto");
  mai "Invia", "Clicca qui" o "Scopri di più" da soli: non dicono cosa c'è dopo e i lettori di schermo leggono i link fuori
  contesto **[Evidenza]** ([NN/g, "Learn More" Links](https://www.nngroup.com/articles/learn-more-links/)).
- Non esiste ricerca primaria recente su colore, dimensione o numero ottimale di CTA: i test "rosso contro verde" sono
  aneddoti. "Una sola azione primaria per pagina" è un principio di gerarchia (effetto Von Restorff), non un numero misurato
  **[Prassi]** ([Laws of UX](https://lawsofux.com/)).
- Ripetere la **stessa** CTA dopo ogni blocco che risponde a un'obiezione va bene; aggiungere azioni diverse no **[Prassi]**.
- Contrasti del pulsante: testo 4,5:1, bordo o forma 3:1 **[Evidenza]**.
- Il pulsante dice cosa succede anche quando il tono è giocoso; per chi guarda e basta, un'uscita leggera ("Vedi prima i
  lavori") **[Prassi]** (TasteSkill).

## 2. Prove di fiducia

- Con 5 recensioni la probabilità d'acquisto è più alta del 270% rispetto a zero; il beneficio crolla dopo le prime 5; il
  massimo è tra 4,0 e 4,7 stelle, poi scende verso il 5,0 perché la perfezione insospettisce; "acquirente verificato" +15%
  **[Evidenza]** ([Spiegel Research Center](https://spiegel.medill.northwestern.edu/how-online-reviews-influence-sales/)).
- La fiducia cala: solo il 42% si fida delle recensioni quanto del passaparola (79% nel 2020), il 46% diventa sospettoso con
  recensioni che sembrano scritte dall'IA, il 63% si aspetta una risposta del titolare **[Evidenza, dato di un fornitore USA]**
  ([BrightLocal 2025](https://www.brightlocal.com/research/local-consumer-review-survey-2025/)). Mancano dati italiani.
- I quattro fattori di credibilità: qualità del design, **trasparenza immediata** (prezzi, condizioni, chi c'è dietro),
  contenuto completo e aggiornato, collegamento al resto del web **[Evidenza]** ([NN/g, Trustworthy Design](https://nngroup.com/articles/trustworthy-design/)).
- Si guardano le foto di persone vere dell'azienda e di prodotti; si saltano quelle di repertorio **[Evidenza]**
  ([NN/g, Photos as Web Content](https://www.nngroup.com/articles/photos-as-web-content/)).
- E-commerce: il 19% ha abbandonato un checkout perché non si fidava con la carta; incorniciare i campi della carta (bordo,
  sfondo distinto, lucchetto) aiuta; difetti grafici anche non correlati fanno sospettare phishing **[Evidenza]**
  ([Baymard, Perceived Security](https://baymard.com/blog/perceived-security-of-payment-form)).

**Regole operative [Prassi]**: recensioni vere con nome, data e fonte (meglio collegate al profilo Google), anche poche; non
nascondere quelle da 4 stelle; testimonianze specifiche e attribuite, parola per parola; loghi clienti solo se riconoscibili e
autorizzati; indirizzo, telefono, P.IVA, titolare e prezzi valgono più di qualsiasi bollino. **Nessuna prova va bene**: un
artigiano o un piccolo studio può reggersi su foto e fatti. Si ritorcono contro: tutte 5 stelle senza nomi, testimonianze
con lo stesso tono, contatori gonfiati, "visto su" non verificabili, stock spacciato per il team.

## 3. Moduli

Il checkout medio ha 11,3 campi quando ne basterebbero 8; i campi pesano più dei passi; con nome e cognome separati il 42%
scrive tutto nel primo campo **[Evidenza]** ([Baymard, Checkout Form Fields](https://baymard.com/blog/checkout-flow-average-form-fields)).
Per i servizi locali circa il 60% preferisce telefonare e solo il 4% usa un modulo (dati USA del 2019) **[Evidenza datata]**
([Small Business Trends](https://smallbiztrends.com/2019/05/customer-contact-statistics.html)): offrire sempre più vie
(`tel:`, WhatsApp, modulo, prenotazione online come CTA se il servizio si vende ad appuntamento).

| Modulo di contatto | Regola | Livello |
|---|---|---|
| Campi | 3-4: "Nome e cognome" (uno), un contatto tra telefono ed email, messaggio, eventuale "servizio che ti interessa"; mai più di 6 | [Evidenza] Baymard; [Prassi] |
| Etichette | sempre visibili sopra il campo, il segnaposto non le sostituisce; facoltativi indicati | [Evidenza] ([NN/g, Placeholders](https://www.nngroup.com/articles/form-design-placeholders/)) |
| Validazione | all'uscita dal campo, mai su un campo vuoto; errore accanto al campo, in testo, tolto appena corretto; focus sul primo errore all'invio | [Evidenza] ([Baymard, Inline Validation](https://baymard.com/blog/inline-form-validation)) |
| Errore | nomina il campo e dice cosa scrivere; `aria-invalid` e `aria-describedby`; il colore non è l'unico segnale | [Evidenza] ([CMS Design System](https://design.cms.gov/v/9.0.0/patterns/Forms/validation)) |
| Misure | campi alti 48 px, testo ≥ 16 px (sotto iOS fa zoom), una colonna sotto 640 px | [Prassi] (TasteSkill) |
| Codice | `type`, `inputmode`, `autocomplete` giusti; incolla sempre permesso | [Prassi] |
| Pulsante | dice cosa succede: "Invia la richiesta, ti rispondo entro 24 ore" | [Prassi] |
| Stato | una riga `role="status"` sotto il pulsante: "Invio…", poi l'esito; se fallisce si tiene tutto ciò che è scritto; conferma solo dopo un invio vero; mai una finestra modale; mai `action="#"` | [Prassi] (TasteSkill) |
| Privacy | link all'informativa; casella separata e non spuntata solo per newsletter o marketing | [Prassi] |

I moduli a più passi (+59% secondo HubSpot, senza metodo) sono un'ipotesi da testare, utile solo per preventivi complessi
**[Opinione]** ([HubSpot](https://blog.hubspot.com/marketing/multi-step-forms)).

## 4. Testi: brevi, oggettivi, verificabili

Il 79% scorre e solo il 16% legge parola per parola; dimezzare le parole aumenta l'usabilità del 58%, renderle scansionabili
del 47%, oggettive del 27%, tutto insieme del 124% **[Evidenza]** ([NN/g, How Users Read on the Web](https://www.nngroup.com/articles/how-users-read-on-the-web/)).
Le pagine scritte a livello da scuola media convertono all'11,1% contro il 5,3% di quelle "professionali" **[Evidenza,
correlazione di un fornitore]** ([Unbounce 2024](https://unbounce.com/conversion-benchmark-report/)). Prima l'informazione più
importante **[Evidenza]** ([NN/g, Inverted Pyramid](https://www.nngroup.com/articles/inverted-pyramid/)).

**Regole [Prassi]**
- Ogni affermazione è verificabile (numeri, tempi, nomi, luoghi, materiali, processi) e passa la prova: **un concorrente
  potrebbe scriverla identica?** Se sì, si riscrive con un fatto del cliente.
- Parole vietate se non seguite da una prova: qualità, professionalità, passione, eccellenza, soluzioni, a 360 gradi,
  innovativo, su misura, leader.
- 3-5 obiezioni reali (da chiamate, email, recensioni) con la risposta vicino alla CTA.
- Microcopy che risponde all'ansia del momento ("Nessun pagamento ora", "Rispondo entro 24 ore lavorative", se vero).
- La landing ripete la promessa e le parole dell'annuncio che porta lì.
- Il posizionamento (alternative, attributi unici, valore, clienti a cui importa, categoria; April Dunford) si fa prima di
  scrivere la home.

### Mosse per parte della pagina **[Prassi]** (TasteSkill `copy-moves.md`, da siti professionali 2014-2021)

| Parte | Mossa |
|---|---|
| H1 | 2-9 parole, una proposizione, nomina la categoria: categoria + pubblico ("Gestionale paghe per studi di Roma"), categoria + luogo ("Forno in via Roma, Lodi"), categoria + promessa vera e inattesa, categoria + ambito, categoria + luogo + anno (se vero), superlativo stretto e dimostrabile |
| Sottotitolo | servizi: 15-30 parole, un fatto o un meccanismo; un luogo: il fatto con gli orari, ≤ 80 caratteri. Le forme "stato del lettore", "il nemico", "novità" vanno qui o nella chiusura, sempre con un fatto |
| Titoli di sezione | il nome della parte con un'affermazione sotto ("Camere e prezzi" / "Sei camere, tutte sul lago"); oppure verbo + cosa; mai un comando nudo ("Inizia ora"); domande solo nelle FAQ |
| Chi siamo | partire da un momento vero; aneddoti o cronologia, mai "i nostri valori: qualità, passione"; fallimenti e fortuna se veri; fondatori come persone; valori come comportamenti con numeri; finire al presente modesto; dire come raggiungerli |
| Servizi | il meccanismo in passi con verbi; prima il risultato, poi la funzione come prova; valori reali negli esempi (tempi, misure, importi); nomi di pacchetti usati sempre uguali |
| Prove | solo dal cliente; i superlativi li dicono gli altri, con attribuzione; meglio grezzo che levigato; una regola al posto di un'affermazione ("ogni telaio lo salda chi ti ha misurato") |
| Prezzi, FAQ, prenotazione | il tono scende ai fatti; extra con prezzo; inversione del rischio solo se vera; ammettere i limiti; rispondere all'obiezione vera in modo secco |
| Chiusura | ripete la promessa dell'hero con un fatto e la CTA parola per parola |
| Microcopy | errore che nomina il campo; conferma con le parole del pulsante e i tempi; 404 che rimanda a menu e orari |
| Piè di pagina | solo fatti: marchio, anno corrente, privacy, termini, indirizzo, orari |
| Numeri e umorismo | numeri dispari e umani battono tondi e grandi; ogni numero in una frase; umorismo su di sé e nel microcopy, mai su acquisti seri |

### Segnali di testo da IA **[Opinione di professionisti]**

Un segnale da solo prova poco: contano i gruppi e le ripetizioni. L'elenco cambia con ogni generazione di modelli: si impara
il perché (il modello sceglie la frase che va bene per più pagine), non la lista. Il rimedio è sempre un fatto del cliente.

**Prima ondata** (parole e frasi): elevare, sbloccare, potenziare, liberare il potenziale, senza intoppi, all'avanguardia,
rivoluzionario, trasformativo, olistico, di nuova generazione, di livello mondiale, sinergia, sfruttare, reinventare,
potente, robusto, senza pari, ecosistema, panorama, viaggio (se non è un viaggio), "nel cuore di", "dove X incontra Y",
"il mondo di"; "Nel mondo frenetico di oggi", "Scopri il potere di", "Il futuro di X è qui", "Di' addio a", "Che tu sia A o
B", "Unisciti a migliaia di", "Immagina un mondo in cui", "Pronto a trasformare…?", "Non cercare oltre", "a portata di
clic", "Non è solo X, è Y". Residui: "[Nome azienda]", lorem ipsum, asterischi visibili. Le parole letterali del mestiere
restano.

**Seconda ondata** (sembrano buoni testi, per questo passano):

| Segnale | Limite | Rimedio |
|---|---|---|
| Voce della casa: calda, ironica, modesta, un po' letteraria, uguale per tutti | — | registro scelto per cliente |
| Dettagli inventati per sembrare concreti ("alle 6:12 dalla finestra", "lotto n. 047") | vietati | solo fatti del cliente, o una frase più semplice |
| Striscia di 3-4 numeri con un'etichetta di una parola sotto l'hero | — | ogni numero nella frase che dimostra |
| Titoli "X. Y." ("Dodici camere. Tre modi di stare.") | 1 per pagina | nome + affermazione, verbo + cosa |
| Titoli a coppia di numeri ("Quattro progetti, quattro problemi") | 0-1 | dire cosa contiene la sezione |
| "Non X ma Y" e sostituti ("invece di", "anziché", "senza il") | 2 in tutto | il fatto positivo da solo |
| Serie di negazioni ("Niente moduli, niente attese") | 1 | solo se ogni voce si verifica |
| Parole di virtù su se stessi (onesto, davvero, con cura, affidabile, semplicemente) | vietate | mostrarlo con un fatto o un'ammissione |
| Battuta secca a fine paragrafo; firma nel footer ("Fatto a Roma, dal 1998") | — | finire sull'informazione |
| Storia d'origine a stampo ("Nel 1998 due amici trovarono…") | — | la storia vera, o nessuna sezione storia |
| Testimonianze levigate: tre, ognuna con numero e chiusa | — | solo citazioni vere, parola per parola |
| Cast di nomi e aziende da esempio (Marco R., Giulia B., Acme) | vietati | nomi solo dal cliente |
| Schema fisso: etichetta, titolo, sottotitolo, 3-4 schede, in ogni sezione | — | forma decisa dalle domande del lettore |
| Tempi di risposta e "dal [anno]" ripetuti; cifre tonde senza fonte ("3x", "10.000+") | 1 volta | solo dati del cliente con l'unità |
| Uniformità perfetta (ogni scheda della stessa lunghezza) | — | le parole dove il cliente ha più materiale |
| La pagina che parla di sé ("In questa sezione", "Ecco 3 motivi") | vietata | — |
| Anno del copyright vecchio | vietato | anno corrente |

**Correzioni eccessive** (le regole stesse producono nuovi segnali): vietare i trattini lunghi produce frasi spezzate (usare
due punti e parentesi); vietare l'enfasi produce parole calme come "con cura" (mettere un fatto); evitare i tre produce tutto
a coppie (elencare quante cose ci sono); "sii specifico" produce numeri inventati; frasi brevi a raffica (una frase per
sezione può essere lunga). **Non sono segnali**: grammatica perfetta, "è" e "ha", un elenco di tre se le cose sono tre, testo
scritto dal cliente, vendere su una pagina di vendita purché su fatti.

## 5. Prezzi, urgenza e pratiche vietate nell'UE

Le interfacce ingannevoli sono già vietate dalla direttiva sulle pratiche commerciali sleali e dalla direttiva Omnibus
(recensioni false vietate, **prezzo più basso dei 30 giorni precedenti** in ogni annuncio di sconto) **[Evidenza, norma]**
([Direttiva 2019/2161](https://eur-lex.europa.eu/eli/dir/2019/2161/oj)); per le piattaforme dall'art. 25 del DSA
([Regolamento 2022/2065](https://eur-lex.europa.eu/eli/reg/2022/2065/oj)). Il Digital Fairness Act (proposta dell'11/11/2026,
62 pratiche vietate di cui 10 dark pattern sempre vietati) è in discussione e può cambiare **[Evidenza, proposta]**
([Parlamento europeo](https://www.europarl.europa.eu/legislative-train/theme-protecting-our-democracy-upholding-our-values/file-digital-fairness-act)).

**Mai**: timer che si azzerano, "ultimi 2 posti" non veri, prezzi barrati non praticati, recensioni inventate o filtrate,
caselle preselezionate, frasi che fanno vergognare chi rifiuta ("No, non voglio risparmiare"), costi che compaiono solo al
pagamento. L'urgenza si scrive con una data vera. Per i servizi almeno un "a partire da" o 2-3 pacchetti con cosa includono:
nessuno studio ne misura l'effetto, ma la trasparenza è un fattore di credibilità documentato **[Prassi]**.

## 6. Misurare senza A/B test

Mediana di conversione 6,6% sulle landing Unbounce (e-commerce 4,2%, servizi professionali 6,1%; l'83% delle visite da
mobile) **[Evidenza, dato di un fornitore]** ([Unbounce](https://unbounce.com/landing-page-articles/what-is-a-good-conversion-rate/)):
vale per landing di campagna, non per una home. Un A/B test serio richiede centinaia di conversioni per variante (circa 592
per un effetto del 20%) **[Evidenza]** ([Convert](https://convert.com/blog/a-b-testing/i-dont-have-enough-traffic-to-a-b-test-now-what/)).
Per un piccolo sito **[Prassi]**: ogni azione di contatto come evento chiave separato in GA4 (clic su `tel:`, WhatsApp,
email, invio riuscito, prenotazione, "indicazioni"); poi 5 persone del pubblico che provano a "trovare il prezzo e chiedere
un preventivo", test dei 5 secondi sulla proposta di valore; cambiamenti grandi uno alla volta, confronto prima/dopo.
