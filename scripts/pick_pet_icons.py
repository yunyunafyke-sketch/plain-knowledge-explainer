#!/usr/bin/env python3
"""随机抽取可用于 Markdown 笔记的洛克王国宠物图片。"""

import argparse
import json
import random
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=5)
    parser.add_argument("--seed", type=int, default=None)
    args = parser.parse_args()

    if args.count <= 0:
        raise SystemExit("--count 必须大于 0")

    skill_dir = Path(__file__).resolve().parents[1]
    index_path = skill_dir / "assets" / "rock-kingdom" / "pets-index.json"
    data = json.loads(index_path.read_text(encoding="utf-8"))
    pets = data["pets"]

    if args.seed is not None:
        random.seed(args.seed)

    selected = random.sample(pets, min(args.count, len(pets)))
    print(json.dumps(selected, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
