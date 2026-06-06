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
