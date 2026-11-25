# Ispirazione e riferimenti

Da leggere nella fase 4. Livelli: **[Evidenza]**, **[Prassi]**, **[Opinione]**. Si copia un principio, mai una pagina.

## 1. Due tipi di galleria

| Gruppo | Gallerie | A cosa servono | Attenzione |
|---|---|---|---|
| **Mestiere visivo** | Awwwards, Godly (forse rinominata "Recent", fonte secondaria), SiteInspire, Minimal Gallery, Typewolf, Fonts In Use | direzione estetica, tipografia, apertura, movimento | Awwwards vota Design 40%, Usabilità 30%, Creatività 20%, Contenuti 10% e **non misura la conversione** **[Evidenza]** ([Awwwards](https://www.awwwards.com/about-evaluation/)); molti di quei siti sono "splendidi e convertono malissimo" ([Colorlib](https://colorlib.com/wp/showcase-inspiration-sites-web-design/)) |
| **Siti in uso** | Land-book (filtrabile per settore), Mobbin (flussi completi), Refero | decisioni di UX, struttura, sezioni per settore | il livello medio è più basso: servono per capire cosa funziona, non per il gusto |

Esistono anche gallerie per singolo componente (hero, navigazione, CTA, footer, pagine 404) **[Prassi]**
([softwarethug.com](https://softwarethug.com/posts/web-design-inspiration-sites-categorized/)).

## 2. Procedura **[Prassi]**

1. **Archivio del gusto** di chi usa la skill (`locale/gusto.md`, se esiste): riferimenti già approvati, tratti comuni,
   bocciature con la causa. Si parte da lì.
2. **Land-book per settore** e Mobbin o Refero per i flussi: come risolvono gli altri lo stesso problema.
3. **SiteInspire, Godly, Awwwards** per la direzione: cercare per tipo di sito e livello di esperienza, non per moda.
4. **Typewolf o Fonts In Use** per abbinamenti di caratteri reali.
5. **Concorrenti diretti del cliente** (`concorrenti-e-strumenti.md`) e i migliori del settore fuori dall'Italia.
6. Tenere **6-10 riferimenti** e per ognuno scrivere **cosa si prende** (ritmo, tipografia, apertura, gestione delle foto,
   movimento, header) e **cosa si lascia**. Mai "fallo come questo sito".

Per un sito di servizi locale le gallerie di premi, che premiano esperienza e WebGL, sono meno utili dei concorrenti reali;
per un'agenzia o un livello esperienziale sono il riferimento giusto **[Prassi]**.

## 3. Come annotare un riferimento

```
| Sito | Perché piace (parole di chi l'ha scelto, se ci sono) | Cosa prendere | Cosa lasciare |
| esempio.com | "mi piace l'apertura" | titolo gigante sopra una foto scura; header a pillola | il corpo scuro uniforme, i testi lunghi in grigio |
```

Poi i **tratti comuni** tra i riferimenti (per esempio: un solo momento visivo forte, caratteri giganti, scorrimento che
racconta, pochi colori usati in grande, materiale fatto apposta): sono la direzione più affidabile, più del singolo sito.

## 4. Catturare i riferimenti

- Statici: `scripts/py.sh cattura_concorrenti.py <url...> --out <cartella> --etichetta riferimenti` (prima schermata,
  telefono, colori, font, punteggio IA).
- **Con movimento**: `scripts/py.sh cattura_scorrimento.py <url> --out <cartella> [--fotogrammi 12]` salva fotogrammi
  dello scorrimento a 1440×900 e un foglio da 4 colonne: si vede cosa succede scorrendo (testo che si rivela, capitoli di
  foto, sezioni fissate). `--webgpu` apre un browser visibile per i siti 3D che richiedono WebGPU.
- Alcuni siti rifiutano il browser automatico (risposta vuota o errore HTTP/2 anche dopo la riprova): lo script scrive
  `errore.txt` senza fermarsi; quei siti si catturano a mano dal browser.
- Si conservano le catture: servono per confrontare la pagina finita con i riferimenti nel controllo estetico.

## 5. Trend: strutturali contro stilistici

I report dei fornitori (Figma 2026: 3D, colori vivi, tipografia espressiva, tema scuro, movimento, neo-brutalismo,
massimalismo) includono tutto senza dire quando non usare un trend ([Figma](https://www.figma.com/resource-library/web-design-trends/)).
Più utili i verdetti degli studi **[Opinione ben argomentata]** ([Metabole Studio](https://metabole.studio/en/blog/web-design-trends-2026)):
sì a illustrazione fatta a mano e texture analogiche, minimalismo editoriale, scrollytelling solo per contenuti narrativi,
micro-interazioni che chiariscono uno stato, font variabili, prestazioni e WCAG dal wireframe; no a bento grid forzate sui
siti di servizi, glassmorphism, tema scuro come default, neo-brutalismo per marchi che vivono di fiducia, 3D se il prodotto
non è fisico, gradienti pesanti. "Una transizione memorabile batte venti dimenticabili".

Regola: i trend **strutturali** (tipografia portante, prestazioni, accessibilità, foto e materiale veri, movimento che
risponde alle azioni) entrano nella base; quelli **stilistici** datano il sito appena passa la moda, e **un trend assorbito
dall'IA diventa subito un segnale da IA** (`segnali-ia.md`).
