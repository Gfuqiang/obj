import pprint
from elasticsearch import Elasticsearch


def get_es_client():
    es = Elasticsearch(
        ['https://10.100.7.1:9200'],
        basic_auth=('elastic', 'JvEDV1igUdZmw5kC'),
        verify_certs=False,
        ssl_show_warn=False
    )
    return es


es_client = get_es_client()
index_name = 'second_test_index'
parent_index_name = 'parent_index'
sub_index_name = 'sub_index_name'


def create_index():
    settings = {
        "number_of_shards": 2,
        "number_of_replicas": 1,
        "max_result_window": 1000000,
        "index.mapping.nested_objects.limit": 10000
    }
    mappings = {
        'settings': settings,
        "mappings": {
            "dynamic_templates": [
                {
                    "default_template": {
                        "match_mapping_type": "*",
                        "match": "FK_*",
                        "mapping": {
                            "type": "object",
                            # "fields": {
                            #     'obj': {
                            #         'type': 'nested'
                            #     }
                            # }
                        }
                    }
                },
                {
                    "text_template": {
                        "match_mapping_type": "long",
                        "mapping": {
                            "type": "text",
                            # "fields": {
                            #     'obj': {
                            #         'type': 'nested'
                            #     }
                            # }
                        }
                    }
                },
                # {
                #     "full_name": {
                #         "path_match": "openPort.*",
                #         # "path_unmatch": "*.middle",
                #         "mapping": {
                #             "type": "nested",
                #             # "copy_to": "full_name"
                #         }
                #     }
                # }
            ],
            "properties": {
                'openPort': {
                    'type': 'nested'
                },
                'networkInterface': {'type': 'object'},
                'age': {'type': 'integer'},
                'score': {'type': 'float'},
                # 'ipv4List': {'type': 'float'},
                "ipv4": {
                    "type": "text",
                    "fields": {
                        "ip": {
                            "type": "ip"
                        }
                    }
                }
            },
            # "nested_objects.limit": 20000
        }
    }
    es_client.indices.create(index=index_name, body=mappings)

    # es_client.indices.create(index=parent_index_name, body=mappings)
    # es_client.indices.create(index=sub_index_name, body=mappings)
    # print(es_client.indices.get_settings(index='assets_account_asset'))
    # print(es_client.indices.get(index="*"))


def delete_index():
    if es_client.indices.exists(index=index_name):
        es_client.indices.delete(index=index_name)


def insert_data():
    document = {
        "hostName": "ETA-BBBB",
        "age": 30,
        "is_active": True,
        "score": 98.11,
        "value": 90,
        "value_float": 95.32,
        "deviceId": "123456",
        "ipv4": ["10.100.7.1", "10.100.10.1"],
        "networkInterface": [{
                "mac": "AE52EA",
                "ipv4List": ['10.100.7.1', '10.100.7.2']
            },
            {
                "mac": "ABC-QWE",
                "ipv4List": ['10.100.7.1', '10.100.7.2']
            }
        ],
        "software": [
            {
                "name": "nginx",
                "version": "1.12.1"
            },
            {
                "name": "uwsgi",
                "version": "1.15.1"
            }
        ],
        "openPort": [
            {
                "port": ["80", "22", "8181"],
                "protocol": "TCP",
                "name": "nginx",
                "version": "1.12.1"
            },
            {
                "port": ["81", "9090", "8181"],
                "protocol": "UDP",
                "name": "uwsgi",
                "version": "1.15.1"
            }
        ],
        "FK_networkInterface": [
            {
                "ip": '127.0.0.1',
                "port": "80"
            },
            {
                "ip": '127.0.0.2',
                "port": "81",
                "ipv4": ["127.0.0.1", "127.0.0.2"]
            }
        ],
        "name": {
            "first": "John",
            "middle": "Winston",
            "last": "Lennon"
        }
    }
    es_client.index(index=index_name, document=document)
    # sub_doc = [
    #     {
    #         "port": 81,
    #         "ip": "172.0.0.1",
    #         "deviceId": "123456"
    #     },
    #     {
    #         "port": 80,
    #         "ip": "172.0.0.2",
    #         "deviceId": "123456"
    #     }
    # ]
    # for item_doc in sub_doc:
    #     es_client.index(index=sub_index_name, document=item_doc)


def search_data():
    query = {
        # "query": {
        "match": {
            "openPort.ip": "172.0.0.1"
        }
        # },
        # "_source": ["name"]
    }
    result = es_client.search(index=index_name, query=query)

    # 处理查询结果
    for hit in result['hits']['hits']:
        pprint.pprint(hit['_source'])


def get_index_mapping():
    mapping_obj = str(es_client.indices.get_mapping(index=index_name))
    mapping = es_client.indices.get_field_mapping(fields='ipv4', index=index_name)
    print(mapping)
    # pprint.pprint(mapping_obj)


def index_exists():
    print(es_client.indices.exists(index=index_name))


def update_doc():
    query = {
        # "script": "ctx._source.new_field = 'new_field_name'"
        "script": {
            "source": "ctx._source.new_field = ''",
        }
    }
    es_client.update_by_query(index=index_name, body=query)


def update_document(index, doc_id, field, new_value):
    update_body = {
        "doc": {
            field: new_value
        }
    }
    es_client.update(index=index, id=doc_id, body=update_body)


def terms_search():
    ret = es_client.terms_enum(index='assets_entity_device', field='ipv4List', string='10.100')
    ret = es_client.terms_enum(index=index_name, field='ip.keyword', string='')
    # ret = es_client.termvectors(index='assets_entity_device', fields='ipv4List')
    print(ret)
    # mapping
    # map = es_client.indices.get_mapping(index=index_name)
    # map.body
    # mapping = str(es_client.indices.get_mapping(index=index_name))

    # pprint.pprint(mapping)
    # print(type(es_client.indices.get_mapping(index=index_name)))


if __name__ == '__main__':
    # delete_index()
    # create_index()
    # insert_data()
    # update_doc()
    # search_data()
    # get_index_mapping()
    # index_exists()
    # terms_search()

    update_document(index='assets_entity_device', doc_id='@OBJID-64eee3e625e3961486159990', field='zScore', new_value=20.0)
