---
name: nettolon
description: Beräkna nettolön/skatteavdrag för svensk månadslön via Skatteverkets skattetabeller (live). Use for Swedish net salary, preliminärskatt, lön efter skatt, arbetsgivarkostnad.
---

```
python ~/.claude/skills/nettolon/nettolon.py BRUTTO -k KOMMUN [-c KOLUMN] [--kyrka] [-f FÖRSAMLING] [-y ÅR] [-b FÖDELSEÅR] [-a AVGIFT]
python ~/.claude/skills/nettolon/nettolon.py BRUTTO -t TABELL
```

Kolumn: 1 lön <66 år (default), 2 pension 66+, 3 lön 66+, 4 sjuk-/aktivitetsersättning <66, 5 a-kassa m.m., 6 pension <66.

Kyrkoavgift varierar per församling. Om tabellen beror på församling listar skriptet alternativen: fråga användaren, gissa inte.

Antaganden: när du presenterar en siffra, lista kort varje antagande som påverkar den och som användaren inte uttryckligen angett, och be användaren bekräfta eller rätta. Visa siffran direkt, fråga inte innan. Typiska antaganden:
- kommun/församling (om ej angiven)
- ålder: kolumn 1 förutsätter <66 år. Utan `-b` räknas full arbetsgivaravgift 31,42 %, vilket förutsätter att den anställda varken är ung (19–23 år) eller 67+
- kyrkoavgift med eller utan
- inkomsttyp: lön, pension, a-kassa m.m.
- år: innevarande
- lönen är huvudinkomst (ej sidoinkomst) och utan förmåner eller bonus
Nämn bara de antaganden som faktiskt gjorts, och säg kort vad det skulle ändra.

Arbetsgivaravgift (fältet `avgiftsgrund` visar vilken sats som använts; nämn den alltid när du redovisar arbetsgivaravgift eller total kostnad):
- 31,42 %: standard, 24–66 år (2026: född 1959–2002)
- 20,81 % på lön upp till 25 000 kr/mån, 31,42 % på resten: 19–23 år (2026: född 2003–2007), 1 apr 2026–30 sep 2027
- 10,21 %: fyllt 67 vid årets ingång (2026: född 1938–1958)
- 0 %: född 1937 eller tidigare
Ange födelseår med `-b` när det är känt, så väljer skriptet sats. Följande avgör skriptet inte, fråga om de kan vara aktuella och ange då satsen med `-a`: växa-stöd (första anställda, 10,21 % upp till 35 000 kr), regional nedsättning i stödområde, FoU-avdrag, utländsk arbetsgivare eller utsänd personal.

Notera: preliminärskatt, ej slutlig skatt. Förmåner: lägg till i brutto, dra av från netto. Engångsbelopp/bonus och sidoinkomst (30 %) täcks ej.
