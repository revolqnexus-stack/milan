import { neon } from "@neondatabase/serverless";
import { hash } from "@node-rs/argon2";
import { readFileSync, existsSync } from "fs";
import { resolve } from "path";

function loadEnvLocal() {
  const p = resolve(process.cwd(), ".env.local");
  if (!existsSync(p)) return;
  for (const line of readFileSync(p, "utf8").split(/\r?\n/)) {
    const m = line.match(/^([^#=]+)=(.*)$/);
    if (!m) continue;
    const key = m[1].trim();
    let val = m[2].trim();
    if (
      (val.startsWith('"') && val.endsWith('"')) ||
      (val.startsWith("'") && val.endsWith("'"))
    ) {
      val = val.slice(1, -1);
    }
    if (!process.env[key]) process.env[key] = val;
  }
}

loadEnvLocal();

const sql = neon(process.env.DATABASE_URL);

const adminId = (
  process.env.SEED_ADMIN_ID || process.env.SEED_ADMIN_EMAIL || ""
).trim().toLowerCase();
const adminPass = process.env.SEED_ADMIN_PASSWORD || "";

if (!adminId || !adminPass) {
  console.error("Set SEED_ADMIN_ID and SEED_ADMIN_PASSWORD in .env.local");
  process.exit(1);
}

const adminHash = await hash(adminPass, {
  memoryCost: 19456,
  timeCost: 2,
  parallelism: 1,
  outputLen: 32,
});

await sql`
  INSERT INTO admins (email, password_hash, name, role, status)
  VALUES (${adminId}, ${adminHash}, 'Owner', 'OWNER', 'ACTIVE')
  ON CONFLICT (email) DO UPDATE SET
    password_hash = EXCLUDED.password_hash,
    name = EXCLUDED.name,
    role = 'OWNER',
    status = 'ACTIVE',
    updated_at = NOW()
`;

console.log("Admin ready:", adminId);
