# Copyright (c) 2016-2023 Martin Donath <martin.donath@squidfunk.com>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

import os
import posixpath

from mergedeep import merge
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.exceptions import  ConfigurationError

# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------

# Transform project configuration
def transform(project: MkDocsConfig, config: MkDocsConfig):
    base = os.path.dirname(project.config_file_path)
    name = os.path.basename(base)

    # Determine path of examples relative to root
    root = os.path.dirname(config.config_file_path)
    path = os.path.relpath(base, root)

    # Inherit settings for repository
    project.repo_name = config.repo_name
    project.repo_url  = f"{config.repo_url}/tree/master/{path}"

    # Inherit settings for site URL and edit URI
    project.site_url = posixpath.join(config.site_url, name, "")
    project.edit_uri = f"edit/master/examples/{name}/docs/"

    # Inherit settings for copyright
    project.copyright = config.copyright

    # check that a theme has been defined and we are not running with the default theme
    if project.theme == "mkdocs":
        raise ConfigurationError("Material is not defined as a theme, add it to mkdocs.yml")

    # Inherit settings for theme
    if project.theme and "features" in project.theme:
        project.theme["features"].extend(config.theme["features"])
    else:
        project.theme["features"] = config.theme["features"]

    if project.theme and "icon" in project.theme:
        merge(project.theme["icon"], config.theme["icon"])
    else:
        project.theme["icon"] = config.theme["icon"]
