import pymongo
import json

def load_json_to_mongo(json_file):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["dashboard_db"]
    collection = db["data"]

    # Open the file with 'utf-8' encoding to avoid encoding errors
    with open(json_file, encoding='utf-8') as file:
        file_data = json.load(file)

    # Insert the data into MongoDB
    if isinstance(file_data, list):
        collection.insert_many(file_data)
    else:
        collection.insert_one(file_data)

    print("Data inserted successfully")

if __name__ == "__main__":
    load_json_to_mongo("data/jsondata.json")
