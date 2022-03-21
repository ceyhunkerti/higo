from flask import Flask, request, jsonify
from .api.crm import get_leads
from .api.coin import get_rate
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/leads")
def leads():
    keys = ["phone_work", "first_name", "last_name"]
    result = get_leads(fields=keys)
    return jsonify([{key: getattr(lead, key) for key in keys} for lead in result])


@app.route("/currency")
def currency():
    rate = get_rate()
    return jsonify(rate)
