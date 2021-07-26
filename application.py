from __future__ import print_function, unicode_literals
from elasticsearch_dsl import (
    Document,
    SearchAsYouType,
    analyzer,
    connections,
    token_filter,
)
from flask import Flask, render_template, request
from elasticsearch import Elasticsearch
from elasticsearch_dsl.query import MultiMatch
import os
import jinja2


#setting up  flask and the elastic search api connection
os.chdir("C:\pythoncode\searchengine_good\SearchEngine\pylasticsearch")

# creates a Flask application, named app
application = Flask(__name__)
es = Elasticsearch('127.0.0.1', port=9200)


#Sample_files
# a route where we will display a welcome message via an HTML template
@application.route('/')
def home():
  return render_template('search.html')

@application.route('/search/results', methods=['GET','POST'])
def request_search():
  search_term = request.form['input']
  res = es.search(
    index='data_science_index',
     body={
            "query": {
                "multi_match" : {
                    "query": search_term, 
                    "fields": [
                        "content"
                    ] 
                }, 
                "highlight": {
                  "fields" :{
                    "content" : {}
                  }
                }
            }
        }
    )
  res['ST']=search_term
  print(res)
  for hit in res['hits']['hits']:
    hit['good_summary']='….'.join(hit['highlight']['content'][1:])
  return render_template('results.html', res=res, search_term=search_term)

# run the application
if __name__ == "__main__":
  application.run('127.0.0.1', debug=True)

