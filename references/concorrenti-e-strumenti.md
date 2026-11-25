# Concorrenti e strumenti di analisi

## Trovare i concorrenti

Obiettivo: 4-8 siti che un potenziale cliente vedrebbe al posto di questo. I riferimenti di gusto (gallerie, studi
creativi, l'archivio del gusto) sono un'altra cosa: `ispirazione.md`. Due gruppi:
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
  `immagini-icone-logo.md`.
- **Skill di supporto**, se installate: `design-motion-principles` (movimento), `emil-design-eng` (finitura), una skill
  di copywriting per i testi lunghi. Le regole utili di TasteSkill, UI/UX Pro Max e unslop sono già dentro questa skill
  (citate nei file `references/`).
- **`scripts/cattura_scorrimento.py`**: fotogrammi dello scorrimento dei siti con movimento (`ispirazione.md`).
- **`scripts/controllo_tecnico.py`**: contrasti, bersagli, SEO di base, terzi prima del consenso; utile anche sul sito
  vecchio del cliente, come argomento nella proposta.
