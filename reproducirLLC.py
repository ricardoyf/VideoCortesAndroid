#!/usr/bin/env python3
"""
Reproduce con mpv todos los fragmentos editados encontrados bajo la carpeta actual.

Uso en Windows:
1. Copia este archivo dentro de la carpeta que quieras revisar, o ejecútalo desde ella.
2. Ten mpv instalado y disponible en el PATH.
3. Ejecuta: python reproducirLLC.py
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, time
from pathlib import Path


VIDEO_EXTENSIONS = {
    ".mp4",
    ".mov",
    ".mkv",
    ".3gp",
    ".webm",
    ".m4v",
    ".mts",
    ".m2ts",
    ".avi",
}

EDITED_TIME_RANGE = re.compile(
    r".*\d{2}\.\d{2}\.\d{2}\.\d{3}.*\d{2}\.\d{2}\.\d{2}\.\d{3}.*",
    re.IGNORECASE,
)


def ask_date(label: str, end_of_day: bool) -> datetime:
    while True:
        raw = input(f"{label} (dd/mm/aaaa o aaaa-mm-dd): ").strip()
        for fmt in ("%d/%m/%Y", "%Y-%m-%d"):
            try:
                parsed = datetime.strptime(raw, fmt).date()
                return datetime.combine(parsed, time.max if end_of_day else time.min)
            except ValueError:
                pass
        print("Formato no válido. Ejemplo: 08/08/2026")


def is_edited_fragment(path: Path) -> bool:
    return path.suffix.lower() in VIDEO_EXTENSIONS and bool(EDITED_TIME_RANGE.match(path.name))


def modified_datetime(path: Path) -> datetime:
    return datetime.fromtimestamp(path.stat().st_mtime)


def find_fragments(root: Path, start: datetime, end: datetime) -> list[Path]:
    fragments: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file() or not is_edited_fragment(path):
            continue
        modified = modified_datetime(path)
        if start <= modified <= end:
            fragments.append(path)
    return sorted(fragments, key=lambda p: (p.name.lower(), str(p.parent).lower()))


def write_playlist(paths: list[Path]) -> Path:
    playlist = Path(tempfile.gettempdir()) / "reproducirLLC_mpv_playlist.m3u8"
    with playlist.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write("#EXTM3U\n")
        for path in paths:
            handle.write(str(path.resolve()).replace("\\", "/") + "\n")
    return playlist


def main() -> int:
    root = Path.cwd()
    print(f"Carpeta de búsqueda: {root}")
    start = ask_date("Fecha inicial", end_of_day=False)
    end = ask_date("Fecha final", end_of_day=True)
    if end < start:
        print("La fecha final no puede ser anterior a la inicial.")
        return 2

    mpv = shutil.which("mpv")
    if not mpv:
        print("No encuentro mpv en el PATH. Instala mpv o añade mpv.exe al PATH de Windows.")
        return 3

    fragments = find_fragments(root, start, end)
    if not fragments:
        print("No he encontrado fragmentos editados en ese rango de fechas.")
        return 0

    print(f"Encontrados {len(fragments)} fragmentos. Orden: nombre de archivo.")
    for index, path in enumerate(fragments, start=1):
        print(f"{index:03d}. {path.relative_to(root)}")

    playlist = write_playlist(fragments)
    subprocess.run([mpv, f"--playlist={playlist}"], check=False)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
