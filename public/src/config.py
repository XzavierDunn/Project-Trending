
import os


class Development:
    '''
    Development Environment config
    '''
    DEBUG = True
    TESTING = False


class Production:
    '''
    Production Environment config
    '''
    DEBUG = False
    TESTING = False


app_config = {
    'development': Development,
    'production': Production,
}
