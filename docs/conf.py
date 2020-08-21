import datetime
import os
import sys

import pkg_resources

sys.path.insert(0, os.path.abspath('../'))
master_doc = 'index'
project = 'topological'
release = version = pkg_resources.get_distribution(project).version
copyright = '{}, AWeber Communications'.format(datetime.date.today().year)

html_theme = 'sphinx_rtd_theme'
html_theme_path = ['_themes']

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx_autodoc_typehints',
    'sphinx.ext.viewcode'
]

set_type_checking_flag = True
typehints_fully_qualified = True
always_document_param_types = True
typehints_document_rtype = True

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None)
}

autodoc_default_options = {'autodoc_typehints': 'description'}
