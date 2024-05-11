---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: main
---

Check out these references!

<div class="list">
  {% for page in site.pages %}
    {% if page.title %}
        <a href="{{ page.url | relative_url }}" class="tile">
          <div class="icolumn">
            {% if page.thumbnail_img %}
              <img src="{{page.thumbnail_img}}" class="preview"/>
            {% endif %}
            {{page.title}}
            {% if page.description %}
              <span>– {{page.description}}</span>
            {% endif %}
          </div>
        </a>
    {% endif %}
  {% endfor %}
</div>

<!-- 
<ul>
    {% for page in site.pages %}
      {% if page.title %}
        <li>
          <a href="{{ pub.url | relative_url }}">{{page.title}}</a>
          {% if page.description %}
            <span>– {{page.description}}</span>
          {% endif %}
        </li>
      {% endif %}
    {% endfor %}
</ul> -->
