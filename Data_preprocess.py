from GoogleNews import GoogleNews


googlenews = GoogleNews()
googlenews = GoogleNews(lang='en')
googlenews = GoogleNews(start='02/28/2020', end='02/28/2020')
googlenews = GoogleNews(encode='utf-8')
googlenews.get_news('IBM')
titles = googlenews.get_texts()



