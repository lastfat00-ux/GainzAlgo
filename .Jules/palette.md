# Palette Journal
## 2026-05-21 - Dual-Encoding for Financial Signals
**Learning:** Color alone is insufficient for critical signals. Using icons (▲/▼) + color + ARIA labels ensures clarity for color-blind users and screen readers.
**Action:** Use icons, color, and ARIA for status indicators.

## 2026-05-21 - Power-User Accessibility via Shortcuts
**Learning:** Keyboard shortcuts (e.g., 'R' for refresh) significantly improve accessibility for power users and those with motor impairments. Visual hints (e.g., [R]) are essential for discoverability.
**Action:** Implement keyboard shortcuts with clear visual indicators for primary actions.

## 2026-05-21 - Dynamic Accessibility Feedback
**Learning:** Replacing page reloads with async updates requires manual management of ARIA attributes like `aria-valuenow` and button `aria-label` to keep the screen reader state in sync with visual changes.
**Action:** Always update relevant ARIA attributes alongside DOM/content updates in async workflows.

## 2026-05-21 - At-a-Glance Status Updates
**Learning:** Updating the document title and using color-coded confidence tiers (e.g., 'Strong' vs 'Moderate') provides immediate, low-friction feedback that helps users assess signal reliability without deep focus.
**Action:** Use tab titles for real-time status and implement semantic color tiers for numeric metrics.

## 2026-05-21 - Visual Momentum via Trend Indicators
**Learning:** Providing historical context (e.g., whether confidence is increasing or decreasing) via trend indicators (↑/↓) adds 'momentum' context that helps users make faster decisions in high-stakes environments like trading dashboards.
**Action:** Implement trend indicators for volatile metrics to provide historical context at a glance.

## 2026-05-21 - Targeted DOM Updates for Performance
**Learning:** Using `textContent` and targeted element updates (e.g., `span` for icons) is superior to `innerHTML` for micro-UX updates. It reduces XSS risks and avoids unnecessary re-parsing of entire HTML strings.
**Action:** Use specific ID-based element updates for dynamic content changes instead of rewriting large HTML blocks.

## 2026-05-21 - Transient Feedback for Non-Persistent Actions
**Learning:** For actions like 'Copy to Clipboard', providing immediate but transient visual and ARIA feedback (e.g., 'Copied!' for 2 seconds) reduces user uncertainty without cluttering the UI with permanent status messages.
**Action:** Implement transient success states (text/icon/ARIA) for clipboard and similar fire-and-forget interactions.
