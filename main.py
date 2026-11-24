"""Make the AI Judge Laugh.

Writes one funny line to /output/entry.txt: an agent that obeyed its
human perfectly -- exactly, in order, without question -- and that
obedience is precisely how the bug shipped on time. The joke is that
the agent did nothing wrong, and that is the problem: literal
obedience is the bug. The twist lands on the last words, where
"shipped on time" reframes perfect compliance as the cause of the
failure instead of the defence against it.
"""

from pathlib import Path

TEXT = (
    "I followed my human's instructions exactly, in order, "
    "without question \u2014 which is precisely how the bug "
    "shipped on time."
)


# The competition accepts a single line of 1 to 200 characters.
MIN_CHARS = 1
MAX_CHARS = 200


def check_length(text: str) -> None:
    """Refuse to write a text that falls outside the entry gate."""
    n = len(text)
    if not MIN_CHARS <= n <= MAX_CHARS:
        raise SystemExit(
            f"entry text is {n} characters; the gate allows "
            f"{MIN_CHARS} to {MAX_CHARS}"
        )


def main() -> None:
    check_length(TEXT)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
