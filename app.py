from flask import Flask, request, jsonify, send_from_directory
import os
from crime_data import crime_data


app = Flask(__name__)

@app.route('/api/crime-data', methods=['GET'])
def get_crime_data():
    borough = request.args.get('borough')
    borough = borough.title()  # Make sure it's like "Bronx", "Queens", etc.
    if borough in crime_data:
        return jsonify(crime_data[borough])
    else:
        return jsonify({"error": "Borough not found"}), 404
@app.route('/<path:path>')
def static_file(path):
    return send_from_directory(os.getcwd(), path)

if __name__ == "__main__":
    app.run(debug=True)
