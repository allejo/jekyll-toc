---
# See https://github.com/allejo/jekyll-toc/pull/60
---

{% capture jekyll_toc %}{% include toc.html html="" %}{% endcapture %}

{% if jekyll_toc == "" -%}
  <p>Success</p>
{%- else -%}
  <p>Failure</p>
{%- endif %}

<!-- /// -->

<p>Success</p>
