---
# See https://github.com/allejo/jekyll-toc/issues/35
---

{% capture markdown %}
## skip me
{: .no_toc}

## skip me also
{: .no_toc}

## skip me, too...
{: .no_toc}

## skip me last
{: .no_toc}

### also skip me as a subheading!
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
