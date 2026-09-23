# Site Smart Konsult Plus

Site-ul public de la [smartkonsultplus.ro](https://smartkonsultplus.ro).
Un singur fișier HTML, fără framework, fără build. Se publică singur pe Netlify la fiecare modificare.

## Ce e în folder

| Fișier | Ce e |
|--------|------|
| `index.html` | Pagina principală. Tot site-ul e aici: text, CSS și JavaScript |
| `politica-confidentialitate.html` | Pagina GDPR |
| `politica-cookies.html` | Politica de cookie-uri |
| `termeni-si-conditii.html` | Termeni și condiții |
| `hero.mp4` | Filmul de fundal din capul paginii (4,5 MB) |
| `anunt-angajare-zidar-germania.png` | Afișul de recrutare |
| `robots.txt`, `sitemap.xml` | Pentru Google |
| `netlify.toml` | Setări de publicare: cache și securitate. Nu-l modifica dacă nu știi ce faci |

## Cum modifici site-ul

**Varianta simplă, direct din browser, fără programe instalate:**

1. Intri pe pagina repo-ului pe GitHub
2. Click pe `index.html`
3. Click pe creionul de editare (dreapta sus)
4. Faci modificarea
5. Jos, scrii pe scurt ce ai schimbat și apeși **Commit changes**

Gata. Netlify publică singur în aproximativ 30 de secunde.

**Varianta de pe calculator:**

```bash
cd ~/Desktop/smartkonsult-site
# faci modificările în fișiere
git add -A
git commit -m "ce am schimbat"
git push
```

## Cum te întorci la o versiune veche

Pe GitHub, fila **Commits**, alegi versiunea dorită și apeși **Revert**.
Sau pe Netlify, în **Deploys**, alegi un deploy vechi și apeși **Publish deploy**. E instant.

Ăsta e marele câștig față de FTP: nu mai poți strica site-ul iremediabil.

## Lucruri de știut

- **Numărul de telefon** din pagină: `+40 774 772 117` (Daria)
- **Cazarea** se declară la fiecare anunț în parte. La zidărie o plătește Smart Konsult. La logistică se reține din salariu. Nu scrie „cazare inclusă" unde se reține
- **Filmul de fundal** nu se încarcă pe telefon, intenționat. Economisește 4,5 MB pentru cineva pe date mobile
- Pozele de fundal vin de pe Unsplash și Pexels, nu sunt în repo

## Istoric

Reparat în septembrie 2026:
- pagina nu se mai mișcă lateral pe telefon
- eroare JavaScript care oprea tot codul de după ea
- hero-ul nu mai descarcă 5,3 MB pe telefon
