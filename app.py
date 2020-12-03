from flask import Flask, jsonify
import psycopg2

conn = psycopg2.connect(dbname="pet_hotel",)

cur = conn.cursor()

app = Flask(__name__)

@app.route('/pets')
def getPets():
    cur.execute('SELECT * from pets;')
    records = cur.fetchall()
    return jsonify(records[1])


app.run()