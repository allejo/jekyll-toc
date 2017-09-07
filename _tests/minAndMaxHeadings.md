---
# Given h_min and h_max are both defined, the TOC should respect both
---

{% capture markdown %}
# Heading 1

## Heading 2.1

### Heading 3

#### Heading 4.1

#### Heading 4.2

##### Heading 5

## Heading 2.2

{% endcapture %}
{% assign text = markdown | markdownify %}

{% include toc.html html=text h_min=2 h_max=4 %}

<!-- /// -->

<ul>
    <li>
        <a href="#heading-21">Heading 2.1</a>
        <ul>
            <li>
                <a href="#heading-3">Heading 3</a>
                <ul>
                    <li><a href="#heading-41">Heading 4.1</a></li>
                    <li><a href="#heading-42">Heading 4.2</a></li>
                </ul>
            </li>
        </ul>
    </li>
    <li><a href="#heading-22">Heading 2.2</a></li>
</ul>
