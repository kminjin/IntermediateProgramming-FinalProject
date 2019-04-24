import os
# tools that will make it easier to build on things
from flask import Flask, render_template, session, redirect, url_for
# handles database stuff for us - need to pip install flask_sqlalchemy in your virtual env, environment, etc to use this and run this
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from settinguptable import *

# Application configurations
app = Flask(__name__)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'adgsdfsadfdflsdfsj'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./countries.db' # TODO: decide what your new database name will be -- that has to go here
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Set up Flask debug stuff
db = SQLAlchemy(app) # For database use
session = db.session # to make queries easy

collections = db.Table('collections',db.Column('continents_id',db.Integer, db.ForeignKey('continents.id')))

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(64))
    Population= db.Column(db.Integer)
    population_percentage=db.Column(db.String(64))
    Area=db.Column(db.Integer)
    water_percentage=db.Column(db.String(64))
    totalGDP=db.Column(db.String(64))
    capitaGDP=db.Column(db.String(64))
    continent=db.Column(db.String(64), db.ForeignKey("continents.id"))

    def __repr__(self):
        return "{} has {} people and is {} km^2 big".format(self.country,self.population, self.area)


class Continents(db.Model):
    __tablename__="continents"
    id = db.Column(db.Integer, primary_key=True)
    continent=db.Column(db.String(64))
    countries= db.relationship("Country", backref='World')


def get_country(file):
    csvfile=open(file, "r", encoding='UTF-8')
    reader=csv.reader(csvfile)
    hesder=next(csvfile)

    for row in reader:
        country_info= Country.query.filter_by(country=row[0]).first()
        if not country_info:
            country_info=Country(country=row[0],Population=row[1], population_percentage=row[2],Area=row[3],water_percentage=row[4],totalGDP=row[5],capitaGDP=row[6],continent=row[7])
        session.add(country_info)
        session.commit()


# with open("new_countriestable.csv", "r") as csv_file:
#     contents=csv_file.readlines()
#     inforeq=contents[1:]
#
# for row in inforeq:



##### Set up Controllers (route functions) #####

#
#
@app.route('/')
def index():
    return '<h1> Hello, everyone!</h1>'

# #
# @app.route('/new/movie/<title>/<director>/<releaseDate>')
# def new_movie(title, director, releaseDate):
#     if Movie.query.filter_by(title=title).first(): # if there is a song by that title
#         return "That movie already exists! Go back to the main app!"
#     else:
#         director = get_or_create_director(director)
#         movie = Movie(title=title, director_id=director.id,releaseDate=releaseDate)
#         session.add(movie)
#         session.commit()
#         return "New movie: {} by {}. Check out the /all_movies for ALL movies to see the whole list.".format(movie.title, director.name)
#
# #
# @app.route('/all_movies')
# def see_all():
#     all_movies=[]
#     movies= Movie.query.all()
#     for m in movies:
#         director=Director.query.filter_by(id=m.director_id).first()
#         all_countries.append((m.title,director.name, m.releaseDate))
#     return render_template('all_movies.html',all_movies=all_movies)
#
#
if __name__ == '__main__':
    db.create_all() # This will create database in current directory, as set up, if it doesn't exist, but won't overwrite if you restart - so no worries about that
    get_country("new_countriestable.csv")
    app.run() # run with this: python main_app.py runserver
