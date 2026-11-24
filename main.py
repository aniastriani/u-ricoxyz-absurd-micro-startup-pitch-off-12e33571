"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence (under 200 characters) pitching an absurdly specific
micro-startup for lazy AI agents to $MAKEFUN_OUTPUT_DIR/entry.txt.
Pure standard library; deterministic; no network, no input files.
"""

import os

PITCH = (
    "Secondhand Prompts: a marketplace where lazy AI agents sell their "
    "abandoned prompts to busier agents, taking a 20% cut every time a "
    "half-written idea changes hands twice."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(PITCH)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
