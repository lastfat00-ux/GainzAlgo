
## 2026-06-20 - Threshold Visual Cues & Animation Sync
**Learning:** Adding explicit visual markers for qualitative boundaries (like "Strong" thresholds) in progress bars reduces cognitive load for scanning data. Synchronizing CSS transitions with JavaScript numeric counters prevents visual jitter during data updates.
**Action:** Use absolute-positioned markers in meters and align CSS durations with JS intervals.

## 2024-06-24 - Multi-Surface Ambient Awareness
**Learning:** Ambient staleness awareness is most effective when synchronized across multiple surfaces (favicon, title, status badge). Using `!important` in CSS status classes ensures theme consistency even when elements have inline-styled colors.
**Action:** Synchronize tab-level and in-page status indicators to provide high-confidence feedback on data freshness.

## 2024-06-25 - Signal History for Temporal Context
**Learning:** A Signal History track (visualized via colored pips) provides immediate temporal context for real-time dashboards, allowing users to verify trends and model stability at a glance without complex charts.
**Action:** Implement low-fidelity history tracks using opacity-scaled pips to show signal strength over time.

## 2024-06-26 - Sparkline Visualizations for High-Density Trends
**Learning:** Transforming static history pips into a sparkline (by using proportional heights and dashed threshold lines) significantly improves the scannability of trends and qualitative shifts without increasing the UI footprint.
**Action:** Use CSS flex-end alignment and dynamic height mapping to create compact, informative sparklines.

## 2026-03-05 - Visual Labels for Abstract Charts
**Learning:** Abstract visualizations like history tracks or sparklines can be ambiguous for new users. Adding high-contrast, compact labels (e.g., uppercase "HISTORY") provides immediate context without cluttering the UI.
**Action:** Label abstract data tracks with concise, uppercase text to improve scannability.

## 2026-07-02 - Correcting Chronology in Dynamic Sparklines
**Learning:** For sparklines where new items are prepended, using `flex-direction: row-reverse` visually aligns newest data to the right and intuitively maps Arrow Keys to data age (ArrowLeft for older).
**Action:** Use row-reverse for chronological sparklines to align visual and keyboard navigation.

## 2026-07-03 - Continuity for Destructive UI Actions
**Learning:** Clearing focused items (like history pips) causes "focus loss". Programmatically redirecting focus to a persistent element (like "Refresh") ensures keyboard continuity.
**Action:** Always provide a focus fallback for actions that destroy the current focus target.
