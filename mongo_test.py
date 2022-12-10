from pymongo import MongoClient
import urllib.parse

username = urllib.parse.quote_plus('root')
password = urllib.parse.quote_plus('example')


client = MongoClient('mongodb://%s:%s@127.0.0.1' % (username, password))

db = client.test_database

collection = db.test_collection

post = {
    "name": "Test Name",
    "text": "test text here to test the text"
}

posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)