from DBconnection import DBconnection
from GetCountries import GetCountries
from GetLinks import GetLinks

class CountryRepository(DBconnection): 
    def parse(self):
        countriesNames = GetCountries().getCountryItems()
        countriesUrls = GetLinks().getLinks()
        db = DBconnection().getConnection()
        cursor = db.cursor(buffered=True)
        for countryName, countryUrl in zip(countriesNames, countriesUrls):
            existedCountryQuery = "SELECT * FROM country WHERE name = %s LIMIT 1"
            cursor.execute(existedCountryQuery,(countryName,))

            if not cursor.fetchone():
                query = "INSERT INTO country (name, url) VALUES (%s, %s)"
                val = (countryName, countryUrl)
                cursor.execute(query, val)

        db.commit()
        cursor.close()
        db.close()

        
"""       
countryRepository = CountryRepository()
countryRepository.parse()"""