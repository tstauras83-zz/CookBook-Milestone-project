In this project, you’ll be building a data-driven web application using the technologies that you have learned throughout Data Centric Development. You can either choose to to follow the example brief below, or you can use your own idea for the website.

CREATE AN ONLINE COOKBOOK:
Create a web application that allows users to store and easily access cooking recipes
Put some effort into designing a database schema based on recipes, and any other related properties and entities 

(e.g. views, upvotes, ingredients, recipe authors, allergens, author’s country of origin, cuisine etc…). Make sure 

to put some thought into the relationships between them, and use either foreign keys (in the case of a relational database) 

or nesting (in the case of a document store) to connect these pieces of data

Create the backend code and frontend form to allow users to add new recipes to the site (at least a basic one, 

if you haven’t taken the frontend course)

Create the backend code to group and summarise the recipes on the site, based on their attributes such as cuisine,

country of origin, allergens, ingredients, etc. and a frontend page to show this summary, and make the categories 

clickable to drill down into a filtered view based on that category. This frontend page can be as simple or as complex 

as you’d like; you can use a Python library such as matplotlib, or a JS library such as d3/dc (that you learned about if 

you took the frontend modules) for visualisation

Create the backend code to retrieve a list of recipes, filtered based on various criteria (e.g. allergens, cuisine, etc…) 

and order them based on some reasonable aspect (e.g. number of views or upvotes). Create a frontend page to display these, 

and to show some summary statistics around the list (e.g. number of matching recipes, number of new recipes. Optionally, 

add support for pagination, when the number of results is large

Create a detailed view for each recipes, that would just show all attributes for that recipe, and the full preparation instructions

Allow for editing and deleting of the recipe records, either on separate pages, or built into the list/detail pages

Optionally, you may choose to add basic user registration and authentication to the site. This can as simple as adding a 

username field to the recipe creation form, without a password (for this project only, this is not expected to be secure)










Use the following guidelines when developing your project:

Logic must be written in Python. HTML, CSS, and JavaScript can be used to enhance the look and feel of the cookbook.
Whenever possible, strive to use semantic HTML5 elements to structure your HTML code better.
The website must be data-driven and can rely on structured data, unstructured data or a mix of structured and unstructured data. 
CRUD operations can be carried out using either SQL (e.g. MySQL/SQLite/Postgres) or NoSQL (e.g. MongoDB).
Use Flask, a micro-framework, to run your application. Provide instructions on how to run your project locally in your README.
Make sure your site is as responsive as possible. You can test this by checking the site on different screen sizes and browsers.
Share details of how you created your database schema in your README. Consider sharing working drafts or finalised versions of your database 
schema in a 'Database Schema' folder in your repo. Provide a link to this folder in your README.
We advise that you write down user stories and create wireframes/mockups before embarking on full-blown development.
The site can also make use of CSS frameworks such as Bootstrap, just make sure you maintain a clear separation between the library code and your code.
Write a README.md file for your project that explains what the project does and the need that it fulfills. It should also describe the 
functionality of the project, as well as the technologies used. If some of the work was based on other code, explain what was kept and 
how it was changed to fit your need. A project submitted without a README.md file will FAIL.
Use Git & GitHub for version control. Each new piece of functionality should be in a separate commit.
Deploy the final version of your code to a hosting platform such as Heroku.
Non-requirements for this project:

Secure user authentication (e.g. via passwords) is not required for this particular project. Having each user 
just choose a username is sufficient. Secure authentication will be introduced in the Django module.
