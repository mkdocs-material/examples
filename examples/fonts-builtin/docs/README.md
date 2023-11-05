# Using built-in browser fonts

This example shows what happens when auto-loading of fonts from Google
is turned off and not other fonts are configured:

regular - __bold__ - *italic* - __*bold italic*__ - `code`

You can inspect which fonts are actually used by your browser by using
the built-in web developer tools (available at least in Chrome, Firefox,
Safari, Edge) and choosing the fonts view. Try this with multiple
browsers and compare the results to see if using only built-in fonts
is an option for you.

## How it works

Turn off the default use of Roboto fonts loaded from Google Fonts in
your `mkdocs.ym`:

```
theme:
  font: false
```

The fonts used are those that are built into the web browser.
Material for MkDocs provides sensible defaults that should work in all
common browsers. 

## (Dis-)Advantages

Turning off Google Fonts means that your website will not cause
browsers to make any font requests to Google, improving privacy.
It also improves performance and network traffic, though browser
caching means the advantages over fonts hosted on CDNs is small.

The downside is that you lose some control over the visual appearance
of your website as different browsers will choose different fonts.

## Alternatives

An alternative is to turn off the use of Roboto from Google Fonts and
then [configure custom fonts to use], as shown in [this example that shows
how to switch to the Noto font family].

[configure custom fonts to use]: https://squidfunk.github.io/mkdocs-material/setup/changing-the-fonts/#additional-fonts
[this example that shows how to switch to the Noto font family]: ../fonts-custom
