import os
# tools that will make it easier to build on things
from flask import Flask, render_template, session, redirect, url_for
# handles database stuff for us - need to pip install flask_sqlalchemy in your virtual env, environment, etc to use this and run this
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from newcountrycsv import *

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

collections = db.Table('collections',db.Column('continents_id',db.String(64), db.ForeignKey('continents.id')))


class Continent(db.Model):
    __tablename__="continents"
    id = db.Column(db.Integer, primary_key=True)
    continent=db.Column(db.String(64))
    country= db.relationship("Country", backref='World')

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(64))
    Population= db.Column(db.Integer)
    population_percentage=db.Column(db.String(64))
    Area=db.Column(db.Integer)
    water_percentage=db.Column(db.String(64))
    totalGDP=db.Column(db.String(64))
    capitaGDP=db.Column(db.String(64))
    continent=db.Column(db.String(64))
    continentID=db.Column(db.Integer, db.ForeignKey("continents.id"))

    def __repr__(self):
        return "{} has {} people and is {} km^2 big".format(self.country,self.population, self.area)



def get_continent(file):
    csvfile=open(file, "r", encoding='UTF-8')
    reader=csv.reader(csvfile)
    header=next(csvfile)
    for row in reader:
        continent_info= Continent.query.filter_by(continent=row[7]).first()
        if not continent_info:
            continent_info=Continent(continent=row[7])
            session.add(continent_info)
            session.commit()

def get_country(file):
    csvfile=open(file, "r", encoding='UTF-8')
    reader=csv.reader(csvfile)
    header=next(csvfile)
    for row in reader:
        country_info= Country.query.filter_by(country=row[0]).first()
        if not country_info:
            continentid = Continent.query.filter_by(continent=row[7]).first().id
            country_info=Country(country=row[0],Population=row[1], population_percentage=row[2],Area=row[3],water_percentage=row[4],totalGDP=row[5],capitaGDP=row[6],continent=row[7], continentID=continentid)
        session.add(country_info)
        session.commit()


##### Set up Controllers (route functions) #####

#
#
@app.route('/')
def index():
    return render_template('index.html')



@app.route('/all_continents')
def all_continents():
    all_continents=[]
    continents=Continent.query.all()
    for c in continents:
        continent=Continent.query.filter_by(id=c.id).first()
        all_continents.append((c.id, c.continent))
    return render_template('all_continents.html', all_continents=all_continents)

@app.route('/all_countries')
def all_countries():
    all_countries=[]
    countries=Country.query.all()
    for c in countries:
        country=Country.query.filter_by(id=c.id).first()
        all_countries.append((c.country, c.Population,c.population_percentage, c.continentID))
    return render_template('all_countries.html', all_countries=all_countries)




if __name__ == '__main__':
    db.create_all() # This will create database in current directory, as set up, if it doesn't exist, but won't overwrite if you restart - so no worries about that
    get_continent("final_countriesDB.csv")
    get_country("final_countriesDB.csv")
    # get_continent("final_continentsDB.csv")
    app.run() # run with this: python main_app.py runserver
