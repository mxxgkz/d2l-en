# Enable Hypothesis Annotations for D2L Book

This guide shows you how to add Hypothesis annotations (highlights + margin notes) to your local D2L book build.

## What is Hypothesis?

Hypothesis is a free, open-source annotation tool that allows you to:
- **Highlight** text on any page
- **Add notes** in the margin
- **Share annotations** with groups
- **Persist annotations** to your Hypothesis account

## Quick Setup (2 minutes)

### Recommended Method: Direct Injection

**This is the most reliable method** because d2lbook regenerates `conf.py` during builds.

```bash
# Step 1: Build the HTML (only needed if you've changed source files)
d2lbook build html

# Step 2: Inject Hypothesis into all HTML files
python inject_hypothesis.py
```

**Note:** You only need to rebuild HTML (`d2lbook build html`) if you've changed the source markdown/RST files. If you're just adding Hypothesis to an existing build, you can skip Step 1 and go straight to Step 2.

### When Do You Need to Rebuild?

You need to rebuild HTML (`d2lbook build html`) when:
- You've modified any `.md` source files
- You've changed `config.ini` settings
- You want fresh HTML output

You **don't** need to rebuild when:
- You're just adding Hypothesis to existing HTML
- You're re-injecting Hypothesis after a previous injection
- The HTML files already exist and are up to date

### Alternative Method: Sphinx Configuration

**Note:** This may not work if d2lbook regenerates `conf.py` during the build.

```bash
# Step 1: Run the setup script (after building RST)
python add_hypothesis.py

# Step 2: Rebuild HTML
d2lbook build html
```

### Step 3: Serve and test

```bash
cd _build/html
python -m http.server 8000
```

**Note:** The server will keep running (this is normal). It's waiting for HTTP requests. To stop it, press `Ctrl+C`.

**To run in background** (so you can use the terminal):
```bash
cd _build/html
python -m http.server 8000 &
# Or use nohup to keep it running after closing terminal:
nohup python -m http.server 8000 > /dev/null 2>&1 &
```

Open `http://localhost:8000` in your browser. You should see the Hypothesis sidebar on the right.

## Why `inject_hypothesis.py` Works But `add_hypothesis.py` Doesn't

### The Problem

The `add_hypothesis.py` script modifies `_build/rst/conf.py` to add:
```python
html_js_files = ['hypothesis.js']
```

However, **`d2lbook build html` regenerates `conf.py`** during the build process, overwriting any manual changes.

### Why This Happens

1. `d2lbook build html` internally runs Sphinx
2. Sphinx reads `conf.py` to configure the build
3. `d2lbook` may regenerate or modify `conf.py` as part of its build process
4. Your `html_js_files` line gets removed
5. Sphinx builds HTML without the Hypothesis script

### The Solution: `inject_hypothesis.py`

The `inject_hypothesis.py` script works because it:

1. **Runs AFTER the build** - It modifies the final HTML files
2. **Bypasses conf.py entirely** - Directly injects script tags into HTML
3. **Can't be overwritten** - The HTML files are the final output

### Why Not Use Sphinx's `html_js_files`?

`html_js_files` is a valid Sphinx configuration option, but:
- It requires the file to exist in `html_static_path`
- It requires `conf.py` to not be regenerated
- With d2lbook, `conf.py` gets regenerated, so it doesn't work

The direct injection method (`inject_hypothesis.py`) is more reliable for this use case.

## How It Works

1. **`static/hypothesis.js`** - Loads the Hypothesis embed script (used by `add_hypothesis.py`)
2. **`add_hypothesis.py`** - Attempts to add `html_js_files = ['hypothesis.js']` to the generated `conf.py` (may be overwritten)
3. **`inject_hypothesis.py`** - Directly injects the Hypothesis script tag into all HTML files (recommended)
4. **Sphinx** - Builds the HTML pages

## Using Hypothesis

### First Time Setup

1. Click the Hypothesis icon (right sidebar) or press `Ctrl+Shift+H` (Windows/Linux) or `Cmd+Shift+H` (Mac)
2. Sign up for a free account at [hypothes.is](https://hypothes.is)
3. Start annotating!

### Features

- **Highlight**: Select text and click "Annotate"
- **Add notes**: Click highlighted text to add margin notes
- **Share**: Create groups to share annotations with others
- **Search**: Find your annotations across all pages
- **Export**: Download your annotations as JSON

## Troubleshooting

### Hypothesis sidebar doesn't appear

1. **Check browser console** (F12 → Console tab) for JavaScript errors

2. **Verify the script is in HTML:**
   ```bash
   grep -i "hypothesis" _build/html/index.html
   ```
   You should see a script tag loading `hypothes.is/embed.js`.

3. **Verify the file exists** (if using `add_hypothesis.py` method):
   ```bash
   ls -la _build/html/_static/hypothesis.js
   ```

4. **Use the reliable method:**
   ```bash
   # If add_hypothesis.py didn't work, use inject_hypothesis.py instead
   python inject_hypothesis.py
   ```

### Script not loading

1. **Check that `static/hypothesis.js` exists** in your source directory
2. **Verify the file was copied** to `_build/html/_static/` (if using Sphinx method)
3. **Use `inject_hypothesis.py`** - This directly injects the script and doesn't rely on file copying

### Quick Fix Steps

If you don't see the Hypothesis sidebar:

1. **Ensure you're in the right directory:**
   ```bash
   cd <dir>/d2l-en
   ```

2. **Inject Hypothesis (no rebuild needed unless source changed):**
   ```bash
   # Only rebuild if you've changed markdown/RST source files
   # d2lbook build html
   
   # Inject Hypothesis into existing HTML files
   python inject_hypothesis.py
   ```

3. **Verify injection worked:**
   ```bash
   grep "hypothes.is/embed.js" _build/html/index.html
   ```

4. **Test in browser:**
   ```bash
   cd _build/html
   python -m http.server 8000
   ```
   Then open `http://localhost:8000` and look for the Hypothesis icon or press `Ctrl+Shift+H`.

## Alternative: Manual Setup

If you prefer to do it manually:

1. After `d2lbook build html`, run:
   ```bash
   python inject_hypothesis.py
   ```

Or if you want to try the Sphinx method (may not work due to conf.py regeneration):

1. After `d2lbook build rst`, edit `_build/rst/conf.py`
2. Find the line: `html_static_path = ['_static']`
3. Add after it:
   ```python
   html_js_files = ['hypothesis.js']
   ```
4. Rebuild: `d2lbook build html`

**Note:** This method may fail because d2lbook regenerates conf.py. Use `inject_hypothesis.py` instead.

## Disabling Hypothesis

To remove Hypothesis from your build:

1. **If using `inject_hypothesis.py`**: Simply don't run it after building
2. **If using `add_hypothesis.py`**: Don't run it, or remove the script tags from HTML files manually
3. **To remove from existing HTML**: Search and replace `hypothes.is/embed.js` script tags in all HTML files

## Notes

- **Static site compatible**: Hypothesis works on fully static HTML sites
- **No backend required**: All annotation data is stored by Hypothesis
- **Privacy**: Users must sign in to Hypothesis to persist annotations
- **Groups**: You can create private groups for sharing annotations with specific people
- **Recommended workflow**: Always use `inject_hypothesis.py` after `d2lbook build html` for reliability
