---
# https://github.com/allejo/jekyll-toc/issues/32
---

{% capture markdown %}
## Heading 2.1

<h2>Heading 2.2 (no link)</h2>

### Heading 2.2.1

<h2 id="heading-23" class="no_toc">Heading 2.3</h2>

## Heading 2.4

<h3 id="super-toast">Heading 2.4.1</h3>
{% endcapture %}
{% assign text = markdown | markdownify %}

{% include toc.html html=text %}

<!-- /// -->

<ul>
    <li>
        <a href="#heading-21">Heading 2.1</a>
    </li>
    <li>
        Heading 2.2 (no link)
        <ul>
            <li>
                <a href="#heading-221">Heading 2.2.1</a>
            </li>
        </ul>
    </li>
    <li>
        <a href="#heading-24">Heading 2.4</a>
        <ul>
            <li>
                <a href="#super-toast">Heading 2.4.1</a>
            </li>
        </ul>
    </li>
</ul>
