#!/usr/bin/env python3
"""
Alternative method: Directly inject Hypothesis script into all HTML files.

Use this if the Sphinx html_js_files method doesn't work.

Usage:
    d2lbook build html
    python inject_hypothesis.py
"""

import os
import re

HTML_DIR = '_build/html'
SCRIPT_TAG = '<script src="https://hypothes.is/embed.js" async></script>'

def inject_hypothesis():
    """Inject Hypothesis script tag into all HTML files."""
    
    if not os.path.exists(HTML_DIR):
        print(f"Error: {HTML_DIR} not found. Run 'd2lbook build html' first.")
        return False
    
    count = 0
    for root, dirs, files in os.walk(HTML_DIR):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Skip if already injected
                    if 'hypothes.is/embed.js' in content:
                        continue
                    
                    # Add before closing </body> tag
                    if '</body>' in content:
                        content = content.replace('</body>', f'{SCRIPT_TAG}\n</body>')
                        count += 1
                    # Or add before closing </head> tag if no body
                    elif '</head>' in content:
                        content = content.replace('</head>', f'{SCRIPT_TAG}\n</head>')
                        count += 1
                    else:
                        continue
                    
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                        
                except Exception as e:
                    print(f"Warning: Could not process {filepath}: {e}")
    
    if count > 0:
        print(f"✓ Injected Hypothesis script into {count} HTML files")
        return True
    else:
        print("No files modified (Hypothesis may already be present)")
        return False

if __name__ == '__main__':
    inject_hypothesis()

