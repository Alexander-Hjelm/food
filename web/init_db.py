import os
import re
import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

for filename in os.listdir(os.path.join(os.getcwd(), "..", "recipes")):
    filename_stripped = os.path.splitext(filename)[0]
    with open(os.path.join(os.getcwd(), "..", "recipes", filename), 'r', encoding='utf-8') as f: # open in readonly mode
        content = f.read()
        content_searchable = ""

        content_stripped = content.replace("\n", "").replace("-", "").replace("|", "")

        # Title searchable
        m = re.search('#(.+?)>', content_stripped)
        if m:
            content_searchable += m.group(1)

        # Tags searchable
        m = re.search('## Tags(.+?)## Ingredients', content_stripped)
        if m:
            content_searchable += m.group(1)

        # Ingredients searchable
        m = re.search('## Ingredients(.+?)## Instructions', content_stripped)
        if m:
            content_searchable += m.group(1)

        cur.execute("INSERT INTO recipes (content, recipe_id, content_searchable) VALUES (?, ?, ?)", (content,filename_stripped,content_searchable))

connection.commit()
connection.close()