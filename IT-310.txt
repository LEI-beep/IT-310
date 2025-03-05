Flask API Mini-Project
Objective:
Research and build a simple Flask API with at least three endpoints.  
Tasks:  
1. Research Flask Basics  
What is Flask?  
Flask is a lightweight and flexible Python web framework that allows developers to build web applications quickly. It is classified as a microframework because it does not require particular tools or libraries, making it easy to extend with additional features as needed.

How do you install and run Flask?
Pip install flask
Create a python file
Run the application using cmd
Open your browser and navigate to (http://127.0.0.1:5000/)

How do you define API routes and return JSON responses?  
Flask uses decorators (@app.route) to define routes. To return JSON responses, use the jsonify function.

What is Jinja2, and how is it used in Flask for rendering HTML templates?  
Jinja2 is a templating engine for Python. In Flask, it is used to dynamically render HTML pages by embedding Python expressions within HTML templates.
Steps to Use Jinja2:
Create a folder named templates in your project directory
Add an HTML file (e.g., index.html) inside the templates folder.
Use Flask's render_template function to render the template.

