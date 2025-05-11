from flask import Flask, request, jsonify, send_from_directory
import os
from crime_data import crime_data

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def serve_index():
    return send_from_directory(os.getcwd(), "index.html")

# Route to serve any static file like borough pages, images, scripts
@app.route('/<path:path>')
def static_file(path):
    return send_from_directory(os.getcwd(), path)

# API route to serve borough-specific arrest and complaint data
@app.route('/api/crime-data')
def get_crime_data():
    borough = request.args.get('borough', '').title()  # Convert to title case to match crime_data keys
    return jsonify(crime_data.get(borough, {}))

if __name__ == "__main__":
    app.run(debug=True, port=5050)
