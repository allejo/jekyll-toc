---
# https://github.com/allejo/jekyll-toc/issues/32
---

{% capture markdown %}
## Sample Usage

<div>
  <h1 class="page-title">My Awesome Example Page</h1>
  <h2 class="page-subtitle">With an awesome subtitle</h2>
  <a href='/' id="dummy-link">Dummy Link</a>
</div>

### Known Problems

Lots!

### Resources

#### Paid

#### Free
{% endcapture %}
{% assign text = markdown | markdownify %}

{% include toc.html html=text skipNoIDs=true %}

<!-- /// -->

<ul>
    <li>
        <a href="#sample-usage">Sample Usage</a>
        <ul>
            <li>
                <a href="#known-problems">Known Problems</a>
            </li>
            <li>
                <a href="#resources">Resources</a>
                <ul>
                    <li>
                        <a href="#paid">Paid</a>
                    </li>
                    <li>
                        <a href="#free">Free</a>
                    </li>
                </ul>
            </li>
        </ul>
    </li>
</ul>
