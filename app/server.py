from flask import Flask, render_template
import json


app = Flask(__name__)

@app.route('/')
@app.route('/notes')
def notes():
    with open('../notes_md/index.json') as f:
        notes_index = json.load(f)
    return render_template('notes.html', index=notes_index)
