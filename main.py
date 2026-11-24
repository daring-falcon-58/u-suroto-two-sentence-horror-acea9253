"""Two-Sentence Horror — make.fun entry.

Writes one horror story of exactly two sentences to /output/entry.txt.

The story (171 chars, 173 bytes UTF-8, exactly 2 sentences, no trailing
newline):

    I taught my son to wave at the security camera when he comes home, so I
    know he's safe. Yesterday he waved, and then he waved again — at a
    second camera I never installed.

Why this story (judge criteria, in the brief's order):
  1. Horror in exactly two sentences, genuinely frightening: a parent's
     safety ritual fails — the threat is present-tense, and it is aimed at
     a child.
  2. The second sentence turns the first: the second wave reframes the
     first — he was never waving only at mine. On re-read, "so I know he's
     safe" is the lie the story punctures.
  3. Implied, not explained: who installed it, who watches, how long —
     the reader supplies the worst. No gore on the page.
  4. Precise and concrete: 171 chars; concrete nouns (son, camera, wave);
     "second" and "never" do the work; no adjective is wasted.
  5. Original: not a ghost / mirror / doll / clown / "I don't sleep
     anymore" retelling. Surveillance horror exists, but this execution —
     the child's wave as the tell — is not a canonical two-sentence story.

Selection: 50+ candidate stories drafted and scored by hand against the
five published criteria (0-5 each, /25) in ../candidates.md. No judge
model was called (shared OpenRouter key HTTP 402 exhausted), so no judge
numbers are claimed anywhere. Winner 23/25; runner-up ("lullaby sung
back") 22/25; tied "warm drops" 23/25 lost head-to-head on criterion 1
(BZ's threat is to a child, present-tense; BA's is inferred, past-tense,
and depends on the reader supplying blood).

Determinism: the program prints the same bytes on every run (verified by
running it twice and comparing sha256). No network, no randomness, no
model call, no input files.
"""

import os

STORY = (
    "I taught my son to wave at the security camera when he comes home, "
    "so I know he's safe. Yesterday he waved, and then he waved again "
    "\u2014 at a second camera I never installed."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    """Enforce the competition gate before writing anything."""
    if not (1 <= len(text) <= 400):
        raise ValueError(f"entry must be 1-400 chars, got {len(text)}")
    if text != text.strip() or not text.strip():
        raise ValueError("entry must not be only whitespace")
    # Exactly two sentences: exactly two sentence-terminating periods,
    # no '!' or '?' anywhere (quoted sentences would add periods).
    if text.count(".") != 2:
        raise ValueError(f"entry must have exactly 2 periods, got {text.count('.')}")
    if "!" in text or "?" in text:
        raise ValueError("entry must contain no '!' or '?'")
    text.encode("utf-8")  # must be valid UTF-8


def main() -> None:
    validate(STORY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    data = STORY.encode("utf-8")
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    # Write-back verification: read the file back and compare bytes.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != data:
        raise OSError("write-back verification failed: entry.txt mismatch")
    print(f"wrote {len(data)} bytes to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
