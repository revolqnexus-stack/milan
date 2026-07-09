# CHN Study Pack (Milan)

GNM Community Health Nursing–I exam app · Q.P. 9114 · Karnataka  
Hosted on **Vercel** · licences in **Neon Postgres** · ₹200 = **1 device**.

## Why plain HTML failed on Vercel

A repo with only `chn.html` (no `index.html`, no framework) often deploys as an empty/wrong root. This project is a **Next.js** app that:

- Serves a landing page at `/`
- Serves the study app at [`/app.html`](./public/app.html)
- Authenticates against Neon at `/api/auth/login`
- Lets you sell licences from `/admin`

## Local setup

```bash
npm install
# put DATABASE_URL + ADMIN_SECRET in .env.local (see .env.example)
npm run db:migrate
npm run db:seed
npm run assemble   # rebuilds chn.html → public/app.html
npm run dev
```

Demo seed: Login ID `chn200` / password `milan@200`

## Vercel deploy

1. Import [revolqnexus-stack/milan](https://github.com/revolqnexus-stack/milan) in Vercel.
2. Framework: **Next.js** (auto).
3. Environment variables (Production):
   - `DATABASE_URL` — Neon **pooled** connection string (`-pooler` host)
   - `ADMIN_SECRET` — long random string (same as local)
4. Deploy. Then open `/admin`, create buyer licences, send ID + password.

Or connect Neon from [Vercel Marketplace → Neon](https://vercel.com/marketplace/neon).

## Sell flow

1. Buyer pays ₹200.
2. `/admin` → create Login ID + password.
3. Buyer opens site → Unlock App once → Neon stores `device_id`.
4. Same ID on another phone → blocked until you **Reset device**.

## Rebuild study content

Edit `_gen/*`, then:

```bash
npm run assemble
```

Commit `chn.html` and `public/app.html`.
