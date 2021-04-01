from GetArea import GetArea
from urllib.parse import urljoin

class GetLinks(GetArea):
    def getLinks(self):
        content_area = GetArea().getContentArea()
        primaryLink = "https://en.numista.com"
        for country_link in content_area:
            link = country_link.find("a").get("href")
            finalLink = urljoin(primaryLink, link)
            yield finalLink
           