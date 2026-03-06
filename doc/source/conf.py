import os
import sys

# Add the project root to Python path
sys.path.insert(0, os.path.abspath('./../../sgpykit'))  # Points to /sgpykit/

import sgpykit as sg
print(f"Reading from sgpykit code version: {sg.__version__}")


autodoc_mock_imports = ["logging"]  # Mock logging to avoid deep introspection
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'show-inheritance': True,
    'exclude-members': '__weakref__, __dict__, __module__',  # Skip common logging attributes
}

# Extensions
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.viewcode',
    'numpydoc',
]

# Tell autosummary to use fully qualified names (e.g., sgpykit.main)
autosummary_generate = True
autosummary_imported_members = True  # Include submodules

html_theme = 'sphinx_rtd_theme'  # Optional: Use RTD theme

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'sgpykit'
copyright = '2026, sgpykit'
author = 'Matthias Werner et al.'
release = f"{sg.__version__}"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

#extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
#html_static_path = ['_static']
