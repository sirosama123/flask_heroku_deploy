from flask import Flask, jsonify,json
from sqlalchemy import null

app = Flask(__name__)

@app.route('/data')
def get_data():
    with open("data.json") as json_file:
        data = json.load(json_file)
        return jsonify(data)
        
app.run(debug=True)


