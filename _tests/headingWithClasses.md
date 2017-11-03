---
# See https://github.com/allejo/jekyll-toc/issues/4
---

{% capture markdown %}
# Miscellaneous features
{: .hide-from-excerpt}

Lorem ipsum dolor sit amet, consectetur adipisicing elit.
{% endcapture %}
{% assign text = markdown | markdownify %}

{% include toc.html html=text %}

<!-- /// -->

<ul>
    <li><a href="#miscellaneous-features">Miscellaneous features</a></li>
</ul>
