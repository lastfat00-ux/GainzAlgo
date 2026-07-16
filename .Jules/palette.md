# Palette Journal
## 2024-06-22 - Tab-Level Visibility & Continuity
**Learning:** Extending status indicators to the favicon (via SVG data URLs) and monitoring network connectivity provides critical "background" awareness, allowing users to monitor volatile data and reliability without keeping the tab in focus.
**Action:** Synchronize tab-level visuals (favicon, title) with primary UI state and connectivity status.

## 2024-06-23 - Smart Re-synchronization
**Learning:** Automatically refreshing stale data upon visibility change or connectivity restoration ensures the UI remains a reliable source of truth without manual user action.
**Action:** Implement automated re-sync for stale data on visibility and online events.

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

## 2026-06-27 - Roving Tabindex & Chronological Sparklines
**Learning:** For sparklines where items are prepended, using `flex-direction: row-reverse` aligns newest items to the right while maintaining intuitive Arrow Key relationships (Left for older, Right for newer). Pairing this with a 'Roving Tabindex' prevents keyboard trap and ensures efficient list navigation.
**Action:** Use `row-reverse` for timelines and implement `tabindex="-1"` on non-focused list items.

## 2026-06-28 - History Persistence & Management
**Learning:** Persisting transient data (like signal history) in `localStorage` provides critical continuity for dashboard users. This must be paired with management controls (Clear button) and empty state feedback to maintain user agency and UI clarity. Focus redirection to a stable element (Refresh) after clearing prevents "focus loss" for keyboard users.
**Action:** Implement `localStorage` for dashboard state and ensure explicit "Clear" actions handle focus and empty states.
