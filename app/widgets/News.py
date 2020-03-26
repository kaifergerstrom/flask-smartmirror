import newsapi
from newsapi.articles import Articles

# Get n amount of news headlines
def get_news(limit=5):
	# Authorize the news api
	apikey = '1a4e2bcd0c2b40e48786ccdbf916959a'

	# Get article information
	a = Articles(API_KEY=apikey)
	articles = a.get(source="cnn", sort_by='popular')

	headlines = {}
	# Loop and create headlines 
	for index, article in enumerate(articles['articles'], start=1):
		headlines[article['title']] = article['description']  # Populate dictionary
		if index == limit:  # Once limit is reached, end the loop
			break

	return headlines  # Return headlines dictionary


if __name__ == '__main__':
	print(get_news())