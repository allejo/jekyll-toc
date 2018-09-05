---
---

{% capture markdown %}
# Heading 1
{% endcapture %}
{% assign text = markdown | markdownify %}

{% include toc.html html=text anchor_class="anchor-link.another-class" %}

<!-- /// -->

<ul>
    <li><a href="#heading-1" class="anchor-link another-class">Heading 1</a></li>
</ul>
