# Jinja Template Syntax Guide

Jinja is a powerful templating engine for Python used in frameworks like Flask and Ansible. This guide explains key features of Jinja:

---

## 1. Parameters (Placeholders)

Placeholders are used to inject values dynamically into templates using double curly braces `{{ ... }}`.

### Syntax:
```jinja
Hello, {{ name }}!
Example:
jinja
Copy
Edit
Hello, {{ user.first_name }} {{ user.last_name }}!
If user.first_name = "John" and user.last_name = "Doe", the output will be:

Copy
Edit
Hello, John Doe!
2. If Conditionals
Jinja allows conditional rendering using {% if %}, {% elif %}, and {% else %} statements.

Syntax:

``` jinja
Copy
Edit
{% if condition %}
  Do something
{% elif another_condition %}
  Do something else
{% else %}
  Do fallback
{% endif %}
Example:
jinja
Copy
Edit
{% if user.is_admin %}
  <p>Welcome, Admin!</p>
{% else %}
  <p>Welcome, User!</p>
{% endif %}
```

3. For Loops
Loops are used to iterate over lists, dictionaries, or any iterable.

Syntax:

```jinja

{% for item in items %}
  {{ item }}
{% endfor %}
```
Example:

```jinja

<ul>
{% for fruit in fruits %}
  <li>{{ fruit }}</li>
{% endfor %}
</ul>
If fruits = ['Apple', 'Banana', 'Cherry'], the output will be:

html
Copy
Edit
<ul>
  <li>Apple</li>
  <li>Banana</li>
  <li>Cherry</li>
</ul>

You can also access loop variables:

jinja
Copy
Edit
{% for fruit in fruits %}
  {{ loop.index }} - {{ fruit }}
{% endfor %}
4. Blocks (Template Inheritance)
Blocks are used in template inheritance to define sections of a template that child templates can override.

Base Template (base.html):
jinja
Copy
Edit
<!DOCTYPE html>
<html>
<head>
  <title>{% block title %}My Site{% endblock %}</title>
</head>
<body>
  {% block content %}{% endblock %}
</body>
</html>
Child Template (home.html):
jinja
Copy
Edit
{% extends "base.html" %}

{% block title %}Home Page{% endblock %}

{% block content %}
  <h1>Welcome to the Home Page!</h1>
{% endblock %}


- Summary

Feature	     Syntax               Example
Placeholder	  {{ variable }}
If Condition	{% if condition %} ... {% endif %}
For Loop	    {% for item in list %} ... {% endfor %}
Block	        {% block name %} ... {% endblock %}
Extends	      {% extends "base.html" %}


- Here's a single Jinja template example that combines placeholders, if conditionals, for loops, and blocks—all in one!

🔧 Example: profile.html (child template)
jinja

{% extends "base.html" %}

{% block title %}{{ user.name }}'s Profile{% endblock %}

{% block content %}
  <h1>Hello, {{ user.name }}!</h1>

  {% if user.is_admin %}
    <p>Status: <strong>Administrator</strong></p>
  {% else %}
    <p>Status: <strong>Regular User</strong></p>
  {% endif %}

  <h2>Your Favorite Languages:</h2>
  <ul>
    {% for lang in user.favorite_languages %}
      <li>{{ loop.index }}. {{ lang }}</li>
    {% endfor %}
  </ul>
{% endblock %}

🧱 Base Template: base.html

jinja

<!DOCTYPE html>
<html>
<head>
  <title>{% block title %}User Profile{% endblock %}</title>
</head>
<body>
  <div class="container">
    {% block content %}{% endblock %}
  </div>
</body>
</html>

🧪 Context Passed to Template:

```python

user = {
  "name": "Alice",
  "is_admin": True,
  "favorite_languages": ["Python", "Go", "Rust"]
}
``
🖥️ Rendered Output:

```html

<!DOCTYPE html>
<html>
<head>
  <title>Alice's Profile</title>
</head>
<body>
  <div class="container">
    <h1>Hello, Alice!</h1>
    <p>Status: <strong>Administrator</strong></p>

    <h2>Your Favorite Languages:</h2>
    <ul>
      <li>1. Python</li>
      <li>2. Go</li>
      <li>3. Rust</li>
    </ul>
  </div>
</body>
</html>

```