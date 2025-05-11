from flask import Flask, request, jsonify, send_from_directory
import os

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
    borough = request.args.get('borough', '').upper()

    data = {
        "MANHATTAN": {"arrests": 22700, "complaints": 48300},
        "BROOKLYN": {"arrests": 28000, "complaints": 55000},
        "QUEENS": {"arrests": 20000, "complaints": 42000},
        "BRONX": {"arrests": 30000, "complaints": 60000},
        "STATEN ISLAND": {"arrests": 10000, "complaints": 20000}
    }

    return jsonify(data.get(borough, {}))

if __name__ == "__main__":
    app.run(debug=True)
