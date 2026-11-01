#!/usr/bin/env python3
"""Baixa a thumbnail de um vídeo do YouTube pelo ID/URL e gera uma prévia pequena.

Uso: python fetch_thumb.py <url-ou-id> [pasta_saida]
Saída: <id>.jpg (maior resolução disponível) e <id>_mini.jpg (160 px sobre fundo #0f0f0f,
simulando a grade do YouTube em modo escuro). Requer Pillow para a prévia (opcional).
"""
import re
import sys
import urllib.request
from pathlib import Path


def video_id(s: str) -> str:
    m = re.search(r"(?:v=|youtu\.be/|shorts/|/vi/)([\w-]{11})", s)
    if m:
        return m.group(1)
    if re.fullmatch(r"[\w-]{11}", s):
        return s
    sys.exit(f"ID de vídeo não reconhecido: {s}")


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    vid = video_id(sys.argv[1])
    out = Path(sys.argv[2] if len(sys.argv) > 2 else ".")
    out.mkdir(parents=True, exist_ok=True)
    dest = out / f"{vid}.jpg"
    for name in ("maxresdefault", "sddefault", "hqdefault"):
        url = f"https://i.ytimg.com/vi/{vid}/{name}.jpg"
        try:
            data = urllib.request.urlopen(url, timeout=20).read()
        except Exception:
            continue
        if len(data) > 2000:  # evita o placeholder cinza
            dest.write_bytes(data)
            print(f"imagem: {dest}  (fonte: {url})")
            break
    else:
        sys.exit("INACESSÍVEL: nenhuma thumbnail encontrada. Não descreva a imagem.")
    try:
        from PIL import Image
        im = Image.open(dest).convert("RGB")
        im.thumbnail((160, 90))
        bg = Image.new("RGB", (180, 110), "#0f0f0f")
        bg.paste(im, (10, 10))
        mini = out / f"{vid}_mini.jpg"
        bg.save(mini, quality=92)
        print(f"prévia pequena: {mini}")
    except ImportError:
        print("Pillow não instalado: prévia pequena não gerada.")


if __name__ == "__main__":
    main()
