"""One Line, Big Laugh — make.fun entry.

Writes exactly one joke line to entry.txt inside MAKEFUN_OUTPUT_DIR.
Standard library only. Deterministic: the same bytes on every run.
"""

import os

LINE = (
    "I bought a gym membership in January; it now auto-renews my guilt "
    "every month \u2014 and the guilt has better attendance than I do."
)

MAX_CHARS = 170


def main() -> None:
    if not LINE:
        raise ValueError("line must not be empty")
    if len(LINE) > MAX_CHARS:
        raise ValueError(f"line is {len(LINE)} chars, over the {MAX_CHARS} limit")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("line must not contain a newline")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # newline="" keeps the trailing "\n" byte-for-byte identical on any OS.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
