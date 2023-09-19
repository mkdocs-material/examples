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

from glob import iglob
from mkdocs.config.defaults import MkDocsConfig
from zipfile import ZipFile, ZIP_DEFLATED

# -----------------------------------------------------------------------------
# Hooks
# -----------------------------------------------------------------------------

# Create an archive
def on_pre_build(config: MkDocsConfig):
    base = os.path.dirname(config.config_file_path)
    project_name = os.path.basename(base)

    archive = f"docs/download/{project_name}.zip"
    os.makedirs(os.path.dirname(archive), exist_ok = True)
    with ZipFile(archive, "w", ZIP_DEFLATED, False) as f:
        for name in os.listdir(base):
            # @todo: load ignore patterns from .gitignore
            if name == "site":
                continue

            # Find all files recursively and add them to the archive
            path = os.path.join(base, name)
            if os.path.isdir(path):
                path = os.path.join(path, "**")

            # @todo
            for file in iglob(path, recursive = True):
                f.write(
                    file,
                    os.path.join(project_name, os.path.relpath(file, base))
                )

#
def on_page_markdown(markdown, *, page, config, files):
    if page.file.src_uri == "README.md":
        page.meta["title"] = "Overview"
