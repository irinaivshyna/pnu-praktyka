from DBconnection import DBconnection
from GetCoinLinks import GetCoinLinks
from GetCoinNames import GetCoinNames
from AccessID import AccessID 
import time


class CoinRepository(DBconnection):
    def parseCoins(self):
        coinNames = GetCoinNames().getCoinNames()
        coinUrls = GetCoinLinks().getCoinLinks()
        countriesID = AccessID().accessID()
        db = DBconnection().getConnection()
        cursor = db.cursor(buffered=True)
        for coinName, coinUrl, countryID in zip(coinNames, coinUrls,countriesID):
                query = "INSERT INTO coin (title, url, country_id) VALUES (%s, %s, %s)"
                value = (coinName, coinUrl, countryID)
                cursor.execute(query, value)
                db.commit()
                print(coinName, coinUrl)
                time.sleep(1)                       
        cursor.close()
        db.close()
            
parser = CoinRepository()
parser.parseCoins()