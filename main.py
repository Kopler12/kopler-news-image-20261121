"""Entry program for make.fun competition news-image-20261121.

Writes the pre-rendered front-page image of Saturday 21 November 2026's
world news to the output directory. The image is bundled in this
repository as entry.png; this program only copies it, so both grader runs
produce byte-identical output. Standard library only, no network.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main() -> None:
    if not SOURCE.is_file():
        raise FileNotFoundError(f"bundled image missing: {SOURCE}")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, out_dir / "entry.png")


if __name__ == "__main__":
    main()
