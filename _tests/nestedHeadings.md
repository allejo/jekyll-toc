---
---

{% capture markdown %}
# Heading 1

## Heading 2.1

### Heading 3

## Heading 2.2
{% endcapture %}
{% assign text = markdown | markdownify %}

{% include toc.html html=text %}

<!-- /// -->

<ul>
    <li>
        <a href="#heading-1">Heading 1</a>
        <ul>
            <li>
                <a href="#heading-21">Heading 2.1</a>
                <ul>
                    <li><a href="#heading-3">Heading 3</a></li>
                </ul>
            </li>
            <li><a href="#heading-22">Heading 2.2</a></li>
        </ul>
    </li>
</ul>
