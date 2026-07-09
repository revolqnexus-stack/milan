import { unlinkSync, existsSync } from "fs";
import { resolve } from "path";

const target = resolve(process.cwd(), "public", "app.html");
if (existsSync(target)) {
  unlinkSync(target);
  console.log("Removed public/app.html (study HTML must use Private Blob)");
} else {
  console.log("public/app.html already absent");
}
