---
---

{% capture markdown %}
# Heading 1
{% endcapture %}
{% assign text = markdown | markdownify %}

{% include toc.html html=text class="awesome-toc-class" %}

<!-- /// -->

<ul class="awesome-toc-class">
    <li><a href="#heading-1">Heading 1</a></li>
</ul>
