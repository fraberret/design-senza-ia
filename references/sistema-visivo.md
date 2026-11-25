# Sistema visivo: colore, layout, tipografia

Da leggere nelle fasi 5 (direzione) e 8 (costruzione). Livelli: **[Evidenza]**, **[Prassi]**, **[Opinione]**.
Principi della skill `frontend-design` di Anthropic (Apache 2.0) e regole di TasteSkill 2.5.1 (MIT) dove indicato.

## 1. Un piccolo sistema per ogni direzione

Ogni direzione ha un sistema scritto prima di costruire **[Prassi]**:
- **4-6 colori con nome e ruolo** (fondo, superficie, testo, testo attenuato, colore del marchio, azione), misurati dal
  materiale vero del cliente;
- **1-2 famiglie di caratteri** non predefinite, con il motivo legato al cliente;
- una **scala** di dimensioni e di spaziature, **2-3 raggi**, le regole del movimento per il livello scelto;
- **una sola mossa audace**: il punto dove si spende il coraggio (caratteri enormi, un colore pieno a tutta pagina, una
  composizione sghemba, un oggetto in movimento). Tutto il resto è sobrio e disciplinato **[Opinione ben argomentata]**
  ([anthropics/skills, frontend-design](https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md)).

**Verifica del piano** (da frontend-design): prima di costruire, chiedersi "con un altro cliente dello stesso settore
arriverei allo stesso piano?". Se sì, il piano è la media: si cambia partendo da ciò che solo questo cliente ha (materiale,
luogo, mestiere, parole) **[Prassi]**.

**Pochi colori, usati in grande.** Un sistema trattenuto non è una pagina grigia: due colori del marchio usati in grande
(blocchi pieni, una fascia, la parola chiave del titolo) fanno più carattere di otto colori piccoli, che fanno arcobaleno.
Una pagina neutra al 95% con un accento minuscolo rischia di sembrare vuota **[Opinione]**.

## 2. Colore e contrasto

Le soglie obbligatorie sono quelle di **WCAG 2.2 AA** **[Evidenza, norma]**: **4,5:1** per il testo normale, **3:1** per il
testo grande (≥ 24 px, o ≥ 18,66 px in grassetto), senza arrotondamenti (4,499:1 non passa); le linee guida del marchio non
esentano il testo, solo i loghi ([W3C, Understanding 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)).
Il criterio 1.4.11 chiede **3:1** per bordi dei campi, icone funzionali, indicatori di focus e parti di grafici
([W3C, Understanding 1.4.11](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html)). APCA (Lc 90 preferito per
il testo corrente, 75 minimo per i blocchi, 60 per testo non in blocco, 45 per titoli grandi, 15 per divisori) è un controllo
percettivo in più **[Prassi]** ([APCA in a Nutshell](https://git.apcacontrast.com/documentation/APCA_in_a_Nutshell)), ma
non fa parte di WCAG 3, ancora senza algoritmo di contrasto ([Adrian Roselli, aprile 2026](https://adrianroselli.com/2026/04/wcag3-contrast-as-of-april-2026.html)).
Regola: **si passa WCAG 2.2; APCA si usa in aggiunta**, per esempio per non usare bianco puro su nero puro in un titolo enorme.

| Palette | Regola | Livello |
|---|---|---|
| Origine | colori misurati dal materiale vero del cliente (logo, insegna, prodotto, foto, sede) | [Prassi] |
| Struttura | 1 neutro tinto verso il marchio (10-12 gradini) + 1 colore del marchio (10-12) + 3-4 semantici (successo, avviso, errore, info) con 3-5 gradini | [Prassi] ([Refactoring UI](https://www.refactoringui.com/previews/building-your-color-palette); [Radix Colors](https://www.radix-ui.com/colors/docs/palette-composition/understanding-the-scale)) |
| Gradini | si parte dal 500 (deve reggere come sfondo di un pulsante) verso 900 (testo) e 100 (sfondo tenue); mai schiarire "al volo" | [Prassi] |
| Spazio colore | OKLCH: a parità di L il contrasto resta stabile cambiando tinta; stati con i colori relativi (`oklch(from var(--accent) calc(l - 0.1) c h)`) | [Evidenza] ([Evil Martians, OKLCH](https://evilmartians.com/chronicles/oklch-in-css-why-quit-rgb-hsl)) |
| In pagina | una o due tinte sature, usate in grande; il resto dalle variazioni di luminosità | [Prassi] |
| Token | custom properties semantiche (`--bg`, `--surface`, `--text`, `--text-muted`, `--accent`, `--border`) | [Prassi] |
| Verifica | testo 4,5:1 (grande 3:1), bordi, icone e focus 3:1; il colore non è mai l'unico segnale | [Evidenza] |
| Tema scuro | superficie scura non nera, accenti più chiari e desaturati, elevazione con superfici più chiare; facoltativo per un sito locale, ma il sito non deve rompersi con il tema scuro di sistema | [Prassi] ([Material, Dark theme](https://m2.material.io/design/color/dark-theme)) |

La regola **60-30-10** viene dall'arredamento e non ha studi dietro **[Opinione]** ([Living Etc](https://www.livingetc.com/us/ideas/60-30-10-rule)).
Non esistono studi affidabili su colori e settori ("blu per la finanza"): non si afferma.

**Testo sopra le foto** **[Prassi]** (TasteSkill): solo nell'hero e in una fascia di chiusura, su un taglio con una zona calma
e scura anche nel taglio da telefono, oppure su un riquadro pieno; il contrasto non si calcola, va guardato sulle schermate
(`controllo_tecnico.py` lo segna "a occhio").

## 3. Layout, griglie, spaziature, gerarchia

- Gerarchia con dimensione, peso, contrasto e raggruppamento, in pochi livelli: **al massimo 3 livelli di dimensione e 2
  elementi grandi per schermata**; **test della sfocatura** (sfocare di 5-10 px mostra cosa domina) **[Evidenza]**
  ([NN/g, Visual Hierarchy](https://www.nngroup.com/articles/visual-hierarchy-ux-definition/)).
- Poco spazio tra un titolo e il suo contenuto, molto tra i gruppi; progettare prima in grigio e mettere il colore alla fine;
  spaziature su base 4 o 8 px (4, 8, 16, 24, 32, 48, 64…) **[Prassi]** ([Refactoring UI](https://rjseymour66.github.io/webdev/refactoring-ui/)).
- Misura della colonna di testo: 45-75 caratteri, mai oltre 60ch; primitive flessibili invece di misure fisse **[Prassi]**
  ([Every Layout](https://every-layout.dev/rudiments/axioms/)).
- Caratteri e spaziature fluidi con `clamp()` tra una scala per schermo piccolo e una per schermo grande **[Prassi]**
  ([Utopia](https://utopia.fyi/blog/designing-with-fluid-type-scales/)).
- Raggi e ombre: stesso raggio su tutto e schede identiche con la stessa ombra morbida sono segnali di template
  **[Opinione convergente]** ([Capital & Compute, 2026](https://capitalandcompute.net/blog/fix-ai-slop-design/)). Regola:
  2-3 raggi legati al ruolo (piccolo per input e pulsanti, medio per le schede, zero o pieno per immagini e pillole); insiemi
  di partenza: spigoloso 4/6/8, morbido 8/12/20, tondo 10/16/24 (TasteSkill); 2-3 livelli di ombra con un significato; raggio
  dei figli mai maggiore del contenitore **[Prassi]** ([Vercel](https://vercel.com/design/guidelines)).
- Schede solo quando gli elementi sono davvero paralleli e confrontabili; altrimenti liste, tabelle, layout asimmetrici;
  alternare sezioni dense e ariose, larghezze piene e contenute **[Prassi]**.
- Punti di rottura scelti sul contenuto, non sui dispositivi **[Prassi]**.
- Pulsanti **[Prassi]** (TasteSkill): alti 44 px (48 nella barra del telefono), etichetta 16 px, 24 px di margine laterale;
  al massimo due affiancati; un solo pulsante pieno per vista; mai inclinati, in gradiente, "fantasma" o con ombra; a tutta
  larghezza su telefono.

## 4. Tipografia

| Parametro | Valore | Fonte |
|---|---|---|
| Corpo | 16-20 px; 17-18 px desktop, mai sotto 16 px su telefono | [Prassi] ([Practical Typography](https://practicaltypography.com/summary-of-key-rules.html)) |
| Note, legale, etichette | mai sotto 13 px; grigio attenuato (≥ 4,5:1) solo qui | [Prassi] (TasteSkill) |
| Lunghezza riga | 45-75 caratteri, ideale 66; `max-width: 33em` o 60-70ch | [Prassi] ([webtypography.net](http://webtypography.net/2.1.2)) |
| Interlinea | corpo 1,45-1,6; titoli grandi 1,05-1,2 | [Prassi] |
| Maiuscole | spaziatura +5-12%; tutto maiuscolo solo per meno di una riga | [Prassi] |
| Paragrafi | rientro oppure spazio, non entrambi | [Prassi] |
| Scala | rapporto ~1,2 su telefono, 1,25-1,333 su desktop, con `clamp()`; 5-6 passi | [Prassi] ([Utopia](https://utopia.fyi/blog/designing-with-fluid-type-scales/)) |
| Famiglie e pesi | 1-2 famiglie, 3-4 pesi in totale | [Prassi] |
| Coerenza | una sola misura per tipo di elemento; un numero non supera mai H2 o H1, neanche a 390 px; mai testo dentro un'immagine | [Prassi] (TasteSkill) |
| Enfasi | con il contrasto, non con evidenziatori colorati; colore dentro una parola al massimo una volta per pagina | [Prassi] (TasteSkill) |

**Abbinamenti.** Esaurire prima una famiglia o superfamiglia; un secondo carattere solo se "diverso abbastanza ma non troppo"
**[Prassi]** ([Google Fonts Knowledge](https://fonts.google.com/knowledge/choosing_type/pairing_typefaces_within_a_family_superfamily));
un carattere da titolo pensato per corpi grandi più un carattere da testo con x-height ampia, basso contrasto e corsivo vero
([Typewolf](https://www.typewolf.com/blog/google-fonts-combinations)). Indicazioni per settore **[Prassi, non studi]**: una
sans per professionisti e B2B; serif da testo + sans per legale, consulenza, cultura, artigianato; display serif ad alto
contrasto (solo sopra ~32 px) + sans per moda, cosmetica, ristorazione alta; grotesk condensato pesante per sport, palestre,
officine, edilizia; sans umanista per salute e servizi alla persona; monospace solo come accento per dati e prezzi.

**Caratteri da non usare come default** (senza un motivo esplicito legato al cliente) **[Prassi]**: Inter, Roboto, Open Sans,
Lato, Poppins, Montserrat, Raleway, Space Grotesk, Geist, DM Sans, Plus Jakarta Sans, Manrope, Outfit, Satoshi, Instrument
Serif, Playfair Display, Cormorant, DM Serif Display, Oswald; in particolare "serif display elegante + sans geometrico".
Inter domina l'output dei modelli: è un segnale **per contesto, non per frequenza**; vietato, i modelli ripiegano su Space
Grotesk **[Evidenza]** ([Claude blog](https://www.claude.com/blog/improving-frontend-design-through-skills); [Web Almanac 2025](https://almanac.httparchive.org/en/2025/fonts)).
Il serif elegante sta diventando a sua volta un segnale ([Creative Bloq](https://www.creativebloq.com/design/fonts-typography/why-ai-brands-are-obsessed-with-serif-fonts)).

**Alternative non inflazionate** (licenza da ricontrollare sulla pagina di ogni font prima dell'uso):

| Categoria | Caratteri (licenza) |
|---|---|
| Grotesk / neo-grotesk | Hanken Grotesk, Schibsted Grotesk, Familjen Grotesk, Bricolage Grotesque, Archivo, Onest, Host Grotesk, Mona Sans, Chivo, Epilogue, Reddit Sans, SUSE, Albert Sans, Work Sans, Rethink Sans, Red Hat Display + Red Hat Text, Funnel Display + Funnel Sans (OFL); Switzer, General Sans, Supreme (Fontshare) |
| Umanisti | Source Sans 3, Alegreya Sans, Fira Sans, Commissioner, Atkinson Hyperlegible Next, Proza Libre (OFL) |
| Geometrici e arrotondati, con cautela | Jost, Figtree, Gabarito, Nunito Sans (OFL); Author (Fontshare) |
| Serif da testo | Source Serif 4, Literata, Newsreader, Spectral, Libre Caslon Text, Gelasio, Alegreya, Lora, Besley, Vollkorn, EB Garamond (OFL); Erode, Gambetta, Sentient (Fontshare) |
| Slab | Zilla Slab (OFL) |
| Serif display | Fraunces, Young Serif, Gloock, Bodoni Moda (OFL); Zodiak, Boska, Bespoke Serif (Fontshare) |
| Larghi, condensati e display | Anybody, Big Shoulders Display, Barlow Condensed, Saira Condensed, League Gothic, IBM Plex Sans Condensed (OFL); Clash Display, Tanker, Panchang (Fontshare) |
| Monospace | JetBrains Mono, IBM Plex Mono, Martian Mono, Fragment Mono, Azeret Mono (OFL) |
| Libre d'autore, per titoli | Velvetyne (Le Murmure, Degheest, Savate, Karrik, Basteleur); Collletttivo (Mazius Display, Ribes); League Spartan |

Le aggiunte rispetto alla ricerca (Host Grotesk, Mona Sans, Chivo, Epilogue, Reddit Sans, SUSE, Albert Sans, Work Sans,
Rethink Sans, Red Hat, Funnel, Gabarito, Nunito Sans, Lora, Besley, Vollkorn, EB Garamond, Zilla Slab, Anybody, IBM Plex Sans
Condensed) vengono dalla libreria di TasteSkill e sono OFL secondo i metadati di Google Fonts (revisione 038b637, agosto 2026).

**Licenze [Evidenza]**: la **SIL Open Font License** permette uso commerciale, hosting e modifica, purché il font non sia
venduto da solo ([openfontlicense.org](https://openfontlicense.org/why-use-the-ofl/)); **Fontshare** è gratuito per uso
personale e commerciale con licenza propria: conservare il file di licenza dello zip ([ITF](https://www.indiantypefoundry.com/news/introducing-fontshare));
le **versioni di prova di Pangram Pangram e Production Type non si possono usare in lavori commerciali**
([Pangram Pangram FAQ](https://pangrampangram.com/faq); [Production Type](https://www.productiontype.com/help/free_trial_license)).

## 5. Caricare i caratteri

- **Font sempre ospitati sul proprio dominio**: il Tribunale di Monaco (20/01/2022) ha condannato il caricamento da Google
  per la trasmissione dell'IP senza base giuridica; non vincolante in Italia, ma il principio vale in tutta l'UE **[Evidenza]**
  ([IHK](https://www.ihk.de/bergische/recht-und-steuern/wettbewerbsrecht/google-fonts-5646176)).
- WOFF2 (circa 30% più leggero di WOFF), sottoinsiemi con `unicode-range`, preload solo dei 1-2 file più importanti,
  `font-display: swap` per titoli e marchio, `optional` per il corpo **[Evidenza]** ([web.dev, Font best practices](https://web.dev/articles/font-best-practices));
  fallback calibrati con `size-adjust` e `ascent-override` per non far scattare il layout ([Chrome for Developers](https://developer.chrome.com/blog/font-fallbacks)).
- Ricetta **[Prassi]**: al massimo 2 famiglie, 4 file WOFF2, circa 100-160 KB di font sulla prima pagina; font variabile
  solo da 3 pesi in su; il sottoinsieme `latin` copre l'italiano (à è é ì ò ù, «», ’, €); in Elementor disattivare il
  caricamento remoto e verificare che non partano richieste a `fonts.gstatic.com` (`controllo_tecnico.py`:
  `terzi-al-caricamento`, `font-formato`).

## 6. Regole per l'italiano

- `<html lang="it">`, necessario anche per la sillabazione (`hyphens: auto`) **[Evidenza]** ([MDN, hyphens](https://developer.mozilla.org/en-US/docs/Web/CSS/hyphens)).
- Apostrofo tipografico ’ e accenti veri sulle maiuscole (È, mai E') ([html.it](https://www.html.it/magazine/di-apostrofi-e-virgolette/));
  un sistema di virgolette coerente, per esempio « » con “ ” annidate **[Prassi]**.
- Sillabazione sul corpo ma non sui titoli; `text-wrap: balance` sui titoli e `pretty` sui paragrafi; `tabular-nums` per
  prezzi e tabelle; spazio unificatore tra numero e unità; numeri in un solo formato (`1.250 €` ovunque); pulsanti e menu con
  margine, perché l'italiano è più lungo dell'inglese **[Prassi]**.
