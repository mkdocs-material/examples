# Auto-loading fonts from Google Fonts

This example shows how you can automatically load fonts from Google Fonts by
simply choosing the font family in your configuration file. This example
uses Ubuntu for text and Ubuntu Mono for code.

regular - __bold__ - *italic* - __*bold italic*__ - `code`

You can inspect which fonts are actually used by your browser by using
the built-in web developer tools (available at least in Chrome, Firefox,
Safari, Edge) and choosing the fonts view. 

## How it works

To replace the default font Roboto, specify the Ubuntu font or a font of your
choosing in your `mkdocs.yml`:

```yaml
theme:
  font: 
    text: Ubuntu
    code: Ubuntu Mono
```

## (Dis-)advantages

When you use Google Fonts, each page-load will result in a request being made to
Google Fonts. The alternatives below provide alternative approaches that are
more privacy preserving.

## Alternatives

!!! tip "Privacy Plugin"

    The [privacy plugin] provided by Material for MkDocs provides a
    best-of-both-worlds solution in that it allows you to specify
    fonts available on Google Fonts directly in your `mkdocs.yml`.
    It automatically downloads the ones used and includes them in
    your website so they are served up by your own server.
    No need for a custom stylesheet.

Another alternative is to turn off the use of Google Fonts and
[configure custom fonts to use] that you host yourself, as shown in 
[this example that shows how to switch to the Noto font family].

[privacy plugin]: https://squidfunk.github.io/mkdocs-material/plugins/privacy/
[configure custom fonts to use]: https://squidfunk.github.io/mkdocs-material/setup/changing-the-fonts/#additional-fonts
[this example that shows how to switch to the Noto font family]: ../fonts-custom
