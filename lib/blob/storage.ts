import { put, del, get } from "@vercel/blob";

/** Token from env, or undefined so the SDK can use Vercel OIDC on deployed builds. */
function resolveBlobAuth(): { token?: string } {
  const token = process.env.BLOB_READ_WRITE_TOKEN?.trim();
  if (token) return { token };
  if (process.env.VERCEL) return {};
  throw new Error(
    "BLOB_READ_WRITE_TOKEN is not set. Add it to .env.local locally, or connect a Vercel Blob store and redeploy."
  );
}

export async function uploadPrivateHtml(opts: {
  slug: string;
  bytes: Buffer | ArrayBuffer | Blob;
  contentType?: string;
}) {
  const auth = resolveBlobAuth();
  const pathname = `study-content/${opts.slug}/index.html`;
  const result = await put(pathname, opts.bytes, {
    access: "private",
    ...auth,
    contentType: opts.contentType || "text/html; charset=utf-8",
    addRandomSuffix: false,
    allowOverwrite: true,
  });
  return { pathname: result.pathname, url: result.url };
}

export async function uploadPrivateThumbnail(opts: {
  slug: string;
  bytes: Buffer | ArrayBuffer | Blob;
  contentType: string;
  ext: string;
}) {
  const auth = resolveBlobAuth();
  const pathname = `study-content/${opts.slug}/thumb.${opts.ext}`;
  const result = await put(pathname, opts.bytes, {
    access: "private",
    ...auth,
    contentType: opts.contentType,
    addRandomSuffix: false,
    allowOverwrite: true,
  });
  return { pathname: result.pathname, url: result.url };
}

export async function fetchPrivateBlob(pathnameOrUrl: string): Promise<string> {
  const auth = resolveBlobAuth();
  const result = await get(pathnameOrUrl, {
    access: "private",
    ...auth,
  });
  if (!result || !result.stream) {
    throw new Error("Blob fetch failed: empty stream");
  }
  const res = new Response(result.stream);
  return res.text();
}

export async function deletePrivateBlob(pathnameOrUrl: string) {
  const auth = resolveBlobAuth();
  try {
    await del(pathnameOrUrl, auth);
  } catch {
    // ignore missing
  }
}
