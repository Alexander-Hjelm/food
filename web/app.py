import sqlite3
import markdown
from flask import Flask, render_template, request, flash, redirect, url_for
from markdown.extensions.tables import TableExtension

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this should be a secret random string'

@app.route('/')
def index():
    conn = get_db_connection()
    db_recipes = conn.execute('SELECT id, created, content, recipe_id FROM recipes;').fetchall()
    conn.close()

    recipes = []
    for recipe_key in db_recipes:
       recipe = dict(recipe_key)
       recipe['content'] = markdown.markdown(recipe['content'], extensions=[TableExtension(use_align_attribute=True)])
       recipes.append(recipe)

    return render_template('index.html', recipes=recipes)

@app.route('/recipes/<page>')
def recipe(page: str):
    conn = get_db_connection()
    db_recipes = conn.execute(f'SELECT id, created, content, recipe_id FROM recipes WHERE recipe_id="{page}";').fetchall()
    conn.close()

    if len(db_recipes) == 0:
        return render_template('404.html')

    recipes = []
    for recipe_key in db_recipes:
       recipe = dict(recipe_key)
       recipe['content'] = markdown.markdown(recipe['content'], extensions=[TableExtension(use_align_attribute=True)])
       recipes.append(recipe)

    return render_template('index.html', recipes=recipes)
