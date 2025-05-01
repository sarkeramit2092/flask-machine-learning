In Flask, we will import the Flask class. After that, we create an application instance using:

```python
from flask import Flask

app = Flask(__name__)

```
This app object is the core of our Flask application.
========================================================================================================

The #action parameter in an HTML form specifies where to send the form data when the user submits the form. For example, if a user fills out a signup form and clicks "Submit", the action tells the browser which URL to send that data to. If the action is left empty, the form submits the data to the same page.

========================================================================================================

The #method parameter defines how the data is sent. If you're retrieving data (like searching), you use GET, which sends data as query parameters. But if you're storing or submitting sensitive information (like a signup form), you use POST, which sends data securely in the request body.

========================================================================================================
- signup.html

```html
<form action="" method="post">
   {{form.hidden_tag()}} #csrf token called from app.py
</form>
```

- login.html

```html
<form action = "" method="post">
</form>
```
========================================================================================================

You’re submitting a form with random values like gender, date of birth, and password. After clicking submit, you're getting an error: "Method Not Allowed." This happens because the form uses the POST method, but the application doesn't allow POST requests for that endpoint yet.

In your HTML form, you've set the method to POST, but you also need to inform your Flask application that the corresponding route should accept POST requests. So, in your Flask code, you should define the route with both GET and POST methods.

By default, the method is GET, which is used to request data. But when the form is submitted with user input, it sends a POST request. If your route doesn’t allow POST, it throws a "Method Not Allowed" error.

To fix this, you write your route to accept both methods:

```python
@app.route("/signup", methods=["GET", "POST"])
```
Now, when the form is accessed in the browser (initially), it uses GET, and when the user submits the form, it uses POST. If you write only POST, the form page won't even load because it can't respond to a GET request. So, include both GET and POST to handle form display and form submission properly.

========================================================================================================

We have our form, the signup page. In the code, we can access that form as a variable—this is an instance of our signup form. To use the username field and display its label, we write:

```python
form.username.label
```
- This will show the label "Username".

- To show the input box for the username, we write:

```python
form.username
```

========================================================================================================

When we come to the login page, we will create an object of the LoginForm. This form object needs to be processed in the backend.

Once we have created the form object, we need to pass it to our HTML page. In the backend, we can use render_template to send the form to the frontend by passing it as a parameter:

```python
return render_template("signup.html", form=form)
```
Now, when a user accesses the signup page, the signup.html template is rendered, and the form instance is passed to it as a variable named form.

In the HTML file, when we want to work with the form, we just refer to this form variable. To access specific fields inside the form, we use the dot operator, like form.username, form.password, etc., because all these fields are attributes of the form object.

It’s simple and clear—this is how we connect the form from the backend to the frontend using Flask and WTForms.

========================================================================================================

We’ll write code specifically for displaying the form using Jinja inside a <form> tag. We will not use any traditional HTML <td> elements or manually write field HTML. Instead, we’ll use Jinja to handle the form rendering.

First, we’ll open the <form> tag.

The action attribute tells where to send the form data after submission. Since we want to keep the user on the same page for now, we'll leave action="".

The method attribute should be POST because we want to send the data to the backend server, not just generate query parameters.

Here’s the form tag structure:

```html
<form action="" method="POST">
```
Now we’ll design the form layout.
---------------------------------
# We want each field to appear like this:

Field name/label (e.g., "Username")

Input box (to collect value)

Repeat this for each field

A final Submit button

To access and display the label and input box using Jinja:

Assume we passed the form instance to the template using render_template('signup.html', form=form)

Then in the HTML, to display the username field:

```html
<div>
  {{ form.username.label }}
  {{ form.username }}
</div>
<br>
```
Similarly, for the password:

```html
<div>
  {{ form.password.label }}
  {{ form.password }}
</div>
<br>
```
Finally, add a submit button:

```html
<div>
  {{ form.submit }}
</div>
```

This simple structure dynamically creates the form using WTForms in Flask with Jinja templating.