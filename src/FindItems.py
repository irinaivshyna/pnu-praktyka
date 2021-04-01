from GetURL import GetURL
from bs4 import BeautifulSoup

class FindItems(GetURL):
    def findItems(self):
        url = GetURL().getUrl()
        soup = BeautifulSoup(url, "html.parser")
        all_items = soup.findAll("ul", class_="liste_pays")
        return all_items 