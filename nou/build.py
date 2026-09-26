#!/usr/bin/env python3
"""Construieste site-ul nou in toate limbile.

Sursa: src/*.html, scrise in romana.
Traduceri: i18n/<limba>.json, cheie = textul romanesc exact, valoare = traducerea.
Rezultat: *.html (romana) si <limba>/*.html.

  python3 build.py            construieste tot; se opreste daca lipseste o traducere
  python3 build.py --extract  listeaza textele care trebuie traduse
"""
import html, json, os, re, sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.abspath(__file__))
LANGS = ['ro', 'de', 'en', 'es', 'uk', 'hu']
NAMES = {'ro': 'Română', 'de': 'Deutsch', 'en': 'English', 'es': 'Español', 'uk': 'Українська', 'hu': 'Magyar'}
PAGES = ['index.html', 'firme.html', 'candidati.html', 'confidentialitate.html', 'cookies.html', 'termeni.html']
ATTRS = ('alt', 'placeholder', 'aria-label', 'content', 'title')
SKIP_TAGS = ('script', 'style')
# texte care raman la fel in orice limba
SAME = re.compile(r'^(SmartKonsult Plus( SRL)?|SK|RO|DE|EN|ES|UK|HU|Română|Deutsch|English|Español|Українська|Magyar|'
                  r'AlphaConsult Premium KG|Modern Business Solutions GmbH|Chronos Operations GmbH|Gheorghe Hojda|'
                  r'[\d\s.,:+/·–—−°C€%h()-]*|[\w.+-]+@[\w.-]+|DGUV 308-001|Staplerschein|→|/|\*)$')


def needs(t):
    t = t.strip()
    return bool(t) and bool(re.search(r'[^\W\d_]', t)) and not SAME.match(t)


class Walker(HTMLParser):
    def __init__(self, tr):
        super().__init__(convert_charrefs=False)
        self.tr, self.out, self.skip, self.found = tr, [], 0, []

    def t(self, s):
        core = s.strip()
        if not needs(core):
            return s
        self.found.append(core)
        if self.tr is None:
            return s
        if core not in self.tr:
            raise KeyError(core)
        return s.replace(core, self.tr[core], 1)

    def attrs(self, tag, attrs):
        parts = []
        for k, v in attrs:
            if v is None:
                parts.append(k); continue
            if k in ATTRS and not (tag == 'meta' and k == 'content' and dict(attrs).get('name') not in ('description',)):
                v = self.t(html.unescape(v))
            parts.append(f'{k}="{html.escape(v, quote=True)}"')
        return parts

    def handle_starttag(self, tag, attrs):
        if tag in SKIP_TAGS: self.skip += 1
        raw = self.get_starttag_text()
        if any(k in ATTRS for k, _ in attrs):
            p = self.attrs(tag, attrs)
            raw = '<' + tag + (' ' + ' '.join(p) if p else '') + ('/>' if raw.endswith('/>') else '>')
        self.out.append(raw)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)

    def handle_endtag(self, tag):
        if tag in SKIP_TAGS: self.skip -= 1
        self.out.append(f'</{tag}>')

    def handle_data(self, d):
        self.out.append(d if self.skip else self.t(d))

    def handle_entityref(self, n): self.out.append(f'&{n};')
    def handle_charref(self, n): self.out.append(f'&#{n};')
    def handle_comment(self, d): self.out.append(f'<!--{d}-->')
    def handle_decl(self, d): self.out.append(f'<!{d}>')


def url(lang, page):
    return page if lang == 'ro' else f'{lang}/{page}'


def build_page(src, page, lang, tr):
    w = Walker(tr); w.feed(src); w.close()
    s = ''.join(w.out)
    pre = '' if lang == 'ro' else '../'
    s = s.replace('<html lang="ro">', f'<html lang="{lang}">', 1)
    s = s.replace('href="site.css"', f'href="{pre}site.css"').replace('src="site.js"', f'src="{pre}site.js"')
    # meniul de limbi: fiecare limba duce la aceeasi pagina
    cur = ' aria-current="true"'
    items = ''.join('<li><a href="%s%s" hreflang="%s" lang="%s"%s>%s <span>%s</span></a></li>'
                    % (pre, url(l, page), l, l, cur if l == lang else '', NAMES[l], l.upper()) for l in LANGS)
    s = re.sub(r'(<div class="lang" id="lang">\s*<button[^>]*>)RO', r'\g<1>' + lang.upper(), s, 1)
    s = re.sub(r'<ul>\s*<li><a href="#">Română.*?</ul>', '<ul>' + items + '</ul>', s, 1, flags=re.S)
    alt = ''.join(f'\n<link rel="alternate" hreflang="{l}" href="{pre}{url(l, page)}">' for l in LANGS)
    s = s.replace('<link rel="stylesheet"', alt.lstrip('\n') + '\n<link rel="stylesheet"', 1)
    return s, w.found


def main():
    srcs = {p: open(os.path.join(ROOT, 'src', p), encoding='utf-8').read() for p in PAGES}
    if '--extract' in sys.argv:
        seen = []
        for p in PAGES:
            _, f = build_page(srcs[p], p, 'ro', None)
            for x in f:
                if x not in seen: seen.append(x)
        print(json.dumps(seen, ensure_ascii=False, indent=1)); return
    missing = {}
    for lang in LANGS:
        tr = None
        if lang != 'ro':
            tr = json.load(open(os.path.join(ROOT, 'i18n', f'{lang}.json'), encoding='utf-8'))
        for p in PAGES:
            try:
                out, _ = build_page(srcs[p], p, lang, tr or {k: k for k in build_page(srcs[p], p, 'ro', None)[1]})
            except KeyError as e:
                missing.setdefault(lang, []).append(str(e)); continue
            d = ROOT if lang == 'ro' else os.path.join(ROOT, lang)
            os.makedirs(d, exist_ok=True)
            open(os.path.join(d, p), 'w', encoding='utf-8').write(out)
    if missing:
        for l, m in missing.items(): print(f'LIPSESTE [{l}]:', *m, sep='\n  ')
        sys.exit(1)
    print('construit:', ', '.join(LANGS))


if __name__ == '__main__':
    main()
