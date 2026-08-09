#!/usr/bin/env python3
"""
Regenerate index.html (the launcher) from apps.json.

Usage:  python3 build_launcher.py [folder]
Reads   <folder>/apps.json
Writes  <folder>/index.html

Links are RELATIVE (e.g. "road-trip-companion.html"), so the launcher works
identically on GitHub Pages, on any other host, and opened straight off disk.
No usernames or URLs are baked in.

Deterministic: safe to re-run any time. Never edit index.html by hand —
edit apps.json and re-run this.
"""
import json, sys, os, html
from datetime import date

FOLDER = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(FOLDER, "apps.json")
OUT = os.path.join(FOLDER, "index.html")

with open(DATA) as f:
    cfg = json.load(f)

apps = cfg.get("apps", [])


def link_for(a):
    """Relative file link wins; absolute url is a fallback for externally hosted apps."""
    if a.get("file") and os.path.exists(os.path.join(FOLDER, a["file"])):
        return a["file"], False
    if a.get("url"):
        return a["url"], True
    return None, False


live, pending = [], []
for a in apps:
    (live if link_for(a)[0] else pending).append(a)


def esc(s):
    return html.escape(s or "", quote=True)


def card(a):
    href, external = link_for(a)
    icon = a.get("icon") or "▦"
    colour = a.get("colour") or "#0a84ff"
    tags = "".join(f'<span class="tag">{esc(t)}</span>' for t in a.get("tags", []))
    meta = f'Updated {esc(a["updated"])}' if a.get("updated") else "Not built yet"
    if href:
        tgt = ' target="_blank" rel="noopener"' if external else ""
        return f'''<a class="app" href="{esc(href)}"{tgt}>
      <div class="ic" style="background:{esc(colour)}22;color:{esc(colour)}">{icon}</div>
      <div class="txt">
        <div class="nm">{esc(a.get("name"))}</div>
        <div class="bl">{esc(a.get("blurb"))}</div>
        <div class="mt">{meta}{tags}</div>
      </div>
      <div class="chev">›</div>
    </a>'''
    return f'''<div class="app off">
      <div class="ic" style="background:#2c2c2e;color:#68686e">{icon}</div>
      <div class="txt">
        <div class="nm">{esc(a.get("name"))}</div>
        <div class="bl">{esc(a.get("blurb"))}</div>
        <div class="mt">{meta}{tags}</div>
      </div>
    </div>'''


body = ""
if live:
    body += '<div class="sec">Your apps</div>' + "\n".join(card(a) for a in live)
if pending:
    body += '<div class="sec">Not built yet</div>' + "\n".join(card(a) for a in pending)
if not apps:
    body += '<div class="empty">No apps yet. Ask Claude to build one.</div>'

doc = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="theme-color" content="#000000">
<title>{esc(cfg.get("title") or "My Apps")}</title>
<style>
  :root{{--bg:#000;--card:#1c1c1e;--card2:#2c2c2e;
    --lab:#fff;--lab2:#98989f;--lab3:#68686e;--blue:#0a84ff;
    --st:env(safe-area-inset-top,0px);--sb:env(safe-area-inset-bottom,0px);}}
  *{{box-sizing:border-box;margin:0;padding:0;-webkit-tap-highlight-color:transparent}}
  body{{background:var(--bg);color:var(--lab);
    font:17px/1.4 -apple-system,BlinkMacSystemFont,"SF Pro Text","Segoe UI",Roboto,sans-serif;
    -webkit-font-smoothing:antialiased;padding:calc(var(--st) + 12px) 16px calc(var(--sb) + 40px)}}
  a{{color:inherit;text-decoration:none}}
  h1{{font-size:34px;font-weight:800;letter-spacing:-1px}}
  .sub{{font-size:15px;color:var(--lab2);margin-top:4px}}
  .sec{{font-size:12px;font-weight:700;letter-spacing:.7px;text-transform:uppercase;
    color:var(--lab2);margin:26px 0 10px}}
  .app{{display:flex;align-items:center;gap:14px;background:var(--card);
    border-radius:18px;padding:15px;margin-bottom:11px;transition:transform .12s}}
  .app:active{{transform:scale(.975)}}
  .app.off{{opacity:.5}}
  .ic{{width:52px;height:52px;border-radius:14px;flex:none;display:flex;
    align-items:center;justify-content:center;font-size:26px}}
  .txt{{flex:1;min-width:0}}
  .nm{{font-size:17px;font-weight:700;letter-spacing:-.4px}}
  .bl{{font-size:13.5px;color:var(--lab2);margin-top:3px;line-height:1.4}}
  .mt{{font-size:11px;color:var(--lab3);margin-top:7px;display:flex;flex-wrap:wrap;gap:6px;align-items:center}}
  .tag{{background:var(--card2);color:var(--lab2);border-radius:5px;padding:2px 6px;font-weight:600}}
  .chev{{flex:none;color:var(--lab3);font-size:26px;font-weight:300;line-height:1}}
  .empty{{text-align:center;color:var(--lab2);padding:60px 20px}}
  footer{{margin-top:34px;font-size:12px;color:var(--lab3);line-height:1.6;text-align:center}}
</style>
</head>
<body>
  <h1>{esc(cfg.get("title") or "My Apps")}</h1>
  <div class="sub">{esc(cfg.get("tagline") or "")}</div>
  {body}
  <footer>Add to Home Screen to use this like an app.<br>Rebuilt {date.today().isoformat()}</footer>
</body>
</html>
'''

with open(OUT, "w") as f:
    f.write(doc)

print(f"Wrote {OUT}")
print(f"  {len(live)} linked, {len(pending)} pending, {len(apps)} total")
for a in apps:
    href, _ = link_for(a)
    print(f"   {'✓' if href else '·'} {a.get('name'):<26} {href or ''}")
