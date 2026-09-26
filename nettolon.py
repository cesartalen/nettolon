#!/usr/bin/env python3
"""Nettolön från Skatteverkets skattetabeller (månadslön)."""
import argparse, datetime, json, sys, urllib.parse, urllib.request

API = "https://skatteverket.entryscape.net/rowstore/dataset/"
TAB, KOM = "88320397-5c32-4c16-ae79-d36d95b17b95", "c67b320b-ffee-4876-b073-dd9236cd2a99"
AVG = 0.3142


def get(ds, **q):
    url, rows = API + ds + "?" + urllib.parse.urlencode({**q, "_limit": 500}), []
    while url:
        d = json.load(urllib.request.urlopen(url))
        rows += d["results"]
        url = d.get("next") if d["results"] else None
    return rows


def main():
    p = argparse.ArgumentParser()
    p.add_argument("brutto", type=int)
    p.add_argument("-k", "--kommun")
    p.add_argument("-t", "--tabell", type=int)
    p.add_argument("-c", "--kolumn", type=int, default=1, choices=range(1, 7))
    p.add_argument("-f", "--forsamling", help="del av församlingsnamn")
    p.add_argument("--kyrka", action="store_true")
    p.add_argument("-y", "--ar", type=int, default=datetime.date.today().year)
    a = p.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

    sats = fors = None
    if a.brutto < 0:
        p.error("brutto < 0")
    if not (a.tabell or a.kommun):
        p.error("ange --kommun eller --tabell")
    if not a.tabell:
        rs = get(KOM, år=a.ar, kommun=a.kommun.upper())
        rs = [r for r in rs if (a.forsamling or "").upper() in r["församling"]]
        if not rs:
            raise SystemExit(f"Hittar inte {a.kommun} {a.forsamling or ''} ({a.ar})")
        k, tabs = "summa, inkl. kyrkoavgift" if a.kyrka else "summa, exkl. kyrkoavgift", {}
        for r in rs:
            s = float(r[k])
            tabs.setdefault(int(s) + (s % 1 > 0.5), []).append(r)
        if len(tabs) > 1:
            raise SystemExit("Tabell beror på församling, ange -f:\n" + "\n".join(
                f"{t}: {', '.join(r['församling'] for r in v)}" for t, v in sorted(tabs.items())))
        (a.tabell, rs), = tabs.items()
        fors = rs[0]["församling"] if len(rs) == 1 else None
        sats = sorted({float(r[k]) for r in rs})
        sats = sats[0] if len(sats) == 1 else sats

    col, b = f"kolumn {a.kolumn}", max(a.brutto, 1)
    for r in get(TAB, år=a.ar, tabellnr=a.tabell):
        hi = r["inkomst t.o.m."]
        if int(r["inkomst fr.o.m."]) <= b <= (int(hi) if hi else b):
            v = int(r[col])
            skatt = a.brutto * v // 100 if r["antal dgr"] == "30%" else v
            break
    else:
        raise SystemExit(f"Ingen tabell {a.tabell} för {a.ar}")

    print(json.dumps({
        "år": a.ar, "församling": fors, "skattesats": sats, "tabell": a.tabell, "kolumn": a.kolumn,
        "brutto": a.brutto, "skatt": skatt, "netto": a.brutto - skatt,
        "arbetsgivaravgift": round(a.brutto * AVG), "total_kostnad": round(a.brutto * (1 + AVG)),
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
