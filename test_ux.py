import os
import time
from playwright.sync_api import sync_playwright

def test_ux_enhancements():
    html_path = 'file://' + os.path.abspath('index.html')

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(permissions=['clipboard-read', 'clipboard-write'])
        page = context.new_page()
        page.goto(html_path)

        # On init, 1 signal exists. Clear history to test empty state.
        page.keyboard.press('x') # First press triggers confirm
        page.keyboard.press('x') # Second press clears history
        time.sleep(1.2) # Wait for "Cleared!" timeout to reset clear-btn

        # 1. Test X key press when history is empty (clear-btn disabled)
        page.keyboard.press('x')
        time.sleep(0.1)
        announcer_text = page.inner_text('#announcer')
        print('Empty Clear X Announcer:', announcer_text)
        assert 'No signal history to clear' in announcer_text

        # 2. Test ArrowLeft / ArrowRight / Home / End when history track is empty
        empty_notice = page.query_selector('#empty-history-notice')
        if empty_notice:
            empty_notice.focus()
            page.keyboard.press('ArrowLeft')
            time.sleep(0.1)
            announcer_text = page.inner_text('#announcer')
            print('Empty Track ArrowLeft Announcer:', announcer_text)
            assert 'No signal history to navigate' in announcer_text

        # 3. Test R key press and Empty Notice click when network is offline
        context.set_offline(True)
        page.evaluate("window.dispatchEvent(new Event('offline'))")
        time.sleep(0.1)

        page.keyboard.press('r')
        time.sleep(0.1)
        announcer_text = page.inner_text('#announcer')
        print('Offline R Announcer:', announcer_text)
        assert 'Refresh disabled: Network is offline' in announcer_text

        empty_notice_aria = page.get_attribute('#empty-history-notice', 'aria-label')
        empty_notice_title = page.get_attribute('#empty-history-notice', 'title')
        print('Offline Empty Notice ARIA:', empty_notice_aria, '| Title:', empty_notice_title)
        assert empty_notice_aria == 'No signal history yet. Refresh disabled (Offline).'
        assert empty_notice_title == 'Refresh disabled (Offline)'

        page.click('#empty-history-notice')
        time.sleep(0.1)
        announcer_text = page.inner_text('#announcer')
        print('Offline Empty Notice Click Announcer:', announcer_text)
        assert 'Refresh disabled: Network is offline' in announcer_text

        # Restore online state
        context.set_offline(False)
        page.evaluate("window.dispatchEvent(new Event('online'))")
        time.sleep(0.1)

        # 4. Test Shortcuts Guide keycap clicks for disabled states
        page.click('#shortcut-help-btn')
        time.sleep(0.1)

        # Click X keycap in legend box when history is empty
        page.click('#kbd-key-x')
        time.sleep(0.1)
        announcer_text = page.inner_text('#announcer')
        print('Legend Kbd X Announcer:', announcer_text)
        assert 'No signal history to clear' in announcer_text

        # Click Left keycap in legend box when history is empty
        page.click('#kbd-key-left')
        time.sleep(0.1)
        announcer_text = page.inner_text('#announcer')
        print('Legend Kbd Left Announcer:', announcer_text)
        assert 'No signal history to navigate' in announcer_text

        # 5. Test Shortcuts Guide trigger ARIA label and title sync
        help_btn_aria = page.get_attribute('#shortcut-help-btn', 'aria-label')
        help_btn_title = page.get_attribute('#shortcut-help-btn', 'title')
        print('Help Btn Open ARIA:', help_btn_aria, '| Title:', help_btn_title)
        assert help_btn_aria == 'Close Keyboard Shortcuts Guide (Shortcut: ?)'
        assert help_btn_title == 'Close Keyboard Shortcuts Guide (Shortcut: ?)'

        page.click('#close-shortcuts-btn')
        time.sleep(0.1)
        help_btn_aria = page.get_attribute('#shortcut-help-btn', 'aria-label')
        help_btn_title = page.get_attribute('#shortcut-help-btn', 'title')
        print('Help Btn Closed ARIA:', help_btn_aria, '| Title:', help_btn_title)
        assert help_btn_aria == 'Keyboard Shortcuts Guide (Shortcut: ?)'
        assert help_btn_title == 'Shortcut: ?'

        # 6. Test signal display ARIA label update on copy
        signal_aria_before = page.get_attribute('#signal-display', 'aria-label')
        page.click('#signal-display')
        time.sleep(0.1)
        signal_aria_after = page.get_attribute('#signal-display', 'aria-label')
        print('Signal Display ARIA Copy:', signal_aria_after)
        assert signal_aria_after == 'Signal copied to clipboard'

        # Reset copy feedback
        page.keyboard.press('Escape')
        time.sleep(0.1)
        signal_aria_reset = page.get_attribute('#signal-display', 'aria-label')
        print('Signal Display ARIA Reset:', signal_aria_reset)
        assert signal_aria_reset.lower() == signal_aria_before.lower()

        print("ALL UX TESTS PASSED SUCCESSFULLY!")
        browser.close()

if __name__ == '__main__':
    test_ux_enhancements()
