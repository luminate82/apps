# My Apps

Single-file HTML apps built with Claude, hosted on GitHub Pages.

| File | What it is |
|---|---|
| `index.html` | The launcher. **Generated — never edit by hand.** |
| `apps.json` | The registry. Edit this. |
| `build_launcher.py` | Regenerates `index.html` from `apps.json`. |
| `*.html` | One self-contained app per file. |

Rebuild the launcher after any change to `apps.json`:

```bash
python3 build_launcher.py .
```

---

## One-off setup (about 10 minutes)

You only do this once. After it, publishing is a single push.

### 1. Create the repo

On github.com → **New repository**
- Name: **`apps`**
- **Public** (GitHub Pages needs this on the free plan)
- Do **not** add a README, .gitignore or licence — this folder already has what it needs

### 2. Push this folder

Open Terminal and paste, replacing `YOURNAME`:

```bash
cd ~/Downloads/ClaudeApps
git remote add origin https://github.com/YOURNAME/apps.git
git branch -M main
git push -u origin main
```

If it asks for a password, use a **personal access token**, not your account
password — github.com → Settings → Developer settings → Personal access tokens →
Fine-grained tokens → Generate, with **Contents: Read and write** on this repo.
macOS will remember it in Keychain after the first push.

*(No Terminal? On the repo page use **Add file → Upload files**, drag everything in
this folder, and commit. Same result.)*

### 3. Turn Pages on

Repo → **Settings** → **Pages** → Source: **Deploy from a branch** →
Branch: **main**, folder: **/ (root)** → Save.

Wait a minute or two, then open:

```
https://YOURNAME.github.io/apps/
```

Add that to your iPhone Home Screen.

---

## Publishing after that

```bash
cd ~/Downloads/ClaudeApps
python3 build_launcher.py .
git add -A && git commit -m "Add nanny finder" && git push
```

Live in under a minute. **Every app URL is predictable**, so links work the moment
they land:

```
https://YOURNAME.github.io/apps/                          launcher
https://YOURNAME.github.io/apps/road-trip-companion.html  an app
```

## Why this over drag-and-drop hosting

- URLs never change, so Home Screen icons keep working
- Full version history — roll back a broken rebuild with `git revert`
- Free, no expiry, no account juggling
- Real HTTPS, so **geolocation works** (it doesn't on files opened from Files.app)
