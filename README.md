# design-senza-ia

Una skill per Claude Code che progetta **siti belli, specifici per il cliente e che non sembrano fatti con l'intelligenza
artificiale**, corretti per SEO, accessibilità, velocità e leggi italiane ed europee. In italiano, pensata per chi fa siti a
piccole imprese, studi professionali, negozi e agenzie.

Il "look da IA" non è un font o un colore: è la somma di tante scelte predefinite che nessuno ha deciso. Vietarle una per una
non basta, perché il modello passa alla successiva; e togliere i difetti non basta, perché una pagina pulita può restare
anonima. Questa skill parte dal **materiale vero del cliente**, sceglie **tipo di sito e livello di esperienza** in base al
cliente, **decide ogni scelta con un motivo** e **misura** il risultato con tre controlli.

## Cosa fa

1. **Brief**: tipo di sito (vetrina, servizio, landing di prodotto, e-commerce, esperienziale), obiettivo e CTA, traffico,
   livello di esperienza (sobrio e curato, immersivo, esperienziale) con il motivo.
2. **Analisi** del sito attuale e dei concorrenti, con schermate, colori misurati, font, contenuti e punteggi.
3. **Riferimenti** da gallerie e da un archivio del gusto personale, anche con i fotogrammi dello scorrimento dei siti animati.
4. **Tre direzioni**, ognuna con un piccolo sistema visivo (colori con un ruolo, caratteri non predefiniti, una sola mossa
   audace) e la verifica "con un altro cliente arriverei allo stesso piano?".
5. **Struttura, testi e asset**: ordine delle sezioni per tipo di sito, testi senza i segnali da IA, foto vere, icone su
   misura, logo solo su richiesta.
6. **Costruzione** di un'anteprima HTML con SEO, accessibilità, velocità e privacy dentro dal primo file, e le note per
   rifarla in WordPress con Elementor.
7. **Tre controlli**: segnali da IA (script con punteggio), qualità estetica (otto punti, guardando le schermate),
   tecnico e legale (script con errori e avvisi).

Ogni regola nei `references/` ha la fonte e il livello della prova: **[Evidenza]**, **[Prassi]** o **[Opinione]**.

## Installazione

```bash
git clone https://github.com/fraberret/design-senza-ia ~/.claude/skills/design-senza-ia
```

Gli script richiedono Python 3 con Playwright e Pillow. Il lanciatore `scripts/py.sh` cerca da solo un Python adatto; se
non lo trova, stampa il comando per crearne uno nella cartella della skill:

```bash
cd ~/.claude/skills/design-senza-ia
python3 -m venv .venv && .venv/bin/pip install playwright pillow
PLAYWRIGHT_BROWSERS_PATH=.venv/ms-playwright .venv/bin/python -m playwright install chromium
```

`py.sh` è scritto per zsh (macOS); su Linux installa zsh o lancia gli script direttamente con il Python del venv.

## Uso

Basta chiederlo a Claude con parole tue ("rifai la home di https://…", "questa pagina sembra fatta con l'IA", "analizza
i concorrenti di …"): la skill si attiva da sola. Gli script si possono usare anche a mano:

```bash
S=~/.claude/skills/design-senza-ia/scripts
$S/py.sh analizza_sito.py https://esempio.it --out lavoro/analisi
$S/py.sh cattura_concorrenti.py https://a.it https://b.it --out lavoro/analisi
$S/py.sh cattura_scorrimento.py https://studio-animato.example --out lavoro/riferimenti/studio --fotogrammi 12
$S/py.sh controllo_slop.py lavoro/home-v1.html --out lavoro/controllo-v1 --soglia 80
$S/py.sh controllo_tecnico.py lavoro/home-v1.html --out lavoro/tecnico-v1
```

- `controllo_slop.py` scrive `controllo.md` con il punteggio da 0 a 100, i segnali trovati (dove sono e cosa fare), il
  conteggio per gruppo delle co-occorrenze, una riga tecnica e una di finitura, più le schermate. Un segnale scelto di proposito si dichiara con `--accetta id1,id2`.
- `controllo_tecnico.py` scrive `tecnico.md` e `tecnico.json`: contrasti (WCAG 2.2, "a occhio" sopra foto e gradienti),
  bersagli tattili, sbordamenti a 360/390/1440 px, testi piccoli, meta viewport, H1, lingua, title, description, canonical, Open Graph,
  JSON-LD, alt, dimensioni delle immagini, immagine principale in lazy-load, richieste a terzi prima del consenso, formato
  dei font, movimento ridotto, testo senza JavaScript, P.IVA, link `tel:`.
- `cattura_scorrimento.py` salva i fotogrammi dello scorrimento e un foglio di confronto; `--webgpu` apre un browser
  visibile per i siti 3D.
- Test degli script: `scripts/py.sh tests/test_<nome>.py`.

### Convenzioni personali e archivio del gusto

Se nella cartella della skill crei un file `locale.md`, Claude lo legge prima di cominciare: dove salvare i lavori, dove
tieni le guide di stile, quali strumenti usi. Nella cartella `locale/` puoi tenere un **archivio del gusto** (`locale/gusto.md`):
i siti che ti piacciono con cosa prendere da ciascuno, i tratti comuni, e ogni anteprima bocciata o approvata con la causa.
La skill lo legge prima di scegliere una direzione e ci confronta la pagina finita. Entrambi sono esclusi da Git.

## Limiti dei controlli

Il punteggio misura forme e ripetizioni, non il gusto: le schermate vanno sempre guardate, e il controllo estetico resta un
giudizio. Il controllo tecnico non sostituisce la prova con la tastiera, con un lettore di schermo e i dati reali di
PageSpeed. È tarato su siti di attività e
servizi. I siti di prodotti tech (Linear, Stripe) usano di proposito molti di questi schemi e prendono punteggi bassi
senza essere fatti con l'IA. Spaziature e lettere strette sono riportate ma non tolgono punti, perché le sbagliano anche
ottimi studi.

## Crediti

- Il catalogo dei segnali (`references/segnali-ia.md`) è adattato e ampliato da
  [Signs of AI design](https://github.com/febbhav/signs-of-ai-design) (CC BY-SA 4.0) e dalle altre fonti citate nel file.
- Le cinque righe della direzione, i livelli di intervento, la prova dello scambio di nome, alcune regole di finitura e la
  guida alle immagini generate sono adattati da [unslop](https://github.com/heydamir/unslop) di Damir Sokolovsky (CC BY 4.0).
- La seconda ondata di segnali, la "sola mossa audace" e la verifica del piano vengono dalla skill
  [frontend-design](https://github.com/anthropics/skills) di Anthropic (Apache 2.0).
- Segnali di testo, mosse per parte della pagina, token di movimento, "momenti", regole su foto, pesi e loghi di terzi e
  alcuni caratteri sono adattati da [TasteSkill](https://github.com/Leonxlnx/taste-skill) 2.5.1 (MIT, © 2026 Leonxlnx).
- Disciplina delle icone, indicazioni su GSAP e metadati delle licenze dei font vengono da
  [UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) (MIT, © 2024 Next Level Builder). Note di licenza complete in `LICENSE`.
- Le regole con le soglie vengono da una ricerca su fonti primarie (NN/g, Baymard, W3C, Google, web.dev, norme UE e
  italiane), citate riga per riga nei `references/`.

## Licenza

Testi (`SKILL.md`, `references/`): [CC BY-SA 4.0](LICENSE-CC-BY-SA-4.0.txt). Script (`scripts/`): MIT. Dettagli in
[LICENSE](LICENSE).

Di [Francesco Berretta](https://github.com/fraberret).
