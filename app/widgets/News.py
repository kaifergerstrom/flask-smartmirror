import newsapi
from newsapi.articles import Articles

def get_news():
	#Authorize the api
	apikey = '1a4e2bcd0c2b40e48786ccdbf916959a'

	a = Articles(API_KEY=apikey)
	articles = a.get(source="cnn", sort_by='popular')

	headlines = []
	limit = 5

	for index, article in enumerate(articles['articles']):
		headlines.append([article['title'], article['description']])

		if index >= limit - 1:
			break

	return headlines


if __name__ == '__main__':
	get_news()