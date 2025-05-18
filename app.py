from flask import Flask, request, jsonify
import os
import logging

app = Flask(__name__)

# Loglama seviyesini INFO yapıyoruz, böylece info seviyesindeki mesajlar da loglanır
logging.basicConfig(level=logging.INFO)

@app.route('/data', methods=['POST'])
def get_data():
    data = request.get_json()
    logging.info(f" Veri geldi: {data}")  # Burada print yerine logging.info kullandık
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
