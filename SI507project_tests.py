import sqlite3
import unittest



#IMPORTANT INFO: Not sure about the code yet but I will be testing the following:
#test if csv has 193 number of rows.
#test if type of response is a correct type.
#test if % is in any csv data for countries population table.
#test if continent csv has right number of states.

class finalprojectSQLiteDBTests(unittest.TestCase):

	def setUp(self):
		self.conn = sqlite3.connect('countries.db') # Connecting to database that should exist in autograder
		self.cur = self.conn.cursor()

	def test_for_countries_table(self):
		self.cur.execute("select country, Population, population_percentage, Area, water_percentage, totalGDP, capitaGDP, continent, continentID from countries where country = ' Nigeria'")
		data = self.cur.fetchone()
		self.assertEqual(data,('Nigeria', '193392517', '2.51', 9237682, 1.4, '$447.013 billion','$2,244', 'Africa', '4'), "Testing data that results from selecting country ALA")

	# def test_country_insert_works(self):
	# 	chocolate = ('A. Morin', 'Kappi', '2015', 70.0, "Haiti", 2.75)
	# 	ch = ('A. Morin', 'Kappi', '2015', 70.0, 98, 2.75)
	# 	self.cur.execute("insert into chocolatebars(company, specificBeanBarName, reviewDate, cocoaPercent, companyCountry, rating) values (?, ?, ?, ?, (select id from countries where englishname=?), ?)", chocolate)
	# 	self.conn.commit()
	#
	# 	self.cur.execute("select company, specificBeanBarName, reviewDate, cocoaPercent, companyCountry, rating from chocolatebars where specificBeanBarName= 'Kappi'")
	# 	data = self.cur.fetchone()
	# 	self.assertEqual(data,ch,"Testing another select statement after a sample insertion")

	def test_for_chocolate_table(self):
		res = self.cur.execute("select * from Country")
		data = res.fetchall()
		self.assertTrue(data, 'Testing that you get a result from making a query to the Country table')


	def tearDown(self):
		self.conn.commit()
		self.conn.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)



finalprojectSQLiteDBTests('countries.db')
