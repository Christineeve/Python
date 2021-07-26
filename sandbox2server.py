from __future__ import print_function, unicode_literals
from elasticsearch_dsl import (
    Document,
    SearchAsYouType,
    analyzer,
    connections,
    token_filter,
)
from flask import Flask, render_template, request
from elasticsearch import Elasticsearch, RequestsHttpConnection
from elasticsearch_dsl.query import MultiMatch
import os
import jinja2
import boto3
from requests_aws4auth import AWS4Auth

# creates a Flask application, named app
application = Flask(__name__)
es = Elasticsearch('127.0.0.1', port=9200)

@application.route('/')
def home():
  return render_template('search.html')

@application.route('/search/results', methods=['GET','POST'])

#start my function to get the search data back. yes, it's terrible. 
def request_search():
  host = 'search-tika-2-gwpygqekxcdd6pvh3dxs62r3dq.us-west-2.es.amazonaws.com'
  region = 'us-west-2'
  service = 'es'
  credentials = boto3.Session().get_credentials()
  awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

  es = Elasticsearch(
      hosts=[{'host': host, 'port': 443}],
      http_auth=awsauth,
      use_ssl=True,
      verify_certs=True,
      connection_class=RequestsHttpConnection
  )
  es.info()
  print(es.info())
  search_term = request.form['input']
  # print("Do I have the search term?")
  print(search_term)

  res= es.search(index='data_science_index',body={'query':{'match_all':{}}})
  print(res)
  # res = es.search(
  #       index="lambda-index2", 
  #      size=20, 
  #       body={
  #           "query": {
  #               "multi_match" : {
  #                   "query": search_term, 
  #                   "fields": [
  #                       "url", 
  #                       "title", 
  #                       "tags"
  #                   ] 
  #               }
  #           }
  #       }
  #   )
        #'query' : {'match_all':{}}},
        # "query" : {"match": {"content": search_term}},
        # "highlight": {
        #      "fields": {"content": {"pre_tags": ["<b>"],"post_tags": ["</b>"]}}}})
#   res['ST']=search_term
#   print(res)
#  # print(search_term)
#   for hit in res['hits']['hits']:
#         hit['good_summary']='….'.join(hit['highlight']['content'][1:])
#   print(res['hits']['hits'])
  print(search_term)
  
  return render_template('results.html', res=res)

# run the application
if __name__ == "__main__":
  application.run('127.0.0.1', debug=True)

