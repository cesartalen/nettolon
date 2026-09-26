---
name: nettolon
description: Beräkna nettolön/skatteavdrag för svensk månadslön via Skatteverkets skattetabeller (live). Use for Swedish net salary, preliminärskatt, lön efter skatt, arbetsgivarkostnad.
---

```
python ~/.claude/skills/nettolon/nettolon.py BRUTTO -k KOMMUN [-c KOLUMN] [--kyrka] [-f FÖRSAMLING] [-y ÅR]
python ~/.claude/skills/nettolon/nettolon.py BRUTTO -t TABELL
```

Kolumn: 1 lön <66 år (default), 2 pension 66+, 3 lön 66+, 4 sjuk-/aktivitetsersättning <66, 5 a-kassa m.m., 6 pension <66.

Kyrkoavgift varierar per församling. Om tabellen beror på församling listar skriptet alternativen: fråga användaren, gissa inte.

Notera: preliminärskatt, ej slutlig skatt. Arbetsgivaravgift 31,42 % (full). Förmåner: lägg till i brutto, dra av från netto. Engångsbelopp/bonus och sidoinkomst (30 %) täcks ej.
