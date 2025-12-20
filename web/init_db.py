import os
import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

for filename in os.listdir(os.getcwd() + "\\..\\recipes"):
    filename_stripped = os.path.splitext(filename)[0]
    with open(os.path.join(os.getcwd(), "..", "recipes", filename), 'r', encoding='utf-8') as f: # open in readonly mode
        content = f.read()
        cur.execute("INSERT INTO recipes (content, recipe_id) VALUES (?, ?)", (content,filename_stripped,))

connection.commit()
connection.close()