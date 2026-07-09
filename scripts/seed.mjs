import { neon } from "@neondatabase/serverless";
import bcrypt from "bcryptjs";
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
const hash = await bcrypt.hash("milan@200", 10);

await sql`
  INSERT INTO licences (login_id, password_hash, buyer_note, active)
  VALUES ('chn200', ${hash}, 'Demo licence — change password after first sale', TRUE)
  ON CONFLICT (login_id) DO NOTHING
`;

const rows = await sql`SELECT login_id, device_id, active, created_at FROM licences ORDER BY id`;
console.log("Seeded. Current licences:");
console.table(rows);
