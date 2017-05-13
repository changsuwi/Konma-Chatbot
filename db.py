# -*- coding: utf-8 -*-


import pymongo


#  Standard URI format: mongodb://[dbuser:dbpassword@]host:port/dbname

uri = 'mongodb://vic010744:vic32823@ds135700.mlab.com:35700/heroku_4w25h5pt'

###############################################################################
# main
###############################################################################


def upload_flag(flag, sender_id):
    client = pymongo.MongoClient(uri)
    db = client.get_default_database()
    Category = db['flag']
    query = {'ID': sender_id}
    if(Category.count(query) == 0):
        Category.insert_one({'ID': sender_id, 'flag': flag})
    else:
        query = {'ID': sender_id}
        Category.update(query, {'$set': {'flag': flag}})


def get_flag(sender_id):
    client = pymongo.MongoClient(uri)
    db = client.get_default_database()
    Category = db['flag']
    dat = Category.find_one({'ID': sender_id})
    return dat['flag']


def upload_db_photo_url(url, sender_id):
    client = pymongo.MongoClient(uri)
    db = client.get_default_database()
    # First we'll add a few songs. Nothing is required to create the songs
    # collection; it is created automatically when we insert.

    Postcard = db['postcard']

    # Note that the insert method can take either an array or a single dict.
    query = {'ID': sender_id}
    if(Postcard.count(query) == 0):
        SEED_DATA = {
            'url': url,
            'ID': sender_id
        }
        print Postcard.insert_one(SEED_DATA)
    else:
        Postcard.update(query, {'$set': {'url': url}})


def upload_db_intro(text, sender_id):
    client = pymongo.MongoClient(uri)

    db = client.get_default_database()
    # First we'll add a few songs. Nothing is required to create the songs
    # collection; it is created automatically when we insert.

    Postcard = db['postcard']
    query = {'ID': sender_id}
    Postcard.update(
        query, {'$set': {'intro': text, 'match': '0', 'match_id': "None"}})
    client.close()
