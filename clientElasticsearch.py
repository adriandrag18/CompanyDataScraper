from elasticsearch import Elasticsearch
import time
import os

class EsClient:
    def __init__(self):
        self.client = self._connect()

    def _connect(self):
        es = Elasticsearch(
            "https://localhost:9200",
            basic_auth=("elastic", os.getenv("ELASTIC_PASSWORD", "your_fixed_password")),
            verify_certs=False,
            ssl_show_warn=False
        )
        for _ in range(10):
            if es.ping():
                return es
            print("Elasticsearch not ready, retrying in 2s...")
            time.sleep(2)
        raise Exception("Failed to connect to Elasticsearch")

    def index(self, index, id, body):
        return self.client.index(index=index, id=id, body=body)

    def search(self, index, body):
        return self.client.search(index=index, body=body)

    def count(self, index):
        return self.client.count(index=index)['count']