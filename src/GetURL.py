from urllib.request import urlopen


class GetURL:
    def getUrl(self): 
        url = urlopen("https://en.numista.com/catalogue/index.php?ct=coin")
        return url






