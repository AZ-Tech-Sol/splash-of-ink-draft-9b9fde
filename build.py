"""Splash of Ink: a Starter Site draft (brochure pages, simple forms, booking and payments link out). Generated; edit here, then python3 build.py."""
import pathlib, html
R = pathlib.Path(__file__).parent
SHOP = 'Splash of Ink'

SHOPS = [
  dict(slug='fourth-avenue', name='Fourth Avenue', addr='532 N 4th Ave<br>Tucson, AZ 85705', map='https://maps.google.com/?cid=3162480668975808258', phone=('(520) 651-1910','+15206511910'), blurb='The original shop, on Tucson\u2019s historic Fourth Avenue.'),
  dict(slug='stone-avenue', name='Stone Avenue', addr='3050 N Stone Ave<br>Tucson, AZ 85705', map='https://maps.app.goo.gl/h9L7F6SiUq7BHN4W7', phone=('(520) 651-1910','+15206511910'), blurb='Our second shop, on Stone Avenue.'),
]
PHONES = [('Master D', '(520) 651-1910', '+15206511910', 'Main line'), ('Magic', '(520) 392-3594', '+15203923594', 'Second line')]
def callbar():  # D's number first, Magic's right beside it and just as big
    return '<div class="callbar">' + ''.join(f'<a class="call{" alt" if n else ""}" href="tel:{e}"><span class="cl">{lab} · {who}</span><span class="cn">{num}</span></a>' for n, (who, num, e, lab) in enumerate(PHONES)) + '</div>'
def phones_inline():
    return ' · '.join(f'<a href="tel:{e}">{num}</a> ({who})' for who, num, e, _ in PHONES)
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
       minimum='', book=('Book with Angel on Setmore', '#', 'Setmore link coming'),
       socials=[('Instagram', 'https://www.instagram.com/thegreatsagetattoosandtarot/'), ('TikTok', 'https://www.tiktok.com/@greatsagetattooandtarot')]),
]
SHOPNAME = {s['slug']: s['name'] for s in SHOPS}

CSS = '''
:root{--ink:#0b0910;--ink2:#15111d;--card:#1b1526;--line:#2e2540;--purple:#8b3dff;--purple2:#b98cff;--glow:#a855f7;--fog:#f3eefb;--body:#cfc6de;--mute:#968bab}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--ink);color:var(--body);font:16px/1.65 Inter,system-ui,sans-serif}
a{color:var(--purple2)}img{max-width:100%;display:block}
h2{font-family:UnifrakturMaguntia,serif!important;font-weight:400!important;letter-spacing:.01em!important;text-shadow:3px 3px 0 #3b3150}
h1,h3{font-family:Oswald,sans-serif;}
h1,h2,h3{color:var(--fog);line-height:1.15;margin:0 0 .5em;letter-spacing:.01em;font-weight:600}
.wrap{max-width:1120px;margin:0 auto;padding:0 20px}
.draft{background:var(--purple);color:#fff;text-align:center;font:600 13px/1.4 Inter,sans-serif;padding:7px 16px}
header{background:rgba(11,9,16,.92);border-bottom:3px solid var(--purple);box-shadow:0 2px 18px rgba(139,61,255,.35);position:sticky;top:0;z-index:5;backdrop-filter:blur(6px)}
header .wrap{display:flex;align-items:center;justify-content:space-between;gap:16px;padding:12px 20px;flex-wrap:wrap}
.brand{font:400 34px/1 "Pirata One",serif;color:var(--fog);text-decoration:none;letter-spacing:.02em}
.brand img{height:46px;width:auto;display:block}
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
.prow{display:flex;justify-content:space-between;align-items:center;gap:14px;flex-wrap:wrap}
.askd{border:1px solid var(--line);border-radius:18px;background:var(--card);color:var(--body);padding:0;max-width:600px;width:calc(100% - 28px)}
.askd::backdrop{background:rgba(5,3,9,.75)}.askd form{padding:26px 24px;position:relative;max-width:none}
.askx{position:absolute;top:10px;right:14px;background:none;border:0;color:var(--mute);font-size:28px;cursor:pointer;line-height:1}
'''

HEAD = '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow"><title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Oswald:wght@500;600&family=UnifrakturMaguntia&family=Mr+Dafoe&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css"></head><body>
<div class="draft">DRAFT for Splash of Ink · samples, links and hours are placeholders · forms send nothing</div>
<header><div class="wrap"><a class="brand" href="index.html"><img src="assets/brand/lockup-dark.svg?v=10eb4ea9" alt="Splash of Ink" height="46"></a>
<nav>{nav}</nav></div></header>
'''
NAV = [('index.html', 'Home'), ('artists.html', 'Artists'), ('prices.html', 'Prices'), ('apprentice.html', 'Apprentices'), ('visit.html', 'Visit')]
FOOT = '''<footer><div class="wrap"><span>© 2026 Splash of Ink · Fourth Avenue and Stone Avenue, Tucson · <a href="tel:+15206511910">(520) 651-1910</a> · <a href="tel:+15203923594">(520) 392-3594</a></span>
<span class="credit">Website by <a href="https://aztechsol.com/" target="_blank" rel="noopener">AZ Tech Solutions</a></span></div></footer>
</body></html>'''

SITE = 'https://az-tech-sol.github.io/splash-of-ink-draft-9b9fde/'
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
    (R / fn).write_text(HEAD.format(title=html.escape(title), nav=nav).replace('</title>', '</title>' + og_tags(fn, title), 1) + body + FOOT.replace('</body>', extra + '</body>'))

def ph(label): return f'<div class="ph">{html.escape(label)}<br>photo coming</div>'
def portrait(a):  # a real photo when the shop has sent one (assets/artists/<slug>.jpg), else the labelled placeholder
    f = R / 'assets' / 'artists' / f"{a['slug']}.jpg"
    return f'<img class="portrait" src="assets/artists/{a["slug"]}.jpg" alt="{html.escape(a["name"])}" width="900" height="900" loading="lazy">' if f.exists() else ph(a['name'] + ' · portrait')

def acard(a):
    return f'''<a class="card acard" href="artist-{a['slug']}.html">{portrait(a)}
      <h3 style="margin:4px 0 0">{a['name']}</h3><div class="note">{a['role']} · {SHOPNAME[a['shop']]}</div>
      <div class="tags">{''.join(f'<span>{s}</span>' for s in a['styles'])}</div><span class="btn ghost" style="text-align:center;margin-top:auto">See {a['name'].split()[0]}’s page</span></a>'''

def shop_block(s, heading='h2'):
    arts = [a for a in ARTISTS if a['shop'] == s['slug']]
    maplink = f'<a href="{s["map"]}" target="_blank" rel="noopener">Open in Google Maps →</a>' if s['map'] else f'<span class="note">{s.get("pending","")}</span>'
    phone = phones_inline()
    return f'''<div class="shop" id="{s['slug']}"><div class="shophead"><div><div class="eyebrow">Shop</div><{heading} style="font-size:34px;margin-bottom:6px">{s['name']}</{heading}><p style="margin:0">{s['blurb']}</p></div>
      <div class="card shopinfo"><p style="margin:0 0 6px">{s['addr']}</p><p style="margin:0 0 6px">{phone}</p><p style="margin:0">{maplink}</p></div></div>
      <div class="grid3" style="margin-top:18px">{''.join(acard(a) for a in arts)}</div></div>'''

STYLES = ['Black and gray', 'Color', 'Fine line', 'Piercing']
def ask_modal():
    opts = ''.join(f'<option value="{a["slug"]}">{a["name"]} · {SHOPNAME[a["shop"]]}</option>' for a in ARTISTS)
    return f'''<dialog id="ask" class="askd"><form class="f" id="askf" novalidate>
  <button class="askx" type="button" aria-label="Close" onclick="this.closest('dialog').close()">×</button>
  <h2 style="font-size:28px;margin:0" id="askh">Request prices</h2>
  <p class="note" style="margin:0">Every artist sets their own prices. Tell <b id="askwho">them</b> about your idea and they’ll send you a price range.</p>
  <input type="hidden" name="artist" id="askartist">
  <label id="askpick">Which artist?<select id="asksel">{opts}</select></label>
  <div class="two"><label>Your name<input name="name" autocomplete="name" required></label><label>Phone<input name="phone" type="tel" autocomplete="tel" required></label></div>
  <label>Email<input name="email" type="email" autocomplete="email" required></label>
  <div class="two"><label>Placement<input name="placement" placeholder="Forearm, back, ankle…" required></label><label>Size <small>(roughly)</small><input name="size" placeholder="About 3 × 4 in"></label></div>
  <fieldset><legend>What kind?</legend><div class="chk">{''.join(f'<label><input type="radio" name="style" value="{s}"{" checked" if n == 0 else ""}> {s}</label>' for n, s in enumerate(STYLES))}</div></fieldset>
  <label>Tell them about it <small>(optional)</small><textarea name="notes" rows="3"></textarea></label>
  <label>Reference image <small>(optional)</small><input name="image" type="file" accept="image/*"></label>
  <p class="note" id="askerr" hidden></p>
  <button class="btn" type="submit">Send to the artist</button>
  <p class="note" style="margin:0;text-align:center">Draft: this form doesn’t send anything yet.</p>
</form></dialog>
<script>
(function(){{var d=document.getElementById('ask'),f=document.getElementById('askf'),sel=document.getElementById('asksel'),hid=document.getElementById('askartist');
var names={{{','.join(f'"{a["slug"]}":"{a["name"]}"' for a in ARTISTS)}}};
function open(slug){{var known=slug&&names[slug];document.getElementById('askpick').style.display=known?'none':'';
 if(known){{sel.value=slug}} hid.value=sel.value; document.getElementById('askwho').textContent=names[sel.value]||'them';
 document.getElementById('askh').textContent=known?'Request prices from '+names[slug]:'Request prices'; d.showModal?d.showModal():d.setAttribute('open','')}}
sel.addEventListener('change',function(){{hid.value=sel.value;document.getElementById('askwho').textContent=names[sel.value]}});
document.addEventListener('click',function(e){{var b=e.target.closest('[data-ask]');if(!b)return;e.preventDefault();open(b.getAttribute('data-ask'))}});
d.addEventListener('click',function(e){{if(e.target===d)d.close()}});
var q=new URLSearchParams(location.search).get('artist'); if(q&&names[q]) open(q);
f.addEventListener('submit',function(e){{e.preventDefault();var bad=[];['name','phone','email','placement'].forEach(function(n){{if(!f[n].value.trim())bad.push(n)}});
 var er=document.getElementById('askerr');if(bad.length){{er.hidden=false;er.textContent='Still needed: '+bad.join(', ')+'.';return}}
 var who=names[hid.value]||'the artist'; f.innerHTML='<h2 style="font-size:26px;margin:0">Sent to '+who+'.</h2><p>'+who+' will get back to you with a price range. (Draft: nothing was sent.)</p><button class="btn" type="button" id="askdone">Close</button>'; document.getElementById('askdone').onclick=function(){{d.close()}};}});
}})();
</script>'''

HOURSCARD = '<div class="card"><h3>Hours</h3><p style="font-size:18px;color:var(--fog);margin:0 0 10px">Open 24/7 by appointment.</p><p class="note" style="margin:0 0 6px">Walk-in hours</p><table class="hours">' + ''.join(f'<tr><td>{d}</td><td>{h}</td></tr>' for d, h in WALKIN) + '</table><p class="note" style="margin:8px 0 0">Late nights can run longer or shorter with how busy it is. Call ahead to be sure.</p></div>'

# Home
page('index.html', 'Splash of Ink · Tattoo and piercing in Tucson', f'''
<section class="hero"><div class="wrap">
  <div class="eyebrow">Tattoo and piercing · two shops in Tucson</div>
  <h1 class="lockup"><img src="assets/brand/lockup-dark.svg?v=10eb4ea9" alt="Splash of Ink"></h1>
  <p class="lead">Good art, good people, good vibes. Find your shop, pick your artist, and ask them for prices.</p>
  <div class="row"><a class="btn" href="#shops">Find your shop</a><a class="btn ghost" href="artists.html">Meet the artists</a></div>
  {callbar()}
  <p class="note" style="margin-top:14px">{HOURS}</p>
</div></section>
<section class="alt" id="shops"><div class="wrap">{''.join(shop_block(s) for s in SHOPS)}</div></section>
<section><div class="wrap"><div class="info">
  <div class="card"><h3>Pricing</h3><p>Every artist sets their own prices, and price depends on size and placement. Ask the artist you want and they’ll send a range.</p><a href="prices.html">Request prices →</a></div>
  <div class="card"><h3>Piercing</h3><p>Magic and Annie pierce at the Fourth Avenue shop.</p><a href="artist-annie.html">See Annie’s page →</a></div>
  <div class="card"><h3>Apprentices</h3><p>Want to learn? Our apprentice application is always open.</p><a href="apprentice.html">Apply →</a></div>
</div></div></section>''', ask_modal())

# Artists directory, by shop
page('artists.html', 'Artists · Splash of Ink', f'''
<section class="hero" style="padding:60px 0 30px"><div class="wrap"><div class="eyebrow">Artists</div><h1 style="font-size:clamp(46px,8vw,80px)">Pick your artist</h1>
<p class="lead">Each artist works for themselves under the Splash of Ink roof, with their own style and their own prices.</p></div></section>
<section style="padding-top:10px"><div class="wrap">{''.join(shop_block(s, 'h2') for s in SHOPS)}</div></section>''')

# Artist pages
for a in ARTISTS:
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
    <div class="row" style="justify-content:flex-start"><a class="btn" href="#" data-ask="{a['slug']}">Request prices from {a['name'].split()[0]}</a><a class="btn ghost" href="{a['book'][1]}">{a['book'][0]}</a></div>
    <p class="note">{a['book'][2]}. How to pay is at the bottom of this page.</p>
    <div class="soc" style="margin-top:12px">{soc}</div>
  </div></div></section>
<section class="alt"><div class="wrap"><div class="eyebrow">Best work</div><h2 style="font-size:30px">One best piece per style</h2>
<div class="samples" style="margin-top:16px">{samples}</div></div></section>
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
