import logging

import azure.functions as func
import os
import json
import pymongo
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        url = os.environ['connection']
        print(f"Url: {url}")
        client = pymongo.MongoClient(url)
        database = client['lab2db']
        collection = database['notes']
        print(f"Collection: {collection}")

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request", status_code=400)
