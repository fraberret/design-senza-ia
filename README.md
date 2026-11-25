# design-senza-ia

Una skill per Claude Code che rifà o crea siti, landing page e grafiche **che non sembrano fatti con l'intelligenza
artificiale**. In italiano, pensata per i siti di attività e studi professionali.

Il "look da IA" non è un font o un colore: è la somma di tante scelte predefinite che nessuno ha deciso. Etichetta
maiuscola sopra ogni titolo, tre schede uguali con l'icona nel cerchio, parola colorata nel titolo, comparsa dal basso
allo scorrimento, stesso arrotondamento ovunque. Vietarle una per una non basta, perché il modello passa alla successiva.
Questa skill parte invece dal **materiale vero del cliente**, **decide ogni scelta con un motivo** e **misura** il
risultato.

## Cosa fa

Dall'indirizzo del sito al risultato controllato, quasi senza intervento:

1. **Analizza il sito attuale**: schermate su computer e telefono, colori misurati sui pixel, font, testi, contatti, video,
   pagine interne.
2. **Trova e cattura i concorrenti**, con il loro punteggio.
3. **Fa l'inventario del materiale vero**: logo, foto, video, testi, fatti. Quello che manca si chiede, non si inventa.
4. **Decide quanto cambiare** (rifacimento, ritocco o quasi niente) e propone **tre direzioni**, ognuna in cinque righe:
   attività, carattere, mondo, momenti, firma.
5. **Costruisce** la pagina con regole precise di composizione e di finitura.
6. **Controlla** la pagina con uno script che conta i segnali da IA, dà un punteggio da 0 a 100 e dice come correggere
   ogni segnale. Si ripete finché il punteggio supera la soglia e quello di tutti i concorrenti.

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
$S/py.sh controllo_slop.py lavoro/home-v1.html --out lavoro/controllo-v1 --soglia 80
```

`controllo_slop.py` scrive `controllo.md` con il punteggio, i segnali trovati (con dove sono e cosa fare), una riga
tecnica (sbordamenti, H1, testi piccoli) e una riga di finitura (spaziature, lettere strette), più le schermate su computer
e telefono. Un segnale scelto di proposito si dichiara con `--accetta id1,id2`.

### Convenzioni personali

Se nella cartella della skill crei un file `locale.md`, Claude lo legge prima di cominciare. È il posto per le tue
convenzioni: dove salvare i lavori, dove tieni le guide di stile, quali strumenti usi per le immagini. È escluso da Git.

## Limiti del punteggio

Il punteggio misura forme e ripetizioni, non il gusto: le schermate vanno sempre guardate. È tarato su siti di attività e
servizi. I siti di prodotti tech (Linear, Stripe) usano di proposito molti di questi schemi e prendono punteggi bassi
senza essere fatti con l'IA. Spaziature e lettere strette sono riportate ma non tolgono punti, perché le sbagliano anche
ottimi studi.

## Crediti

- Il catalogo dei segnali è adattato e ampliato da [Signs of AI design](https://github.com/febbhav/signs-of-ai-design)
  (CC BY-SA 4.0) e da altre fonti citate in `references/catalogo-segnali.md`.
- Le cinque righe della direzione, i livelli di intervento, la prova dello scambio di nome, alcune regole di finitura e la
  guida alle immagini generate sono adattati da [unslop](https://github.com/heydamir/unslop) di Damir Sokolovsky
  (CC BY 4.0).

## Licenza

Testi (`SKILL.md`, `references/`): [CC BY-SA 4.0](LICENSE-CC-BY-SA-4.0.txt). Script (`scripts/`): MIT. Dettagli in
[LICENSE](LICENSE).

Di [Francesco Berretta](https://github.com/fraberret).
