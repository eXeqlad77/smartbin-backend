from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def get_data():
    data = request.get_json()
    print("Veri geldi:", data)  # BU SATIR OLMAZSA LOGDA GÖRÜNMEZ!
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
