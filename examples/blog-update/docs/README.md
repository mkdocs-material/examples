# A blog with update dates shown

This example shows how to add a small customization that will show
then blog posts were [updated] on the blog index pages. (The blog page
template already contains this.)

It shows how to:

- add an update date in addition to the creation date for a post as in [My first post]
- override the template index pages, so
  that the [main blog index], the [archive index] and the [categories
  index] show the update date

**Note**: Please note that when overriding templates you are copying
part of the code that makes up Material for MkDocs and so need to take
care when upgrading. The [changelog] contains a note on which
templates have changed, if any. 

If you have not already set up a blog for your site then please start
with the [Basic blog] example.

[changelog]: https://squidfunk.github.io/mkdocs-material/changelog/
[Basic blog]: ../blog-basic
[My first post]: blog/2023/10/11/my-first-blog-post
[main blog index]: blog
[archive index]: blog/archive/2023
[categories index]: blog/category/meta
