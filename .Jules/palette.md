# Palette Journal - GainzAlgo

## 2025-04-25 - Reliable Navigation and Accessible Emojis
**Learning:** Standard Markdown heading IDs are inconsistent when headings contain HTML/emoji spans, and raw emojis are not accessible to screen readers.
**Action:** Use explicit HTML anchors (`<a id="anchor-name"></a>`) for headings and wrap emojis in `<span role="img" aria-label="...">` to ensure accessibility and reliable internal navigation.

## 2025-04-25 - Avoid Placeholder Documentation
**Learning:** Documentation must accurately reflect the repository's state; including illustrative or "placeholder" commands is confusing for developers.
**Action:** Only document features or commands that actually exist in the codebase.
