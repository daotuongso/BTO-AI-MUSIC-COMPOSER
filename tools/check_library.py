#!/usr/bin/env python3
import json
from pathlib import Path
p=Path(__file__).resolve().parents[1]/"references/EXT_Style_Library_10_Rev5.json"
data=json.loads(p.read_text(encoding="utf-8"))
names=["Mood","Vocal","Genre","Tempo","Instruments","Production","Structure","Language","Theme","Avoid"]
assert len(data["styles"])==10
assert {x["style_id"] for x in data["styles"]}=={"EXT-%02d"%i for i in range(1,11)}
for i,x in enumerate(data["styles"],1):
 assert x["emotion_order"]==i
 v=x["full_suno_prompt"]
 assert [z.split(":",1)[0] for z in v.split("\n")]==names
 assert 900<=len(v)<=950 and len(v)==x["character_count"]
print("PASS: 10 EXT Styles, field order and length; Audio QA NOT RUN")
