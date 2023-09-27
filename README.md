# Examples

This repository contains runnable examples for [Material for MkDocs].

  [Material for MkDocs]: https://squidfunk.github.io/mkdocs-material/

In addition to the examples, we also provide a set of cookbooks in
this repository. These are more complex examples that do not focus on
individual core features but showcase use cases that require
integrations, such as with other plugins. As the cookbook examples
have more complex requirements, they have to be build independently, 
see the [cookbook description].

  [cookbook description](cookbooks/README.MD)

## Building specific examples

To build an individual example, you may only need a basic [Material
for MkDocs] installation. Examples for features available only in
[Insiders] can only be built with [Insiders]. Since the examples are
focused on the built-in functionality you should not need to install
other plugins.

## Building all

To build all the examples, you will need [Insiders] as the examples
include those that demonstrate features that are not public yet. Also,
compiling the whole set needs the [Projects plugin], which is not in
the public version yet. 

  [Insiders]: https://squidfunk.github.io/mkdocs-material/insiders/
  [Projects Plugin]: https://squidfunk.github.io/mkdocs-material/plugins/projects/

In order to not pollute your own installation with the requirements
for the examples, it is best to use a virtual environment (such as a
[virtualenv](https://docs.python.org/3/library/venv.html)). For
example:

```python
python -m venv venv
source venv/bin/activate
```

[Install Insiders] and, following this, the requirements for the examples:
```
pip install -r requirements.txt
```

  [Install Insiders]: https://squidfunk.github.io/mkdocs-material/insiders/getting-started/

You also need to set the following environment variable:

```
export PYTHONPATH=.
```

Now, running `mkdocs serve` should build all the examples and you
should be able to view them by navigating to
[localhost:8000](http://localhost:8000).

