---
# Given a markdown block with no headings, no TOC will be generated
---

{% capture markdown %}
Some **awesome** markdown that doesn't have any headings
{% endcapture %}
{% assign text = markdown | markdownify %}

<div id="unit-test">
{% include toc.html html=text id="Jekyll-TOC" %}
</div>

<!-- /// -->

<div id="unit-test">

</div>
