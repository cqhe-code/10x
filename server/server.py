#!/usr/bin/env python
import os
from flask import Flask, request, jsonify
from util import WeatherDataReader, WeatherDataQuery
from datetime import datetime
from copy import deepcopy

app = Flask(__name__)

PATH = "data/seattle-weather.csv"
data_reader = WeatherDataReader(PATH)
colnames = data_reader.colnames()
data = data_reader.data()

def combine_data(colnames, data):
    result = []
    for row in data:
        result.append({colnames[i]:r for i,r in enumerate(row)})
    return result

@app.route('/query')
def query():
    limit_str = request.args.get('limit', "")
    weather_type = request.args.get('type', "")
    date_str = request.args.get('date', "")
    try:
        limit, date = None, None
        if limit_str:
            limit = int(limit_str)
        if date_str:
            date = datetime.strptime(date_str, '%Y-%m-%d')
        print(f'weather_type: {weather_type}, limit:{limit_str}, date: {date}')
        result = WeatherDataQuery(deepcopy(data))\
            .query_by_limit(limit)\
            .query_by_weather(weather_type)\
            .query_by_date(date).data()
        return jsonify({'result': combine_data(colnames, result)}), 200
    except Exception as e:
        return jsonify({'code': 400, 'error': getattr(e, 'message', repr(e))}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 9090), debug=True)
