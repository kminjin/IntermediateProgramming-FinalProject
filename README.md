# Project Title

Name

[Link to this repository](__)

---

## Project Description
This project will have a home page that shows a number of countries recorded and a list of countries.

There will be a form that one can enter in favorite country, its leadership/president, and continent and this will result in new database. When you type a '/country' you will get information from the list of countries database and the new info entered into the flask about its leadership, continent. New modules are urllib and re.


[Database Diagram](https://docs.google.com/document/d/1SjZxCZpYq6sDtC8OhyiG4sWar8sjkY6VpvgeVPiammQ/edit?usp=sharing)




## How to run

1. First, while in the "base" virtual environment (default environment which conda itself is installed into, "root"), install all requirements with `pip install -r requirements.txt`
2. Then, type in "python SI507project_tools.py" in the terminal while in the base virtual environment with new installed requirements
3. Then, run newcountrycsv.py
4. Then, run db.py (type "python db.py runserver" at terminal)
5.
6.

## How to use

1. A useful instruction goes here
2. A useful second step here
3. (Optional): Markdown syntax to include an screenshot/image: ![alt text](image.jpg)

## Routes in this application
- `/home` -> This page will show Links in the views of Flask application pages

- `/result` -> this route is where the form sends the result...
- `/newuser/<username>` -> hello ___

## How to run tests
1. While in conda, if not "conda activate", do a pip install -r requirements.txt
2. Enter python SI507project_tools.py
3.
NOTE: Need not have 3 steps, but should have as many as are appropriate!

## In this repository:
- Directory Name
  - SI507project_tests.py
  - SI507project_tools.py
- File name
- File name

---
## Code Requirements for Grading
Please check the requirements you have accomplished in your code as demonstrated.
- [x] This is a completed requirement.
- [ ] This is an incomplete requirement.

Below is a list of the requirements listed in the rubric for you to copy and paste.  See rubric on Canvas for more details..
### General
- [x] Project is submitted as a Github repository
- [x] Project includes a working Flask application that runs locally on a computer
- [ ] Project includes at least 1 test suite file with reasonable tests in it.
- [x] Includes a `requirements.txt` file containing all required modules to run program
- [x] Includes a clear and readable README.md that follows this template
- [x] Includes a sample .sqlite/.db file
- [x] Includes a diagram of your database schema
- [x] Includes EVERY file needed in order to run the project
- [ ] Includes screenshots and/or clear descriptions of what your project should look like when it is working

### Flask Application
- [x] Includes at least 3 different routes
- [x] View/s a user can see when the application runs that are understandable/legible for someone who has NOT taken this course
- [x] Interactions with a database that has at least 2 tables
- [x] At least 1 relationship between 2 tables in database
- [x] Information stored in the database is viewed or interacted with in some way

### Additional Components (at least 6 required)
- [x] Use of a new module
- [x] Use of a second new module
- [] Object definitions using inheritance (indicate if this counts for 2 or 3 of the six requirements in a parenthetical)
- [] A many-to-many relationship in your database structure
- [] At least one form in your Flask application
- [x] Templating in your Flask application
- [] Inclusion of JavaScript files in the application
- [x] Links in the views of Flask application page/s
- [] Relevant use of `itertools` and/or `collections`
- [x] Sourcing of data using web scraping
- [ ] Sourcing of data using web REST API requests
- [x] Sourcing of data using user input and/or a downloaded .csv or .json dataset
- [x] Caching of data you continually retrieve from the internet in some way

### Submission
- [ ] I included a link to my GitHub repository with the correct permissions on Canvas! (Did you though? Did you actually? Are you sure you didn't forget?)
- [ ] I included a summary of my project and how I thought it went **in my Canvas submission**!
