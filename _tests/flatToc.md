---
# https://github.com/allejo/jekyll-toc/issues/70
---

{% capture markdown %}
# Heading 1

## Heading 2

### Heading 3

## Heading 4
{% endcapture %}
{% assign text = markdown | markdownify %}

{% include toc.html html=text flat_toc=true %}

<!-- /// -->

<ul>
    <li><a href="#heading-1">Heading 1</a></li>
    <li><a href="#heading-2">Heading 2</a></li>
    <li><a href="#heading-3">Heading 3</a></li>
    <li><a href="#heading-4">Heading 4</a></li>
</ul>
