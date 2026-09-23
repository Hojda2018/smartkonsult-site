# Cum conectezi Netlify (o singură dată, ~10 minute)

Repo: <https://github.com/Hojda2018/smartkonsult-site>

Netlify e gratuit pentru un site ca ăsta. Nu ai nevoie de card.

---

## Partea 1 — publici site-ul pe o adresă de test

Aici nu se schimbă nimic la site-ul tău actual. Rulează în paralel, pe o adresă temporară.

1. Intri pe **[netlify.com](https://www.netlify.com)** și apeși **Sign up**
2. Alegi **Sign up with GitHub**, cu contul `Hojda2018`
3. În panou, apeși **Add new site** → **Import an existing project**
4. Alegi **Deploy with GitHub**
5. Netlify cere permisiune să vadă repo-urile. Apeși **Configure Netlify on GitHub** și alegi:
   - **Only select repositories** → bifezi `smartkonsult-site`
   - Apeși **Install**
6. Te întorci în Netlify și alegi repo-ul `smartkonsult-site` din listă
7. La setările de build **nu completezi nimic**. Fișierul `netlify.toml` din repo le spune el.
   Verifică doar că **Publish directory** e `.` (un punct)
8. Apeși **Deploy site**

După ~30 de secunde primești o adresă de forma `numeAleatoriu-123abc.netlify.app`.

**Deschide adresa aia și verifică site-ul.** Pe telefon și pe calculator. Dacă totul arată bine, treci la Partea 2. Dacă nu, oprește-te aici și spune-mi: site-ul tău real n-a fost atins.

---

## Partea 2 — muți domeniul pe Netlify

⚠️ **Abia aici se schimbă site-ul live.** Fă pasul ăsta doar după ce adresa de test arată corect.

1. În Netlify: **Domain settings** → **Add a domain**
2. Scrii `smartkonsultplus.ro` și apeși **Verify** → **Add domain**
3. Netlify îți arată ce trebuie schimbat în DNS. De obicei:

   | Tip | Nume | Valoare |
   |-----|------|---------|
   | A | `@` | `75.2.60.5` |
   | CNAME | `www` | `numeleSituluiTau.netlify.app` |

   **Folosește valorile pe care ți le arată Netlify**, nu pe astea. Se pot schimba.

4. Intri la firma de unde ai cumpărat domeniul `smartkonsultplus.ro`, la secțiunea **DNS**, și pui valorile alea
5. Aștepți. De obicei 15 minute până la 2 ore, uneori până la 24
6. Netlify pune singur certificatul HTTPS, gratuit. Nu trebuie să faci nimic

---

## După ce e gata

**Ca să modifici site-ul:** editezi `index.html` direct pe GitHub, din browser, și apeși Commit. Netlify publică singur în 30 de secunde.

**Ca să te întorci la o versiune veche:** în Netlify, fila **Deploys**, alegi un deploy vechi și apeși **Publish deploy**. Instant, fără să atingi nimic altceva.

**Vechea găzduire:** nu o desființa imediat. Ține-o încă o lună, până te convingi că totul merge.

---

## Dacă ceva nu merge

- **Site-ul apare gol pe Netlify:** verifică în Netlify că Publish directory e `.`
- **Pozele sau filmul nu apar:** verifică pe GitHub că `hero.mp4` și fișierele PNG chiar sunt în repo
- **Domeniul nu se mută:** e aproape întotdeauna DNS-ul. Verifică valorile la registrar și mai așteaptă
- **Certificatul HTTPS nu apare:** în Netlify, Domain settings → HTTPS → **Verify DNS configuration**
