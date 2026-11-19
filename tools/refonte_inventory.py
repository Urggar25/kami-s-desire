"""Garde-fous structurels J4+ : python tools/refonte_inventory.py --check.
Ce contrôle ne remplace ni le lint Ren'Py ni une lecture en jeu.
"""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASELINE = ROOT / "docs/refonte/baseline.json"
LABEL = re.compile(r"^label\s+([A-Za-z_]\w*)", re.M)
ANCHOR = re.compile(r"\bfrom\s+([A-Za-z_]\w*)\s*(?:#.*)?$")
VISUAL_CALL = re.compile(r"^\s*call\s+(cutin|reactions|trial_intro)\b")
VISUAL_PY = re.compile(r"^\s*\$\s*(showGroup|hideGroup|showP|close_up|release_cam|wide_shot|punch_in|dutch|dutch_off)\s*\(")
CONTROL = re.compile(r"^\s*(?:label\s|default\s|menu\s*[:(]|if\s|elif\s|else\s*:|jump\s|call\s|return\b|\$\s*)")

def source_files():
    return sorted(p for p in (ROOT / "game").rglob("*.rpy")
                  if "tl" not in p.relative_to(ROOT / "game").parts)

def contract(text):
    # Comparaison conservatrice des flags, conditions, labels et appels.
    # Les blocs Python multilignes restent à relire et à tester dans Ren'Py.
    return [line.rstrip() for line in text.splitlines()
            if CONTROL.match(line) and not VISUAL_CALL.match(line)
            and not VISUAL_PY.match(line)]

def inventory():
    entries = {}
    for p in source_files():
        if "scenario" not in p.parts or not re.match(r"^\d+_", p.name):
            continue
        day = int(p.name.split("_", 1)[0])
        if day < 4:
            continue
        text = p.read_text(encoding="utf-8-sig")
        entries[p.relative_to(ROOT).as_posix()] = {
            "day": day, "lines": len(text.splitlines()),
            "labels": LABEL.findall(text), "contract": contract(text)}
    return entries

def check(entries):
    baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
    previous = {f["path"]: f for f in baseline["files"]}
    errors = []
    for path in sorted(previous.keys() - entries.keys()):
        errors.append("Fichier retiré : " + path)
    for path in sorted(previous.keys() & entries.keys()):
        if previous[path]["contract"] != entries[path]["contract"]:
            errors.append("Contrat de continuité modifié, à examiner : " + path)
    occurrences = {}
    for p in source_files():
        text = p.read_text(encoding="utf-8-sig")
        for n, line in enumerate(text.splitlines(), 1):
            match = LABEL.match(line)
            if not match and line.lstrip().startswith("call "):
                match = ANCHOR.search(line)
            if match:
                occurrences.setdefault(match.group(1), []).append(
                    (p.relative_to(ROOT).as_posix(), n))
    # Ne pas attribuer à ce lot d'éventuels doublons hérités.
    for name, locations in occurrences.items():
        if len(locations) > 1 and "_kv2_" in name:
            errors.append(f"Retour de mise en scène dupliqué : {name} {locations}")
    for error in errors:
        print(error)
    print(f"{len(entries)} fichiers ; {sum(len(f['labels']) for f in entries.values())} labels ; {len(errors)} écart(s) de contrat.")
    print("Contrôle statique uniquement : rendu et exécution Ren'Py non validés.")
    return bool(errors)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    entries = inventory()
    if args.check:
        raise SystemExit(int(check(entries)))
    print(json.dumps({"files": len(entries),
                      "labels": sum(len(f["labels"]) for f in entries.values()),
                      "lines": sum(f["lines"] for f in entries.values())}, indent=2))

if __name__ == "__main__":
    main()
