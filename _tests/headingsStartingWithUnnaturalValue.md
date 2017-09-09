---
# If headings start at an "unnatural" value such as <h3>, then that'll be treated
# as the minimum heading
---

{% capture markdown %}
### Ut libero elit

# In hac habitasse platea dictumst.

## Duis tristique enim quis
{% endcapture %}
{% assign text = markdown | markdownify %}

{% include toc.html html=text %}

<!-- /// -->

<ul>
    <li><a href="#ut-libero-elit">Ut libero elit</a></li>
</ul>
