---
# Given h_max is defined, it should only use headings less than or equal to this value
---

{% capture markdown %}
# Heading 1

## Heading 2.1

### Heading 3

#### Heading 4

## Heading 2.2
{% endcapture %}
{% assign text = markdown | markdownify %}

{% include toc.html html=text h_max=2 %}

<!-- /// -->

<ul>
    <li>
        <a href="#heading-1">Heading 1</a>
        <ul>
            <li><a href="#heading-21">Heading 2.1</a></li>
            <li><a href="#heading-22">Heading 2.2</a></li>
        </ul>
    </li>
</ul>
