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

def process_sources()
