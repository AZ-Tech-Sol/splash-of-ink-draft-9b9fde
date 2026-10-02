"""Splash of Ink: a Starter Site draft (brochure pages, simple forms, booking and payments link out). Generated; edit here, then python3 build.py."""
import pathlib, html
R = pathlib.Path(__file__).parent
SHOP = 'Splash of Ink'

ARTISTS = [
  dict(slug='magic', name='Magic', role='Head artist · with the shop since day one',
       bio='The last of the shop’s original artists. There’s very little Magic doesn’t do, from delicate fine line to full realism.',
       styles=['Fine line', 'Black and gray', 'Neo-traditional', 'American traditional', 'Color', 'Realism'],
       minimum='$100 shop minimum', book=('Book with Magic', '#', 'Booking link coming'),
       socials=[('Instagram', '#'), ('TikTok', '#'), ('Facebook', '#')]),
  dict(slug='angel-perez', name='Angel Perez', role='Artist · anime, comic and color',
       bio='Anime and comic work with bold color and clean black and gray, and fine line on the way.',
       styles=['Anime', 'Comic', 'Color', 'Black and gray'],
       minimum='', book=('Book with Angel on Setmore', '#', 'Setmore link coming'),
       socials=[('Instagram', '#'), ('TikTok', '#'), ('Facebook', '#')]),
  dict(slug='artist', name='Artist name', role='Placeholder for the next artist',
       bio='A slot for another artist’s page. Their styles, best samples and booking link go here.',
       styles=['Style one', 'Style two', 'Style three'],
       minimum='', book=('Book with this artist', '#', 'Booking link coming'),
       socials=[('Instagram', '#')], placeholder=True),
]

CSS = '''
:root{--ink:#0b0910;--ink2:#15111d;--card:#1b1526;--line:#2e2540;--purple:#8b3dff;--purple2:#b98cff;--glow:#a855f7;--fog:#f3eefb;--body:#cfc6de;--mute:#968bab}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--ink);color:var(--body);font:16px/1.65 Inter,system-ui,sans-serif}
a{color:var(--purple2)}img{max-width:100%;display:block}
h1,h2,h3{font-family:Oswald,sans-serif;color:var(--fog);line-height:1.15;margin:0 0 .5em;letter-spacing:.01em;font-weight:600}
.wrap{max-width:1120px;margin:0 auto;padding:0 20px}
.draft{background:var(--purple);color:#fff;text-align:center;font:600 13px/1.4 Inter,sans-serif;padding:7px 16px}
header{border-bottom:1px solid var(--line);background:rgba(11,9,16,.92);position:sticky;top:0;z-index:5;backdrop-filter:blur(6px)}
header .wrap{display:flex;align-items:center;justify-content:space-between;gap:16px;padding:12px 20px;flex-wrap:wrap}
.brand{font:400 34px/1 "Pirata One",serif;color:var(--fog);text-decoration:none;letter-spacing:.02em}
.brand span{color:var(--purple2)}
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
'''

HEAD = '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow"><title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Oswald:wght@500;600&family=Pirata+One&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css"></head><body>
<div class="draft">DRAFT for Splash of Ink · samples, links and hours are placeholders · forms send nothing</div>
<header><div class="wrap"><a class="brand" href="index.html">Splash <span>of</span> Ink</a>
<nav>{nav}</nav></div></header>
'''
NAV = [('index.html', 'Home'), ('artists.html', 'Artists'), ('prices.html', 'Request prices'), ('apprentice.html', 'Apprentices'), ('visit.html', 'Visit')]
FOOT = '''<footer><div class="wrap"><span>© 2026 Splash of Ink · 532 N 4th Ave, Tucson, AZ 85705 · <a href="tel:+15206511910">(520) 651-1910</a></span>
<span class="credit">Website by <a href="https://aztechsol.com/" target="_blank" rel="noopener">AZ Tech Solutions</a></span></div></footer>
</body></html>'''

def page(fn, title, body, extra=''):
    nav = ''.join(f'<a href="{h}"{" class=on" if h == fn or (fn.startswith("artist-") and h == "artists.html") else ""}>{t}</a>' for h, t in NAV)
    (R / fn).write_text(HEAD.format(title=html.escape(title), nav=nav) + body + FOOT.replace('</body>', extra + '</body>'))

def ph(label): return f'<div class="ph">{html.escape(label)}<br>photo coming</div>'

def acard(a):
    return f'''<a class="card acard" href="artist-{a['slug']}.html">{ph(a['name'] + ' · portrait')}
      <h3 style="margin:4px 0 0">{a['name']}</h3><div class="note">{a['role']}</div>
      <div class="tags">{''.join(f'<span>{s}</span>' for s in a['styles'])}</div><span class="btn ghost" style="text-align:center;margin-top:auto">See {a['name'].split()[0]}’s page</span></a>'''

# Home
page('index.html', 'Splash of Ink · Tattoo shop in Tucson', f'''
<section class="hero"><div class="wrap">
  <div class="eyebrow">Tattoo shop · Fourth Avenue, Tucson</div>
  <h1>Splash of Ink</h1>
  <p class="lead">Good art, good people, good vibes. Pick your artist, see their best work, and book straight with them.</p>
  <div class="row"><a class="btn" href="artists.html">Meet the artists</a><a class="btn ghost" href="prices.html">Request prices</a></div>
</div></section>
<section class="alt"><div class="wrap">
  <div class="eyebrow">The artists</div><h2 style="font-size:34px">Every artist has their own page</h2>
  <p style="max-width:640px">Each page shows the styles that artist does, one best piece for each, where to follow them, and how to book with them.</p>
  <div class="grid3" style="margin-top:22px">{''.join(acard(a) for a in ARTISTS)}</div>
</div></section>
<section><div class="wrap"><div class="info">
  <div class="card"><h3>Pricing</h3><p>Price depends on size and placement: the same design costs more on ribs, stomach, neck, hands or feet. Tell us what you want and we’ll send the prices.</p><a href="prices.html">Request prices →</a></div>
  <div class="card"><h3>Big pieces</h3><p>Larger work can be split into sessions to fit your budget. Talk it through with your artist.</p><a href="artists.html">Choose an artist →</a></div>
  <div class="card"><h3>Apprentices</h3><p>Want to learn? Our apprentice application is always open.</p><a href="apprentice.html">Apply →</a></div>
</div></div></section>''')

# Artists directory
page('artists.html', 'Artists · Splash of Ink', f'''
<section class="hero" style="padding:60px 0 30px"><div class="wrap"><div class="eyebrow">Artists</div><h1 style="font-size:clamp(46px,8vw,80px)">Pick your artist</h1>
<p class="lead">Choose the artist whose style fits your idea. They’ll confirm your booking.</p></div></section>
<section style="padding-top:10px"><div class="wrap"><div class="grid3">{''.join(acard(a) for a in ARTISTS)}</div></div></section>''')

# Artist pages
for a in ARTISTS:
    samples = ''.join(f'<figure>{ph(a["name"] + " · " + s)}<figcaption>{s}</figcaption></figure>' for s in a['styles'])
    soc = ''.join(f'<a href="{u}">{n}</a>' for n, u in a['socials'])
    minimum = f'<p><b style="color:var(--fog)">{a["minimum"]}</b></p>' if a['minimum'] else ''
    page(f'artist-{a["slug"]}.html', f'{a["name"]} · Splash of Ink', f'''
<section><div class="wrap prof">
  <div>{ph(a['name'] + ' · portrait')}</div>
  <div><div class="eyebrow"><a href="artists.html" style="text-decoration:none">Artists</a> › {a['name']}</div>
    <h1 style="font-size:52px">{a['name']}</h1><p class="note" style="margin-top:-8px">{a['role']}</p>
    <p>{a['bio']}</p>{minimum}
    <div class="tags" style="margin:12px 0 18px">{''.join(f'<span>{s}</span>' for s in a['styles'])}</div>
    <div class="row" style="justify-content:flex-start"><a class="btn" href="{a['book'][1]}">{a['book'][0]}</a><a class="btn ghost" href="prices.html?artist={a['slug']}">Request prices</a></div>
    <p class="note">{a['book'][2]}. Booking and payment happen in the artist’s booking tool, not on this site.</p>
    <div class="soc" style="margin-top:12px">{soc}</div>
  </div></div></section>
<section class="alt"><div class="wrap"><div class="eyebrow">Best work</div><h2 style="font-size:30px">One best piece per style</h2>
<div class="samples" style="margin-top:16px">{samples}</div></div></section>''')

# Request prices
opts = ''.join(f'<option value="{a["slug"]}">{a["name"]}</option>' for a in ARTISTS) + '<option value="any">Any artist</option>'
page('prices.html', 'Request prices · Splash of Ink', f'''
<section class="hero" style="padding:60px 0 24px"><div class="wrap"><div class="eyebrow">Request prices</div><h1 style="font-size:clamp(46px,8vw,80px)">Tell us your idea</h1>
<p class="lead">Price depends on size and placement. Send the details and we’ll get back to you with prices.</p></div></section>
<section style="padding-top:10px"><div class="wrap">
<form class="f card" id="pf" novalidate>
  <div class="two"><label>Your name<input name="name" autocomplete="name" required></label><label>Phone<input name="phone" type="tel" autocomplete="tel" required></label></div>
  <label>Email<input name="email" type="email" autocomplete="email" required></label>
  <div class="two"><label>Which artist?<select name="artist" id="artist">{opts}</select></label><label>Placement<input name="placement" placeholder="Forearm, back, ankle…" required></label></div>
  <label>Size <small>(roughly, in inches)</small><input name="size" placeholder="About 3 × 4 in"></label>
  <fieldset><legend>Style</legend><div class="chk"><label><input type="radio" name="style" value="black-gray" checked> Black and gray</label><label><input type="radio" name="style" value="color"> Color</label><label><input type="radio" name="style" value="fine-line"> Fine line</label></div></fieldset>
  <label>Tell us about it <small>(optional)</small><textarea name="notes" rows="4"></textarea></label>
  <label>Reference image <small>(optional)</small><input name="image" type="file" accept="image/*"></label>
  <p class="err note" id="perr" hidden></p>
  <button class="btn" type="submit">Request prices</button>
  <p class="note">Draft: this form doesn’t send anything yet.</p>
</form></div></section>''', '''<script>
(function(){var q=new URLSearchParams(location.search).get('artist');if(q){var s=document.getElementById('artist');if([].some.call(s.options,function(o){return o.value===q}))s.value=q;}
var f=document.getElementById('pf');f.addEventListener('submit',function(e){e.preventDefault();var bad=[];['name','phone','email','placement'].forEach(function(n){if(!f[n].value.trim())bad.push(n)});
var er=document.getElementById('perr');if(bad.length){er.hidden=false;er.textContent='Still needed: '+bad.join(', ')+'.';return}
f.outerHTML='<div class="done"><h3>Thanks, we’ve got it.</h3><p>We’ll be in touch with prices. (Draft: nothing was sent.)</p></div>';});})();
</script>''')

# Apprentice
page('apprentice.html', 'Apprentice applications · Splash of Ink', '''
<section class="hero" style="padding:60px 0 24px"><div class="wrap"><div class="eyebrow">Apprentices · always open</div><h1 style="font-size:clamp(46px,8vw,80px)">Learn with us</h1>
<p class="lead">We’re always looking for people who love to draw and want to learn the craft. Applications stay open all year.</p></div></section>
<section style="padding-top:10px"><div class="wrap">
<form class="f card" id="af" novalidate>
  <div class="two"><label>Your name<input name="name" required></label><label>Phone<input name="phone" type="tel" required></label></div>
  <label>Email<input name="email" type="email" required></label>
  <label>Portfolio link <small>(Instagram, a drive folder, anything)</small><input name="portfolio" type="url" placeholder="https://"></label>
  <label>Experience <small>(drawing, art school, any tattooing)</small><textarea name="experience" rows="3"></textarea></label>
  <label>Why Splash of Ink?<textarea name="why" rows="3"></textarea></label>
  <button class="btn" type="submit">Send my application</button>
  <p class="note">Draft: this form doesn’t send anything yet.</p>
</form></div></section>''', '''<script>document.getElementById('af').addEventListener('submit',function(e){e.preventDefault();this.outerHTML='<div class="done"><h3>Thanks for applying.</h3><p>We’ll look at your work and reach out. (Draft: nothing was sent.)</p></div>';});</script>''')

# Visit
page('visit.html', 'Visit · Splash of Ink', '''
<section class="hero" style="padding:60px 0 24px"><div class="wrap"><div class="eyebrow">Visit</div><h1 style="font-size:clamp(46px,8vw,80px)">Come say hi</h1>
<p class="lead">Walk-ins welcome when an artist is free. Booking ahead is the surest way to get your artist.</p></div></section>
<section style="padding-top:10px"><div class="wrap"><div class="info">
  <div class="card"><h3>Where</h3><p>532 N 4th Ave<br>Tucson, AZ 85705</p><p>On Tucson's historic Fourth Avenue.</p><p><a href="https://maps.app.goo.gl/kkLf8c94uTDTxXT69" target="_blank" rel="noopener">Open in Google Maps →</a></p></div>
  <div class="card"><h3>Hours</h3><table class="hours">
    <tr><td>Monday</td><td>hours</td></tr><tr><td>Tuesday</td><td>hours</td></tr><tr><td>Wednesday</td><td>hours</td></tr><tr><td>Thursday</td><td>hours</td></tr><tr><td>Friday</td><td>hours</td></tr><tr><td>Saturday</td><td>hours</td></tr><tr><td>Sunday</td><td>hours</td></tr></table><p class="note">Hours to confirm with the shop</p></div>
  <div class="card"><h3>Walk-ins</h3><p>Walk-ins depend on who’s free that day. Call ahead, or book with an artist from their page.</p><p><a href="tel:+15206511910">(520) 651-1910</a></p></div>
</div></div></section>''')

(R / 'style.css').write_text(CSS)
(R / '.nojekyll').write_text('')
print('built')
