# Jekyll Pure Liquid Table of Contents

[![Unit Tests](https://github.com/allejo/jekyll-toc/workflows/Unit%20Tests/badge.svg)](https://github.com/allejo/jekyll-toc/actions?query=workflow%3A%22Unit+Tests%22)
[![Latest release](https://img.shields.io/github/release/allejo/jekyll-toc.svg)](https://github.com/allejo/jekyll-toc/releases/latest)
[![ko-fi](https://img.shields.io/static/v1.svg?label=&message=Support%20me%20on%20Ko-fi&color=333&logo=ko-fi)](https://ko-fi.com/Q5Q4J7IX)
[![Buy me a coffee](https://img.shields.io/static/v1.svg?label=&message=Buy%20me%20a%20coffee&color=333&logo=buy-me-a-coffee)](https://www.buymeacoffee.com/allejo)

GitHub Pages can't run custom Jekyll plug-ins so when generating Tables of Contents (TOCs), you're stuck with either a JavaScript solution or using kramdown's `{:toc}` option. However, by using `{:toc}`, you are forced to have that code next to your actual markdown and you can't place it in a layout. This means _every_. _single_. _post_. will need to have the snippet. If you choose the JavaScript approach, that's perfectly fine but what if JS is disabled on someone's browser or your page is just _really_ long and it becomes inefficient.

Instead, I wrote this solution entirely in Liquid and can be used as an `{% include %}` in any website you want, in any layout you want. Want to see it in action? Here are some awesome websites that I know of using this solution :heart:.

- [the docs.docker.com website](https://github.com/docker/docker.github.io/pull/1474)
- [the UK Ministry of Justice Technical Guidance site](https://github.com/ministryofjustice/technical-guidance/pull/7)
- ["Minimal Mistakes" Jekyll Theme](https://github.com/mmistakes/minimal-mistakes/pull/1310)
- Apache's [Beam](https://github.com/apache/beam-site/blob/5a9fb94b27575bc1a73fbc3725d0e31c3114aa9f/src/_includes/page-toc.html) and [PDFBox](https://github.com/apache/pdfbox-docs/commit/37123aa785562c08ad3fa748a289a9ad81c8734c) websites
- [JetBrains' OSS Jekyll Theme](https://github.com/JetBrains/oss-site-jekyll-theme/commit/ff779cfa2ebc2c34f0d1e194a1d6a27a748f0c96)
- [Bitcoin.org](https://github.com/bitcoin-dot-org/bitcoin.org/commit/adf254847a4bfe8d8c1185bd875776dd7c24ef62)
- [CloudCannon](https://github.com/CloudCannon/documentation/commit/2dca0e9ecede5ac3ecdff0bf631293aff72ffa71)
- [British Antarctic Survey](https://github.com/antarctica/bas-style-kit-jekyll-theme/commit/7398c88bf18f20ecca575f44bceb784b5e538e67)
- [Travis CI Docs](https://github.com/travis-ci/docs-travis-ci-com/pull/1909)
- [the City of Amsterdam](https://github.com/Amsterdam/amsterdam-jekyll-theme/commit/598f0d78198cbb322b0b005ba336680a0376f55b)
- [Intuit's Karate](https://github.com/intuit/karate/pull/634)
- [Duality's developer docs](https://github.com/AdamsLair/duality-docs/commit/e7e3e173c0e05669fc6ed569f9445c126bbb5ee6)
- ["Bulma Clean" Jekyll Theme](https://github.com/chrisrhymes/bulma-clean-theme/commit/547e88c131e892ff1c013b0801c180dbd845aaa5#diff-cef4f277dc360c0c0b73134898ed0a5f)
- The Google APIs team [homepage](https://github.com/googleapis/googleapis.github.io/commit/ca1d4499c076ee01be67f1abc965438b1801b993#diff-cef4f277dc360c0c0b73134898ed0a5f), [Google AIP website](https://github.com/googleapis/aip/commit/b25841f9b7efaf1b85c23166ba6a70d75dbf72f1#diff-cef4f277dc360c0c0b73134898ed0a5f) and [API Linter project](https://github.com/googleapis/api-linter/commit/fbed405f4e74a9ce56c043048e144bb8499b2fd5#diff-808e6284272b61fc0ce1aa390a006e4b)
- [Shopify App CLI Extensions](https://github.com/Shopify/shopify-app-cli-extensions/commit/9e2fd9f82b495d93e7d6b7ea26c2c74a81b8b479#diff-808e6284272b61fc0ce1aa390a006e4b)
- [AWS' Open Distro for Elasticsearch Documentation](https://github.com/opendistro/for-elasticsearch-docs/commit/bfcf72e928dacabf1ad0008e973d96417885a3aa#diff-ae5bddf889465c887d2c57e786a6b29f4ac82b277fcce0672ce8bbdba11ebf3a)
- [GitHub's Open Source Guides website](https://github.com/github/opensource.guide/blob/c97bd849cce0a13cc67228975294bbbadc1beb41/_includes/jekyll-toc.html)
- [Gitbook Jekyll Theme](https://github.com/sighingnow/jekyll-gitbook/commit/e0f385fc85a67beb964ebd09394cc0365cecf499)

For more information regarding how this include works, [read the blog post](https://allejo.io/blog/a-jekyll-toc-in-liquid-only/).

> **Want anchors next to your Jekyll headings without JavaScript or a plug-in?**
>
> Check out the sister project over at [allejo/jekyll-anchor-headings](https://github.com/allejo/jekyll-anchor-headings).

## Usage

Alright, so how do you use it?

1. Download the `toc.html` file from [the latest release](https://github.com/allejo/jekyll-toc/releases/latest) or [the master branch](/_includes/toc.html)
2. Toss that file in your `_includes` folder.
3. Use it in your template layout where you have `{{ content }}` which is the HTML rendered from the markdown source with this liquid tag:

   ```liquid
   {% include toc.html html=content %}
   ```

## Parameters

This snippet is highly customizable. Here are the available parameters to change the behavior of the snippet.

| Parameter       |  Type  | Default | Description |
| --------------- | :----: | :-----: | ----------- |
| `html`          | string | <sup>*</sup> | the HTML of compiled markdown generated by kramdown in Jekyll |
| `sanitize`      | bool   | false  | when set to true, the headers will be stripped of any HTML in the TOC |
| `class`         | string | ''     | a CSS class assigned to the TOC; concat multiple classes with '.' |
| `id`            | string | ''     | an ID to be assigned to the TOC |
| `h_min`         | int    | 1      | the minimum TOC header level to use; any heading lower than this value will be ignored |
| `h_max`         | int    | 6      | the maximum TOC header level to use; any heading greater than this value will be ignored |
| `ordered`       | bool   | false  | when set to true, an ordered list will be outputted instead of an unordered list |
| `item_class`    | string | ''     | add custom class for each list item; has support for `%level%` placeholder, which is the current heading level |
| `submenu_class` | string | ''     | add custom class(es) for each child group of headings; has support for `%level%` placeholder which is the current "submenu" heading level |
| `base_url`      | string | ''     | add a base url to the TOC links for when your TOC is on another page than the actual content |
| `anchor_class`  | string | ''     | add custom class(es) for each anchor element |
| `skip_no_ids`   | bool   | false  | skip headers that do not have an `id` attribute |
| `flat_toc`      | bool   | false  | when set to true, the TOC will be a single level list |

<sup>*</sup> This is a required parameter

### Deprecated Variables

- `baseurl` has been deprecated since 1.1.0, use `base_url` instead
- `skipNoIDs` has been deprecated since 1.1.0, use `skip_no_ids` instead

## Common Problems

### An `<li>` is rendering outside of a `<ul>`

This happens when your headings are placed out of order or when you skip headings. For example, if you go from an `<h2>` to an `<h4>` with no `<h3>` in between; see "Heading 2.A" in this example,

```markdown
## Heading 1
### Heading 1.A
## Heading 2
#### Heading 2.A
```

This project expects headings to be nested/ordered correctly, which is the [recommended way of headings working](https://www.w3.org/WAI/tutorials/page-structure/headings/#heading-ranks).

> Skipping heading ranks can be confusing and should be avoided where possible: Make sure that a `<h2>` is not followed directly by an `<h4>`, for example. It is ok to skip ranks when closing subsections, for instance, a `<h2>` beginning a new section, can follow an `<h4>` as it closes the previous section.
>
> \- [w3.org](https://www.w3.org/WAI/tutorials/page-structure/headings/#heading-ranks)

While it is possible to fix this and have the TOC internally keep track of indentation, I've chosen not to allow for this bad practice of allowing headings to be out of order. If you'd like to proceed anyways, see [#13 for a third-party patch](https://github.com/allejo/jekyll-toc/pull/13) that can enable this functionality.

## Performance

The performance impact of this snippet on your site is pretty negligible. The stats below were gotten from Jekyll's `--profile` option.

```
Filename                              | Count |      Bytes |    Time
--------------------------------------+-------+------------+--------

# performance on docs.docker.com from ~Feb 2017
_includes/toc.html                    |   813 |    524.17K |  6.422

# performance on the "Minimal Mistakes" Jekyll theme
_includes/toc.html                    |    94 |     29.43K |  0.413
```

## License

This snippet may be redistributed under either the [BSD-3](https://github.com/allejo/jekyll-toc/blob/master/LICENSE.BSD3.md) or [MIT](https://github.com/allejo/jekyll-toc/blob/master/LICENSE.MIT.md) licenses.
