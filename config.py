import os

class Config:
    '''
    for general configuration
    '''
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
class ProdConfig(Config):
    '''
    Child class for production
    '''
class Devconfig(Config):
    '''
    Child class for development
    '''

    DEBUG= True

    config_options = {
    'development': DevConfig,
    'production': ProdConfig
    }
