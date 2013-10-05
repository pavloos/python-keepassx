# -*- coding: utf-8 -*-
#
# keepassx documentation build configuration file, created by
# sphinx-quickstart on Sat Jan  5 19:54:29 2013.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os
import guzzle_sphinx_theme

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'keepassx'
copyright = u'2013, James Saryerwinnie'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.1'
# The full version, including alpha/beta/rc tags.
release = '0.1'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'guzzle_sphinx_theme.GuzzleStyle'


# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# Adds an HTML table visitor to apply Bootstrap table classes
html_translator_class = 'guzzle_sphinx_theme.HTMLTranslator'
html_theme_path = guzzle_sphinx_theme.html_theme_path()
html_theme = 'guzzle_sphinx_theme'
extensions.append("guzzle_sphinx_theme")


html_static_path = ['_static']

# Output file base name for HTML help builder.
htmlhelp_basename = 'keepassxdoc'

# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'keepassx', u'keepassx Documentation',
     [u'James Saryerwinnie'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False

# Guzzle theme options (see theme.conf for more information)
html_theme_options = {

    # Set the path to a special layout to include for the homepage
    #"index_template": "special_index.html",

    # Set the name of the project to appear in the nav menu
    "project_nav_name": "python-keepassx",

    # Set your GitHub user and repo to enable GitHub stars links
    "github_user": "jamesls",
    "github_repo": "python-keepassx",

    # Set your Disqus short name to enable comments
    #"disqus_comments_shortname": "my_disqus_comments_short_name",

    # Set you GA account ID to enable tracking
    "google_analytics_account": "UA-28869503-3",

    # Set a custom class to add to the navbar (e.g. navbar-inverse)
    "navbar_class": "",

    # Path to a touch icon
    "touch_icon": "",

    # Set to true to bind left and right key events to turn the page
    "bind_key_events": True,

    # Specify a base_url used to generate sitemap.xml links. If not
    # specified, then no sitemap will be built.
    "base_url": "http://keepassx.readthedocs.org/en/latest/"
}
