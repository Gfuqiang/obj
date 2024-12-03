import pprint

from pymongo.errors import CollectionInvalid
from pymongo import MongoClient, ASCENDING
import urllib.parse
from bson.objectid import ObjectId


class MongoSearchClient:

    def __init__(self, db_name, host, collection=None):
        self.host = host
        self.mongo_client = self._init_client()
        self.db = self.mongo_client[f'{db_name}']
        self.collection_name = collection

    def _init_client(self):
        return MongoClient(f"mongodb://scmdb:kOlXPoOG6t16GZ11c5q4hsZN@{self.host}:27017/?timeoutMS=3000")

    def get_collection(self, collection_name):
        if not (collection := getattr(self.db, collection_name)):
            raise CollectionInvalid
        return collection

    @property
    def collection(self):
        if not (collection := getattr(self.db, self.collection_name)):
            raise CollectionInvalid
        return collection

    def lookup_search(self):
        asset_entity = [
            ('assets_entity_software', 'software'),
            ('assets_entity_open_ports', 'open_ports'),
            ('assets_entity_process_list', 'process_list'),
            ('assets_entity_services', 'services')
        ]
        pipline = []
        for model, _as in asset_entity:
            lookup_temp = {
                'from': model,
                'localField': 'deviceId',
                'foreignField': 'deviceId',
                'as': _as
            }
            pipline.append({'$lookup': lookup_temp})
        pipline.append(
            {"$project": {"osType": 1, "deviceName": 1, "_adapters.AdapterInstanceName": 1, "software.name": 1,
                          "software.version": 1}},
        )
        pipline.append({'$match': {}})
        cursor = self.collection.aggregate(pipline)

        for data in cursor:
            print(data)

    def aggregate_search(self):
        result = self.collection.aggregate([
            {
                "$match": {
                    "_id": {"$in": [ObjectId('64eee3ea25e3961486159996')]}
                }
            },
            {
                '$lookup': {
                    'from': 'assets_entity_software',
                    'localField': 'deviceId',
                    'foreignField': 'deviceId',
                    'as': 'results'
                }
            },
            {
                '$lookup': {
                    'from': 'assets_entity_openPorts',
                    'localField': 'deviceId',
                    'foreignField': 'deviceId',
                    'as': 'results1'
                }
            },
            # {
            # '$unwind': "$results"
            # },
            {
                '$project': {
                    '_id': 1,
                    '_adapters': 0,
                    '_adapters_data': 0,
                    'results._adapters': 0,
                    'results._adapters_data': 0,
                    'results1._adapters': 0,
                    'results1._adapters_data': 0
                }
            }
        ])
        for data in result:
            pprint.pprint(data)

