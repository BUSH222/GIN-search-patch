import pathlib
import sqlite3
from flask import Flask, render_template, request, redirect


app = Flask(__name__)


def load_db():
    conn = sqlite3.connect("db.db")
    cur = conn.cursor()
    p = pathlib.Path(__file__).parent.resolve().glob('**/*.sql')
    toread = list(map(str, p))
    if len(toread) > 1:
        print('remove the old db')
    toread = toread[0]
    data_raw = []
    data = []
    with open(toread) as q:  # what am i doing
        query = q.readlines()
        for item in query:
            if item.startswith('('):
                data_raw.append(item)
    print(len(data_raw))
    for item in data_raw:
        item = item[1:].strip().split(', ', maxsplit=19)
        id_ = int(item[0])
        name = item[1][1:-1].strip()
        bio = item[-1]
        data.append([id_, name.lower(), bio.lower()])
    query = """DROP TABLE IF EXISTS people;
CREATE TABLE people (
    id INTEGER PRIMARY KEY,
    name INTEGER,
    bio STRING);"""
    cur.executescript(query)
    for r in data:
        cur.execute('INSERT INTO people VALUES (?, ?, ?)', r)
    conn.commit()


@app.route("/")
def ginsearch():
    """search page for gin search patch"""
    return render_template('search-ginsearch-patch.html')


@app.route("/view")
def ginsearch_view():
    """view records page for gin search patch"""
    conn = sqlite3.connect("db.db")
    cur = conn.cursor()
    query = dict(request.args)
    if len(query) == 2:
        tosearch = str(query['query']).strip()
        print(tosearch)
        if query['category'] == 'content':
            res = cur.execute("SELECT * FROM people WHERE bio LIKE ?", ('%' + tosearch.lower() + '%',))
        elif query['category'] == 'person':
            res = cur.execute("SELECT * FROM people WHERE name LIKE ?", ('%' + tosearch.lower() + '%',))
        else:
            return redirect('/ginsearch')  # nothing
        to_process = res.fetchall()
        out = []
        for i in range(len(to_process)):
            print(to_process[i][1].title())
            out.append([to_process[i][0], to_process[i][1].title(), to_process[i][2]])
        return render_template('search-ginsearch-view.html', data=out)
    else:
        return redirect('/ginsearch')


if __name__ == '__main__':
    # load_db()
    app.run()
