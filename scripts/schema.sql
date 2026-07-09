CREATE TABLE IF NOT EXISTS licences (
  id SERIAL PRIMARY KEY,
  login_id TEXT NOT NULL UNIQUE,
  password_hash TEXT NOT NULL,
  device_id TEXT,
  buyer_note TEXT,
  active BOOLEAN NOT NULL DEFAULT TRUE,
  unlocked_at TIMESTAMPTZ,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS licences_login_id_idx ON licences (login_id);
CREATE INDEX IF NOT EXISTS licences_device_id_idx ON licences (device_id);
