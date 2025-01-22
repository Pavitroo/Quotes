from flask import Flask, jsonify
import json
import random
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load quotes from JSON file
with open('quotes.json', 'r') as file:
    quotes = json.load(file)

@app.route('/api/quote')
def get_quote():
    return jsonify(random.choice(quotes))

if __name__ == '__main__':
    app.run(port=3000)
