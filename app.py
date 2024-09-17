from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["dashboard_db"]
collection = db["data"]

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/api/data')
def get_data():
    year = request.args.get('year')
    intensity = request.args.get('intensity')
    likelihood = request.args.get('likelihood')
    relevance = request.args.get('relevance')
    country = request.args.get('country')
    topic = request.args.get('topic')
    region = request.args.get('region')
    city = request.args.get('city')

    query = {}
    
    if year:
        query['end_year'] = year
    if intensity:
        query['intensity'] = int(intensity)
    if likelihood:
        query['likelihood'] = int(likelihood)
    if relevance:
        query['relevance'] = int(relevance)
    if country:
        query['country'] = country
    if topic:
        query['topic'] = topic
    if region:
        query['region'] = region
    if city:
        query['city'] = city

    data = list(collection.find(query, {'_id': 0}))
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
