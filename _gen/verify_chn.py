# -*- coding: utf-8 -*-
from pathlib import Path
import re
t = Path(r"c:\Users\eathe\milan\chn.html").read_text(encoding="utf-8")
ids = re.findall(r'data-id="(t\d+)"', t)
print("ids", ids)
print("count", len(ids), "unique", len(set(ids)))
print("Full Exam", t.count("Full Exam Version"))
print("mock ids", len(re.findall(r'id="mock-\d"', t)))
print("chnDoneTopics", "chnDoneTopics" in t)
print("TOTAL", re.search(r"const TOTAL = (\d+)", t).group(1))
print("Bio leak", "Bio Science" in t or "Myocardium" in t)
print("diagram-box", t.count("diagram-box"))
print("drill-item", t.count("drill-item"))
pages = ["page-home","page-topics","page-score","page-drill","page-mock","page-templates","page-quick"]
print("pages", [p for p in pages if f'id="{p}"' in t])
missing = [f"t{i}" for i in range(1,37) if f"t{i}" not in ids]
print("missing", missing)
print("stubs left", t.count("Full → Topics") + t.count("Full answer → Topics") + t.count("open matching Topics"))
print("NIS placeholder", "as per current NIS" in t or "Write ages exactly as taught" in t)
print("diagram-box", t.count("diagram-box"))
print("model-answer", t.count("model-answer"))
print("tmpl-diagrams", 'id="tmpl-diagrams"' in t)
print("mock papers", len(re.findall(r'id="mock-\d"', t)))
print("Mark-wise Answer", t.count("Mark-wise Answer"))
print("survival h3", t.count("1 Day Before Exam"))
print("start ok", t.startswith("<!DOCTYPE html>"))
print("end ok", t.rstrip().endswith("</html>"))
print("lines", t.count("\n")+1)
# category section topic counts
for label in ["FOUNDATIONS", "EPIDEMIOLOGY", "ENVIRONMENT"]:
    print(label, "present", label in t)
