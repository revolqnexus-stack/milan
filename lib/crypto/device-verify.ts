import { createPublicKey, verify as cryptoVerify } from "crypto";

/**
 * Verify ECDSA P-256 signature over challenge.
 * Client signs UTF-8 challenge bytes with Web Crypto ECDSA SHA-256.
 * publicKeySpkiB64: base64-encoded SPKI public key from Web Crypto export.
 * signatureB64: base64-encoded signature (IEEE P1363 / Web Crypto default).
 */
export function verifyDeviceSignature(opts: {
  publicKeySpkiB64: string;
  challenge: string;
  signatureB64: string;
  algorithm?: string;
}): boolean {
  try {
    const spki = Buffer.from(opts.publicKeySpkiB64, "base64");
    const key = createPublicKey({
      key: spki,
      format: "der",
      type: "spki",
    });
    const signature = Buffer.from(opts.signatureB64, "base64");
    const data = Buffer.from(opts.challenge, "utf8");
    return cryptoVerify(
      "sha256",
      data,
      {
        key,
        dsaEncoding: "ieee-p1363",
      },
      signature
    );
  } catch {
    return false;
  }
}
