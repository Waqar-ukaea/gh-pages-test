import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'My Test Docs'
author = 'Your Name'
release = '0.1'

extensions = []
templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'  # Simple built-in Sphinx theme
html_static_path = ['_static']
