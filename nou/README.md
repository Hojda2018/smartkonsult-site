# Site-ul nou SmartKonsult Plus

Șase pagini în șase limbi: prima pagină, „Pentru firme”, „Pentru candidați” și cele trei pagini legale (confidențialitate, cookie-uri, termeni).

## Ce e în folder

| Fișier sau folder | Ce e |
|---|---|
| `src/` | Paginile în română. **Aici se schimbă textul și structura** |
| `i18n/de.json`, `en.json`, `es.json`, `uk.json`, `hu.json` | Traducerile. Cheia e textul românesc exact, valoarea e traducerea |
| `site.css`, `site.js` | Aspectul și animațiile, comune tuturor paginilor |
| `build.py` | Programul care construiește paginile în toate limbile |
| `*.html`, `de/`, `en/`, `es/`, `uk/`, `hu/` | Paginile gata construite. **Nu le modifica de mână**, se rescriu la fiecare construire |

## Cum schimbi un text

1. Schimbi textul românesc în `src/`.
2. Pui aceeași schimbare ca cheie nouă în fiecare fișier din `i18n/`, cu traducerea ei.
3. Rulezi:

```bash
python3 build.py
```

Dacă o traducere lipsește, programul se oprește și îți arată exact care text și în ce limbă. Nu se publică nimic pe jumătate tradus.

Ca să vezi toate textele care trebuie traduse:

```bash
python3 build.py --extract
```

## De știut

- Opțiunile din formulare trimit mereu valoarea în română, indiferent de limba paginii, ca Daria să primească cererile uniform.
- Formularele (`firme-nou`, `candidati-nou`) primesc cereri doar pe Netlify. Pe GitHub Pages butonul nu trimite nimic.
- Paginile au `noindex` până la lansare, ca Google să nu le afișeze. Se scoate la mutarea domeniului.
- Fostul angajator al fondatorului nu se numește niciodată în texte.
- Site-ul nu încarcă fonturi de la Google (în Germania e risc de amendă). Folosește fonturile telefonului sau calculatorului.
- Site-ul nu folosește cookie-uri și nici localStorage. Dacă se adaugă vreodată statistici, trebuie actualizată pagina de cookie-uri și cerut acordul.
- Datele firmei (adresă, J2025094668006, CUI 53058020, TVA intracomunitar RO53171010) sunt în paginile legale și în „Date legale” (Impressum), obligatorie pentru clienții din Germania.
- Pe site apare doar telefonul Dariei, +40 774 772 117. Numărul german al lui Gheorghe se dă doar direct clienților, nu se publică.
