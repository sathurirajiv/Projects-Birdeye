---
description: Switch the email editor prototype between light and dark mode
---

Toggle the theme of the email editor prototype between light and dark mode.

**File locations:**
- Source: `/Users/rajivsurya/Documents/email-editor/index.html`
- Preview (served): `/tmp/email-preview/index.html`

**Steps:**

1. Read the `<html>` tag in `/Users/rajivsurya/Documents/email-editor/index.html` to check the current `data-theme` attribute.

2. Determine the target theme:
   - If `data-theme="dark"` is present → switch to **light** (remove the attribute or set `data-theme="light"`)
   - If `data-theme` is absent or `"light"` → switch to **dark** (set `data-theme="dark"`)

3. Edit the `<html lang="en">` tag accordingly:
   - Light mode: `<html lang="en">`
   - Dark mode:  `<html lang="en" data-theme="dark">`

4. Copy the updated file to `/tmp/email-preview/index.html` using:
   ```
   cp /Users/rajivsurya/Documents/email-editor/index.html /tmp/email-preview/index.html
   ```

5. Reload the preview with `window.location.reload()` via the preview tool if available.

6. Tell the user which mode is now active and confirm the change was applied.

**Note:** The in-browser toggle button (sun/moon icon at the bottom of the left rail) also switches themes at runtime and persists the preference to `localStorage`. This skill sets the *default* theme that loads on first visit or hard reload.
