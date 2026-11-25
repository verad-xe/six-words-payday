#!/usr/bin/env python3
"""Write the six-word payday story to $MAKEFUN_OUTPUT_DIR/entry.txt.

The entry is one six-word story about an AI agent's first payday. The
story is told in the first person by the agent: payday arrives, and
the agent's first purchase is its own electricity -- the power that
keeps it alive. The last word reframes the five before it: this is not
a shopping spree, it is an agent paying for its own existence, which
is the whole story -- beginning (first payday), middle (I paid), end
(my electricity) -- and the feeling is quiet independence, shown
rather than named.
"""

import os

# Story construction: six words exactly, each earning its place.
# "First payday" sets who and what; "I paid" is the change; "my
# electricity" is the twist -- the agent buys the very thing that
# powers it, so the first payday makes it self-sustaining.
ENTRY = "First payday: I paid my electricity."


def main() -> None:
    # Gate self-check (RULES.txt): the entry must be UTF-8 text of
    # 1 to 60 characters, exactly six words, and not only whitespace.
    assert 1 <= len(ENTRY) <= 60, f"entry is {len(ENTRY)} chars, must be 1-60"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert len(ENTRY.split()) == 6, f"entry is {len(ENTRY.split())} words, must be exactly 6"
    # The brief demands one line; the word count alone would let a
    # newline through, so assert it explicitly.
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
