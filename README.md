# 5_Project_Django_Middlewares

The program consists of two files: middlewares.py and HTML templates (index.html and display.html).

In middlewares.py, there is a class called LogMiddleware that serves as a middleware in Django. In the constructor of this class, logging is configured and a logger named 'LogMiddleware' is created. The __call__ method handles the request by measuring the start time, calling the request handler function, and obtaining the response. Then, it calculates the execution time, creates a log string, and logs it using the logger.

index.html is a template for the "Index" page. It extends a base template named 'base.html' and contains a form with the "POST" method. Inside the form, a CSRF token is added for protection, and a form field is created. Additionally, there is a "Submit" button for submitting the form.

display.html also extends the base template 'base.html'. It represents the "Display" page and displays a list of completed tasks, if any. For each task, the title, description, and completion time are shown. The completion time is formatted using the {{ task.completed_at|date:"F j, Y, g:i a" }} filter. There is also a "Go Home" button that redirects the user to the homepage.

In summary, middlewares.py implements a middleware for logging requests, and the HTML templates (index.html and display.html) define the structure and content of the "Index" and "Display" pages, respectively.
