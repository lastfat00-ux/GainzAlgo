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
