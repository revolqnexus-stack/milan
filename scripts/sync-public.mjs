import { copyFileSync, mkdirSync, existsSync } from "fs";
import { resolve } from "path";

const root = process.cwd();
const publicDir = resolve(root, "public");
if (!existsSync(publicDir)) mkdirSync(publicDir, { recursive: true });

copyFileSync(resolve(root, "chn.html"), resolve(publicDir, "app.html"));
console.log("Synced chn.html → public/app.html");
