import sqlite3
import pymongo
import ssl

sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

character_select_query = """SELECT * FROM charactercreator_character"""

sl_curs.execute(character_select_query)
character_results = sl_curs.fetchall()

mongo_client = pymongo.MongoClient(
    "mongodb://localhost:27017/test?retryWrites=true&w=majority",
    ssl_cert_reqs=ssl.CERT_NONE)
rpg_collection = mongo_client.test.rpg_collection
rpg_collection.drop({})

for character in character_results:
    keys = ['name', 'level', 'exp', 'hp', 'strength', 'intelligence', 'dexterity', 'wisdom']
    doc = {}
    for key, value in zip(keys, list(character)[1:]):
        doc.update({key: value})
    rpg_collection.insert_one(doc)


armory_select_query = """SELECT * FROM charactercreator_character"""

sl_curs.execute(armory_select_query)
character_results = sl_curs.fetchall()

mongo_client = pymongo.MongoClient(
    "mongodb://localhost:27017/test?retryWrites=true&w=majority",
    ssl_cert_reqs=ssl.CERT_NONE)
rpg_collection = mongo_client.test.rpg_collection
rpg_collection.drop({})

for character in character_results:
    keys = ['name', 'level', 'exp', 'hp', 'strength', 'intelligence', 'dexterity', 'wisdom']
    doc = {}
    for key, value in zip(keys, list(character)[1:]):
        doc.update({key: value})
    rpg_collection.insert_one(doc)