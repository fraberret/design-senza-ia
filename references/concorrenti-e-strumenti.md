# Concorrenti e strumenti di analisi

## Trovare i concorrenti

Obiettivo: 4-8 siti che un potenziale cliente vedrebbe al posto di questo. Due gruppi:
- **concorrenti diretti**: stessa attività, stessa zona (per le attività locali) o stesso mercato;
- **riferimenti del settore**: i migliori del mestiere a livello nazionale, per capire il livello e la media.

Come cercarli:
1. **Ricerche Google** con le parole che userebbe un cliente: `<servizio> <città>`, `<servizio> <quartiere>`,
   `rivenditore <prodotto> <città>`, `<prodotto> alternative`. WebSearch è centrato sugli USA: per l'Italia è più affidabile
   Google aperto nel browser (Claude in Chrome, profilo giusto per il cliente) con `&hl=it&gl=it`.
2. **Google Maps**: categorie e "Ricerche correlate" nella scheda del cliente.
3. **Elenchi di settore**: i rivenditori del produttore (pagina "partner" o "rivenditori"), associazioni di categoria.
4. Scarta portali, directory e siti fermi da anni; tieni chi vende davvero la stessa cosa.

Poi: `scripts/py.sh cattura_concorrenti.py <url...> --out <cartella>` (aggiungi `--etichetta riferimenti` per i siti di
riferimento). Leggi `concorrenti.md` e guarda `concorrenti-computer.jpg`.

Cosa ricavarne (scrivilo nell'analisi):
- **la media del settore**: cosa fanno tutti (colori, aperture, frasi). È quello da non fare;
- **il migliore**: chi comunica meglio e perché (spesso: foto vere, frasi specifiche, una cosa riconoscibile);
- **lo spazio libero**: cosa nessuno dice o mostra e il cliente ha davvero (un servizio, una storia, una persona, un luogo);
- il **punteggio IA** di ciascuno: il nuovo sito deve superarli tutti.

## Strumenti

- **Gli script della skill** (Playwright, browser invisibile): analisi del sito, cattura dei concorrenti, controllo finale.
  Sono il metodo principale: ripetibili e senza clic.
- **Claude in Chrome**: per pagine che richiedono login, consenso o interazione, e per le ricerche su Google e Maps in
  italiano. Usa il profilo Chrome giusto per il cliente; non accettare cookie per conto dell'utente.
- **Estensione "DESIGN.md Style Extractor" (TypeUI,** github.com/bergside/design-md-chrome**)**, se l'utente l'ha
  caricata in Chrome: estrae colori, font, spaziature e componenti di un sito in un file DESIGN.md. Utile quando l'utente
  vuole un riferimento preciso ("fallo come questo sito"): chiedigli di aprire il sito, cliccare l'estensione e salvare il
  DESIGN.md, poi leggilo. Non si attiva da sola: serve il clic dell'utente.
- **PageSpeed/Lighthouse** (per esempio con una skill SEO e una chiave Google, se presenti): prestazioni e accessibilità del
  sito vecchio, argomento utile nella proposta al cliente.
- **Uno strumento per generare immagini** (un'app web, un server MCP), se serve un momento senza foto vere: vedi
  `immagini-generate.md`.
- **Skill di supporto**, se installate: `ui-ux-pro-max` (ricerca di tavolozze, abbinamenti di font e regole UX per settore,
  da usare come spunto e non come stile), `design-motion-principles` (movimento), `emil-design-eng` (finitura).
  `design-taste-frontend` (TasteSkill) produce pagine rigide e vuote per i servizi: non usarla per costruire, al massimo
  per le sue regole sui testi. `unslop` (heydamir) è pensata per app e dashboard: le sue idee utili sono già qui dentro.
