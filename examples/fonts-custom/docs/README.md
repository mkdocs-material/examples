# Using a custom font

This example uses the Noto Serif and Noto Mono font families to show
how custom fonts can be used. These families were chosen because the 
[Noto fonts are well documented] and they are available under the 
[Open Font License].

[Noto fonts are well documented]: https://notofonts.github.io/noto-docs/
[Open Font License]: https://scripts.sil.org/ofl

In this example, the fonts are loaded from a CDN (that is not Google)
to keep the example itself small and allow you to use it as a template
for your own site, without assuming what fonts you might want to use.
We also describe how to use custom fonts that are hosted on your own
server, see below.

Here we have some text in:

- regular - using Noto Serif
- **bold** - using Noto Serif bold
- *italic* - using Noto Serif italic
- __*bold italic*__ - using Noto Serif bold italic
- `code` - using Noto Mono

## Hot it works

In `mkdocs.yml`, turn off the auto-loading of fonts from Google Fonts
and add an extra CSS stylesheet to configure your custom fonts.

```yaml
theme:
  font: false

extra_css:
  - assets/stylesheets/extra.css
```

Then, [configure custom fonts] hosted either on a CDN or on your own
server, depending on your needs. We demonstrate this here with the 
Noto Sans and Noto Mono font families.

[configure custom fonts] https://squidfunk.github.io/mkdocs-material/setup/changing-the-fonts/#additional-fonts

### Using a CDN

If you are using a CDN to load your fonts, you may want to use CSS
that the operators of the CDN are providing, instead of writing your
own:

```yaml
extra_css:
  - https://fonts.cdnfonts.com/css/noto-serif
  - https://fonts.cdnfonts.com/css/noto-mono
  - assets/stylesheets/extra.css
```


### Hosting on your own server



## (Dis-)Advantages

If you are loading the fonts from a CDN as in this example, you are
still not limiting traffic to only your website. 

TODO: what about fonts hosted on GitHub Pages? A lot of documentation lies on GHP anyway, so why not load the fonts from there? Do they offer this?

## Alternatives

!!! tip "Privacy Plugin"

    The [privacy plugin] provided by Material for MkDocs provides a
    best-of-both-worlds solution in that it allows you to specifc 
    fonts available on Google Fonts directly in your `mkdocs.yml`.
    It automatically downloads the ones used and includes them in 
    your website so they are served up by your own server. 
    No need for a custom stylesheet.

Alternatively, you can simply [use built-in browser fonts] but that
does mean giving up some control over the look of your site.

[privacy plugin]: https://squidfunk.github.io/mkdocs-material/plugins/privacy/
[use built-in browser fonts]: ../fonts-builtin
