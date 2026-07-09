-- REVOLQNEXUS vault schema (Neon)

CREATE TYPE user_status AS ENUM ('ACTIVE', 'DISABLED', 'SUSPENDED');
CREATE TYPE payment_method AS ENUM ('UPI', 'BANK_TRANSFER', 'CASH', 'RAZORPAY');
CREATE TYPE payment_status AS ENUM ('PENDING', 'CONFIRMED', 'FAILED', 'REFUNDED');
CREATE TYPE admin_role AS ENUM ('OWNER', 'ADMIN', 'SUPPORT');
CREATE TYPE admin_status AS ENUM ('ACTIVE', 'DISABLED');

CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  student_id TEXT NOT NULL,
  name TEXT NOT NULL,
  password_hash TEXT NOT NULL,
  status user_status NOT NULL DEFAULT 'ACTIVE',
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  last_login_at TIMESTAMPTZ
);
CREATE UNIQUE INDEX IF NOT EXISTS users_student_id_uidx ON users (student_id);

CREATE TABLE IF NOT EXISTS devices (
  id SERIAL PRIMARY KEY,
  user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  public_key TEXT NOT NULL,
  public_key_algorithm TEXT NOT NULL DEFAULT 'ECDSA_P256',
  device_label TEXT,
  activated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  last_seen_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  revoked_at TIMESTAMPTZ,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
CREATE INDEX IF NOT EXISTS devices_user_id_idx ON devices (user_id);
CREATE UNIQUE INDEX IF NOT EXISTS devices_one_active_per_user_uidx
  ON devices (user_id) WHERE revoked_at IS NULL;

CREATE TABLE IF NOT EXISTS device_challenges (
  id SERIAL PRIMARY KEY,
  user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  device_id INTEGER NOT NULL REFERENCES devices(id) ON DELETE CASCADE,
  challenge TEXT NOT NULL,
  expires_at TIMESTAMPTZ NOT NULL,
  consumed_at TIMESTAMPTZ,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
CREATE INDEX IF NOT EXISTS device_challenges_user_id_idx ON device_challenges (user_id);
CREATE UNIQUE INDEX IF NOT EXISTS device_challenges_challenge_uidx ON device_challenges (challenge);

CREATE TABLE IF NOT EXISTS sessions (
  id SERIAL PRIMARY KEY,
  user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  device_id INTEGER NOT NULL REFERENCES devices(id) ON DELETE CASCADE,
  session_token_hash TEXT NOT NULL,
  expires_at TIMESTAMPTZ NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  last_seen_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  revoked_at TIMESTAMPTZ
);
CREATE UNIQUE INDEX IF NOT EXISTS sessions_token_hash_uidx ON sessions (session_token_hash);
CREATE INDEX IF NOT EXISTS sessions_user_id_idx ON sessions (user_id);
CREATE INDEX IF NOT EXISTS sessions_device_id_idx ON sessions (device_id);

CREATE TABLE IF NOT EXISTS content (
  id SERIAL PRIMARY KEY,
  title TEXT NOT NULL,
  slug TEXT NOT NULL,
  course TEXT NOT NULL DEFAULT 'GNM',
  study_year INTEGER NOT NULL DEFAULT 1,
  subject TEXT NOT NULL,
  paper_code TEXT,
  description TEXT,
  html_blob_path TEXT,
  thumbnail_blob_path TEXT,
  price_inr_paise INTEGER NOT NULL DEFAULT 29900,
  is_active BOOLEAN NOT NULL DEFAULT FALSE,
  sort_order INTEGER NOT NULL DEFAULT 0,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
CREATE UNIQUE INDEX IF NOT EXISTS content_slug_uidx ON content (slug);
CREATE INDEX IF NOT EXISTS content_course_year_idx ON content (course, study_year);

CREATE TABLE IF NOT EXISTS entitlements (
  id SERIAL PRIMARY KEY,
  user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  content_id INTEGER NOT NULL REFERENCES content(id) ON DELETE CASCADE,
  granted_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  expires_at TIMESTAMPTZ,
  revoked_at TIMESTAMPTZ,
  granted_by_admin_id INTEGER,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
CREATE INDEX IF NOT EXISTS entitlements_user_id_idx ON entitlements (user_id);
CREATE INDEX IF NOT EXISTS entitlements_content_id_idx ON entitlements (content_id);
CREATE UNIQUE INDEX IF NOT EXISTS entitlements_active_user_content_uidx
  ON entitlements (user_id, content_id) WHERE revoked_at IS NULL;

CREATE TABLE IF NOT EXISTS payments (
  id SERIAL PRIMARY KEY,
  user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  amount_paise INTEGER NOT NULL,
  payment_reference TEXT,
  payment_method payment_method NOT NULL DEFAULT 'UPI',
  status payment_status NOT NULL DEFAULT 'PENDING',
  notes TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  confirmed_at TIMESTAMPTZ
);
CREATE INDEX IF NOT EXISTS payments_user_id_idx ON payments (user_id);

CREATE TABLE IF NOT EXISTS admins (
  id SERIAL PRIMARY KEY,
  email TEXT NOT NULL,
  password_hash TEXT NOT NULL,
  name TEXT NOT NULL,
  role admin_role NOT NULL DEFAULT 'ADMIN',
  status admin_status NOT NULL DEFAULT 'ACTIVE',
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
CREATE UNIQUE INDEX IF NOT EXISTS admins_email_uidx ON admins (email);

CREATE TABLE IF NOT EXISTS admin_sessions (
  id SERIAL PRIMARY KEY,
  admin_id INTEGER NOT NULL REFERENCES admins(id) ON DELETE CASCADE,
  session_token_hash TEXT NOT NULL,
  expires_at TIMESTAMPTZ NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  last_seen_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  revoked_at TIMESTAMPTZ
);
CREATE UNIQUE INDEX IF NOT EXISTS admin_sessions_token_hash_uidx ON admin_sessions (session_token_hash);
CREATE INDEX IF NOT EXISTS admin_sessions_admin_id_idx ON admin_sessions (admin_id);

CREATE TABLE IF NOT EXISTS device_reset_logs (
  id SERIAL PRIMARY KEY,
  user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  old_device_id INTEGER,
  admin_id INTEGER REFERENCES admins(id) ON DELETE SET NULL,
  reason TEXT NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
CREATE INDEX IF NOT EXISTS device_reset_logs_user_id_idx ON device_reset_logs (user_id);

CREATE TABLE IF NOT EXISTS login_attempts (
  id SERIAL PRIMARY KEY,
  student_id_attempt TEXT NOT NULL,
  ip_hash TEXT,
  success BOOLEAN NOT NULL DEFAULT FALSE,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
CREATE INDEX IF NOT EXISTS login_attempts_student_idx ON login_attempts (student_id_attempt);
CREATE INDEX IF NOT EXISTS login_attempts_created_idx ON login_attempts (created_at);
