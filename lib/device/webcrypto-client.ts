/**
 * Browser-only Web Crypto device key helpers.
 * Private key is non-extractable and stored in IndexedDB.
 */

const DB_NAME = "milan_device_vault";
const STORE = "keys";
const KEY_ID = "device_signing_key";

function openDb(): Promise<IDBDatabase> {
  return new Promise((resolve, reject) => {
    const req = indexedDB.open(DB_NAME, 1);
    req.onupgradeneeded = () => {
      const db = req.result;
      if (!db.objectStoreNames.contains(STORE)) {
        db.createObjectStore(STORE);
      }
    };
    req.onsuccess = () => resolve(req.result);
    req.onerror = () => reject(req.error);
  });
}

async function idbGet(): Promise<CryptoKey | null> {
  const db = await openDb();
  return new Promise((resolve, reject) => {
    const tx = db.transaction(STORE, "readonly");
    const store = tx.objectStore(STORE);
    const req = store.get(KEY_ID);
    req.onsuccess = () => resolve((req.result as CryptoKey) || null);
    req.onerror = () => reject(req.error);
  });
}

async function idbSet(key: CryptoKey): Promise<void> {
  const db = await openDb();
  return new Promise((resolve, reject) => {
    const tx = db.transaction(STORE, "readwrite");
    const store = tx.objectStore(STORE);
    const req = store.put(key, KEY_ID);
    req.onsuccess = () => resolve();
    req.onerror = () => reject(req.error);
  });
}

export async function hasDevicePrivateKey(): Promise<boolean> {
  try {
    return !!(await idbGet());
  } catch {
    return false;
  }
}

export async function createAndStoreDeviceKeyPair(): Promise<{
  publicKeySpkiB64: string;
  algorithm: string;
}> {
  const pair = await crypto.subtle.generateKey(
    {
      name: "ECDSA",
      namedCurve: "P-256",
    },
    false, // non-extractable private key
    ["sign", "verify"]
  );

  await idbSet(pair.privateKey);

  const spki = await crypto.subtle.exportKey("spki", pair.publicKey);
  const publicKeySpkiB64 = btoa(String.fromCharCode(...new Uint8Array(spki)));

  return { publicKeySpkiB64, algorithm: "ECDSA_P256" };
}

export async function signChallenge(challenge: string): Promise<string> {
  const privateKey = await idbGet();
  if (!privateKey) {
    throw new Error("NO_DEVICE_KEY");
  }
  const data = new TextEncoder().encode(challenge);
  const sig = await crypto.subtle.sign(
    { name: "ECDSA", hash: "SHA-256" },
    privateKey,
    data
  );
  return btoa(String.fromCharCode(...new Uint8Array(sig)));
}

export function deviceLabelGuess(): string {
  if (typeof navigator === "undefined") return "Unknown device";
  const ua = navigator.userAgent || "";
  let browser = "Browser";
  if (ua.includes("Edg/")) browser = "Edge";
  else if (ua.includes("Chrome/")) browser = "Chrome";
  else if (ua.includes("Safari/") && !ua.includes("Chrome")) browser = "Safari";
  else if (ua.includes("Firefox/")) browser = "Firefox";

  let os = "Device";
  if (/Android/i.test(ua)) os = "Android";
  else if (/iPhone|iPad/i.test(ua)) os = "iOS";
  else if (/Windows/i.test(ua)) os = "Windows";
  else if (/Mac OS/i.test(ua)) os = "Mac";
  else if (/Linux/i.test(ua)) os = "Linux";

  return `${os} / ${browser}`;
}
