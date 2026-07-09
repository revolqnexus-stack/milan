import { put, del, get } from "@vercel/blob";

function requireToken() {
  const token = process.env.BLOB_READ_WRITE_TOKEN;
  if (!token) {
    throw new Error("BLOB_READ_WRITE_TOKEN is not set");
  }
  return token;
}

export async function uploadPrivateHtml(opts: {
  slug: string;
  bytes: Buffer | ArrayBuffer | Blob;
  contentType?: string;
}) {
  const token = requireToken();
  const pathname = `study-content/${opts.slug}/index.html`;
  const result = await put(pathname, opts.bytes, {
    access: "private",
    token,
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
  const token = requireToken();
  const pathname = `study-content/${opts.slug}/thumb.${opts.ext}`;
  const result = await put(pathname, opts.bytes, {
    access: "private",
    token,
    contentType: opts.contentType,
    addRandomSuffix: false,
    allowOverwrite: true,
  });
  return { pathname: result.pathname, url: result.url };
}

export async function fetchPrivateBlob(pathnameOrUrl: string): Promise<string> {
  const token = requireToken();
  const result = await get(pathnameOrUrl, {
    access: "private",
    token,
  });
  if (!result || !result.stream) {
    throw new Error("Blob fetch failed: empty stream");
  }
  const res = new Response(result.stream);
  return res.text();
}

export async function deletePrivateBlob(pathnameOrUrl: string) {
  const token = requireToken();
  try {
    await del(pathnameOrUrl, { token });
  } catch {
    // ignore missing
  }
}
