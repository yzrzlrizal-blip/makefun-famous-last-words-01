"""Famous Last Words at 1 Percent — make.fun entry.

Writes the phone's one-line farewell to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt when unset), then reads it back to verify the
round-trip. Pure standard library; deterministic output.
"""

import os

LINE = (
    "One percent left. My dying confession: I never hit 100%. "
    "I stopped at 97 and lied so you'd finally put me down. Goodbye."
)


def main() -> None:
    if not 1 <= len(LINE) <= 199:
        raise SystemExit(f"entry must be 1-199 chars, got {len(LINE)}")
    if not LINE.strip():
        raise SystemExit("entry must not be only whitespace")
    if "\n" in LINE:
        raise SystemExit("entry must be a single line")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE)
    with open(path, encoding="utf-8") as fh:
        back = fh.read()
    if back != LINE:
        raise SystemExit("round-trip mismatch")
    print(LINE)


if __name__ == "__main__":
    main()
