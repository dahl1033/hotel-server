from flask import Flask, jsonify
import psycopg2

conn = psycopg2.connect(dbname="pet_hotel",)

# cur = conn.cursor()
# dict_cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
dict_cur = conn.cursor(cursor_factory=psycopg2.DictCursor)

app = Flask(__name__)

@app.route('/pets')
def getPets():
    print('got to pets')
    dict_cur.execute('SELECT * from pets;')
    records = dict_cur.fetchall()
    print('what records are')
    return jsonify(records)


app.run()