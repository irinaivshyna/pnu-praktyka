from urllib.request import urlopen
from bs4 import BeautifulSoup
from DataAccess import DataAccess

class ParsingArea(DataAccess):
    def parsingArea(self):
        pages = DataAccess().accessUrl()
        for page in pages: 
            soup = BeautifulSoup(urlopen(page), "html.parser")
            parsingArea = soup.findAll("div", class_="description_piece")
            for parsingItem in parsingArea:
                coinLink = parsingItem.findAll("a") 
                yield coinLink 