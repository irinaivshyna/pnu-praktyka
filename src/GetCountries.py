from GetArea import GetArea

class GetCountries(GetArea):
    def getCountryItems(self):
        content_area = GetArea().getContentArea()
        for country in content_area:
            country_item = country.find("a").get_text()
            yield country_item