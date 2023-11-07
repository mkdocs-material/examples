# Copyright (c) 2016-2023 Martin Donath <martin.donath@squidfunk.com>
#                         Alex Voss <alex@corealisation.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

import inspect
import logging
import os
import re
import yaml

from glob import iglob
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import File, Files
from mkdocs.structure.pages import Page
from re import Match

# -----------------------------------------------------------------------------
# State
# -----------------------------------------------------------------------------

# Initialize incremental builds
examples = []

# -----------------------------------------------------------------------------
# Hooks
# -----------------------------------------------------------------------------

def on_pre_build(config: MkDocsConfig):
    """
    Populate the module variable examples with the data from all the
    `.example.y(a)ml` files we can find in `examples/`.
    """
    global examples
    examples = []

    # Create archives for each example
    ymlfiles = iglob("examples/*/.example.y*ml", recursive = True)
    for file in ymlfiles:
        with open(file, 'r') as f:
            example = yaml.safe_load(f)['example']
            example['path'] = os.path.dirname(file)
            examples.append(example)
    log.info(f"Found {len(examples)} examples with metadata.")

def on_page_markdown(markdown: str, page, config, files):
    """
    For each markdown page, look for a marker `<!-- index: filter -->` and
    replace it with the list of examples.
    """

    def replace(match: Match):
        rendered = []
        type, args = match.groups()
        args = args.strip()
        if type == "all":
            for example in examples:
                rendered.append(render(example))
            return '\n'.join(rendered)

    log.info(f"looking for index definitions")
    return re.sub(
        r"<!-- index:(\w+)(.*?) -->",
        replace, markdown, flags = re.I | re.M
    )

def render(example: dict) -> str:
    result = f""" <div class="admonition note">
    <div style="float:right;padding-left:1em">{render_tags(example['tags'])}</div>
    <a href="/{example['path']}">
    {example['name']}
    </a>
    </div>""".strip()
    return result

def render_tags(tags: list) -> str:
    return ', '.join(tags)

# -----------------------------------------------------------------------------
# Data
# -----------------------------------------------------------------------------

# Set up logging
log = logging.getLogger("mkdocs.material.examples")
