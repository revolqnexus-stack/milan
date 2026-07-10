import {
  boolean,
  index,
  integer,
  pgEnum,
  pgTable,
  serial,
  text,
  timestamp,
  uniqueIndex,
} from "drizzle-orm/pg-core";
import { sql } from "drizzle-orm";

export const userStatusEnum = pgEnum("user_status", [
  "ACTIVE",
  "DISABLED",
  "SUSPENDED",
]);

export const paymentMethodEnum = pgEnum("payment_method", [
  "UPI",
  "BANK_TRANSFER",
  "CASH",
  "RAZORPAY",
]);

export const paymentStatusEnum = pgEnum("payment_status", [
  "PENDING",
  "CONFIRMED",
  "FAILED",
  "REFUNDED",
]);

export const adminRoleEnum = pgEnum("admin_role", ["OWNER", "ADMIN", "SUPPORT"]);

export const adminStatusEnum = pgEnum("admin_status", ["ACTIVE", "DISABLED"]);

export const users = pgTable(
  "users",
  {
    id: serial("id").primaryKey(),
    studentId: text("student_id").notNull(),
    name: text("name").notNull(),
    passwordHash: text("password_hash").notNull(),
    status: userStatusEnum("status").notNull().default("ACTIVE"),
    createdAt: timestamp("created_at", { withTimezone: true })
      .notNull()
      .defaultNow(),
    updatedAt: timestamp("updated_at", { withTimezone: true })
      .notNull()
      .defaultNow(),
    lastLoginAt: timestamp("last_login_at", { withTimezone: true }),
  },
  (t) => [uniqueIndex("users_student_id_uidx").on(t.studentId)]
);

export const devices = pgTable(
  "devices",
  {
    id: serial("id").primaryKey(),
    userId: integer("user_id")
      .notNull()
      .references(() => users.id, { onDelete: "cascade" }),
    publicKey: text("public_key").notNull(),
    publicKeyAlgorithm: text("public_key_algorithm").notNull().default("ECDSA_P256"),
    deviceLabel: text("device_label"),
    activatedAt: timestamp("activated_at", { withTimezone: true })
      .notNull()
      .defaultNow(),
    lastSeenAt: timestamp("last_seen_at", { withTimezone: true })
      .notNull()
      .defaultNow(),
    revokedAt: timestamp("revoked_at", { withTimezone: true }),
    createdAt: timestamp("created_at", { withTimezone: true })
      .notNull()
      .defaultNow(),
  },
  (t) => [
    index("devices_user_id_idx").on(t.userId),
    // One active (non-revoked) device per user
    uniqueIndex("devices_one_active_per_user_uidx")
      .on(t.userId)
      .where(sql`${t.revokedAt} IS NULL`),
  ]
);

export const deviceChallenges = pgTable(
  "device_challenges",
  {
    id: serial("id").primaryKey(),
    userId: integer("user_id")
      .notNull()
      .references(() => users.id, { onDelete: "cascade" }),
    deviceId: integer("device_id")
      .notNull()
      .references(() => devices.id, { onDelete: "cascade" }),
    challenge: text("challenge").notNull(),
    expiresAt: timestamp("expires_at", { withTimezone: true }).notNull(),
    consumedAt: timestamp("consumed_at", { withTimezone: true }),
    createdAt: timestamp("created_at", { withTimezone: true })
      .notNull()
      .defaultNow(),
  },
  (t) => [
    index("device_challenges_user_id_idx").on(t.userId),
    uniqueIndex("device_challenges_challenge_uidx").on(t.challenge),
  ]
);

export const sessions = pgTable(
  "sessions",
  {
    id: serial("id").primaryKey(),
    userId: integer("user_id")
      .notNull()
      .references(() => users.id, { onDelete: "cascade" }),
    deviceId: integer("device_id")
      .notNull()
      .references(() => devices.id, { onDelete: "cascade" }),
    sessionTokenHash: text("session_token_hash").notNull(),
    expiresAt: timestamp("expires_at", { withTimezone: true }).notNull(),
    createdAt: timestamp("created_at", { withTimezone: true })
      .notNull()
      .defaultNow(),
    lastSeenAt: timestamp("last_seen_at", { withTimezone: true })
      .notNull()
      .defaultNow(),
    revokedAt: timestamp("revoked_at", { withTimezone: true }),
  },
  (t) => [
    uniqueIndex("sessions_token_hash_uidx").on(t.sessionTokenHash),
    index("sessions_user_id_idx").on(t.userId),
    index("sessions_device_id_idx").on(t.deviceId),
  ]
);

export const content = pgTable(
  "content",
  {
    id: serial("id").primaryKey(),
    title: text("title").notNull(),
    slug: text("slug").notNull(),
    course: text("course").notNull().default("GNM"),
    studyYear: integer("study_year").notNull().default(1),
    subject: text("subject").notNull(),
    paperCode: text("paper_code"),
    description: text("description"),
    htmlBlobPath: text("html_blob_path"),
    thumbnailBlobPath: text("thumbnail_blob_path"),
    priceInrPaise: integer("price_inr_paise").notNull().default(29900),
    isActive: boolean("is_active").notNull().default(false),
    sortOrder: integer("sort_order").notNull().default(0),
    createdAt: timestamp("created_at", { withTimezone: true })
      .notNull()
      .defaultNow(),
    updatedAt: timestamp("updated_at", { withTimezone: true })
      .notNull()
      .defaultNow(),
  },
  (t) => [
    uniqueIndex("content_slug_uidx").on(t.slug),
    index("content_course_year_idx").on(t.course, t.studyYear),
  ]
);

export const entitlements = pgTable(
  "entitlements",
  {
    id: serial("id").primaryKey(),
    userId: integer("user_id")
      .notNull()
      .references(() => users.id, { onDelete: "cascade" }),
    contentId: integer("content_id")
      .notNull()
      .references(() => content.id, { onDelete: "cascade" }),
    grantedAt: timestamp("granted_at", { withTimezone: true })
      .notNull()
      .defaultNow(),
    expiresAt: timestamp("expires_at", { withTimezone: true }),
    revokedAt: timestamp("revoked_at", { withTimezone: true }),
    grantedByAdminId: integer("granted_by_admin_id"),
    createdAt: timestamp("created_at", { withTimezone: true })
      .notNull()
      .defaultNow(),
  },
  (t) => [
    index("entitlements_user_id_idx").on(t.userId),
    index("entitlements_content_id_idx").on(t.contentId),
    uniqueIndex("entitlements_active_user_content_uidx")
      .on(t.userId, t.contentId)
      .where(sql`${t.revokedAt} IS NULL`),
  ]
);

export const payments = pgTable(
  "payments",
  {
    id: serial("id").primaryKey(),
    userId: integer("user_id")
      .notNull()
      .references(() => users.id, { onDelete: "cascade" }),
    amountPaise: integer("amount_paise").notNull(),
    paymentReference: text("payment_reference"),
    paymentMethod: paymentMethodEnum("payment_method").notNull().default("UPI"),
    status: paymentStatusEnum("status").notNull().default("PENDING"),
    notes: text("notes"),
    createdAt: timestamp("created_at", { withTimezone: true })
      .notNull()
      .defaultNow(),
    confirmedAt: timestamp("confirmed_at", { withTimezone: true }),
  },
  (t) => [index("payments_user_id_idx").on(t.userId)]
);

export const admins = pgTable(
  "admins",
  {
    id: serial("id").primaryKey(),
    email: text("email").notNull(),
    passwordHash: text("password_hash").notNull(),
    name: text("name").notNull(),
    role: adminRoleEnum("role").notNull().default("ADMIN"),
    status: adminStatusEnum("status").notNull().default("ACTIVE"),
    createdAt: timestamp("created_at", { withTimezone: true })
      .notNull()
      .defaultNow(),
    updatedAt: timestamp("updated_at", { withTimezone: true })
      .notNull()
      .defaultNow(),
  },
  (t) => [uniqueIndex("admins_email_uidx").on(t.email)]
);

export const adminSessions = pgTable(
  "admin_sessions",
  {
    id: serial("id").primaryKey(),
    adminId: integer("admin_id")
      .notNull()
      .references(() => admins.id, { onDelete: "cascade" }),
    sessionTokenHash: text("session_token_hash").notNull(),
    expiresAt: timestamp("expires_at", { withTimezone: true }).notNull(),
    createdAt: timestamp("created_at", { withTimezone: true })
      .notNull()
      .defaultNow(),
    lastSeenAt: timestamp("last_seen_at", { withTimezone: true })
      .notNull()
      .defaultNow(),
    revokedAt: timestamp("revoked_at", { withTimezone: true }),
  },
  (t) => [
    uniqueIndex("admin_sessions_token_hash_uidx").on(t.sessionTokenHash),
    index("admin_sessions_admin_id_idx").on(t.adminId),
  ]
);

export const deviceResetLogs = pgTable(
  "device_reset_logs",
  {
    id: serial("id").primaryKey(),
    userId: integer("user_id")
      .notNull()
      .references(() => users.id, { onDelete: "cascade" }),
    oldDeviceId: integer("old_device_id"),
    adminId: integer("admin_id").references(() => admins.id, {
      onDelete: "set null",
    }),
    reason: text("reason").notNull(),
    createdAt: timestamp("created_at", { withTimezone: true })
      .notNull()
      .defaultNow(),
  },
  (t) => [index("device_reset_logs_user_id_idx").on(t.userId)]
);

export const loginAttempts = pgTable(
  "login_attempts",
  {
    id: serial("id").primaryKey(),
    studentIdAttempt: text("student_id_attempt").notNull(),
    ipHash: text("ip_hash"),
    success: boolean("success").notNull().default(false),
    createdAt: timestamp("created_at", { withTimezone: true })
      .notNull()
      .defaultNow(),
  },
  (t) => [
    index("login_attempts_student_idx").on(t.studentIdAttempt),
    index("login_attempts_created_idx").on(t.createdAt),
  ]
);

export const accessRequestStatusEnum = pgEnum("access_request_status", [
  "PENDING",
  "CONTACTED",
  "PAID",
  "APPROVED",
  "REJECTED",
]);

export const accessRequests = pgTable(
  "access_requests",
  {
    id: serial("id").primaryKey(),
    contentId: integer("content_id")
      .notNull()
      .references(() => content.id, { onDelete: "cascade" }),
    name: text("name").notNull(),
    phone: text("phone").notNull(),
    college: text("college"),
    status: accessRequestStatusEnum("status").notNull().default("PENDING"),
    adminNotes: text("admin_notes"),
    linkedUserId: integer("linked_user_id").references(() => users.id, {
      onDelete: "set null",
    }),
    createdAt: timestamp("created_at", { withTimezone: true })
      .notNull()
      .defaultNow(),
    updatedAt: timestamp("updated_at", { withTimezone: true })
      .notNull()
      .defaultNow(),
  },
  (t) => [
    index("access_requests_content_id_idx").on(t.contentId),
    index("access_requests_status_idx").on(t.status),
    index("access_requests_created_idx").on(t.createdAt),
  ]
);
