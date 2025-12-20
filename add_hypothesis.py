#!/usr/bin/env python3
"""
Add Hypothesis annotations to the D2L book HTML build.

NOTE: This script may not work reliably because d2lbook regenerates conf.py
during the build process. Use inject_hypothesis.py instead (recommended).

This script modifies the generated Sphinx conf.py to include Hypothesis.js
for collaborative annotation on all pages.

Usage:
    python add_hypothesis.py

Run this after 'd2lbook build rst' and before 'd2lbook build html'

However, if d2lbook regenerates conf.py, use inject_hypothesis.py instead.
"""

import os
import re
import shutil

CONF_PY_PATH = '_build/rst/conf.py'
HYPOTHESIS_JS_SOURCE = 'static/hypothesis.js'
HYPOTHESIS_JS_TARGET = '_build/rst/_static/hypothesis.js'

def add_hypothesis_to_conf():
    """Add Hypothesis JavaScript to the Sphinx configuration."""
    
    if not os.path.exists(CONF_PY_PATH):
        print(f"Error: {CONF_PY_PATH} not found. Run 'd2lbook build rst' first.")
        return False
    
    # Copy hypothesis.js to _static directory
    if os.path.exists(HYPOTHESIS_JS_SOURCE):
        os.makedirs(os.path.dirname(HYPOTHESIS_JS_TARGET), exist_ok=True)
        shutil.copy2(HYPOTHESIS_JS_SOURCE, HYPOTHESIS_JS_TARGET)
        print(f"✓ Copied {HYPOTHESIS_JS_SOURCE} to {HYPOTHESIS_JS_TARGET}")
    else:
        print(f"Warning: {HYPOTHESIS_JS_SOURCE} not found")
    
    with open(CONF_PY_PATH, 'r') as f:
        content = f.read()
    
    # Check if Hypothesis is already added
    if 'hypothesis.js' in content:
        print("Hypothesis is already configured in conf.py")
        return True
    
    # Find html_static_path line and add html_js_files after it
    pattern = r"(html_static_path\s*=\s*\[['\"].*['\"]\])"
    
    if re.search(pattern, content):
        # Add html_js_files right after html_static_path
        replacement = r"\1\n\n# Hypothesis annotations\nhtml_js_files = ['hypothesis.js']"
        content = re.sub(pattern, replacement, content)
        
        with open(CONF_PY_PATH, 'w') as f:
            f.write(content)
        
        print("✓ Added Hypothesis to conf.py")
        print("  Rebuild HTML with: d2lbook build html")
        return True
    else:
        print("Warning: Could not find html_static_path in conf.py")
        print("Manually add this line to conf.py:")
        print("  html_js_files = ['hypothesis.js']")
        return False

if __name__ == '__main__':
    add_hypothesis_to_conf()

