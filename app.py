from flask import Flask, jsonify
import psycopg2
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "pet_hotel"
db = SQLAlchemy(app)
migrate = Migrate(app, db)
class PetsModel(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    owners_id = db.Column(db.Integer())
    name = db.Column(db.String())
    breed = db.Column(db.String())
    color = db.Column(db.String())
    is_checked_in = db.Column(db.Boolean())

    def __init__(self, owners_id, name, breed, color, is_checked_in):
        self.owners_id = owners_id
        self.name = name
        self.breed = breed
        self.color = color
        self.is_checked_in = is_checked_in
    def __repr__(self):
        return f"<Pet {self.name}>"

class OwnersModel(db.Model):
    __tablename__ = 'owners'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    

    def __init__(self, first_name, last_name):
        self.first_name = breed
        self.last_name = color

@app.route('/pets', methods=['GET'])
def getPets():
    pets = PetsModel.query.all()
    results = [
        {
        "owners_id": pet.owners_id,
        "name": pet.name,
        "breed": pet.breed,
        "color": pet.color,
        "is_checked_in": pet.is_checked_in
        } for pet in pets]
    return {"count": len(results), "pets": results}
    

# cur = conn.cursor()
# # dict_cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
# # dict_cur = conn.cursor(cursor_factory=psycopg2)

# app = Flask(__name__)

# @app.route('/pets')
# def getPets():
#     print('got to pets')
#     cur.execute('SELECT * from pets;')
#     records = cur.fetchall()
#     print('what records are')
#     return jsonify(records)


app.run()