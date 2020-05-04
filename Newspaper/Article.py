import nltk
from newspaper import Article


#Get the article
url = 'https://timesofindia.indiatimes.com/blogs/seeing-the-invisible/testing-and-contact-tracing-cant-eradicate-sars-cov-2-part-2/'
article = Article(url)


# Do some NLP
article.download() #Downloads the link’s HTML content
article.parse() #Parse the article
nltk.download('punkt')#1 time download of the sentence tokenizer
article.nlp()#  Keyword extraction wrapper


#Get the authors
article.authors

#Get the publish date
article.publish_date

#Get the top image
article.top_image

#Get the article text
print(article.text)

#Get a summary of the article
print(article.summary)