from pymongo import MongoClient
import os
#import urllib.parse

#username = urllib.parse.quote_plus('root')
#password = urllib.parse.quote_plus('example')

#client = MongoClient('mongodb://%s:%s@127.0.0.1' % (username, password))

mongo_uri = os.getenv('MONGO_URI')

client = MongoClient(mongo_uri)


def get_client():
    return client