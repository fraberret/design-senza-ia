# Movimento e telefono

Da leggere nelle fasi 5 (direzione: quanto movimento per il livello) e 8 (costruzione). Livelli: **[Evidenza]**,
**[Prassi]**, **[Opinione]**. Token, "momenti" e divieti adattati da TasteSkill 2.5.1 (`motion.md`, `moments.md`, MIT);
indicazioni su GSAP da UI/UX Pro Max (`data/motion.csv`, MIT).

## 1. Il movimento deve guadagnarsi il posto

NN/g: feedback semplice circa 100 ms, cambio di schermata 200-300 ms, movimenti grandi fino a 400 ms; sopra i 500 ms
l'animazione "trascina"; ciò che entra dura un po' più di ciò che esce; ease-out per quasi tutto, mai lineare; le animazioni
sono "molto più spesso troppo lunghe che troppo corte" **[Evidenza]** ([NN/g, Animation Duration](https://www.nngroup.com/articles/animation-duration/)).
IBM Carbon: token da 70 ms (pulsanti) a 400 ms (grandi espansioni) e **"se l'utente medio nota spesso il movimento, toglilo o
riducilo"** **[Prassi]** ([Carbon, Motion](https://carbondesignsystem.com/elements/motion/overview/)). Emil Kowalski: quasi tutto
sotto i 300 ms, solo `transform` e `opacity`, animazioni interrompibili, le azioni da tastiera non si animano **[Prassi]**
([Emil Kowalski](https://emilkowal.ski/ui/great-animations)). Rauno Freiberg: si anima dalla vera origine dell'elemento, le
azioni frequenti non si animano, "l'animazione deve guadagnarsi il posto" **[Opinione]** ([Rauno Freiberg](https://rauno.me/craft/interaction-design)).

| Interazione | Durata | Curva |
|---|---|---|
| Hover, pressione, interruttori | 100-150 ms (dentro 150, fuori 120, pressione 90) | ease-out |
| Menu a tendina, tooltip, notifiche | 150-250 ms (apre 200, chiude 120) | ease-out |
| Modale o pannello | 250-300 ms in entrata, circa 200 ms in uscita | ease-out in entrata, accelerazione in uscita |
| Zoom di una foto al passaggio | 600 ms dentro, 400 ms fuori | ease-out |
| Transizione di pagina | 250-400 ms, uscita più veloce dell'entrata | standard |
| Limite per l'interfaccia | mai oltre 500 ms | — |
| Movimento ridotto | spostamenti a zero, resta solo una dissolvenza breve o il cambio di colore | — |

**Curve [Prassi]** (TasteSkill): interfaccia `cubic-bezier(.2,.8,.2,1)`; entrata che si assesta `cubic-bezier(.22,1,.36,1)`;
spostamenti `cubic-bezier(.65,0,.35,1)`; lineare solo per i cicli. Nessun rimbalzo, nessun superamento del punto d'arrivo.

**Distanze [Prassi]** (TasteSkill): scheda con link che si alza 2 px; foto 1,02-1,03 dentro la sua cornice (`overflow: hidden`);
freccia 3 px; menu che scende 6 px; pulsante 1 px su, pressione 1 px giù e scala 0,985. Si animano solo transform, opacità e
colori; mai larghezza, altezza, margini, `top`/`left`.

**Livello di risposta [Prassi]**: hover solo con `@media (hover: hover) and (pointer: fine)`; ogni stato da hover funziona
anche con tocco e tastiera; nulla cambia dimensione né spinge i vicini; anello del focus 2 px, a 2 px dal controllo, mai
animato; schede senza link: nessun hover.

Lo sfalsamento (stagger) non ha numeri ufficiali: 30-80 ms con un tetto totale; nelle liste lunghe 20-40 ms per elemento e
al massimo ~8 elementi **[Prassi]**. La regola che conta di più: **un solo momento di movimento orchestrato batte effetti
sparsi**; le comparse con dissolvenza e salita su ogni sezione sono il default generico **[Opinione ben argomentata]**
([anthropics/skills, frontend-design](https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md);
[Metabole Studio](https://metabole.studio/en/blog/web-design-trends-2026)). Il contenuto non dipende mai dall'animazione per
comparire: si parte da opacità 1, così se lo script fallisce o il movimento è ridotto la pagina è leggibile **[Prassi]**.

## 2. Cosa si anima in ogni livello

| Livello | Si anima | Non si anima |
|---|---|---|
| **Sobrio e curato** | hover e pressione; menu e pannelli; al massimo un momento leggero (una foto che si assesta da 1,05 a 1 in ~1 s, una frase che si accende parola per parola) | titolo, logo, slogan; schede e sezioni allo scorrimento; contatori |
| **Immersivo** | in più: **un momento** di scorrimento in una sezione sua (capitoli di foto, passi accanto a un riquadro fisso, testo che si rivela); al massimo due su pagine lunghe | parallasse sul testo; più di 1-2 sezioni fissate |
| **Esperienziale** | in più: entrata dell'apertura (titolo che sale a righe, ~1,1 s, una volta), oggetti e testi in movimento, transizioni di pagina, scorrimento morbido se serve all'esperienza | movimento che nasconde testo già leggibile; scroll-jacking che impedisce di leggere |

NN/g vieta di animare logo, slogan e titolo della home **[Evidenza]** ([NN/g, Homepage Design Principles](https://www.nngroup.com/articles/homepage-design-principles/)):
nel livello esperienziale l'eccezione si motiva nel brief.

## 3. I "momenti" **[Prassi]** (TasteSkill)

Un momento è il punto che il visitatore ricorda: uno su una pagina breve, due su una lunga (8 sezioni o più), mai tre, ognuno
in una sezione sua. Fuori dal momento lo scorrimento non anima niente.

| Momento | Cosa fa | Quando | Telefono e movimento ridotto |
|---|---|---|---|
| Frase che si accende | una frase grande che si colora parola per parola scorrendo | manifesto, "chi siamo" in una riga | gira su telefono; ridotto: frase tutta colorata |
| Foto che si sviluppa | una foto grande che sale dal grigio (prima i neri, poi il colore), una volta, 1,6-1,8 s | una foto forte con un soggetto chiaro | gira su telefono; ridotto: foto ferma |
| Capitoli di foto | 3-5 capitoli, una foto a tutta larghezza ciascuno, ogni foto scopre la precedente dal basso, il capitolo su un pannello in basso a sinistra; ~2/3 di schermata di scorrimento per capitolo | una storia, un luogo, un prodotto in uso | gira su telefono verticale; ridotto: capitoli in fila |
| Passi con riquadro fisso | 2-4 passi accanto a un riquadro che resta fermo (`position: sticky`) e cambia | "come funziona", "come si prenota" | righe ferme, ogni passo con la sua immagine |
| Lettere che si compongono | una frase di 2-5 parole, molto grande, le cui lettere arrivano al loro posto | livello esperienziale | frase scritta |

**Regole di ogni momento**: fissato solo con `position: sticky` dentro la sua sezione (mai scroll-jacking); legato alla barra
di scorrimento e reversibile; stato finito a entrambi gli estremi; testo vero nell'HTML, leggibile e a 4,5:1 in ogni istante;
con movimento ridotto o senza JavaScript si vede lo stato finito; su telefono girano solo i leggeri (trasformazioni,
ritagli, filtri, colore; niente WebGL). Mai in una scheda, nei prezzi, nelle FAQ o nel footer.

## 4. Scorrimento, tecnologie e librerie

- Lo **scroll-jacking** disorienta la maggior parte degli utenti, alcuni lasciano la pagina o lo scambiano per un guasto, su
  mobile va peggio **[Evidenza]** ([NN/g, Scrolljacking 101](https://www.nngroup.com/articles/scrolljacking-101/)); parallasse,
  caroselli automatici e scroll-jacking possono dare vertigini e nausea. Le librerie di scorrimento morbido come Lenis
  rientrano nelle stesse riserve (inferenza): **solo nel livello esperienziale**, con motivo.
- A novembre 2026 sono Baseline le **animazioni guidate dallo scorrimento in CSS** (`animation-timeline`, con Firefox 159)
  ([web.dev, ottobre 2026](https://web.dev/blog/web-platform-10-2026)), le **View Transitions nello stesso documento**
  ([web.dev](https://web.dev/blog/same-document-view-transitions-are-now-baseline-newly-available)) e l'anchor positioning;
  le View Transitions tra pagine diverse non ancora: solo come miglioramento progressivo
  ([caniuse](https://caniuse.com/cross-document-view-transitions)) **[Evidenza]**.
- **GSAP è gratuito con tutti i plugin**, anche commerciale, dal 30 aprile 2025 ([Webflow](https://webflow.com/blog/gsap-becomes-free)).
  Ordine: CSS prima, Web Animations API per controlli semplici, GSAP + ScrollTrigger solo per sequenze complesse
  **[Prassi]** ([Emil Kowalski](https://emilkowal.ski/ui/great-animations)).
- **GSAP in pratica [Prassi]** (UI/UX Pro Max): ScrollTrigger con `scrub: 0.5-1.5`; al massimo 1-2 sezioni fissate per
  pagina, provate su telefoni medi; parallasse solo su livelli di sfondo, spostamento 5-15%; SplitText solo per titoli brevi
  (< 8 parole), con `revert()` alla fine; `gsap.matchMedia()` per il movimento ridotto; `markers` solo in sviluppo;
  `ScrollTrigger.refresh()` dopo il caricamento di immagini e font.
- **In Elementor** sono native le animazioni d'ingresso e gli effetti di movimento (che però vanno usati con le regole sopra:
  niente comparse su ogni sezione); lo scorrimento legato alla barra, i momenti e GSAP richiedono un widget HTML o codice
  personalizzato **[Prassi]**.

## 5. Mai

Schede, righe o riquadri che compaiono scorrendo; parallasse sul testo; titoli di sezione che salgono in ogni sezione;
schede che si inclinano, ruotano o seguono il puntatore; pulsanti "magnetici"; luce che segue il cursore; caroselli e slider
che avanzano da soli; fila di loghi che scorre; scritte che lampeggiano, si rimescolano o cambiano tinta a caso; contatori
che contano da zero (salvo siti tecnologici, una volta); rimbalzi; `transition: all`. Qualsiasi cosa si muova ancora 5 s dopo
essere stata vista ha un pulsante di pausa (WCAG 2.2.2) **[Evidenza + Prassi]**.

## 6. Movimento ridotto

`@media (prefers-reduced-motion: reduce)` sempre (`controllo_tecnico.py`: `movimento-ridotto`): restano i cambi di colore e
le dissolvenze brevi; spostamenti, zoom, sfondi animati e momenti mostrano lo stato finito; i numeri mostrano il valore
finale; nessun pulsante di pausa da mostrare **[Evidenza]**.

## 7. Telefono progettato, non rimpicciolito

| Regola | Valore | Livello |
|---|---|---|
| Bersagli | **24×24 px minimo obbligatorio** (WCAG 2.2 AA, con eccezioni per spaziatura e link nel testo); obiettivo **44-48 px** per tutto ciò che si tocca; Google 48 dp separati da 8 | [Evidenza] ([W3C 2.5.8](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html); [Apple](https://developer.apple.com/design/tips); [NN/g, Touch Targets](https://www.nngroup.com/articles/touch-target-size/)) |
| Input | testo ≥ 16 px (sotto iOS fa zoom); mai bloccare lo zoom | [Evidenza] ([Vercel](https://vercel.com/design/guidelines)) |
| Altezza | hero con `min-height: 100svh`; `dvh` solo per ciò che deve seguire la barra del browser | [Evidenza] ([web.dev, viewport units](https://web.dev/blog/viewport-units)) |
| Funzioni CSS | container queries, `:has()`, subgrid utilizzabili oggi | [Evidenza] ([web.dev, Baseline](https://web.dev/articles/baseline-features)) |
| Navigazione | voci visibili se 4-5 o meno, altrimenti combinata con pulsante "Menu"; CTA fuori dal menu | [Evidenza] (vedi `tipi-di-sito-e-sezioni.md`) |
| Barra fissa in basso | "Chiama" e "Prenota" (o l'azione principale), con `env(safe-area-inset-bottom)`; compare solo quando il pulsante dell'hero è uscito dallo schermo, sparisce quando lo schermo mostra già una delle sue azioni | [Prassi] (inferenza; TasteSkill) |
| Layout | ordine dei contenuti ripensato, CTA nella zona del pollice, tabelle che diventano liste, pulsanti a tutta larghezza | [Prassi] |
| Tocco | `touch-action: manipulation`; nessun gesto come unico modo per un'azione | [Prassi] (UI/UX Pro Max) |
| Prova | iPhone reale in Safari, anche in risparmio energetico (le animazioni si comportano diversamente) | [Prassi] |

## 8. Leggi di UX utili per motivare le scelte

Le Laws of UX danno un vocabolario per spiegare le scelte al cliente **[Prassi]** ([Laws of UX](https://lawsofux.com/)):
**Jakob** (usa le convenzioni), **Hick** (meno opzioni), **Fitts** (bersagli grandi e vicini), **Miller** e raggruppamento,
**Doherty** (risposta sotto i 400 ms), **estetica-usabilità** (il bello sembra più usabile, e può nascondere problemi),
**Von Restorff** (una sola CTA che si distingue), **picco-fine** (curare il momento migliore e la chiusura, per esempio la
conferma del modulo).
