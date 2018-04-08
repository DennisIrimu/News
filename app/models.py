class Source:
    '''
    Class that defines Source Objects
    '''
    def __init__(self,id,name,description):
        '''
        define properties of the Source
        '''
        self.id = id
        self.name = name
        self.description = description

class Article:
    '''
    Class that defines Article Objects
    '''
    def __init__(self,source,title,urlToImage,description,urlToArticle,publishedAt):
        '''
        define properties of an article
        '''
        self.source = source
        self.title = title
        self.urlToImage = urlToImage
        self.description = description
        self.urlToArticle = urlToArticle
        self.publishedAt = publishedAt

    
