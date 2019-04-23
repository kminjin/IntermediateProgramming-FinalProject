import sqlite3
import unittest

# (100 points) A code file SI507project_tests.py which includes a test suite with
# Reasonable tests for the code in SI507project_tools.py
# Tests for any other functionality you want to include that isn't included yet (the tests DO NOT have to pass right now, and maybe shouldn't! They just have to be written for TDD use)
# Does not have to be A LOT of tests, whatever that means to you, just enough to check that functions/class methods/etc will work properly, whether or not they do now.
# A good way to judge is to make sure you have at least eight individual test methods themselves, or are testing at least four or five 'things' (sentences that are descriptions of something to test). Most test suites of this nature, at this scale, would normally be much more than 8 test methods, so this is not a lot to do comparatively!
#


#IMPORTANT INFO: Not sure about the code yet but I will be testing the following:
#test if csv has 202 number of rows.
#test if type of response is a correct type.
#test if % is in any csv data for countries population table.
#test if continent csv has right number of states.

class finalprojectSQLiteDBTests(unittest.TestCase):

	def setUp(self):
		self.conn = sqlite3.connect("somedatabase.sqlite") # Connecting to database that should exist in autograder
		self.cur = self.conn.cursor()

	def test_for_countries_table(self):
		self.cur.execute("select countrycode, englishname, region, population, area from countries where countrycode = 'ALA'")
		data = self.cur.fetchone()
		self.assertEqual(data,('ALA', 'Åland Islands', 'Europe', 28875, 1580.0), "Testing data that results from selecting country ALA")

	def test_chocolate_insert_works(self):
		chocolate = ('A. Morin', 'Kappi', '2015', 70.0, "Haiti", 2.75)
		ch = ('A. Morin', 'Kappi', '2015', 70.0, 98, 2.75)
		self.cur.execute("insert into chocolatebars(company, specificBeanBarName, reviewDate, cocoaPercent, companyCountry, rating) values (?, ?, ?, ?, (select id from countries where englishname=?), ?)", chocolate)
		self.conn.commit()

		self.cur.execute("select company, specificBeanBarName, reviewDate, cocoaPercent, companyCountry, rating from chocolatebars where specificBeanBarName= 'Kappi'")
		data = self.cur.fetchone()
		self.assertEqual(data,ch,"Testing another select statement after a sample insertion")

	def test_for_chocolate_table(self):
		res = self.cur.execute("select * from chocolatebars")
		data = res.fetchall()
		self.assertTrue(data, 'Testing that you get a result from making a query to the chocolatebars table')

	def test_country_insert_works(self):
		country = ('SIR', '507 Islands', 'Europe', 28875, 1580.0)
		self.cur.execute("insert into countries(countrycode, englishname, region, population, area) values (?, ?, ?, ?, ?)", country)
		self.conn.commit()

		self.cur.execute("select countrycode, englishname, region, population, area from countries where countrycode = 'SIR'")
		data = self.cur.fetchone()
		self.assertEqual(data, country, "Testing a select statement where countrycode = SIR")


	def test_foreign_key_chocolate(self):
		res = self.cur.execute("select * from chocolatebars INNER JOIN countries ON chocolatebars.companyCountry = countries.id")
		data = res.fetchall()
		self.assertTrue(data, "Testing that result of selecting based on relationship between chocolatebars and countries does work")
		self.assertTrue(len(data) in [1795, 1796], "Testing that there is in fact the amount of data entered that there should have been -- based on this query of everything in both tables.{}".format(len(data)))


	def tearDown(self):
		self.conn.commit()
		self.conn.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)
