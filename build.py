"""Splash of Ink: a Starter Site draft (brochure pages, simple forms, booking and payments link out). Generated; edit here, then python3 build.py."""
import pathlib, html
R = pathlib.Path(__file__).parent
SHOP = 'Splash of Ink'

SHOPS = [
  dict(slug='fourth-avenue', name='Fourth Avenue', addr='532 N 4th Ave<br>Tucson, AZ 85705', map='https://maps.google.com/?cid=3162480668975808258', phone=('(520) 651-1910','+15206511910'), blurb='The original shop, on Tucson\u2019s historic Fourth Avenue.'),
  dict(slug='stone-avenue', name='Stone Avenue', addr='3050 N Stone Ave<br>Tucson, AZ 85705', map='https://maps.app.goo.gl/h9L7F6SiUq7BHN4W7', phone=('(520) 651-1910','+15206511910'), blurb='Our second shop, on Stone Avenue.'),
]
PHONES = [('Master D', '(520) 651-1910', '+15206511910', 'Stone Shop'), ('Magic', '(520) 392-3594', '+15203923594', '4th Shop')]
def callbar():  # D's number first, Magic's right beside it and just as big
    return '<div class="callbar">' + ''.join(f'<a class="call{" alt" if n else ""}" href="tel:{e}"><span class="cl">{lab} · {who}</span><span class="cn">{num}</span></a>' for n, (who, num, e, lab) in enumerate(PHONES)) + '</div>'
def phones_inline():
    return ' · '.join(f'<a href="tel:{e}">{num}</a> ({who})' for who, num, e, _ in PHONES)
APPRENTICE_PRICES = {}   # size -> price range, once Magic sets them (2026-10-04: only the $80 minimum is known)
SIZES = [('Small', 'fits inside your palm', '$150–200', 'size-small'), ('Medium', 'your palm, edge to edge', '$225–300', 'size-medium'), ('Large', 'your palm and most of your fingers', '$325–400', 'size-large'), ('Extra large', 'your whole hand, fingertips to wrist', '$425–500', 'size-xl')]  # the shop's pricing guide, sized against a hand
HARD_SPOTS = 'ribs, stomach, neck, hands and feet'
def short(a): return a['name'] if a['name'].startswith('Master') else a['name'].split()[0]
def avatar(a, size=52):
    f = R / 'assets' / 'artists' / f"{a['slug']}.jpg"
    src = f"assets/artists/{a['slug']}.jpg" if f.exists() else 'assets/brand/mark-dark.svg'
    return f'<img class="bubble" src="{src}" alt="" width="{size}" height="{size}" loading="lazy">'
def pricing_section():
    rows = ''.join(f'''<div class="prow2"><a href="artist-{a['slug']}.html" aria-label="{a['name']}'s page">{avatar(a)}</a><div class="pmeta"><a class="pname" href="artist-{a['slug']}.html"><b>{a['name']}</b></a><span>{a['role']} · {SHOPNAME[a['shop']]}</span></div>
      <div class="pmin">{a['minimum'] or '<span class="note">Minimum coming</span>'}</div>
      <a class="btn" href="#" data-ask="{a['slug']}">{'Get apprentice pricing' if a.get('apprentice') else f"Get {short(a)}’s price"}</a></div>''' for a in sorted(ARTISTS, key=lambda a: a['slug'] != 'master-d'))  # the owner first
    sizes = ''.join(f'<div class="tier"><img src="assets/icons/{i}.svg" alt="" width="56" height="56"><div class="tname">{n}</div><div class="tprice">{r}</div><div class="tfit">{d}</div></div>' for n, d, r, i in SIZES)
    return f'''<section id="pricing"><div class="wrap">
  <div class="eyebrow">Pricing</div><h2 style="font-size:40px">What a tattoo costs</h2>
  <p style="max-width:680px">Every artist at Splash of Ink sets their own prices. Your price depends on three things: the size of the piece, where it goes on your body, and how much detail it has. Here’s the shop’s pricing guide, and your artist will send you an exact range for your idea.</p>
  <div class="chart">{sizes}</div>
  <p class="note" style="margin-top:10px">Sizes are measured against your hand. Prices can vary higher or lower depending on detail and placement, and small pieces start at the artist’s minimum.</p>
  <div class="pnotes">
    <div class="pn"><img class="ico" src="assets/icons/placement.svg" alt="" width="48" height="48"><div><h3>Placement</h3><p>The same design costs more on the {HARD_SPOTS}. Those spots take longer and need a steadier hand.</p></div></div>
    <div class="pn"><img class="ico" src="assets/icons/sessions.svg" alt="" width="48" height="48"><div><h3>Big pieces</h3><p>Larger work can be split into sessions to fit your budget. Your artist will plan it with you.</p></div></div>
    <div class="pn"><img class="ico" src="assets/icons/credit.svg" alt="" width="48" height="48"><div><h3>Credit for coming back</h3><p>Spend over $150 and you build a $100 tattoo credit, to use that day or on your next visit.</p></div></div>
  </div>
  <h3 style="margin:30px 0 12px">Get your artist’s price</h3>
  <div class="plist">{rows}</div>
  <p class="note" style="margin-top:12px">Payment is due before the tattoo or piercing is done: Venmo, Cash App, Zelle or cash (there’s an ATM inside).</p>
</div></section>'''
HOURS = 'Open 24/7 by appointment. Walk-ins: Monday to Thursday 11 AM to about 10 PM; Friday to Sunday 11 AM to 5 AM.'
WALKIN = [('Monday', '11 AM – about 10 PM'), ('Tuesday', '11 AM – about 10 PM'), ('Wednesday', '11 AM – about 10 PM'), ('Thursday', '11 AM – about 10 PM'), ('Friday', '11 AM – 5 AM'), ('Saturday', '11 AM – 5 AM'), ('Sunday', '11 AM – 5 AM')]
ARTISTS = [
  dict(slug='magic', name='Magic', shop='fourth-avenue', role='Head artist · tattoo and piercing',
       bio='The last of the shop\u2019s original artists. There\u2019s very little Magic doesn\u2019t do, from delicate fine line to full realism, and he pierces too.',
       styles=['Fine line', 'Black and gray', 'Neo-traditional', 'American traditional', 'Color', 'Realism'],
       minimum='$100 shop minimum', book=('Book with Magic', '#', 'Booking link coming'),
       socials=[('Instagram', 'https://www.instagram.com/splashofink_magicman/'), ('TikTok', 'https://www.tiktok.com/@josephgaspard26')]),
  dict(slug='annie', name='Annie', shop='fourth-avenue', role='Piercer · tattoo apprentice',
       bio='Annie runs piercing at the Fourth Avenue shop and is learning to tattoo as an apprentice.',
       styles=['Piercing', 'Apprentice tattoos'],
       minimum='', book=('Book with Annie', '#', 'Booking link coming'),
       socials=[('Instagram', 'https://www.instagram.com/annie_splash_of_ink/'), ('TikTok', 'https://www.tiktok.com/@anniesplashofink')]),
  dict(slug='master-d', name='Master D', shop='stone-avenue', role='Owner and artist',
       bio='Master D owns Splash of Ink and tattoos at the Stone Avenue shop.',
       styles=['Styles coming'],
       minimum='', book=('Book with Master D', '#', 'Booking link coming'),
       socials=[('Instagram', '#')]),
  dict(slug='angel-perez', name='Angel Perez', shop='stone-avenue', role='Artist · anime, comic and color',
       bio='Anime and comic work with bold color and clean black and gray, and fine line on the way.',
       styles=['Anime', 'Comic', 'Color', 'Black and gray'],
       minimum='', book=('Book with Angel on Setmore', 'https://thegreatsage.setmore.com', 'Books on Setmore'),
       socials=[('Instagram', 'https://www.instagram.com/thegreatsagetattoosandtarot/'), ('TikTok', 'https://www.tiktok.com/@greatsagetattooandtarot')]),
  # One page per shop for whoever is apprenticing there right now, so the price is right without anyone being named.
  # An NFC tag at the station opens it (…/artist-apprentice-<shop>.html?utm_source=nfc&utm_content=apprentice).
  dict(slug='apprentice-fourth', name='Apprentice', shop='fourth-avenue', role='Apprentice pricing', apprentice=True,
       bio='Splash of Ink trains new artists. Whoever is apprenticing at the Fourth Avenue shop right now works at apprentice prices, below the main artists, while they learn under the shop\u2019s artists.',
       styles=['Flash', 'Small pieces', 'Line work'],
       minimum='Apprentice minimum $80', book=('Ask at the counter', 'tel:+15203923594', 'Walk in, or call the shop'),
       socials=[]),
  dict(slug='apprentice-stone', name='Apprentice', shop='stone-avenue', role='Apprentice pricing', apprentice=True,
       bio='Splash of Ink trains new artists. Whoever is apprenticing at the Stone Avenue shop right now works at apprentice prices, below the main artists, while they learn under the shop\u2019s artists.',
       styles=['Flash', 'Small pieces', 'Line work'],
       minimum='Apprentice minimum $80', book=('Ask at the counter', 'tel:+15206511910', 'Walk in, or call the shop'),
       socials=[]),
]
SHOPNAME = {s['slug']: s['name'] for s in SHOPS}
import json as _json
WORK = _json.load(open(R / 'work.json')) if (R / 'work.json').exists() else {}   # hosted photos, picked from each artist's own Instagram
VIDEOS = {  # Instagram posts embedded, not hosted (Angel picked Magic's, 2026-10-02)
  'magic': ['reel/Da6655ETUCR', 'p/DdA3bkrCJY3', 'p/DdS9Unxi6So'],
  'angel-perez': ['p/DeAeS83jNRl', 'p/Dd-Wc1diYcv', 'p/Dd1tPkhTYAm', 'p/Ddj-hUfhzwb'],
}
TIKTOK = {  # (handle, id, kind) embedded with TikTok's own code
  'magic': [('josephgaspard26', '7655531781596122399', 'photo'), ('josephgaspard26', '7656232638323117343', 'video'),
            ('josephgaspard26', '7655834813122874655', 'photo'), ('josephgaspard26', '7655831686009064735', 'photo'),
            ('josephgaspard26', '7672576982168751373', 'photo'), ('josephgaspard26', '7670982383419641119', 'photo')],
}
GROUPS = [('all', 'All'), ('bg', 'Black and gray'), ('color', 'Color'), ('fineline', 'Fine line'), ('florals', 'Florals'), ('animals', 'Animals'), ('butterflies', 'Butterflies'), ('anime', 'Anime and cartoon'), ('ornamental', 'Ornamental')]
WORKSETS = {  # each artist page's galleries, in order: (WORK key, eyebrow, title)
  'magic': [('magic', 'His work', 'Recent tattoos')],
  'angel-perez': [('angel-perez-tattoos', 'His work', 'Recent tattoos'), ('angel-perez', 'His art', 'Paintings and designs')],
}
def filters(slug):
    items = WORK.get(slug, [])
    if not any(w.get('tags') for w in items): return ''
    n = lambda k: len(items) if k == 'all' else sum(k in w.get('tags', '').split() for w in items)
    return '<div class="wfilt" role="group" aria-label="Filter the work">' + ''.join(f'<button type="button" data-f="{k}" aria-pressed="{"true" if k == "all" else "false"}">{lab} <small>{n(k)}</small></button>' for k, lab in GROUPS if n(k)) + '</div>'
FILTERJS = '''<script>document.querySelectorAll('.wfilt').forEach(g=>{const box=g.nextElementSibling;g.addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;g.querySelectorAll('button').forEach(x=>x.setAttribute('aria-pressed',x===b));const f=b.dataset.f;box.querySelectorAll('.wk').forEach(a=>{a.hidden=!(f==='all'||(a.dataset.tags||'').split(' ').includes(f))});});});</script>'''
WORKTITLE = {'magic': ('His work', 'Recent tattoos'), 'angel-perez': ('His art', 'Paintings and designs')}
def gallery(key, n=None):
    items = WORK.get(key, [])[:n]
    who = next((a['name'] for a in ARTISTS if key.startswith(a['slug'])), 'Splash of Ink')
    return ''.join(f'<a class="wk" data-tags="{w.get("tags", "")}" href="{w["post"]}" target="_blank" rel="noopener"><img src="{w["file"]}" alt="Work by {who}" loading="lazy"></a>' for w in items)
def videos(slug):
    return ''.join(f'<div class="vid"><blockquote class="instagram-media" data-instgrm-permalink="https://www.instagram.com/{c}/" data-instgrm-version="14" style="background:#fff;border:0;margin:0;max-width:540px;min-width:280px;width:100%"><a href="https://www.instagram.com/{c}/" target="_blank" rel="noopener">View this post on Instagram</a></blockquote></div>' for c in VIDEOS.get(slug, []))
def tiktoks(slug):
    return ''.join(f'<div class="vid tt"><blockquote class="tiktok-embed" cite="https://www.tiktok.com/@{h}/{k}/{i}" data-video-id="{i}" style="max-width:605px;min-width:280px;margin:0"><section><a target="_blank" rel="noopener" href="https://www.tiktok.com/@{h}/{k}/{i}">View on TikTok</a></section></blockquote></div>' for h, i, k in TIKTOK.get(slug, []))

CSS = '''
:root{--ink:#0b0910;--ink2:#15111d;--card:#1b1526;--line:#2e2540;--purple:#8b3dff;--purple2:#b98cff;--glow:#a855f7;--fog:#f3eefb;--body:#cfc6de;--mute:#968bab}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--ink);color:var(--body);font:16px/1.65 Inter,system-ui,sans-serif}
a{color:var(--purple2)}img{max-width:100%;display:block}
h2{font-family:UnifrakturMaguntia,serif!important;font-weight:400!important;letter-spacing:.01em!important;text-shadow:3px 3px 0 #3b3150}
h1,h3{font-family:Oswald,sans-serif;}
h1,h2,h3{color:var(--fog);line-height:1.15;margin:0 0 .5em;letter-spacing:.01em;font-weight:600}
.wrap{max-width:1120px;margin:0 auto;padding:0 20px}
.draft{background:#120a22;color:#e9def7;text-align:center;font:500 13px/1.4 Inter,sans-serif;letter-spacing:.03em;padding:8px 16px;border-bottom:1px solid rgba(255,255,255,.08)}.draft .azt{display:inline-flex;align-items:center;gap:8px;color:#e9def7;text-decoration:none;background:none;border-radius:0;padding:0}.draft .azt img{width:20px;height:20px;display:block}.draft .azt b{color:var(--purple2)}.draft .azt:hover b{text-decoration:underline}
header{background:rgba(11,9,16,.92);border-bottom:3px solid var(--purple);box-shadow:0 2px 18px rgba(139,61,255,.35);position:sticky;top:0;z-index:5;backdrop-filter:blur(6px)}
header .wrap{display:flex;align-items:center;justify-content:space-between;gap:16px;padding:12px 20px;flex-wrap:wrap}
.brand{font:400 34px/1 "Pirata One",serif;color:var(--fog);text-decoration:none;letter-spacing:.02em}
.brand img{height:58px;width:auto;display:block;margin-block:-6px}
.drip{height:46px;background:url(assets/brand/drip.svg) top/100% 100% no-repeat;margin-bottom:-46px;position:relative;z-index:4;pointer-events:none}
h1.lockup{margin:0 auto 18px;max-width:640px}h1.lockup img{width:100%;height:auto;filter:drop-shadow(0 6px 30px rgba(139,61,255,.35))}
.hero{background:radial-gradient(900px 420px at 50% -10%,rgba(139,61,255,.35),transparent 70%),radial-gradient(circle at 12% 70%,rgba(139,61,255,.18) 0 2px,transparent 3px) 0 0/38px 38px}
nav{display:flex;gap:18px;flex-wrap:wrap}nav a{color:var(--body);text-decoration:none;font:600 14px Oswald,sans-serif;letter-spacing:.08em;text-transform:uppercase}
nav a:hover,nav a.on{color:var(--purple2)}
.hero{padding:84px 0 70px;background:radial-gradient(900px 420px at 50% -10%,rgba(139,61,255,.35),transparent 70%)}
.hero .wrap{text-align:center}
.hero h1{font:400 clamp(56px,10vw,104px)/1 "Pirata One",serif;margin-bottom:14px}
.hero p.lead{font-size:20px;max-width:640px;margin:0 auto 26px}
.btn{display:inline-block;padding:13px 24px;border-radius:999px;font:600 15px Oswald,sans-serif;letter-spacing:.08em;text-transform:uppercase;text-decoration:none;border:2px solid var(--purple);color:#fff;background:var(--purple);cursor:pointer}
.btn.ghost{background:transparent;color:var(--purple2)}
.btn:hover{box-shadow:0 0 24px rgba(168,85,247,.45)}
.row{display:flex;gap:12px;justify-content:center;flex-wrap:wrap}
section{padding:56px 0}section.alt{background:var(--ink2)}
.eyebrow{font:600 13px Oswald,sans-serif;letter-spacing:.18em;text-transform:uppercase;color:var(--purple2);margin-bottom:8px}
.grid3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px}
@media (max-width:860px){.grid3{grid-template-columns:1fr}}
.card{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:22px}
.acard{text-decoration:none;color:inherit;display:flex;flex-direction:column;gap:10px;transition:border-color .2s;height:100%}
.acard:hover{border-color:var(--purple)}
.portrait{aspect-ratio:1/1;width:100%;height:auto;object-fit:cover;border-radius:12px;border:1px solid var(--line)}
.ph{aspect-ratio:1/1;border-radius:12px;border:1px dashed #4a3d63;background:repeating-linear-gradient(45deg,#1f1830 0 12px,#1b1526 12px 24px);display:flex;align-items:center;justify-content:center;text-align:center;color:var(--mute);font:600 13px Inter,sans-serif;padding:12px}
.tags{display:flex;gap:6px;flex-wrap:wrap}.tags span{font-size:12.5px;border:1px solid var(--line);border-radius:999px;padding:3px 10px;color:var(--purple2)}
.samples{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}
@media (max-width:860px){.samples{grid-template-columns:repeat(2,minmax(0,1fr))}}
.samples figure{margin:0}.samples figcaption{font:600 14px Oswald,sans-serif;letter-spacing:.06em;text-transform:uppercase;color:var(--fog);margin-top:8px}
.prof{display:grid;grid-template-columns:300px minmax(0,1fr);gap:32px;align-items:start}
@media (max-width:760px){.prof{grid-template-columns:1fr}}
.soc{display:flex;gap:10px;flex-wrap:wrap}.soc a{font-size:14px;border:1px solid var(--line);border-radius:8px;padding:6px 12px;text-decoration:none}
.note{font-size:13px;color:var(--mute)}
form.f{display:grid;gap:14px;max-width:680px}
.two{display:grid;grid-template-columns:1fr 1fr;gap:14px}@media (max-width:560px){.two{grid-template-columns:1fr}}
label{display:grid;gap:6px;font:600 14px Inter,sans-serif;color:var(--fog)}label small{font-weight:500;color:var(--mute)}
input,select,textarea{background:#0f0c16;border:1px solid var(--line);border-radius:10px;color:var(--fog);padding:11px 12px;font:15px Inter,sans-serif;width:100%}
input:focus,select:focus,textarea:focus{outline:2px solid var(--purple);border-color:var(--purple)}
fieldset{border:1px solid var(--line);border-radius:10px;padding:10px 14px}legend{font:600 14px Inter;color:var(--fog);padding:0 6px}
.chk{display:flex;gap:16px;flex-wrap:wrap}.chk label{display:flex;gap:8px;align-items:center;font-weight:500}.chk input{width:auto}
.done{border:1px solid var(--purple);border-radius:12px;padding:18px;background:rgba(139,61,255,.08)}
.info{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px}@media (max-width:760px){.info{grid-template-columns:1fr}}
.hours{width:100%;border-collapse:collapse}.hours td{padding:6px 0;border-bottom:1px solid var(--line)}.hours td:last-child{text-align:right;color:var(--mute)}
footer{border-top:1px solid var(--line);padding:26px 0 30px;font-size:14px}
footer .wrap{display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap}
.credit{font-size:12.5px;color:var(--mute)}.credit a{color:var(--mute)}
.shop{padding:10px 0 34px}.shop+.shop{border-top:1px solid var(--line);padding-top:40px}
.shophead{display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:20px;align-items:end}@media (max-width:760px){.shophead{grid-template-columns:1fr}}
.callbar{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin-top:22px}
.call{display:grid;gap:2px;min-width:250px;padding:12px 22px;border-radius:14px;border:2px solid var(--purple);background:rgba(139,61,255,.14);text-decoration:none;text-align:center}
.call .cl{font:600 12px Oswald,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:var(--purple2)}
.call .cn{font:600 28px Oswald,sans-serif;color:var(--fog);letter-spacing:.02em}
.call.alt{border-color:var(--purple2)}
.call:hover{box-shadow:0 0 24px rgba(168,85,247,.45)}
.pay{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px;margin-top:14px}@media (max-width:760px){.pay{grid-template-columns:1fr 1fr}}.pay h3{margin:0 0 4px}.pay p{margin:0}
.artistline{margin:14px 0 0;font-size:15px}.artistline a{font-weight:600}
.sizes{margin-top:18px}.sizes4{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px;margin-top:18px}@media (max-width:980px){.sizes4{grid-template-columns:repeat(2,minmax(0,1fr))}}@media (max-width:520px){.sizes4{grid-template-columns:1fr}}.ico{width:60px;height:60px;display:block;margin-bottom:10px}@media (max-width:860px){.ico{margin-inline:auto}}.size{display:flex;flex-direction:column}.size .range{margin-top:auto!important;padding-top:8px}.size h3{margin:0 0 4px}.size p{margin:0}.size .range{margin-top:8px;font:600 22px Oswald,sans-serif;color:var(--purple2)}
.pnotes{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:28px;margin-top:26px}@media (max-width:860px){.pnotes{grid-template-columns:1fr;gap:18px}}
.pnotes h3{margin:0 0 4px;font-size:17px}.pnotes p{margin:0;font-size:14.5px}
.pn{display:grid;grid-template-columns:44px minmax(0,1fr);gap:14px;align-items:start;padding:4px 0}.pn .ico{width:44px!important;height:44px!important;margin:0!important}
.chart{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));margin-top:20px;background:var(--card);border:1px solid var(--line);border-radius:18px;overflow:hidden}
.tier{text-align:center;padding:26px 16px 24px;border-left:1px solid var(--line);display:flex;flex-direction:column;align-items:center}.tier:first-child{border-left:0}
.tier img{width:84px;height:84px;margin-bottom:10px}.tname{font:600 14px Oswald,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:var(--lilac,#b98cff)}
.tprice{font:600 34px Oswald,sans-serif;color:var(--fog);margin:4px 0 6px;letter-spacing:.01em}.tfit{font-size:14px;color:var(--mute);max-width:190px}
@media (max-width:860px){.chart{grid-template-columns:repeat(2,minmax(0,1fr))}.tier:nth-child(3){border-left:0}.tier:nth-child(n+3){border-top:1px solid var(--line)}}
@media (max-width:600px){.chart{grid-template-columns:1fr}.tier{border-left:0}.tier+.tier{border-top:1px solid var(--line)}}
.plist{display:grid;gap:10px}
.prow2{display:grid;grid-template-columns:auto minmax(0,1fr) auto auto;gap:14px;align-items:center;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:10px 14px}
@media (max-width:640px){.prow2{grid-template-columns:auto minmax(0,1fr)}.prow2 .pmin{grid-column:2}.prow2 .btn{grid-column:1 / -1;text-align:center}}
.bubble{width:52px;height:52px;border-radius:50%;object-fit:cover;border:2px solid var(--purple);display:block;background:#0b0910}
.pmeta{display:grid}.pname{text-decoration:none}.pname:hover b{color:var(--purple2);text-decoration:underline}.prow2>a .bubble{transition:box-shadow .2s}.prow2>a:hover .bubble{box-shadow:0 0 0 3px var(--purple2)}.pmeta b{color:var(--fog);font:600 17px Oswald,sans-serif;letter-spacing:.03em}.pmeta span{font-size:13px;color:var(--mute)}
.pmin{font-weight:600;color:var(--fog);font-size:14px}
.wfilt{display:flex;flex-wrap:wrap;gap:8px;margin-top:16px}.wfilt button{font:600 13px Oswald,sans-serif;letter-spacing:.08em;text-transform:uppercase;color:var(--purple2);background:transparent;border:1px solid var(--line);border-radius:99px;padding:7px 14px;cursor:pointer}.wfilt button small{color:var(--mute);font-weight:500;margin-left:4px}.wfilt button[aria-pressed="true"]{background:var(--purple);border-color:var(--purple);color:#fff}.wfilt button[aria-pressed="true"] small{color:#e9dcff}
.works{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px;margin-top:16px}.works.strip{grid-template-columns:repeat(4,minmax(0,1fr))}
.wk{display:block;aspect-ratio:1;overflow:hidden;border-radius:12px;border:1px solid var(--line);background:var(--card)}.wk img{width:100%;height:100%;object-fit:cover;display:block;transition:transform .3s}.wk:hover img{transform:scale(1.04)}.wk[hidden]{display:none}
@media (max-width:760px){.works,.works.strip{grid-template-columns:repeat(2,minmax(0,1fr))}}
.vids{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px;margin-top:16px}@media (max-width:760px){.vids{grid-template-columns:1fr}}
.vids{grid-template-columns:repeat(3,minmax(0,1fr))!important}@media (max-width:1000px){.vids{grid-template-columns:repeat(2,minmax(0,1fr))!important}}@media (max-width:640px){.vids{grid-template-columns:1fr!important}}
.vid{max-width:420px;width:100%;justify-self:center}.vid .instagram-media{border-radius:12px!important}
.prow{display:flex;justify-content:space-between;align-items:center;gap:14px;flex-wrap:wrap}
.askd{border:1px solid var(--line);border-radius:18px;background:var(--card);color:var(--body);padding:0;max-width:600px;width:calc(100% - 28px)}
.askd::backdrop{background:rgba(5,3,9,.75)}.askd form{padding:26px 24px;position:relative;max-width:none}
.askx{position:absolute;top:10px;right:14px;background:none;border:0;color:var(--mute);font-size:28px;cursor:pointer;line-height:1}
'''

HEAD = '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow"><title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Oswald:wght@500;600&family=UnifrakturMaguntia&family=Mr+Dafoe&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css?v={cssv}"><script>
/* Self-hosted Umami. ?notme=1 stops counting this browser, ?countme=1 undoes it. A visit carrying utm_source=nfc
   (an NFC tag at the shop, like the apprentice tag) is also sent as a tag-tap event, named by utm_content. */
(function(){{try{{var q=new URLSearchParams(location.search);if(q.has('notme'))localStorage.setItem('umami.disabled','1');if(q.has('countme'))localStorage.removeItem('umami.disabled')}}catch(x){{}}
var s=document.createElement('script');s.defer=true;s.src='https://stats.aztechsol.com/script.js';s.setAttribute('data-website-id','fde5defc-56bc-49e8-99fb-353d32269204');s.setAttribute('data-domains','splashofink.aztechsol.com');
s.onload=function(){{try{{var q=new URLSearchParams(location.search);if(q.get('utm_source')==='nfc'&&window.umami)umami.track('tag-tap',{{tag:q.get('utm_content')||'shop',page:location.pathname}})}}catch(x){{}}}};document.head.appendChild(s)}})();
</script></head><body>
<div class="draft"><a class="azt" href="https://aztechsol.com/websites/" target="_blank" rel="noopener"><img src="assets/aztech-brandmark.svg" alt="" width="20" height="20"><span>Like this site? <b>Get your own</b> &rarr;</span></a></div>
<header><div class="wrap"><a class="brand" href="index.html"><img src="assets/brand/lockup-dark.svg?v=0828fc1d" alt="Splash of Ink" height="58"></a>
<nav>{nav}</nav></div></header>
'''
NAV = [('index.html', 'Home'), ('artists.html', 'Artists'), ('prices.html', 'Prices'), ('apprentice.html', 'Apprentices'), ('visit.html', 'Visit')]
FOOT = '''<footer><div class="wrap"><span>© 2026 Splash of Ink · Fourth Avenue and Stone Avenue, Tucson · <a href="tel:+15206511910">(520) 651-1910</a> · <a href="tel:+15203923594">(520) 392-3594</a></span>
<span class="credit">Website by <a href="https://aztechsol.com/" target="_blank" rel="noopener">AZ Tech Solutions</a></span></div></footer>
</body></html>'''

SITE = 'https://splashofink.aztechsol.com/'
def og_tags(fn, title):
    slug = fn[len('artist-'):-5] if fn.startswith('artist-') else None
    img = f'og-{slug}.png' if slug and (R / 'assets' / 'og' / f'og-{slug}.png').exists() else 'og-site.png'
    desc = 'Tattoo and piercing on Fourth Avenue and at Stone Avenue, Tucson. Open 24/7 by appointment.'
    return (f'<meta property="og:type" content="website"><meta property="og:site_name" content="Splash of Ink">'
            f'<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{desc}">'
            f'<meta property="og:url" content="{SITE}{fn}"><meta property="og:image" content="{SITE}assets/og/{img}">'
            f'<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">'
            f'<meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="{SITE}assets/og/{img}">'
            f'<meta name="description" content="{desc}">')
def page(fn, title, body, extra=''):
    nav = ''.join(f'<a href="{h}"{" class=on" if h == fn or (fn.startswith("artist-") and h == "artists.html") else ""}>{t}</a>' for h, t in NAV)
    (R / fn).write_text(HEAD.format(title=html.escape(title), nav=nav, cssv=__import__('hashlib').md5(CSS.encode()).hexdigest()[:8]).replace('</title>', '</title>' + og_tags(fn, title), 1) + body + FOOT.replace('</body>', extra + '</body>'))

def ph(label): return f'<div class="ph">{html.escape(label)}<br>photo coming</div>'
def portrait(a):  # a real photo when the shop has sent one (assets/artists/<slug>.jpg), else the labelled placeholder
    f = R / 'assets' / 'artists' / f"{a['slug']}.jpg"
    return f'<img class="portrait" src="assets/artists/{a["slug"]}.jpg" alt="{html.escape(a["name"])}" width="900" height="900" loading="lazy">' if f.exists() else ph(a['name'] + ' · portrait')

def acard(a):
    return f'''<a class="card acard" href="artist-{a['slug']}.html">{portrait(a)}
      <h3 style="margin:4px 0 0">{a['name']}</h3><div class="note">{a['role']} · {SHOPNAME[a['shop']]}</div>
      <div class="tags">{''.join(f'<span>{s}</span>' for s in a['styles'])}</div><span class="btn ghost" style="text-align:center;margin-top:auto">See {a['name'].split()[0]}’s page</span></a>'''

def shop_block(s, heading='h2', compact=False):
    arts = [a for a in ARTISTS if a['shop'] == s['slug']]
    maplink = f'<a href="{s["map"]}" target="_blank" rel="noopener">Open in Google Maps →</a>' if s['map'] else f'<span class="note">{s.get("pending","")}</span>'
    phone = phones_inline()
    return f'''<div class="shop" id="{s['slug']}"><div class="shophead"><div><div class="eyebrow">Shop</div><{heading} style="font-size:34px;margin-bottom:6px">{s['name']}</{heading}><p style="margin:0">{s['blurb']}</p></div>
      <div class="card shopinfo"><p style="margin:0 0 6px">{s['addr']}</p><p style="margin:0 0 6px">{phone}</p><p style="margin:0">{maplink}</p></div></div>
      {('<p class="artistline">Artists: ' + ' · '.join(f'<a href="artist-{a["slug"]}.html">{a["name"]}</a>' for a in arts) + '</p>') if compact else ('<div class="grid3" style="margin-top:18px">' + ''.join(acard(a) for a in arts) + '</div>')}</div>'''

STYLES = ['Black and gray', 'Color', 'Fine line', 'Piercing']
def ask_modal():
    import json as _j
    opts = ''.join(f'<option value="{a["slug"]}">{a["name"]} · {SHOPNAME[a["shop"]]}</option>' for a in ARTISTS)
    names = {a['slug']: a['name'] + (' · ' + SHOPNAME[a['shop']] if a.get('apprentice') else '') for a in ARTISTS}
    igs = {}
    for a in ARTISTS:
        for n, u in a.get('socials', []):
            if n == 'Instagram' and 'instagram.com/' in u: igs[a['slug']] = u.rstrip('/').split('/')[-1]
    data = _j.dumps({'names': names, 'ig': igs, 'shop': ['+15206511910', '+15203923594']})
    form = f'''<dialog id="ask" class="askd"><form class="f" id="askf" novalidate>
  <button class="askx" type="button" aria-label="Close" onclick="this.closest('dialog').close()">×</button>
  <div id="askform">
  <h2 style="font-size:28px;margin:0" id="askh">Request prices</h2>
  <p class="note" style="margin:0">Every artist sets their own prices. Tell <b id="askwho">them</b> about your idea, and we’ll write it up as a text you can send the shop.</p>
  <input type="hidden" name="artist" id="askartist">
  <label id="askpick">Which artist?<select id="asksel">{opts}</select></label>
  <div class="two"><label>Your name<input name="name" autocomplete="name" required></label><label>Phone<input name="phone" type="tel" autocomplete="tel" required></label></div>
  <div class="two"><label>Placement<input name="placement" placeholder="Forearm, back, ankle…" required></label><label>Size <small>(roughly)</small><input name="size" placeholder="Palm size, about 3 × 4 in…"></label></div>
  <fieldset><legend>What kind?</legend><div class="chk">{''.join(f'<label><input type="radio" name="style" value="{s}"{" checked" if n == 0 else ""}> {s}</label>' for n, s in enumerate(STYLES))}</div></fieldset>
  <label>Tell them about it <small>(optional)</small><textarea name="notes" rows="3"></textarea></label>
  <p class="note" id="askerr" hidden></p>
  <button class="btn" type="submit">Get my message ready</button>
  <p class="note" style="margin:0;text-align:center">Have a reference picture? You can add it to the text once it opens.</p>
  </div>
  <div id="askready" hidden>
    <h2 style="font-size:26px;margin:0">Your message is ready.</h2>
    <p class="note" style="margin:4px 0 10px">Send it to the shop and <b id="askwho2">your artist</b> will get back to you with a price range.</p>
    <textarea id="askmsg" rows="7" readonly aria-label="Your message"></textarea>
    <a class="btn" id="asktext" href="#" style="display:block;text-align:center;margin-top:12px">Text the shop</a>
    <p class="note" style="margin:6px 0 0;text-align:center">Opens a group text to Master D and Magic with your message typed in. Add your reference picture, then send.</p>
    <p class="note" style="margin:10px 0 0;text-align:center">Group text not working? <a id="asktd" href="#">Text Master D only</a> · <a id="asktm" href="#">Text Magic only</a></p>
    <div id="askigwrap"><a class="btn ghost" id="askig" href="#" target="_blank" rel="noopener" style="display:block;text-align:center;margin-top:14px">Copy &amp; message <span id="askign">them</span> on Instagram</a>
    <p class="note" style="margin:6px 0 0;text-align:center">The message is copied: in the chat, tap the box, choose Paste, and send.</p></div>
    <p class="note" style="margin:12px 0 0;text-align:center"><a href="#" id="askedit">Change something</a> · <a href="#" id="askclose">Close</a></p>
  </div>
</form></dialog>
<script>var ASK={data};</script>'''
    js = r"""<script>
/* The price request is written up as a message and shown first. Primary: a group text to the shop (Master D + Magic)
   with the message typed in. Backups: text one of them. Secondary: the artist's own Instagram. Nothing opens on its own. */
(function(){var d=document.getElementById('ask'),f=document.getElementById('askf'),sel=document.getElementById('asksel'),hid=document.getElementById('askartist');
var $=function(i){return document.getElementById(i)},msg='',ios=/iPhone|iPad|iPod/.test(navigator.userAgent);
var track=function(n,x){try{if(window.umami)umami.track(n,x)}catch(e){}};
var sms=function(nums,body){var b=encodeURIComponent(body);if(nums.length>1)return ios?'sms://open?addresses='+nums.join(',')+'&body='+b:'sms:'+nums.join(',')+'?body='+b;return ios?'sms:'+nums[0]+'&body='+b:'sms:'+nums[0]+'?body='+b};
function show(ready){$('askform').hidden=ready;$('askready').hidden=!ready}
function open(slug){var known=slug&&ASK.names[slug];$('askpick').style.display=known?'none':'';if(known)sel.value=slug;hid.value=sel.value;
 $('askwho').textContent=ASK.names[sel.value]||'them';$('askh').textContent=known?'Request prices from '+ASK.names[slug]:'Request prices';show(false);$('askerr').hidden=true;d.showModal?d.showModal():d.setAttribute('open','')}
sel.addEventListener('change',function(){hid.value=sel.value;$('askwho').textContent=ASK.names[sel.value]});
document.addEventListener('click',function(e){var b=e.target.closest('[data-ask]');if(!b)return;e.preventDefault();open(b.getAttribute('data-ask'))});
d.addEventListener('click',function(e){if(e.target===d)d.close()});
var q=new URLSearchParams(location.search).get('artist');if(q&&ASK.names[q])open(q);
f.addEventListener('submit',function(e){e.preventDefault();var bad=[];['name','phone','placement'].forEach(function(n){if(!f[n].value.trim())bad.push(n)});
 var er=$('askerr');if(bad.length){er.hidden=false;er.textContent='Still needed: '+bad.join(', ')+'.';return}er.hidden=true;
 var who=ASK.names[hid.value]||'any artist',v=function(n){return (f[n].value||'').trim()},st=(f.querySelector('input[name=style]:checked')||{}).value;
 var L=['Hi Splash of Ink! I would like a price for a tattoo.','Artist: '+who,'Name: '+v('name'),'Phone: '+v('phone'),'Placement: '+v('placement')];
 if(v('size'))L.push('Size: '+v('size'));if(st)L.push('Style: '+st);if(v('notes'))L.push('Idea: '+v('notes'));msg=L.join('\n');
 $('askmsg').value=msg;$('askwho2').textContent=who;
 $('asktext').href=sms(ASK.shop,msg);$('asktd').href=sms([ASK.shop[0]],msg);$('asktm').href=sms([ASK.shop[1]],msg);
 var ig=ASK.ig[hid.value];$('askigwrap').hidden=!ig;if(ig){$('askig').href='https://ig.me/m/'+ig;$('askign').textContent=who.split(' ')[0]}
 show(true);track('price-ready',{artist:hid.value})});
$('asktext').addEventListener('click',function(){track('price-sent',{via:'text-shop',artist:hid.value})});
$('asktd').addEventListener('click',function(){track('price-sent',{via:'text-master-d',artist:hid.value})});
$('asktm').addEventListener('click',function(){track('price-sent',{via:'text-magic',artist:hid.value})});
$('askig').addEventListener('click',function(){try{navigator.clipboard&&navigator.clipboard.writeText(msg)}catch(e){};track('price-sent',{via:'instagram',artist:hid.value})});
$('askedit').addEventListener('click',function(e){e.preventDefault();show(false)});
$('askclose').addEventListener('click',function(e){e.preventDefault();d.close()});
})();
</script>"""
    return form + js

HOURSCARD = '<div class="card"><h3>Hours</h3><p style="font-size:18px;color:var(--fog);margin:0 0 10px">Open 24/7 by appointment.</p><p class="note" style="margin:0 0 6px">Walk-in hours</p><table class="hours">' + ''.join(f'<tr><td>{d}</td><td>{h}</td></tr>' for d, h in WALKIN) + '</table><p class="note" style="margin:8px 0 0">Late nights can run longer or shorter with how busy it is. Call ahead to be sure.</p></div>'

# Home
page('index.html', 'Splash of Ink · Tattoo and piercing in Tucson', f'''
<section class="hero"><div class="wrap">
  <div class="eyebrow">Tattoo and piercing · two shops in Tucson</div>
  <h1 class="lockup"><img src="assets/brand/lockup-dark.svg?v=0828fc1d" alt="Splash of Ink"></h1>
  <p class="lead">Good art, good people, good vibes. Find your shop, pick your artist, and ask them for prices.</p>
  <div class="row"><a class="btn" href="#shops">Find your shop</a><a class="btn ghost" href="artists.html">Meet the artists</a></div>
  {callbar()}
  <p class="note" style="margin-top:14px">{HOURS}</p>
</div></section>
<section class="alt" id="work"><div class="wrap"><div class="eyebrow">Recent work</div><h2 style="font-size:40px">Fresh from the chair</h2>
  <div class="works strip">{gallery('magic', 6)}{gallery('angel-perez-tattoos', 2)}</div>
  <p class="note" style="margin-top:10px">More on <a href="artist-magic.html">Magic’s</a> and <a href="artist-angel-perez.html">Angel’s</a> pages.</p></div></section>
{pricing_section()}
<section><div class="wrap"><div class="info">
  <div class="card"><h3>Pricing</h3><p>Every artist sets their own prices, and price depends on size and placement. Ask the artist you want and they’ll send a range.</p><a href="#pricing">See pricing →</a></div>
  <div class="card"><h3>Piercing</h3><p>Magic and Annie pierce at the Fourth Avenue shop.</p><a href="artist-annie.html">See Annie’s page →</a></div>
  <div class="card"><h3>Apprentices</h3><p>Want to learn? Our apprentice application is always open.</p><a href="apprentice.html">Apply →</a></div>
</div></div></section>
<section class="alt" id="shops"><div class="wrap">{''.join(shop_block(s, compact=True) for s in SHOPS)}</div></section>''', ask_modal())

# Artists directory, by shop
page('artists.html', 'Artists · Splash of Ink', f'''
<section class="hero" style="padding:60px 0 30px"><div class="wrap"><div class="eyebrow">Artists</div><h1 style="font-size:clamp(46px,8vw,80px)">Pick your artist</h1>
<p class="lead">Each artist works for themselves under the Splash of Ink roof, with their own style and their own prices.</p></div></section>
<section style="padding-top:10px"><div class="wrap">{''.join(shop_block(s, 'h2') for s in SHOPS)}</div></section>''')

# Artist pages
for a in ARTISTS:
    def work_sections(a, samples):
        if a.get('apprentice'):
            rows = ''.join(f'<div class="tier"><img src="assets/icons/{i}.svg" alt="" width="84" height="84"><div class="tname">{n}</div><div class="tprice">{APPRENTICE_PRICES.get(n, "To confirm")}</div><div class="tfit">{d}</div></div>' for n, d, r, i in SIZES)
            return f'''<section class="alt"><div class="wrap"><div class="eyebrow">Apprentice pricing</div><h2 style="font-size:30px">What it costs with the apprentice</h2>
<p style="max-width:680px">Apprentice prices are lower than the shop's main artists. The minimum is <b style="color:var(--fog)">$80</b>, and the final price still depends on size, placement and detail.</p>
<div class="chart">{rows}</div>
<p class="note" style="margin-top:10px">Sizes are measured against your hand, like the shop's main pricing guide. Questions? Ask at the counter.</p></div></section>'''
        if not WORK.get(a['slug']):
            return f'''<section class="alt"><div class="wrap"><div class="eyebrow">Best work</div><h2 style="font-size:30px">One best piece per style</h2>
<div class="samples" style="margin-top:16px">{samples}</div></div></section>'''
        sets = WORKSETS.get(a['slug'], [(a['slug'], 'Work', 'Recent work')])
        v, tk = videos(a['slug']), tiktoks(a['slug'])
        vs = (f'''<section><div class="wrap"><div class="eyebrow">Watch</div><h2 style="font-size:30px">In the chair</h2>
<div class="vids">{v}</div></div></section><script async src="https://www.instagram.com/embed.js"></script>''' if v else '') + (f'''<section class="alt"><div class="wrap"><div class="eyebrow">On TikTok</div><h2 style="font-size:30px">More from {a['name']}</h2>
<div class="vids">{tk}</div></div></section><script async src="https://www.tiktok.com/embed.js"></script>''' if tk else '')
        secs = ''.join(f'''<section class="alt"><div class="wrap"><div class="eyebrow">{eb}</div><h2 style="font-size:30px">{h}</h2>
{filters(key)}<div class="works">{gallery(key)}</div><p class="note" style="margin-top:10px">Tap any piece to see it on Instagram.</p></div></section>''' for key, eb, h in sets if WORK.get(key))
        return secs + vs + (FILTERJS if any(filters(k) for k, _, _ in sets) else '')
    samples = ''.join(f'<figure>{ph(a["name"] + " · " + s)}<figcaption>{s}</figcaption></figure>' for s in a['styles'])
    soc = ''.join(f'<a href="{u}"' + ('' if u == '#' else ' target="_blank" rel="noopener"') + f'>{n}{" (coming)" if u == "#" else ""}</a>' for n, u in a['socials'])
    minimum = f'<p><b style="color:var(--fog)">{a["minimum"]}</b></p>' if a['minimum'] else ''
    page(f'artist-{a["slug"]}.html', f'{a["name"]} · Splash of Ink', f'''
<section><div class="wrap prof">
  <div>{portrait(a)}</div>
  <div><div class="eyebrow"><a href="artists.html" style="text-decoration:none">Artists</a> › <a href="index.html#{a['shop']}" style="text-decoration:none">{SHOPNAME[a['shop']]}</a></div>
    <h1 style="font-size:52px">{a['name']}</h1><p class="note" style="margin-top:-8px">{a['role']}</p>
    <p>{a['bio']}</p>{minimum}
    <div class="tags" style="margin:12px 0 18px">{''.join(f'<span>{s}</span>' for s in a['styles'])}</div>
    <div class="row" style="justify-content:flex-start"><a class="btn" href="#" data-ask="{a['slug']}">{'Request apprentice pricing' if a.get('apprentice') else 'Request prices from ' + a['name'].split()[0]}</a><a class="btn ghost" href="{a['book'][1]}">{a['book'][0]}</a></div>
    <p class="note">{a['book'][2]}. How to pay is at the bottom of this page.</p>
    <div class="soc" style="margin-top:12px">{soc}</div>
  </div></div></section>
{work_sections(a, samples)}
<section><div class="wrap"><div class="eyebrow">Paying</div><h2 style="font-size:30px">How to pay</h2>
<p>All payments are due before the tattoo or piercing is done. Questions? Call Master D at <a href="tel:+15206511910">(520) 651-1910</a> or Magic at <a href="tel:+15203923594">(520) 392-3594</a>.</p>
<div class="pay">
  <div class="card"><h3>Venmo</h3><p>(520) 651-1910</p></div>
  <div class="card"><h3>Cash App</h3><p><a href="https://cash.app/$TattdGlassyy" target="_blank" rel="noopener">$TattdGlassyy</a></p></div>
  <div class="card"><h3>Zelle</h3><p>(520) 651-1910</p></div>
  <div class="card"><h3>Cash</h3><p>ATM inside the shop</p></div>
</div></div></section>''', ask_modal())

# Prices: a list of artists, each with their own request
rows = ''.join(f'''<div class="card prow"><div><h3 style="margin:0">{a['name']}</h3><div class="note">{a['role']} · {SHOPNAME[a['shop']]}</div></div>
  <div class="row" style="justify-content:flex-end"><a class="btn ghost" href="artist-{a['slug']}.html">Learn more</a><a class="btn" href="#" data-ask="{a['slug']}">Request prices</a></div></div>''' for a in ARTISTS)
page('prices.html', 'Request prices · Splash of Ink', f'''
<section class="hero" style="padding:60px 0 24px"><div class="wrap"><div class="eyebrow">Request prices</div><h1 style="font-size:clamp(46px,8vw,80px)">Ask your artist</h1>
<p class="lead">Each artist sets their own prices, and price depends on size and placement. Pick the artist you want and they’ll send you a range.</p></div></section>
<section style="padding-top:10px"><div class="wrap" style="display:grid;gap:12px">{rows}</div></section>''', ask_modal())

# Apprentice
page('apprentice.html', 'Apprentice applications · Splash of Ink', '''
<section class="hero" style="padding:60px 0 24px"><div class="wrap"><div class="eyebrow">Apprentices · always open</div><h1 style="font-size:clamp(46px,8vw,80px)">Learn with us</h1>
<p class="lead">We’re always looking for people who love to draw and want to learn tattooing or piercing. Applications stay open all year.</p></div></section>
<section style="padding-top:10px"><div class="wrap">
<form class="f card" id="af" novalidate>
  <div class="two"><label>Your name<input name="name" required></label><label>Phone<input name="phone" type="tel" required></label></div>
  <label>Email<input name="email" type="email" required></label>
  <label>Which shop?<select name="shop"><option>Fourth Avenue</option><option>Stone Avenue</option><option>Either</option></select></label>
  <label>Tattooing or piercing?<select name="track"><option>Tattooing</option><option>Piercing</option><option>Both</option></select></label>
  <label>Portfolio link <small>(Instagram, a drive folder, anything)</small><input name="portfolio" type="url" placeholder="https://"></label>
  <label>Experience <small>(drawing, art school, anything you’ve done)</small><textarea name="experience" rows="3"></textarea></label>
  <label>Why Splash of Ink?<textarea name="why" rows="3"></textarea></label>
  <button class="btn" type="submit">Send my application</button>
  <p class="note">Draft: this form doesn’t send anything yet.</p>
</form></div></section>''', '''<script>document.getElementById('af').addEventListener('submit',function(e){e.preventDefault();this.outerHTML='<div class="done"><h3>Thanks for applying.</h3><p>We’ll look at your work and reach out. (Draft: nothing was sent.)</p></div>';});</script>''')

# Visit
shopcards = ''.join(f'''<div class="card"><h3>{s['name']}</h3><p>{s['addr']}</p><p>{phones_inline()}</p><p>{f'<a href="{s["map"]}" target="_blank" rel="noopener">Open in Google Maps →</a>' if s['map'] else f'<span class="note">{s.get("pending","")}</span>'}</p></div>''' for s in SHOPS)
page('visit.html', 'Visit · Splash of Ink', f'''
<section class="hero" style="padding:60px 0 24px"><div class="wrap"><div class="eyebrow">Visit</div><h1 style="font-size:clamp(46px,8vw,80px)">Come say hi</h1>
<p class="lead">There’s always someone close enough to open the door. Book ahead to get the artist you want.</p>{callbar()}</div></section>
<section style="padding-top:10px"><div class="wrap"><div class="info">{shopcards}{HOURSCARD}</div></div></section>''')

(R / 'style.css').write_text(CSS)
(R / '.nojekyll').write_text('')
print('built')
