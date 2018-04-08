import urllib.request,json
from .models import Source, Article

api_key = None

def configure_request(app):
    global api_key
    api_key = app.connfig['NEWS_API_KEY']

def get_sources():
    '''
    Getting json response o url requests
    '''
    get_sources_url = 'https://newsapi.org/v1/sources'

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        geT_sources_response = json.loads(geT_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = geT_sources_response['sources']
            sources_results = process_sources(sources_results_list)

    return sources_results

def process_sources():
    '''
    Function to process the source results to change from JSON language
    '''
    source_results = []

    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')

        source_object = Source(id,name,description)

        source_results.append(source_object)

    return source_results

def get_articles():
    '''
    Function to get a source and it's get_articles
    '''
    get_articles_url = 'https://newsapi.org/v1/articles?source={}&apikey={}'.format(id,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_sources_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)

    return articles_results

def process_articles(article_list):
    '''
    Function that processes article results
    '''
    article_results = []

    for article_item in article_list:
        source = article_item.get('source')
        title = article_item.get('title')
        urlToImage = article_item.get('urlToImage')
        description = article_item.get('description')
        urlToArticle = article_item.get('url')
        publishedAt = article_item.get('publishedAt')

        
