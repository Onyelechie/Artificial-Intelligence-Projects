from textblob import TextBlob
from newspaper import Article

url = 'https://www.cnbc.com/2023/09/12/decongestant-phenylephrine-ineffective.html'
article = Article(url)
article.download()
article.parse()
article.nlp

text = article.title 
print(text)

blob = TextBlob(text)
sentiment = blob.sentiment.polarity
print(sentiment)