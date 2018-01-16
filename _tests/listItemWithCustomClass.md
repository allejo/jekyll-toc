---
# see https://github.com/allejo/jekyll-toc/issues/5
---

{% capture markdown %}
# Heading 1

## Heading 2

### Some Heading 3

#### A Heading 4
{% endcapture %}
{% assign text = markdown | markdownify %}

{% capture itemClass %}toc-entry.toc-h%level%{% endcapture %}
{% include toc.html html=text class="ul-level-class" item_class=itemClass %}

<!-- /// -->

<ul class="ul-level-class">
    <li class="toc-entry toc-h1">
        <a href="#heading-1">Heading 1</a>
        <ul>
            <li class="toc-entry toc-h2">
                <a href="#heading-2">Heading 2</a>
                <ul>
                    <li class="toc-entry toc-h3">
                        <a href="#some-heading-3">Some Heading 3</a>
                        <ul>
                            <li class="toc-entry toc-h4">
                                <a href="#a-heading-4">A Heading 4</a>
                            </li>
                        </ul>
                    </li>
                </ul>
            </li>
        </ul>
    </li>
</ul>
