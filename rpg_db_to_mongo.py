# MongoDB was easier to connect the data.
# Converting sqlite3 to dict was fairly easy to find
# However it just makes more sense intuituvely when moving
# sqlite3 to PostgreSQL


import sqlite3
import pymongo

# Get the data from sqlite3
select_query = """SELECT *
FROM (SELECT *
      FROM (SELECT *
            FROM charactercreator_character
                     LEFT JOIN charactercreator_character_inventory
                               on charactercreator_character.character_id =
                                  charactercreator_character_inventory.character_id) as char_inventory
               LEFT JOIN armory_item on char_inventory.item_id = armory_item.item_id) as char_inventory_item
         INNER JOIN armory_weapon on char_inventory_item.item_id = armory_weapon.item_ptr_id"""

sl_conn = sqlite3.connect('rpg_db.sqlite3')
results = sl_conn.execute(select_query).fetchall()


# Data to dict form
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


sl_conn.row_factory = dict_factory
curs = sl_conn.cursor()
curs.execute
results = sl_conn.execute(select_query).fetchall()

# Connecting to MongoDB
connection_string = "mongodb://localhost:27017/test?retryWrites=true&w=majority"
client = pymongo.MongoClient(connection_string)
db = client.test

for result in results:
    db.test.insert_one(result)

print(list(db.test.find()))
