---
# Supporting multiple classes for the TOC works by concatenating them with periods
---

{% capture markdown %}
# Heading 1
{% endcapture %}
{% assign text = markdown | markdownify %}

{% include toc.html html=text class="first-class.second-class" %}

<!-- /// -->

<ul class="first-class second-class">
    <li><a href="#heading-1">Heading 1</a></li>
</ul>
