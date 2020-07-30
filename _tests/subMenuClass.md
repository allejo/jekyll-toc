---
# https://github.com/allejo/jekyll-toc/issues/40
---

{% capture markdown %}
# Heading 1

## Heading 2.1

### Heading 3.1

### Heading 3.2

## Heading 2.2

### Heading 3.3

### Heading 3.4
{% endcapture %}
{% assign text = markdown | markdownify %}

{% include toc.html html=text submenu_class="submenu-%level%" %}

<!-- /// -->

<ul>
    <li>
        <a href="#heading-1">Heading 1</a>
        <ul class="submenu-1">
            <li>
                <a href="#heading-21">Heading 2.1</a>
                <ul class="submenu-2">
                    <li><a href="#heading-31">Heading 3.1</a></li>
                    <li><a href="#heading-32">Heading 3.2</a></li>
                </ul>
            </li>
            <li>
                <a href="#heading-22">Heading 2.2</a>
                <ul class="submenu-2">
                    <li><a href="#heading-33">Heading 3.3</a></li>
                    <li><a href="#heading-34">Heading 3.4</a></li>
                </ul>
            </li>
        </ul>
    </li>
</ul>
