from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import csv

my_url = ['https://www.standardmedia.co.ke/?categoryID=56&pageNo=2',
          'https://www.standardmedia.co.ke/?categoryID=56&pageNo=3',
          'https://www.standardmedia.co.ke/?categoryID=56&pageNo=4',
          'https://www.standardmedia.co.ke/?categoryID=56&pageNo=5']
# opening up connection, grabbing the page

pages = []
for pg in my_url:
    uClient = uReq(pg)
    page_html = uClient.read()
    # html parsing
    page_soup = soup(page_html, "html.parser")

    # grabs each article
    containers = page_soup.findAll("div", {"class": "cat-pane"})

    for container in containers:
        title = container.h3.a.text
        print(title)
        article_date = container.span.text
        print(article_date)
        article_link = container.div.a["href"]
        print(article_link)
        pages.append((title, article_date, article_link))

with open('website.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    # header1 = 'Article'
    # header2 = 'Date'
    # header3 = 'Link'
    # writer.writerow([header1,header2,header3])
    for title, article_date, article_link in pages:
        writer.writerow([title, article_date, article_link])