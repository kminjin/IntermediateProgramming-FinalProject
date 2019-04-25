# SI 507 Final Project: Flask Application Which Allows You to View Countries and Continents.

by Min Jin Kim

[Link to this repository](https://github.com/michellek1995/finalproject)

---

## Project Description
I scraped my data from a wikipedia page with a list of countries then went into each link and also scraped data for each country. I found a csv with list of countries and continents. I then merged a column of continents in the continents.csv with the cleaned country csv and created a new csv to transfer information into a database. Then from the same csv, I created a separate table of continents where which continent was given an id. I then connected the tables by the ids of continents going into the table of countries. My Flask app has three routes index, all_continents which displays all continents and their ID using a template, and all_countries which displays all countries, population, and percentage of world population using a template.



[Database Diagram](https://docs.google.com/document/d/1SjZxCZpYq6sDtC8OhyiG4sWar8sjkY6VpvgeVPiammQ/edit?usp=sharing)




## How to run

1. First, while in the "base" virtual environment (default environment which conda itself is installed into, "root"), install all requirements with `pip install -r requirements.txt` If this does not work,go into Anaconda Navigator, go to the root environment and click non installed packages and activate the required packages manually.
2. Then, type in "python SI507project_tools.py" in the terminal while in the base virtual environment with new installed requirements. This will create the country table.
3. Then, run newcountrycsv.py which will create a new merged csv for a database.
4. Then, run db.py (type "python db.py runserver" at terminal) which will create the database with two tables and set up flask.

## How to use

1. There are links in the homepage for easy navigation.
2. (Optional): Markdown syntax to include an screenshot/image: ![alt text](image.jpg)
3. (Optional): Markdown syntax to include an screenshot/image: ![alt text](image.jpg)

## Routes in this application
- `/` -> The index will display Links in the views of Flask application pages
- `/all_countries` -> this route displays all the countries, its population, and population %.
- `/all_continents` -> this route displays all the continents and its IDs.


## How to run tests
1. While in conda, if not "conda activate", do a pip install -r requirements.txt
2. Enter python SI507project_tests.py

## In this repository:
- SI507project_tests.py
- SI507project_tools.py
- README.md
- advanced_expiry_caching.py
- continents.csv (downloaded from https://datahub.io/JohnSnowLabs/country-and-continent-codes-list)
- dp.py
- newcountrycsv.py
- requirements.txt

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
