---
# Given `sanitize` is set to true, any HTML in the TOC should be stripped
---

{% capture markdown %}
# Heading 1

## `Heading` 2.1

### Heading **3**

#### Heading _4_

## Heading 2.2
{% endcapture %}
{% assign text = markdown | markdownify %}

{% include toc.html html=text sanitize=true %}

<!-- /// -->

<ul>
    <li>
        <a href="#heading-1">Heading 1</a>
        <ul>
            <li>
                <a href="#heading-21">Heading 2.1</a>
                <ul>
                    <li>
                        <a href="#heading-3">Heading 3</a>
                        <ul>
                            <li><a href="#heading-4">Heading 4</a></li>
                        </ul>
                    </li>
                </ul>
            </li>
            <li><a href="#heading-22">Heading 2.2</a></li>
        </ul>
    </li>
</ul>
