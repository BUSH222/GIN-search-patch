import pathlib
import sqlite3


def load_db():
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
        data.append([id_, name, bio])
    conn = sqlite3.connect("db.db")
    cur = conn.cursor()
    query = """DROP TABLE IF EXISTS people;
CREATE TABLE people (
    id INTEGER PRIMARY KEY,
    name INTEGER,
    bio STRING);"""
    cur.executescript(query)
    for r in data:
        cur.execute('INSERT INTO people VALUES (?, ?, ?)', r)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    load_db()
