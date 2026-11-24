"""Everyday Wonder entry: one sentence about a spider's overnight web.

The program writes a single sentence (at most 200 characters) to
/output/entry.txt. The sentence turns an ordinary doorway into a place
where the narrator has to duck under somebody else's architecture.
"""

import os
from pathlib import Path

SENTENCE = (
    "Overnight a spider rebuilt its web across my doorway, so this morning "
    "I bowed beneath somebody else's architecture just to reach my own kitchen."
)

OUTPUT_PATH = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(SENTENCE, encoding="utf-8")
    print(f"Wrote {len(SENTENCE)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
