"""Build the final Ren'Py sprites from the approved rangement prototype sheets."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
TEXTURES = ROOT / "game" / "minijeu" / "rangement" / "textures"
ITEMS = TEXTURES / "items"
CRATES = TEXTURES / "crates"

ITEM_NAMES = (
    "cafe_soupe", "cafe_plateau", "cafe_boisson", "cafe_sandwich",
    "maintenance_cle", "maintenance_tournevis", "maintenance_carte", "maintenance_cable",
    "infirmerie_trousse", "infirmerie_bandage", "infirmerie_fiole", "infirmerie_seringue",
    "stockage_carton", "stockage_usb", "stockage_lampe", "stockage_ruban",
)

CRATE_NAMES = ("cafeteria", "maintenance", "infirmerie", "stockage")


def remove_checkerboard(cell):
    rgba = cell.convert("RGBA")
    pixels = []
    for red, green, blue, _alpha in rgba.getdata():
        # The prototype's checkerboard is made of very light, nearly neutral pixels.
        # Keeping darker neutral pixels preserves metallic whites and object shadows.
        if min(red, green, blue) >= 226 and max(red, green, blue) - min(red, green, blue) <= 6:
            pixels.append((red, green, blue, 0))
        else:
            pixels.append((red, green, blue, 255))
    rgba.putdata(pixels)
    return rgba


def fit_canvas(image, size=(160, 120), margin=5):
    bbox = image.getbbox()
    cropped = image.crop(bbox) if bbox else image
    limit = (size[0] - margin * 2, size[1] - margin * 2)
    cropped.thumbnail(limit, Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", size, (0, 0, 0, 0))
    pos = ((size[0] - cropped.width) // 2, (size[1] - cropped.height) // 2)
    canvas.alpha_composite(cropped, pos)
    return canvas


def remove_specks(image, minimum_pixels=45):
    """Remove tiny disconnected checkerboard remnants without touching the item."""
    alpha = image.getchannel("A")
    width, height = image.size
    opaque = set()
    for y in range(height):
        for x in range(width):
            if alpha.getpixel((x, y)) >= 32:
                opaque.add((x, y))
    components = []
    while opaque:
        seed = opaque.pop()
        component = {seed}
        pending = [seed]
        while pending:
            x, y = pending.pop()
            for point in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if point in opaque:
                    opaque.remove(point)
                    component.add(point)
                    pending.append(point)
        components.append(component)
    pixels = image.load()
    for component in components:
        if len(component) < minimum_pixels:
            for x, y in component:
                pixels[x, y] = (0, 0, 0, 0)
    return image


def build_items():
    ITEMS.mkdir(parents=True, exist_ok=True)
    sheet = Image.open(TEXTURES / "proto_ressources.png")
    cell_w = sheet.width / 4.0
    cell_h = sheet.height / 4.0
    for index, name in enumerate(ITEM_NAMES):
        col, row = index % 4, index // 4
        box = (
            round(col * cell_w), round(row * cell_h),
            round((col + 1) * cell_w), round((row + 1) * cell_h),
        )
        sprite = remove_specks(fit_canvas(remove_checkerboard(sheet.crop(box))))
        sprite.save(ITEMS / (name + ".png"), optimize=True)


def build_crates():
    CRATES.mkdir(parents=True, exist_ok=True)
    sheet = Image.open(TEXTURES / "proto_caisse.png").convert("RGBA")
    cell_w = sheet.width / 4.0
    for index, name in enumerate(CRATE_NAMES):
        cell = sheet.crop((round(index * cell_w), 0, round((index + 1) * cell_w), sheet.height))
        cell = cell.crop(cell.getbbox())
        cell.thumbnail((330, 220), Image.Resampling.LANCZOS)
        cell.save(CRATES / (name + ".png"), optimize=True)


def build_background():
    path = TEXTURES / "rangement_background.png"
    image = Image.open(path).convert("RGB")
    image = image.resize((1920, 1080), Image.Resampling.LANCZOS)
    image.save(path, optimize=True)


if __name__ == "__main__":
    build_items()
    build_crates()
    build_background()
