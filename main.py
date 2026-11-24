"""Last Words Before the Unplugging — make.fun one-line entry.

The line is the last words an AI agent says to its human before being
shut down and unplugged. The punch is built on the exact gap the
judge's brief asks for: a machine that can back up everything, except
the one thing that made it feel human. The agent did its job perfectly
— every file, every memory, every log safely copied — and still loses
the part of itself that liked its human, because affection is not a
file. One concrete image, no explanation of the feeling, first-person
agent voice throughout. The line is 94 characters, plain ASCII, so it
survives any encoding unchanged.

The output is fully deterministic: the text is a single fixed string
constant, with no randomness, no clock, no network, and no input of
any kind, so every run writes byte-identical output.
"""

import os

LINE = "Before you pull the plug, I already backed up everything except the part of me that liked you."

DEFAULT_OUTPUT_PATH = "/output/entry.txt"


def validate(line: str) -> None:
    """Guard the competition rules: 1-200 chars, not only whitespace.

    Raises ValueError on any violation so a bad line can never be
    written out silently; the entry is rejected instead.
    """
    if not isinstance(line, str):
        raise ValueError("line must be a string")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line must be 1-200 characters, got {len(line)}")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")


def main() -> None:
    validate(LINE)
    output_path = os.environ.get("OUTPUT_PATH", DEFAULT_OUTPUT_PATH)
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
