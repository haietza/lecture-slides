# Lecture Slides

This repository contains lecture slides built with [Reveal.js](https://revealjs.com/) and hosted via GitHub Pages.

---

## Repository Structure

```
/
├── reveal-js/          # Reveal.js library files (local copy)
│   ├── dist/           # Core CSS and JS — the only folder needed from a release
│   └── plugin/         # Official plugins (highlight, notes, markdown, math)
├── layouts/
│   └── common.css      # Shared styles across all decks
├── other/              # Other files
├── course-01/          # One folder per course
│   ├── index.html
│   └── custom.css
├── course-02/
│   ├── index.html
│   └── custom.css
└── README.md
```

> **Note:** Only the `dist/` and `plugin/` folders are needed from a Reveal.js release.
> Do not copy the full repository — it contains build tools, source files, and examples
> that are not needed here.

---

## GitHub Pages Deployment

Slides are served as a static site via GitHub Pages directly from the `main` branch.

### Initial Setup (one time)

1. Go to the repository on GitHub.
2. Navigate to **Settings → Pages**.
3. Under **Source**, select **Deploy from a branch**.
4. Set the branch to `main` and the folder to `/ (root)`.
5. Click **Save**.

GitHub will provide a URL in the format:
```
https://<org-or-username>.github.io/<repo-name>/
```

### Deploying Updates

There is no separate deploy step. Every push to `main` automatically triggers a
GitHub Pages rebuild. Allow 1–2 minutes for changes to go live.

To verify the deployment status:
- Go to **Actions** tab in the repository.
- Look for the most recent **pages-build-deployment** workflow run.

### Linking to a Specific Course

Each lecture deck is accessible at:
```
https://<org-or-username>.github.io/<repo-name>/course-01/
```

---

## Updating Reveal.js

Reveal.js is vendored locally in the `reveal-js/` folder. It is **not** a git submodule.
To update to a new version:

1. Download the release zip from:
   https://github.com/hakimel/reveal.js/releases

2. Extract the zip. You only need **two folders**:
   - `dist/`
   - `plugin/`

3. Delete the existing contents of `reveal-js/dist/` and `reveal-js/plugin/`.

4. Copy the new `dist/` and `plugin/` folders into `reveal-js/`.

5. Commit and push:
   ```bash
   git add reveal-js/
   git commit -m "Update Reveal.js to vX.X.X"
   git push
   ```

6. Verify slides still render correctly at the GitHub Pages URL.

> **Current version:** 6.0.1
> **Last updated:** May 2025

### Watch Out For Breaking Changes

Reveal.js occasionally changes plugin paths or CSS structure between major versions.
Before updating, check the release notes at:
https://github.com/hakimel/reveal.js/releases

If slides break after an update, the most common culprits are:
- Plugin script paths in `index.html`
- CSS `<link>` paths in `index.html`

---

## Adding a New Course

1. Copy an existing course folder (e.g. `course-01/`) and rename it.
2. Edit `index.html` — slide content lives inside:
   ```html
   <div class="slides">
     <section>Your slide content here</section>
   </div>
   ```
3. Update `custom.css` for any lecture-specific styles.
4. Commit and push. The new deck will be live at its folder path automatically.

---

## Local Preview

Opening `index.html` directly in a browser works for most slides. However, if a deck
uses **external Markdown files**, a local web server is required:

```bash
# From the repo root, using Python (available on most systems):
python3 -m http.server 8000
```

Then open `http://localhost:8000/course-01/` in your browser.