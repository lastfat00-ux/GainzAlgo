# Palette Journal
## 2024-06-08 - Interaction & Semantics
**Learning:** Making data nodes focusable/clickable and using `<kbd>` for shortcut hints improves discoverability and semantic clarity.
**Action:** Treat primary info as interaction points with styled shortcut hints.
## 2024-06-10 - Qualitative & Traceability
**Learning:** Subtle glows for high-confidence states and timestamps in copied data improve qualitative scanning and temporal traceability.
**Action:** Apply visual emphasis for thresholds and include time context in clipboard.
## 2024-06-12 - Tab-Level Status Feedback
**Learning:** Using the document title for transient feedback (e.g., '✅ Copied!') and persistent context (e.g., momentum deltas) provides a low-friction confirmation for power users and keyboard shortcut enthusiasts without interrupting the visual flow.
**Action:** Use document.title for high-value status updates and action confirmations.
## 2024-06-15 - Dark Theme Contrast
**Learning:** In dark-themed interfaces (e.g., background `#1e293b`), standard 500/600-level colors often fail WCAG AA contrast (ratio < 4.5:1). Shifting to 400-level shades and using dark text on primary buttons ensures accessibility without sacrificing the dark aesthetic.
**Action:** Always verify contrast against dark containers and prefer lighter shades for text-heavy indicators.

## 2024-06-18 - Temporal Context & Staleness
**Learning:** Global dashboards benefit from dual-time tooltips (Local + UTC) for traceability. Visual "Stale" indicators for data older than a threshold (e.g., 2m) prevent user reliance on outdated signals.
**Action:** Include UTC context in timestamps and implement explicit staleness warnings.

## 2024-06-19 - Async State Protection
**Learning:** Concurrent async UI updates (e.g., feedback timeouts vs. data refreshes) can corrupt icon states. Clearing transient timeouts during data refreshes ensures the UI always accurately reflects the latest source of truth.
**Action:** Use persistent handles to clear transient feedback states upon source data updates.

## 2024-06-20 - Multi-Modal Loading Feedback
**Learning:** Async transitions benefit from synchronized visual and state resets. Applying a loading overlay while clearing transient feedback (e.g., 'Copied' states) prevents cognitive dissonance during data refreshes.
**Action:** Implement global loading classes and immediate state resets for async operations.

## 2024-06-21 - Skeleton Shimmer & Perceived Performance
**Learning:** Skeleton shimmer animations (via CSS pseudo-elements) provide a more dynamic and "active" feel than static opacity changes during async transitions, reducing perceived wait time.
**Action:** Use CSS-only shimmer gradients to enhance loading states while respecting motion preferences.

## 2024-06-22 - Tab-Level Visibility & Continuity
**Learning:** Extending status indicators to the favicon (via SVG data URLs) and monitoring network connectivity provides critical "background" awareness, allowing users to monitor volatile data and reliability without keeping the tab in focus.
**Action:** Synchronize tab-level visuals (favicon, title) with primary UI state and connectivity status.
