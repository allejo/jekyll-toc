---
# Another unit test in addition to headingsStartingAtTwoWithClass.md
---

{% capture markdown %}
### Ut libero elit

### In hac habitasse platea dictumst.

#### Duis tristique enim quis
{% endcapture %}
{% assign text = markdown | markdownify %}

{% include toc.html html=text class="toc" %}

<!-- /// -->

<ul class="toc">
    <li><a href="#ut-libero-elit">Ut libero elit</a></li>
    <li>
        <a href="#in-hac-habitasse-platea-dictumst">In hac habitasse platea dictumst.</a>
        <ul>
            <li><a href="#duis-tristique-enim-quis">Duis tristique enim quis</a></li>
        </ul>
    </li>
</ul>
