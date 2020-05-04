from newspaper import Article
import newspaper
import json

class categoriesHtmlWithURLDetails:
    def __init__(self, NewsPaperName, html, url):
        self.NewsPaperName = NewsPaperName
        self.html = html
        self.url = url

categoriesHtmlWithURL = []

def timesOfIndia_Function():
   timesOfIndia = newspaper.build('https://www.timesofindia.com/world')
   return timesOfIndia

def categoryUrl():
    for category in timesOfIndia_Function().category_urls():
        categoryUrl = category
    for article in timesOfIndia_Function().articles:
        articleUrl = article.url

def getHTMLWithUrl():
    for categories in timesOfIndia_Function().categories:

        categoriesHtmlWithURL.append(categoriesHtmlWithURLDetails('TimesOfIndia',categories.url,categories.html))
    return categoriesHtmlWithURL

categoryUrl()
html = json.dumps(getHTMLWithUrl(), default=lambda o: o.__dict__, sort_keys=True, indent=4)

timesOfIndia_Function().download()
timesOfIndia_Function().parse()
timesOfIndia_Function().nlp()

feeds = timesOfIndia_Function().download_feeds()
value = feeds