from pymongo import MongoClient
import os

mongo_uri = os.getenv('MONGO_URI')

client = MongoClient(mongo_uri)


def get_client():
    return client