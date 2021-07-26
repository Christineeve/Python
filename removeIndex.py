from elasticsearch import Elasticsearch
es = Elasticsearch()
es.indices.delete(index='lambda-index8', ignore=[400, 404])