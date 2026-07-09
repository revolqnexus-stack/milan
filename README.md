# Milan Study Vault

Paid GNM study-content platform.

**Stack:** Next.js · Vercel · Neon Postgres · Drizzle ORM · Vercel Private Blob · Web Crypto (ECDSA P-256)

**Not used:** Supabase · Firebase · public `/public` HTML for study apps

## Product rules

1. Admin creates **Student ID + temporary password** (WhatsApp delivery).
2. First successful login **binds one browser** via non-extractable Web Crypto private key (IndexedDB) + public key in Neon.
3. Later logins require **challenge/response signature** with that private key.
4. Study HTML lives in **Vercel Private Blob** — never in `/public`.
5. `/study/[slug]` checks session + device + entitlement, then streams HTML server-side into a sandboxed iframe.

## Local setup

```bash
npm install
cp .env.example .env.local
# fill DATABASE_URL, SESSION_SECRET, BLOB_READ_WRITE_TOKEN

npm run db:push
npm run db:seed
npm run dev
```

Default seed admin (change immediately):

- Email: `admin@milan.local` (or `SEED_ADMIN_EMAIL`)
- Password: `MilanAdmin!2026` (or `SEED_ADMIN_PASSWORD`)

## Vercel

1. Import this repo (Framework: Next.js).
2. Env vars: `DATABASE_URL`, `DATABASE_URL_UNPOOLED`, `SESSION_SECRET`, `BLOB_READ_WRITE_TOKEN`, seed vars if needed.
3. Connect Neon + Blob from Vercel dashboard.
4. Deploy → open `/admin/login` → create students → upload HTML → grant entitlements.

## Routes

| Path | Role |
|------|------|
| `/` | Landing |
| `/login` | Student ID + password |
| `/library` | Entitled + locked catalogue |
| `/study/[slug]` | Protected HTML gateway |
| `/admin/login` | Admin email login |
| `/admin/*` | CRM |

## Sell flow (v1 manual)

Pay UPI → Admin confirms payment → Create student → Grant entitlement → WhatsApp credentials.
