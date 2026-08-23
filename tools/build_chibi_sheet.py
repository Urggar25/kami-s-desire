"""Re-cut a chibi sprite sheet into clean, evenly spaced cells.

Hand-drawn sheets are rarely divisible by the number of poses: arms, hair
and clothes cross the nominal cell borders, so a uniform crop drags slabs
of the neighbouring pose into the frame. This tool rebuilds the sheet so
that a uniform crop is exactly right:

  1. the real gaps between poses are found from the alpha profile;
  2. inside each slab, only the pose itself is kept — anything severed at
     a cut (a stray lock of the neighbour's hair) is dropped, while
     detached parts of the pose itself (sweat drops, effect marks) are
     kept;
  3. every pose is re-centred on a stable anchor (the feet) and its
     ground line is aligned, so cutting from pose to pose no longer makes
     the character drift;
  4. the poses are laid out in identical cells.

    python tools/build_chibi_sheet.py \
        --src game/images/.../noam_change_animation.png \
        --out game/images/.../noam_change_frames.png --cells 8

The metadata printed at the end (sheet_size, cols, content) is what the
ChibiMontageSpec needs.
"""

import argparse
from pathlib import Path

import numpy as np
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]

ALPHA_FLOOR = 8      # en dessous, on considere le pixel transparent
SEAM_SEARCH = 90     # rayon de recherche du vrai creux autour d'une frontiere
SEAM_MARGIN = 2      # tolerance pour "touche le bord de coupe"


# ------------------------------------------------------------------
# Composantes connexes, par segments de lignes (rapide, sans scipy)
# ------------------------------------------------------------------
def row_runs(row):
    """Segments contigus de pixels opaques dans une ligne."""
    padded = np.concatenate(([False], row, [False]))
    edges = np.diff(padded.astype(np.int8))
    starts = np.flatnonzero(edges == 1)
    ends = np.flatnonzero(edges == -1)
    return list(zip(starts.tolist(), ends.tolist()))


def connected_components(mask):
    """Retourne une liste de composantes : {area, bbox, runs, touches}."""
    parent = []

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    def union(i, j):
        ri, rj = find(i), find(j)
        if ri != rj:
            parent[max(ri, rj)] = min(ri, rj)

    runs = []           # (y, x0, x1)
    prev_ids = []
    for y in range(mask.shape[0]):
        current = row_runs(mask[y])
        current_ids = []
        for (x0, x1) in current:
            idx = len(runs)
            runs.append((y, x0, x1))
            parent.append(idx)
            current_ids.append(idx)
            for pid in prev_ids:
                py, px0, px1 = runs[pid]
                if px0 < x1 and x0 < px1:      # chevauchement horizontal
                    union(idx, pid)
        prev_ids = current_ids

    groups = {}
    for idx, (y, x0, x1) in enumerate(runs):
        root = find(idx)
        comp = groups.setdefault(root, {
            "area": 0, "runs": [],
            "x0": x1, "x1": x0, "y0": y, "y1": y,
        })
        comp["area"] += x1 - x0
        comp["runs"].append((y, x0, x1))
        comp["x0"] = min(comp["x0"], x0)
        comp["x1"] = max(comp["x1"], x1)
        comp["y0"] = min(comp["y0"], y)
        comp["y1"] = max(comp["y1"], y)
    return list(groups.values())


# ------------------------------------------------------------------
def find_cuts(mask, cells):
    """Position de coupe reelle entre chaque pose."""
    ink = mask.sum(axis=0)
    width = mask.shape[1]
    cuts = [0]
    for i in range(1, cells):
        nominal = int(round(i * width / float(cells)))
        lo = max(cuts[-1] + 1, nominal - SEAM_SEARCH)
        hi = min(width - 1, nominal + SEAM_SEARCH)
        window = ink[lo:hi]
        # Le creux le plus profond ; a egalite, le plus proche du nominal.
        best = int(np.min(window))
        candidates = [lo + int(j) for j in np.flatnonzero(window == best)]
        cuts.append(min(candidates, key=lambda x: abs(x - nominal)))
        if best:
            print("  couture %d : creux de %d px a x=%d (nominal %d)"
                  % (i, best, cuts[-1], nominal))
    cuts.append(width)
    return cuts


def extract_pose(rgba, mask, x0, x1):
    """Isole la pose d'un segment, sans les eclats du voisin."""
    slab = mask[:, x0:x1]
    comps = connected_components(slab)
    if not comps:
        raise SystemExit("segment vide entre %d et %d" % (x0, x1))

    main = max(comps, key=lambda c: c["area"])
    kept = [main]
    dropped = 0
    for comp in comps:
        if comp is main:
            continue
        # Un eclat coupe par la couture touche forcement un bord du segment.
        at_seam = (comp["x0"] <= SEAM_MARGIN
                   or comp["x1"] >= slab.shape[1] - SEAM_MARGIN)
        if at_seam:
            dropped += comp["area"]
        else:
            kept.append(comp)

    keep_mask = np.zeros_like(slab)
    for comp in kept:
        for (y, rx0, rx1) in comp["runs"]:
            keep_mask[y, rx0:rx1] = True

    piece = rgba[:, x0:x1].copy()
    piece[~keep_mask] = 0
    return piece, keep_mask, dropped


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--cells", type=int, required=True)
    ap.add_argument("--foot-band", type=int, default=110,
                    help="hauteur, au bas de la pose, servant d'ancrage")
    ap.add_argument("--pad", type=int, default=12)
    args = ap.parse_args()

    src = Path(args.src)
    if not src.is_absolute():
        src = ROOT / src
    image = Image.open(src).convert("RGBA")
    rgba = np.array(image)
    mask = rgba[:, :, 3] > ALPHA_FLOOR
    height = rgba.shape[0]

    print("planche source %dx%d, %d poses" % (image.width, image.height,
                                              args.cells))
    cuts = find_cuts(mask, args.cells)

    poses = []
    for i in range(args.cells):
        piece, keep, dropped = extract_pose(rgba, mask, cuts[i], cuts[i + 1])
        cols = np.flatnonzero(keep.any(axis=0))
        rows = np.flatnonzero(keep.any(axis=1))
        x0, x1 = int(cols[0]), int(cols[-1]) + 1
        y0, y1 = int(rows[0]), int(rows[-1]) + 1

        # Ancrage : centre des pieds, stable d'une pose a l'autre.
        foot = keep[max(y0, y1 - args.foot_band):y1]
        foot_cols = np.flatnonzero(foot.any(axis=0))
        anchor = (int(foot_cols[0]) + int(foot_cols[-1]) + 1) / 2.0

        poses.append({"piece": piece, "x0": x0, "x1": x1, "y0": y0, "y1": y1,
                      "anchor": anchor})
        print("  pose %d : %dx%d, ancrage x=%.1f, %d px de voisin retires"
              % (i + 1, x1 - x0, y1 - y0, anchor, dropped))

    # Largeur de cellule : assez pour la pose la plus debordante.
    reach = max(max(p["anchor"] - p["x0"], p["x1"] - p["anchor"])
                for p in poses)
    cell_w = int(np.ceil(reach + args.pad)) * 2
    baseline = max(p["y1"] for p in poses)     # ligne de sol commune

    sheet = Image.new("RGBA", (cell_w * args.cells, height), (0, 0, 0, 0))
    top = height
    for i, pose in enumerate(poses):
        crop = Image.fromarray(pose["piece"]).crop(
            (pose["x0"], pose["y0"], pose["x1"], pose["y1"]))
        px = int(round(i * cell_w + cell_w / 2.0 - (pose["anchor"] - pose["x0"])))
        py = baseline - (pose["y1"] - pose["y0"])
        sheet.paste(crop, (px, py))
        top = min(top, py)

    out = Path(args.out)
    if not out.is_absolute():
        out = ROOT / out
    out.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out, optimize=True)

    # Garantie : avec une decoupe uniforme, aucune pose ne touche une
    # couture, donc aucun eclat du voisin ne peut apparaitre.
    check = np.array(sheet)[:, :, 3] > 0
    clean = True
    for i in range(args.cells):
        cell = check[:, i * cell_w:(i + 1) * cell_w]
        used = np.flatnonzero(cell.any(axis=0))
        left, right = int(used[0]), cell_w - 1 - int(used[-1])
        clean &= cell[:, 0].sum() == 0 and cell[:, -1].sum() == 0
        print("  cellule %d : marges de %d et %d px" % (i + 1, left, right))
    if not clean:
        raise SystemExit("une pose touche encore une couture : augmente --pad")

    print()
    print("planche -> %s" % out)
    print("    sheet_size=(%d, %d)," % (sheet.width, sheet.height))
    print("    cols=%d," % args.cells)
    print("    content=(%d, %d)," % (top, baseline))


if __name__ == "__main__":
    main()
