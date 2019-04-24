from numpy import genfromtxt
from time import time
from datetime import datetime
from sqlalchemy import Column, Integer, Float, Date, String, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def Load_Data(file_name):
    data = genfromtxt(file_name, delimiter=',', skip_header=1, converters={0: lambda s: str(s)})
    return data.tolist()

Base = declarative_base()

class Country(Base):
    id = Column(Integer, primary_key=True)
    country = Column(VARCHAR)
    Population= Column(Integer)
    population_percentage=Column(VARCHAR)
    Area=Column(Integer)
    water_percentage=Column(VARCHAR)
    totalGDP=Column(VARCHAR)
    capitaGDP=Column(VARCHAR)
    continent=Column(VARCHAR), ForeignKey("continents.id")

    def __repr__(self):
        return "{} has {} people and is {} km^2 big".format(self.country,self.population, self.area)



if __name__ == "__main__":
    t = time()

    #Create the database
    engine = create_engine('sqlite:///csv_test.db')
    Base.metadata.create_all(engine)

    #Create the session
    session = sessionmaker()
    session.configure(bind=engine)
    s = session()


    try:
        file_name = "final_dataset.csv" #sample CSV file used:  http://www.google.com/finance/historical?q=NYSE%3AT&ei=W4ikVam8LYWjmAGjhoHACw&output=csv
        data = Load_Data(file_name)

        for i in data:
            record = Country(**{
                'country' : datetime.strptime(i[0], '%d-%b-%y').date(),
                'population' : i[1],
                'population_percentage' : i[2],
                'Area' : i[3],
                'water_percentage' : i[4],
                'totalGDP' : i[5],
                'capitaGDP' : i[5],
                'continent' : i[5]
            })
            s.add(record) #Add all the records

        s.commit() #Attempt to commit all the records
    except:
        s.rollback() #Rollback the changes on error
    finally:
        s.close() #Close the connection
