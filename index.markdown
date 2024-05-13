---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: main
---

<!-- <h2>Welcome!</h2> -->
<div class="tilelist">
  {% for page in site.pages %}
    {% if page.title %}
        <a href="{{ page.url | relative_url }}" class="tile icolumn">
            {% if page.thumbnail_img %}
              <img src="{{page.thumbnail_img}}" class="preview"/>
            {% endif %}
            <h5>{{page.title}}</h5>
            {% if page.description %}
              <span>– {{page.description}}</span>
            {% endif %}
        </a>
    {% endif %}
  {% endfor %}
</div>
