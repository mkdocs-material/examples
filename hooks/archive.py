# Copyright (c) 2016-2025 Martin Donath <martin.donath@squidfunk.com>

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

import logging
import os

from glob import iglob
from mkdocs.config.defaults import MkDocsConfig
from pathspec.gitignore import GitIgnoreSpec
from zipfile import ZipFile, ZIP_DEFLATED

# -----------------------------------------------------------------------------
# State
# -----------------------------------------------------------------------------

# Initialize incremental builds
is_serve = False

# -----------------------------------------------------------------------------
# Hooks
# -----------------------------------------------------------------------------

# Determine whether we're serving the site
def on_startup(command, dirty):
    global is_serve
    is_serve = command == "serve"

# Create archives for all examples
def on_post_build(config: MkDocsConfig):
    if is_serve:
        return

    # Read files to ignore from .gitignore
    with open(".gitignore") as f:
        spec = GitIgnoreSpec.from_lines([
            line for line in f.read().split("\n")
                if line and not line.startswith("#")
        ])

    # Create archives for each example
    for file in iglob("examples/*/mkdocs.yml", recursive = True):
        base = os.path.dirname(file)

        # Compute archive name and path
        example = os.path.basename(base)
        archive = os.path.join(config.site_dir, f"{example}.zip")

        # Start archive creation
        log.info(f"Creating archive '{example}.zip'")
        with ZipFile(archive, "w", ZIP_DEFLATED, False) as f:
            for name in spec.match_files(os.listdir(base), negate = True):
                path = os.path.join(base, name)
                if os.path.isdir(path):
                    path = os.path.join(path, "**")

                # Find all files recursively and add them to the archive
                for file in iglob(path, recursive = True, include_hidden = True):
                    log.debug(f"+ '{file}'")
                    f.write(file, os.path.join(
                        example, os.path.relpath(file, base)
                    ))

# -----------------------------------------------------------------------------
# Data
# -----------------------------------------------------------------------------

# Set up logging
log = logging.getLogger("mkdocs.material.examples")
