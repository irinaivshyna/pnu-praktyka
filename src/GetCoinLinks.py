from ParsingArea import ParsingArea
from urllib.parse import urljoin


class GetCoinLinks(ParsingArea):
    def getCoinLinks(self):
        commonParsingArea = ParsingArea().parsingArea()
        primaryLink = "https://en.numista.com"     
        for parsingArea in commonParsingArea:  
            for coinItems in parsingArea:
                link = coinItems.get("href")
                coinLink = urljoin(primaryLink, link)
                yield coinLink