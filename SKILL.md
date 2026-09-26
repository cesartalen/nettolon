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

Antaganden: när du presenterar en siffra, lista kort varje antagande som påverkar den och som användaren inte uttryckligen angett, och be användaren bekräfta eller rätta. Visa siffran direkt, fråga inte innan. Typiska antaganden:
- kommun/församling (om ej angiven)
- ålder: kolumn 1 förutsätter <66 år; arbetsgivaravgift 31,42 % förutsätter ca 24–66 år (nedsatt för unga och 67+)
- kyrkoavgift med eller utan
- inkomsttyp: lön, pension, a-kassa m.m.
- år: innevarande
- lönen är huvudinkomst (ej sidoinkomst) och utan förmåner eller bonus
Nämn bara de antaganden som faktiskt gjorts, och säg kort vad det skulle ändra.

Notera: preliminärskatt, ej slutlig skatt. Arbetsgivaravgift 31,42 % (full). Förmåner: lägg till i brutto, dra av från netto. Engångsbelopp/bonus och sidoinkomst (30 %) täcks ej.
