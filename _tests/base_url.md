---
---

{% capture markdown %}
# Heading 1
{% endcapture %}
{% assign text = markdown | markdownify %}

{% include toc.html html=text baseurl="example.org" %}

<!-- /// -->

<ul>
    <li><a href="example.org#heading-1">Heading 1</a></li>
</ul>
