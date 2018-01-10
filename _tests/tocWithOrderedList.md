---
# Given `ordered` is set to true, an ordered list should be output instead of an unordered list
---

{% capture markdown %}
# Heading 1

## Heading 2.1

### Heading 3

#### Heading 4

## Heading 2.2
{% endcapture %}
{% assign text = markdown | markdownify %}

{% include toc.html html=text ordered=true %}

<!-- /// -->

<ol>
    <li>
        <a href="#heading-1">Heading 1</a>
        <ol>
            <li>
                <a href="#heading-21">Heading 2.1</a>
                <ol>
                    <li>
                        <a href="#heading-3">Heading 3</a>
                        <ol>
                            <li><a href="#heading-4">Heading 4</a></li>
                        </ol>
                    </li>
                </ol>
            </li>
            <li><a href="#heading-22">Heading 2.2</a></li>
        </ol>
    </li>
</ol>
