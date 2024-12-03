from elasticsearch.exceptions import NotFoundError
from datetime import datetime
from elasticsearch import Elasticsearch, helpers
ELASTIC_PASSWORD = 'JvEDV1igUdZmw5kC'


class ElasticsearchDemo():

    def __init__(self):
        self.es_client = self.get_client()

    def get_client(self):
        url = "https://10.100.7.3:9200"
        es_clint = Elasticsearch(
            url,
            basic_auth=("elastic", ELASTIC_PASSWORD),
            verify_certs=False,
            ssl_show_warn=False
        )
        return es_clint

    def doc_data(self):
        doc = {
            'author': 'author_name',
            'text': 'This is text data',
            'timestamp': datetime.now()
        }
        return doc

    def create_index(self, index_name: str, doc):
        resp = self.es_client.index(index=index_name, id=1, document=doc)
        print(resp['result'])

    def get_doc_data(self, index_name):
        try:
            resp = self.es_client.get(index=index_name, id='1')
            print(f'doc data: {resp["_source"]}')
        except NotFoundError as e:
            print(f'get doc exceptions: {e}')

    def search(self, index_name):
        resp = self.es_client.search(index=index_name, query={"match_all": {}})
        print(f'search func resp: {resp}')

    def delete_doc(self, index_name):
        resp = self.es_client.delete(index=index_name, id='1')
        print(f'delete doc func resp: {resp}')


    def test_helpers(self):
        data = [
            {
                "_index": "assets_ip_asset",
                "_id": "1",
                "_source": {

                }
            }
        ]

        ret = helpers.bulk(self.es_client, data)
        print(ret)

    def update_document(self, index_name, doc_id, field, new_value):
        self.es_client.update(index=index_name, id=doc_id, )
        update_url = f"{url}/{index}/_doc/{doc_id}/_update"
        update_body = {
            "doc": {
                field: new_value
            }
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(update_url, json=update_body, headers=headers)
        if response.status_code == 200:
            print("文档更新成功")
        else:
            print("文档更新失败")


def main():
    es_obj = ElasticsearchDemo()
    # doc = es_obj.doc_data()
    # test_index_name = 'test_index_name'
    # es_obj.create_index(test_index_name, doc)
    # es_obj.get_doc_data(test_index_name)
    # es_obj.search(test_index_name)
    # # es_obj.delete_doc(test_index_name)
    # es_obj.get_doc_data(test_index_name)
    es_obj.test_helpers()


if __name__ == '__main__':
    main()



