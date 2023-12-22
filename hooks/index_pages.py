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

"""
Hook for building an index of examples in `examples/` by parsing the 
`README.md` files for metadata, both from the Markdown header and the
Markdown itself.
"""

import logging
import os
from glob import iglob

import yaml
from mkdocs.config.defaults import MkDocsConfig

# -----------------------------------------------------------------------------
# State
# -----------------------------------------------------------------------------

# pre-defined structure for the tag filters.
tags = [
    ["public", "insiders", "integration"],
    ["colors", "fonts", "icons", "page_status"],
    ["blog", "group", "info", "meta", "offline", "optimize", \
     "privacy", "projects", "search", "social", "tags", "typeset"]
]

# The list of examples.
examples = []

def on_pre_build(config: MkDocsConfig):
    """
    Populate the module variables examples and tags with the data from all 
    the `.example.y(a)ml` files we can find in `examples/`.
    """

    if len(examples) > 0:
        examples.clear()

    readmes = iglob("examples/*/docs/README.md", recursive = True)
    for file in readmes:
        example = read_header(file)
        example['path'] = os.path.dirname(file)
        examples.append(example)
    log.info("Found %d examples with metadata.", len(examples))

def read_header(file) -> dict:
    """
    Read the YAML header from a Markdown file (or the first document from 
    a multi-document yaml file) by scanning for the separator lines ('---').
    If the metadata do not specify a name for the example, the markdown is 
    scanned for a top-level heading.

    Limitation: currently assumes there *is* a markdown header, so files
    without one will fail to parse, resulting in a message on the log and
    an example object that contains an error message.
    """
    header = []
    with open(file, 'r', encoding='utf-8') as fd:
        line = fd.readline()
        if line == '---\n': # found a markdown yaml header
            example = read_yaml_header(file, header, fd)
        else: # found plain Markdown file
            example = {}
        if not 'name' in example:
            example['name'] = read_first_markdown_heading(line, fd)
        return example

def read_yaml_header(file, header, fd):
    """
    Read the YAML header from `fd`, scanning up to the second separating
    line and using `yaml.safe_load()` to do the parsing.
    """
    line = fd.readline()
    while line not in ("---\n", ""):
        header.append(line)
        line = fd.readline()
    try:
        example = yaml.safe_load("".join(header))
    except yaml.error.YAMLError as err:
        log.warning("could not read Markdown header in: %s - error: %s", file, str(err))
        example = {"name": "failed to parse"}
    return example

def read_first_markdown_heading(line, fd) -> str:
    """
    After reading the YAML header, scan the Markdown for a first-level
    heading, indicated by '# ' as the first non-whitespace characters.
    """
    while not line.startswith('# '):
        if line == '':
            return 'no name'
        line = fd.readline()
    return line.removeprefix('# ')

def on_page_context(context, *, page, config, nav):
    """
    Put the data collected into the rendering context so the data are 
    available to the template.
    """
    context["exampletags"] = tags
    context["examples"] = examples

# Set up logging
log = logging.getLogger("mkdocs.material.examples")
