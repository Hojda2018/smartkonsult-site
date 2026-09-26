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
| `anunt-angajare-zidar-germania.png` | Afișul de recrutare |
| `robots.txt`, `sitemap.xml` | Pentru Google |
| `netlify.toml` | Setări de publicare: cache și securitate. Nu-l modifica dacă nu știi ce faci |

## Unde e publicat

| | |
|---|---|
| Adresă Netlify | <https://smartkonsultplus.netlify.app> |
| Panou Netlify | <https://app.netlify.com/projects/smartkonsultplus> |
| Repo | <https://github.com/Hojda2018/smartkonsult-site> |
| Publicare automată | **activă** — orice push pe `main` se publică singur |

## Cum modifici site-ul

**Varianta simplă, direct din browser, fără programe instalate:**

1. Intri pe pagina repo-ului pe GitHub
2. Click pe `index.html`
3. Click pe creionul de editare (dreapta sus)
4. Faci modificarea
5. Jos, scrii pe scurt ce ai schimbat și apeși **Commit changes**

Gata. Netlify publică singur în aproximativ 30 de secunde. Verificat: un push ajunge live fără să atingi nimic.

**Varianta de pe calculator:**

```bash
cd ~/Desktop/smartkonsult-site
# faci modificările în fișiere
git add -A
git commit -m "ce am schimbat"
git push
```

## Cum pui un film în secțiunea video

Fiecare card din secțiunea „Vezi cu ochii tăi” are trei câmpuri goale în `index.html`:

```html
<figure class="vid" data-cat="cazare" data-src="" data-yt="" data-poster="" ...>
```

- `data-src` — un film pus în folderul `video/` din repo, de exemplu `video/cazare-logistica.mp4`. Ține-l sub 20 MB (filmat pe telefon, 30–60 de secunde, 720p)
- `data-yt` — sau, în loc de fișier, codul unui film de pe YouTube (partea de după `v=` din link)
- `data-poster` — o poză de copertă, opțional, de exemplu `video/cazare-logistica.jpg`

Cât timp câmpurile sunt goale, cardul arată „Film în curând”. Filmul se descarcă doar când cineva apasă pe el, așa că pagina rămâne ușoară pe telefon.

## Cum te întorci la o versiune veche

Pe GitHub, fila **Commits**, alegi versiunea dorită și apeși **Revert**.
Sau pe Netlify, în **Deploys**, alegi un deploy vechi și apeși **Publish deploy**. E instant.

Ăsta e marele câștig față de FTP: nu mai poți strica site-ul iremediabil.

## Lucruri de știut

- **Numărul de telefon** din pagină: `+40 774 772 117` (Daria)
- **Cazarea** se declară la fiecare anunț în parte. La zidărie o plătește Smart Konsult. La logistică se reține din salariu. Nu scrie „cazare inclusă" unde se reține
- **Capul paginii** are o poză cu apropiere lentă, nu film. Filmul vechi era reclama unui motostivuitor (marca Jungheinrich), nu material propriu. Când avem cadre filmate de noi, facem din ele un film de 12–15 secunde și îl punem în locul pozei
- Pozele de fundal vin de pe Unsplash și Pexels, nu sunt în repo

## Istoric

Reparat în septembrie 2026:
- pagina nu se mai mișcă lateral pe telefon
- eroare JavaScript care oprea tot codul de după ea
- hero-ul nu mai descarcă 5,3 MB pe telefon
