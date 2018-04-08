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

    with urllib.request.urlopen(get_sources_data)
