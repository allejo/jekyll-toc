---
# see https://github.com/allejo/jekyll-toc/issues/15
---

{% capture markdown %}
# Contents header
{:.no_toc}

* A markdown unordered list which will be replaced with the ToC, excluding the "Contents header" from above
{:toc}

# H1 header

## H2 header
{% endcapture %}
{% assign text = markdown | markdownify %}

{% include toc.html html=text %}

<!-- /// -->

<ul>
    <li>
        <a href="#h1-header">H1 header</a>
        <ul>
            <li>
                <a href="#h2-header">H2 header</a>
            </li>
        </ul>
    </li>
</ul>
