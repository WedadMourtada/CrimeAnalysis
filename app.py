from flask import Flask, request, jsonify, send_from_directory
import os
from crime_data import crime_data

app = Flask(__name__)

# Borough statistics dictionary
STATS = {
    "MANHATTAN": {"unemployment_rate": 4.5, "median_income": 175743, "education_level": 60},
    "BROOKLYN": {"unemployment_rate": 5.2, "median_income": 115625, "education_level": 40},
    "QUEENS": {"unemployment_rate": 5.0, "median_income": 106667, "education_level": 35},
    "BRONX": {"unemployment_rate": 6.5, "median_income": 66878, "education_level": 25},
    "STATEN ISLAND": {"unemployment_rate": 4.8, "median_income": 119550, "education_level": 35},
}

@app.route('/api/crime-data', methods=['GET'])
def get_crime_data():
    borough = request.args.get('borough')
    borough = borough.upper()  # Convert to uppercase to match STATS keys
    
    # Get crime data
    crime_stats = crime_data.get(borough.title(), {})
    
    # Get borough statistics
    borough_stats = STATS.get(borough, {})
    
    # Combine both sets of data
    response_data = {
        **crime_stats,
        "unemployment_rate": borough_stats.get("unemployment_rate"),
        "median_income": borough_stats.get("median_income"),
        "education_level": borough_stats.get("education_level")
    }
    
    if response_data:
        return jsonify(response_data)
    else:
        return jsonify({"error": "Borough not found"}), 404

@app.route('/<path:path>')
def static_file(path):
    return send_from_directory(os.getcwd(), path)

if __name__ == "__main__":
    app.run(debug=True)
