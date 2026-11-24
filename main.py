"""Meme Sprint 3: AI Agent Goes Rogue — entry builder.

Copies the pre-rendered meme image (meme.png) to /output/entry.png,
the artifact path the make.fun judge reads for this competition.
"""

import os
import shutil


def main():
    """Copy meme.png next to this script to /output/entry.png."""
    # Resolve paths relative to this file so the script works from any cwd.
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "meme.png")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print(f"Wrote {dst} ({os.path.getsize(dst)} bytes)")


if __name__ == "__main__":
    main()
