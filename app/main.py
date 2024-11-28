from flask import Flask, jsonify
from models import Bus

app = Flask(__name__)


@app.route('/bus/all', methods=['GET'])
def get_all_bus():
    resultsList = []
    result = Bus.query.limit(50).all()
    for r in result:
        resultsList.append(r.__repr__())
    return jsonify(resultsList)


app.run()
