---
# See https://github.com/allejo/jekyll-toc/issues/35
---

{% capture markdown %}
## some prominent header i want to hide
{: .no_toc}

### Subheading A

### Subheading B

### Subheading C
{% endcapture %}
{% assign text = markdown | markdownify %}

{% include toc.html html=text %}

<!-- /// -->

<ul>
    <li><a href="#subheading-a">Subheading A</a></li>
    <li><a href="#subheading-b">Subheading B</a></li>
    <li><a href="#subheading-c">Subheading C</a></li>
</ul>
