---
# Given `sanitize` is set to false, any HTML from headings should remain
---

{% capture markdown %}
# Heading 1

## Heading 2.1

### Heading **3**

#### Heading _4_

## Heading 2.2
{% endcapture %}
{% assign text = markdown | markdownify %}

{% include toc.html html=text sanitize=false %}

<!-- /// -->

<ul>
    <li>
        <a href="#heading-1">Heading 1</a>
        <ul>
            <li>
                <a href="#heading-21">Heading 2.1</a>
                <ul>
                    <li>
                        <a href="#heading-3">Heading <strong>3</strong></a>
                        <ul>
                            <li><a href="#heading-4">Heading <em>4</em></a></li>
                        </ul>
                    </li>
                </ul>
            </li>
            <li><a href="#heading-22">Heading 2.2</a></li>
        </ul>
    </li>
</ul>
