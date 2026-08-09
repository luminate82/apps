# Getting your apps online — the no-jargon version

**No Terminal. No commands. No tokens.** Everything here is done by clicking in a
web browser. About 10 minutes, once ever.

At the end you'll have a web address like `https://avinash.github.io/apps/` that
opens your apps on your iPhone, and an icon on your Home Screen that looks like a
real app.

---

## What GitHub actually is

Think of it as Dropbox for files that make up a website.

- A **repository** (repo) is just a folder.
- **GitHub Pages** is a free switch that says "take the files in this folder and
  serve them as a real website."

That's the whole idea. There is a lot of programmer machinery underneath, and you
can ignore all of it.

---

## Step 1 — Make an account

Go to **github.com** → **Sign up**.

Your username becomes part of your web address, so pick something you're happy
seeing: `avinash` gives you `avinash.github.io`. Lowercase, no spaces.

Free plan is all you need. Skip anything it tries to upsell.

---

## Step 2 — Make the folder (the "repo")

Once signed in, go to **github.com/new**.

Fill in exactly this:

| Field | What to put |
|---|---|
| Repository name | `apps` |
| Description | Leave blank |
| Public / Private | **Public** ← must be this |
| Add a README file | **Leave unticked** |
| Add .gitignore | **None** |
| Choose a licence | **None** |

Click **Create repository**.

> **Why Public?** Free GitHub Pages only works on public repos. It means anyone with
> the address could view your apps. There's nothing private in them — hotel names,
> road junctions, opening times. Don't put anything personal in an app you publish
> here. If you ever want private hosting, that's GitHub Pro at about £3/month.

---

## Step 3 — Put the files in

You'll land on a mostly empty page with some commands on it. **Ignore all of it.**
Find the line of small text that says:

> *…or **upload an existing file***

Click **upload an existing file**.

Now open **Finder** → **Downloads** → **ClaudeApps**, select these five files:

- `index.html`
- `road-trip-companion.html`
- `apps.json`
- `build_launcher.py`
- `README.md`

Drag all five onto the GitHub page.

Scroll down, click the green **Commit changes** button.

> "Commit" just means "save". You'll see the word constantly. It means save.

You should now see your five files listed.

---

## Step 4 — Flip the website switch

In your repo, click **Settings** (top right, near the ⚙️).

Down the **left sidebar**, click **Pages**.

Under **Build and deployment**:

- **Source** → `Deploy from a branch`
- **Branch** → `main`, and the folder dropdown next to it → `/ (root)`
- Click **Save**

---

## Step 5 — Wait, then open it

Give it **2–3 minutes**. GitHub is building your site.

Refresh that Settings → Pages page. A green banner appears with your address:

```
https://YOURNAME.github.io/apps/
```

Open it. You should see **My Apps** with the road trip listed.

Tapping through gets you to the app itself at:

```
https://YOURNAME.github.io/apps/road-trip-companion.html
```

---

## Step 6 — Put it on your iPhone

1. Open `https://YOURNAME.github.io/apps/` in **Safari** (not Chrome — only Safari
   can add to the Home Screen)
2. Tap the **Share** button (square with an arrow)
3. Scroll down → **Add to Home Screen**
4. Name it "My Apps" → **Add**

It now opens full-screen with no browser bars, like a real app.

**Tap "Locate me" and allow location when asked.** This is the whole reason for
hosting it — location is blocked on files opened from the Files app, but works
properly on a real web address.

---

## Adding a new app later

Ask Claude to build and publish it. Then:

1. Go to `github.com/YOURNAME/apps`
2. **Add file** → **Upload files**
3. Drag in the new app file **and** the updated `index.html`
4. **Commit changes**

Live in about a minute. Uploading a file with a name that already exists just
replaces it — that's how updates work.

---

## When it goes wrong

**"404 — There isn't a GitHub Pages site here"**
Normal for the first few minutes. Wait 3 minutes and refresh. If it persists, check
Settings → Pages actually says Branch `main` and folder `/ (root)`.

**Launcher loads but tapping an app 404s**
The app file didn't upload. Check `road-trip-companion.html` is listed on the repo's
main page.

**Everything is blank**
Force-refresh: on iPhone, close the Safari tab completely and reopen. If it's still
blank, screenshot it and send it to Claude — the app prints its own error onto the
page precisely so this is diagnosable.

**"Locate me" does nothing**
Settings → Safari → Location → Ask. Also check the address starts `https://` — that's
required for location, and is exactly why we're not opening the file from Files.

**I can't find "upload an existing file"**
It only shows on a genuinely empty repo. If you accidentally ticked "Add a README",
use **Add file** → **Upload files** at the top of the repo page instead.

---

## Things you can safely ignore forever

Branches, pull requests, forks, issues, actions, stars, the green squares. None of it
is needed to host a page. If GitHub suggests any of it, close the tab and carry on.
