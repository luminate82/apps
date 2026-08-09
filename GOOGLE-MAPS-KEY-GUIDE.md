# Getting a Google Maps key — and making it safe

About 20 minutes. No coding. **Do the steps in this order** — the safety settings come
before the key goes anywhere near your website, not after.

> **Before you start:** Google requires a **credit card** on file, even though your
> actual usage here will be free. If that's a dealbreaker, stop now — the app works
> fine without a key and the Live traffic button already hands off to Google Maps.

---

## Part 1 — Create the account and project

### 1. Start the setup wizard

Go to **[console.cloud.google.com/google/maps-apis/start](https://console.cloud.google.com/google/maps-apis/start)**

Sign in with your Google account. This is Google's guided flow for people who've never
used Cloud before — it walks you through project and billing together.

### 2. Create a project

Call it **`road-trip`**. A project is just a container so usage and billing are kept
separate from anything else you do later.

### 3. Enable billing

You'll be asked for a card. What actually happens:

- New Cloud customers get a **$300 credit, valid 90 days**
- Beyond that, each Maps product has its own **monthly free allowance** — roughly the
  first 10,000 requests
- The old universal **$200/month Maps credit was retired in March 2025** — ignore any
  blog post that still mentions it

Your realistic usage for this trip is a few dozen calls. You will not get near paying.

---

## Part 2 — Turn on the four APIs

Go to the **[Maps API Library](https://console.cloud.google.com/project/_/google/maps-apis/api-list)**
and click **Enable** on each:

| API | What it gives the app |
|---|---|
| **Maps JavaScript API** | Google map tiles instead of OpenStreetMap |
| **Places API** | **Real hotel photos** — the main prize |
| **Routes API** | Live-traffic ETAs |
| **Distance Matrix API** | True road distances instead of estimates |

Enable only these four. Every extra API is extra exposure.

---

## Part 3 — Set the spending caps FIRST

**Do this before creating the key.** A budget alert does *not* stop spending — it
emails you while the charges continue. **Quota limits are the only hard stop.**

For each of the four APIs: **APIs & Services → [that API] → Quotas & System Limits →
Requests per day → edit**

| API | Requests/day |
|---|---|
| Maps JavaScript API | 500 |
| Places API | 200 |
| Routes API | 100 |
| Distance Matrix API | 100 |

Hit the cap and the API simply stops answering. That is what makes a runaway bill
impossible.

---

## Part 4 — Create the key

Go to **[Credentials](https://console.cloud.google.com/project/_/google/maps-apis/credentials)**
→ **Create credentials** → **API key**.

Copy it somewhere safe. Then **immediately** click **Edit API key**:

**Application restrictions** → *Websites* → Add:
```
luminate82.github.io/*
```

**API restrictions** → *Restrict key* → tick only your four APIs.

**Save.**

> **An honest caveat:** referrer restrictions are sent by the browser and can be forged
> by someone determined. They stop casual copy-and-paste abuse, not a real attacker.
> **Part 3 is what actually protects your card.** Never rely on referrer restrictions
> alone for a key sitting in a public repo.

---

## Part 5 — Budget alert (early warning only)

**Billing → Budgets & alerts → Create budget** → £5, alerts at 50/90/100%.

Last on the list deliberately: it tells you something is wrong, it doesn't stop it.

---

## Part 6 — Put it in the app

The app will contain one line near the top:

```js
const GMAPS_KEY = "PASTE_YOUR_KEY_HERE";
```

Edit that line in GitHub — open `road-trip-companion.html`, click the pencil ✏️, paste
your key between the quotes, **Commit changes**.

**Never paste your key into a chat window — not to Claude, not to anyone.** There is no
need to: the placeholder is the only thing that changes.

---

## If it all goes wrong

Delete the key: **Credentials → tick it → Delete**. Every request using it stops
instantly. Then make a new one. Nothing else in the app breaks — it falls back to the
built-in estimates.

---

## Is it worth it?

| | Without a key | With a key |
|---|---|---|
| ETAs | Calibrated speed profile + your live GPS speed | Live traffic |
| Distances | Straight-line × 1.3 | True road distance |
| **Hotel photos** | **Link out to image search** | **Real photos on the cards** |

The ETA model is now calibrated against real Google times, so live traffic is a
refinement rather than a transformation. **Photos are the genuinely new thing.**
Decide on that basis.
