from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import csv
my_url='https://www.standardmedia.co.ke/?categoryID=56&pageNo=1'
# opening up connection, grabbing the page
uClient = uReq(my_url)
page_html=uClient.read()
# html parsing
page_soup = soup(page_html,"html.parser")
#grabs each article
containers = page_soup.findAll("div",{"class":"col-xs-4 zero-4"})
with open('website.csv', 'a') as csv_file:
	writer = csv.writer(csv_file)
	header1 = 'Article'
	header2 = 'Date'
	header3 = 'Link'
	writer.writerow([header1,header2,header3])
for container in containers:
	title = container.h4.a.text.strip()
	print(title)
	article_date = container.span.text
	print(article_date)
	article_link = container.div.a["href"]
	print(article_link)
	with open('website.csv', 'a') as csv_file:
		writer = csv.writer(csv_file)
		writer.writerow([title,article_date,article_link])