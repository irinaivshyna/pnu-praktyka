from DBconnection import DBconnection
import re


class AccessID(DBconnection):
    def accessID(self):
        db = DBconnection().getConnection()
        cursor = db.cursor(buffered=True)
        query = ("SELECT id FROM country")
        cursor.execute(query)
        countriesID = cursor.fetchall()
        cursor.close()
        db.close()
        for countryID in countriesID:
            stringID = str(countryID) 
            cID = int(re.search(r'\d+', stringID).group())
            yield cID