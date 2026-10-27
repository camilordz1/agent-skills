#!/usr/bin/env python3
"""Revisa los básicos de SEO de un post en Markdown con front matter YAML.

Uso: python3 check_post.py ruta/al/post.md
Códigos de salida: 0 sin errores, 1 con errores, 2 archivo ilegible o sin front matter.
"""
import re
import sys
from pathlib import Path

TITLE_MAX = 60  # convención editorial: Google acorta lo que no cabe, no hay límite oficial
DESC_MIN, DESC_MAX = 70, 160  # convención editorial, ver references/umbrales.md
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def split_front_matter(text):
    """Devuelve (front matter, cuerpo, línea del archivo donde empieza el cuerpo)."""
    match = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.DOTALL)
    if not match:
        return None, text, 1
    return match.group(1), match.group(2), match.group(1).count("\n") + 4


def read_field(front, key):
    # Solo valores de una línea, con comillas dobles, simples o sin comillas.
    match = re.search(rf"""^{key}:\s*["']?(.*?)["']?\s*$""", front, re.MULTILINE)
    return match.group(1).strip() if match else ""


def check(front, body, first_line=1):
    findings = []
    title = read_field(front, "title")
    desc = read_field(front, "description")
    slug = read_field(front, "slug")

    if not title:
        findings.append(("ERROR", "Falta el título (title)."))
    elif len(title) > TITLE_MAX:
        findings.append(("AVISO", f"Título de {len(title)} caracteres (máx. recomendado {TITLE_MAX})."))

    if not desc:
        findings.append(("ERROR", "Falta la descripción (description)."))
    elif not DESC_MIN <= len(desc) <= DESC_MAX:
        findings.append(("AVISO", f"Descripción de {len(desc)} caracteres (rango recomendado {DESC_MIN}-{DESC_MAX})."))

    if slug and not SLUG_RE.match(slug):
        findings.append(("ERROR", f"Slug no válido: '{slug}' (usa minúsculas, números y guiones)."))

    fence = None  # marcador del bloque de código abierto (``` o ~~~)
    last_level = 1
    has_internal_link = False
    for number, line in enumerate(body.splitlines(), start=first_line):
        marker = re.match(r"\s{0,3}(`{3,}|~{3,})", line)
        if marker:
            mark = marker.group(1)
            if fence is None:
                fence = mark
                continue
            if mark[0] == fence[0] and len(mark) >= len(fence):
                fence = None
                continue
        if fence:
            continue
        heading = re.match(r"^(#{1,6})\s+\S", line)
        if heading:
            level = len(heading.group(1))
            if level == 1:
                findings.append(("AVISO", f"Línea {number}: hay un H1 en el cuerpo; la plantilla ya usa el título."))
            elif level > last_level + 1:
                findings.append(("AVISO", f"Línea {number}: salto de H{last_level} a H{level}."))
            last_level = level
        if re.search(r"!\[\s*\]\(", line):
            findings.append(("ERROR", f"Línea {number}: imagen sin texto alternativo."))
        if re.search(r"\]\(/[^)]*\)", line):
            has_internal_link = True

    if not has_internal_link:
        findings.append(("AVISO", "No hay ningún enlace interno (que empiece por '/')."))
    return findings


def main():
    if len(sys.argv) != 2:
        print("Uso: python3 check_post.py ruta/al/post.md", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as error:
        print(f"No se pudo leer {path}: {error}", file=sys.stderr)
        return 2
    front, body, first_line = split_front_matter(text)
    if front is None:
        print(f"{path} no tiene front matter entre líneas '---'.", file=sys.stderr)
        return 2

    findings = check(front, body, first_line)
    for level, message in findings:
        print(f"{level}: {message}")
    errors = sum(1 for level, _ in findings if level == "ERROR")
    print(f"Resumen: {errors} errores, {len(findings) - errors} avisos.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
