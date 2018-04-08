import os

class Config:
    '''
    for general configuration
    '''
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
