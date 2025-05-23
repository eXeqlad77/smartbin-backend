from flask import Flask, request, jsonify
import os
import logging
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv  

load_dotenv()  

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)


app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class SensorData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float, nullable=False)
    humidity = db.Column(db.Float, nullable=False)
    gas = db.Column(db.Float, nullable=False)
    distance = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())

with app.app_context():
    db.create_all()

@app.route('/data', methods=['POST'])
def get_data():
    data = request.get_json()
    logging.info(f" Veri geldi: {data}")

    sensor_data = SensorData(
        temperature=data.get('temperature'),
        humidity=data.get('humidity'),
        gas=data.get('gas'),
        distance=data.get('distance')
    )

    db.session.add(sensor_data)
    db.session.commit()

    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
