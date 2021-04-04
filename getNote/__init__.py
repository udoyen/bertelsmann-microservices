import logging

import azure.functions as func
import os
import pymongo
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    doc_id = req.params.get('id')
    if not doc_id:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            doc_id = req_body.get('id')

    if doc_id:
            try:
                url = os.environ['jacklineuduak_DOCUMENTDB']
                client = pymongo.MongoClient(url)
                database = client['lab2db']
                collection = database['notes']

                result = collection.find({id: doc_id})
                result = dumps(result)

                return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
            except:
                return func.HttpResponse("Bad request,", status_code=400)
            else:
                return func.HttpResponse(
                    "This HTTP triggered function executed successfully. Pass the id of the document to get back a json document object.",
                    status_code=200
                )
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass the id of the document as a query string.",
             status_code=200
        )
