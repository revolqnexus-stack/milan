import { neon } from "@neondatabase/serverless";

export function getSql() {
  const url = process.env.DATABASE_URL;
  if (!url) {
    throw new Error("DATABASE_URL is not set");
  }
  return neon(url);
}

export type LicenceRow = {
  id: number;
  login_id: string;
  password_hash: string;
  device_id: string | null;
  buyer_note: string | null;
  active: boolean;
  unlocked_at: string | null;
  created_at: string;
};
