from ParsingArea import ParsingArea

class GetCoinNames(ParsingArea):
    def getCoinNames(self):
        commonParsingArea = ParsingArea().parsingArea()
        for parsingArea in commonParsingArea:
            for coinItem in parsingArea:  
                coinData = coinItem.get_text()
                coinName = coinData.strip()
                yield coinName