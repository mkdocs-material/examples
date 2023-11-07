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

- Noto Serif
- **Noto Serif bold**
- *Noto Serif italic*
- __*Noto Serif bold italic*__
- `Noto Mono`
- __`Noto Mono bold`__ 

!!! tip "Privacy Plugin"

    Before you consider the examples below, you should know that loading fonts
    or other assets from a CDN may bring you into non-compliance with data
    protection legislation such as the GDPR in the EU. You can read more about
    this in the [ensuring data privacy] section of the documentation.

    The [privacy plugin] provided by Material for MkDocs provides a
    best-of-both-worlds solution in that it allows you to specify fonts
    available on Google Fonts directly in your `mkdocs.yml`.  It automatically
    downloads the ones used and includes them in your website so they are served
    up together with your documentation.  No need for a custom stylesheet.

[ensuring data privacy]: https://squidfunk.github.io/mkdocs-material/setup/ensuring-data-privacy
[privacy plugin]: https://squidfunk.github.io/mkdocs-material/plugins/privacy/

## How it works

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

[configure custom fonts]: https://squidfunk.github.io/mkdocs-material/setup/changing-the-fonts/#additional-fonts

### Using a CDN's CSS

If you are using a CDN to load your fonts, you may want to use CSS
that the operators of the CDN are providing for defining the font
faces, instead of writing your own. You still need to configure the
fonts for Material to use, though:

=== "`mkdocs.yml`"

    ```yaml
    extra_css:
      - https://fonts.cdnfonts.com/css/noto-serif
      - https://fonts.cdnfonts.com/css/noto-mono
      - assets/stylesheets/extra.css
    ```

=== "`extra.css`"

    ```css
    :root {
      --md-text-font: "Noto Serif";
      --md-code-font: "Noto Mono";
    }
    ```

### Hosting on your own site

The code for hosting the fonts yourself as part of your site, looks
very similar to the previous example that used a CDN. You need to
write your own font face definitions and point the browser 
to the files located on your own server, e.g., in
`docs/assets/fonts`:

=== "`mkdocs.yml`"

    ```yaml
    extra_css:
      - assets/stylesheets/extra.css
    ```

=== "`extra.css`"

    ```css
    @font-face {
      font-family: "Noto Serif"; 
      font-weight: normal; 
      font-style: normal;
      src: url("../fonts/NotoSerif-Regular.otf");
    }

    @font-face {
      font-family: "Noto Serif"; 
      font-weight: bold; 
      font-style: normal;
      src: url("../fonts/NotoSerif-Bold.otf");

    }

    @font-face {
      font-family: "Noto Serif"; 
      font-weight: normal; 
      font-style: italic;
      src: url("../fonts/NotoSerif-Italic.otf");

    }

    @font-face {
      font-family: "Noto Mono"; 
      font-weight: normal; 
      font-style: normal;
      src: url("../fonts/NotoSansMono-Regular.otf");

    }

    @font-face {
      font-family: "Noto Mono"; 
      font-weight: bold; 
      font-style: normal;
      src: url("../fonts/NotoSansMono-Bold.otf");
    }

    :root {
      --md-text-font: "Noto Serif";
      --md-code-font: "Noto Mono";
    }
    ```


## (Dis-)Advantages

If you are loading the fonts from a CDN as in this example, you are still not
limiting traffic to only your website. To do that you would need to host the
fonts as part of your site as described above. We include the CDN example here
because you may have other reasons to use a CDN other than Google Fonts.

Try not to use too many different fonts as that will slow down your page load
and rendering times.

Compared to using built-in browser fonts only, you have more control over the
look of your site.

## Alternatives

Alternatively, you can simply [use built-in browser fonts] but that
does mean giving up some control over the look of your site.

[use built-in browser fonts]: ../fonts-builtin
