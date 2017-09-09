---
# If we use both `class` and `id`, both should appear in our final TOC
---

{% capture markdown %}
# Heading 1.1

# Heading 1.2
{% endcapture %}
{% assign text = markdown | markdownify %}

{% include toc.html html=text id="Jekyll-TOC" class="toc" %}

<!-- /// -->

<ul class="toc" id="Jekyll-TOC">
    <li><a href="#heading-11">Heading 1.1</a></li>
    <li><a href="#heading-12">Heading 1.2</a></li>
</ul>
