# Palette Journal

## 2024-06-04 - Signal Momentum
**Learning:** Including numeric deltas (e.g., +2%) alongside trend icons reduces cognitive load by quantifying the change without requiring users to recall previous values.
**Action:** Always provide magnitude context for real-time data updates.

## 2024-06-04 - Interactive Icon Feedback
**Learning:** Swapping icons (e.g., 📋 to ✅) during transient states provides a stronger visual confirmation of success than label changes alone.
**Action:** Use icon transitions for fire-and-forget actions like copying.

## 2026-06-05 - Relative Data Freshness
**Learning:** High-volatility dashboards should use a 1-second granularity for relative timestamps (e.g., 'Updated 5s ago') via `setInterval` to maintain a persistent sense of 'liveness' and data freshness.
**Action:** Implement 1-second intervals for data-critical timestamps.

## 2026-06-06 - Animated Confidence Counters
**Learning:** Implement numeric counters for volatile percentages to provide smooth visual continuity during data refreshes, ensuring animations respect `prefers-reduced-motion` settings.
**Action:** Use requestAnimationFrame for numeric transitions while checking media queries.

## 2026-06-08 - Interactive Data Displays
**Learning:** Making central data displays focusable (`tabindex="0"`) and interactive (e.g., clickable for copying) with appropriate `cursor: pointer` and hover/focus styles improves discoverability for both mouse and keyboard users.
**Action:** Always consider if primary information nodes can serve as direct interaction points.

## 2026-06-09 - Semantic Keyboard Shortcut Hints
**Learning:** Using semantic `<kbd>` elements with 'physical key' CSS styling (e.g., background, border, box-shadow) provides clear visual affordance and semantic clarity for keyboard shortcut hints within buttons.
**Action:** Replace plain text shortcut hints with styled `<kbd>` elements.

## 2024-06-10 - Qualitative Signal Emphases
**Learning:** High-confidence data states (e.g., confidence >= 85%) can be visually emphasized with a subtle `glow` (via `text-shadow: 0 0 12px currentColor`) to provide non-textual qualitative feedback alongside icons.
**Action:** Apply visual glow effects to primary data points when specific confidence thresholds are met to improve qualitative scanning.
