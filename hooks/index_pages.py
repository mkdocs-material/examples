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

import logging
import os
from glob import iglob

import yaml
from mkdocs.config.defaults import MkDocsConfig

# -----------------------------------------------------------------------------
# State
# -----------------------------------------------------------------------------

# pre-defined structure for the tag filters.
# TODO: perhaps use tags plugin or tag definition in mkdocs.yml???
tags = [
    ["public", "insiders", "simple", "integration"],
    ["colors", "fonts"],
    ["blog", "group", "info", "meta", "offline", "optimize", \
     "privacy", "projects", "search", "social", "tags", "typeset"]
]

# The list of examples.
examples = []

def on_pre_build(_: MkDocsConfig):
    """
    Populate the module variables examples and tags with the data from all 
    the `.example.y(a)ml` files we can find in `examples/`.
    """

    if len(examples) > 0:
        examples.clear()

    ymlfiles = iglob("examples/*/.example.y*ml", recursive = True)
    for file in ymlfiles:
        with open(file, 'r', encoding='utf-8') as f:
            example = yaml.safe_load(f)['example']
            example['path'] = os.path.dirname(file)
            examples.append(example)
    log.info("Found %d examples with metadata.", len(examples))


def on_page_context(context, *, page, config, nav):
    """
    Put the data collected into the rendering context so the data are 
    available to the template.
    """
    context["exampletags"] = tags
    context["examples"] = examples

# Set up logging
log = logging.getLogger("mkdocs.material.examples")
