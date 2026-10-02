"""Open Graph images (1200x630) for Splash of Ink: one for the site, one per artist with their portrait. Rendered with headless Chrome."""
import subprocess, pathlib, importlib.util, html
R = pathlib.Path(__file__).parent
spec = importlib.util.spec_from_file_location('b', R / 'build.py')
src = (R / 'build.py').read_text(); ns = {'__file__': str(R / 'build.py')}
exec(src.split('CSS = ')[0], ns)  # ARTISTS, SHOPS, SHOPNAME without building the pages
ARTISTS, SHOPNAME = ns['ARTISTS'], ns['SHOPNAME']
CH = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
BASE = '''<!doctype html><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@500;600&family=Oswald:wght@600&family=UnifrakturMaguntia&display=swap" rel="stylesheet">
<style>html,body{margin:0;width:1200px;height:630px;overflow:hidden}
body{background:radial-gradient(800px 420px at 50% 0%,rgba(139,61,255,.38),transparent 70%),radial-gradient(circle,rgba(139,61,255,.20) 0 2px,transparent 3px) 0 0/40px 40px,#0b0910;font-family:Inter,sans-serif;color:#cfc6de;position:relative}
.drip{position:absolute;left:0;right:0;top:0;height:70px;background:url(../assets/brand/drip.svg) top/100% 100% no-repeat}
.eye{font:600 22px Oswald,sans-serif;letter-spacing:.2em;text-transform:uppercase;color:#b98cff}
.foot{position:absolute;left:0;right:0;bottom:30px;text-align:center;font:500 22px Inter;color:#968bab}
</style><div class="drip"></div>'''
def shot(name, body):
    h = R / 'og' / f'{name}.html'; h.write_text(BASE + body)
    out = R / 'og' / f'og-{name}.png'
    subprocess.run([CH, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--window-size=1200,630', '--virtual-time-budget=3000', f'--screenshot={out}', f'file://{h}'], capture_output=True)
    print(out.name)
shot('site', '''<div style="position:absolute;inset:110px 0 0 0;text-align:center">
<div class="eye">Tattoo and piercing · Tucson</div>
<img src="../assets/brand/lockup-dark.svg" style="width:760px;margin:26px auto 0;display:block;filter:drop-shadow(0 8px 40px rgba(139,61,255,.4))"></div>
<div class="foot">Fourth Avenue · Stone &amp; Fort Lowell · Open 24/7 by appointment</div>''')
for a in ARTISTS:
    pic = R / 'assets' / 'artists' / f"{a['slug']}.jpg"
    if not pic.exists(): continue
    styles = '' if 'coming' in ' '.join(a['styles']).lower() else ' · '.join(a['styles'][:4])
    fs = 120 if len(a['name']) <= 8 else 92
    shot(a['slug'], f'''<img src="../assets/artists/{a['slug']}.jpg" style="position:absolute;right:70px;top:95px;width:440px;height:440px;object-fit:cover;border-radius:22px;border:3px solid #8b3dff;box-shadow:0 0 50px rgba(139,61,255,.35)">
<div style="position:absolute;left:80px;top:120px;width:560px">
<div class="eye">{html.escape(SHOPNAME[a['shop']])}</div>
<div style="font:400 {fs}px/1 UnifrakturMaguntia,serif;white-space:nowrap;color:#f3eefb;text-shadow:5px 5px 0 #3b3150;margin:16px 0 12px">{html.escape(a['name'])}</div>
<div style="font:600 30px Oswald,sans-serif;color:#cfc6de;letter-spacing:.03em">{html.escape(a['role'])}</div>
<div style="font:500 22px Inter;color:#968bab;margin-top:10px">{html.escape(styles)}</div>
<img src="../assets/brand/lockup-dark.svg" style="width:300px;margin-top:40px;display:block"></div>''')
