---
# Test the 'id' attribute correctly assigns the ID to the generated TOC
---

{% capture markdown %}
# Heading 1
{% endcapture %}
{% assign text = markdown | markdownify %}

{% include toc.html html=text id="Jekyll-TOC" %}

<!-- /// -->

<ul id="Jekyll-TOC">
    <li><a href="#heading-1">Heading 1</a></li>
</ul>
