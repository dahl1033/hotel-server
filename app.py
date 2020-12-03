from flask import Flask
import psycopg2

conn = psycopg2.connect(
    dbname="pet_hotel",
)

cur = conn.cursor()

cur.execute('SELECT * from owners;')

records = cur.fetchall()

print(records)
    # user="leroydahl",
    # password="Randy2020!"

app = Flask(__name__)

@app.route('/')
def helloWorld():
    return {'hello': 'world'}

app.run()