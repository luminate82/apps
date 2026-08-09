# Using the Google Maps API without risking your card

**The thing everyone gets wrong:** a *budget alert* does **not** cap spending. It emails
you when you cross a threshold and then lets the charges keep running. The only
control that actually stops the meter is a **quota limit**, which makes the API stop
responding once you hit it.

So set up three layers, in this order of importance.

---

## Layer 1 — Quota caps (the real stop button)

**Google Cloud Console → APIs & Services → your API → Quotas & System Limits**

For each API you enable, set **Requests per day**. Suggested for this app:

| API | Requests/day | Why |
|---|---|---|
| Maps JavaScript API | 500 | Map loads |
| Directions API | 100 | Live-traffic ETAs |
| Distance Matrix API | 100 | Real road distances |
| Places API | 200 | Hotel photos |

You are one family on one weekend. Real usage is a few dozen calls a day. These caps
are generous and still make a runaway bill impossible — if something goes wrong, the
API simply stops answering.

Google's own formula if you want to set your own number:

```
(monthly spend you'll accept ÷ price per 1000 calls) ÷ 30 = daily cap
```

---

## Layer 2 — Lock the key to your site

**APIs & Services → Credentials → your key**

1. **Application restrictions** → *Websites*
   Add: `luminate82.github.io/*`
2. **API restrictions** → *Restrict key* → tick only the four APIs above

This stops the key working from anyone else's website.

> **Be honest about this one:** referrer headers are sent by the browser and a
> determined person can forge them. Referrer restrictions stop casual copy-and-paste
> abuse, not a motivated attacker. **Layer 1 is what actually protects you.** Never
> rely on referrer restrictions alone for a key in a public repo.

---

## Layer 3 — Budget alert (early warning only)

**Billing → Budgets & alerts → Create budget** — set £5, alerts at 50 / 90 / 100%.

This tells you something is wrong. It does not stop it. That's why it's last.

---

## Putting the key in the app

The app will have one line near the top:

```js
const GMAPS_KEY = "PASTE_YOUR_KEY_HERE";
```

Edit that line yourself and commit. **Don't paste your key into a chat window** —
not to Claude, not to anyone. There's no need: the placeholder is the only thing
that has to change.

---

## What it buys you

| Feature | Without a key (today) | With a key |
|---|---|---|
| ETAs | Calibrated speed profile + your live GPS speed | Live traffic from Google |
| Distances | Straight-line × 1.3 estimate | True road distance |
| Hotel photos | Link out to image search | Real photos in the cards |
| Map | OpenStreetMap tiles, free | Google tiles |

**Be clear-eyed about the gain.** The ETA model is now calibrated against real Google
times and takes your actual speed into account, so live traffic is a refinement, not
a transformation. **Hotel photos are the genuinely new capability.**

---

## If you'd rather not

Perfectly reasonable. The app works fully without a key, and the **Live traffic**
button already hands off to Google Maps proper — real-time routing, no key, no card,
no exposure.
