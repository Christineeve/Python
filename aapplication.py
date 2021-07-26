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
aapplication = Flask(__name__)
es = Elasticsearch('127.0.0.1', port=9200)

@aapplication.route('/')
def home():
  return render_template('indextest.html')

@aapplication.route('/search/results', methods=['GET','POST'])

#start my function to get the search data back. yes, it's terrible.
def request_search():
  host = 'your host'
  region = 'your region'
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
 
  
# Defining the data for the index, and putting it into the index.
#   e1={
#     "first_name":"christine",
#     "last_name":"lee",
#     "age": 27,
#     "about": "Love to play cricket",
#     "interests": ['vr','games'],
# }
#   e2={
#     "first_name" :  "Jane",
#     "last_name" :   "Smith",
#     "age" :         32,
#     "about" :       "I like to collect rock albums",
#     "interests":  [ "music" ]
#   }
#   e3={
#       "first_name" :  "Douglas",
#       "last_name" :   "Fir",
#       "age" :         35,
#       "about":        "I like to build cabinets",
#       "interests":  [ "forestry" ]
#   }

  # e4={
  #     "first_name" :  "Douglas",
  #     "last_name" :   "Fir",
  #     "age" :         35,
  #     "about":        "I like to build cabinets",
  #     "interests":  [ "forestry" ]
  # }
#  Putting the data into the index
#   res = es.index(index='mycorp',doc_type='employee',id=1,body=e1)
#   print('created1')
#   res = es.index(index='mycorp',doc_type='employee',id=2,body=e2)
#   print('created2')
#   res = es.index(index='mycorp',doc_type='employee',id=3,body=e3)
#   print('done')

  # res = es.index(index='mycorp',doc_type='employee',id=4,body=e4)
  # print('done')
 
 
  # search_term = request.form['input']

  #res= es.search(index='lambda-index5',body={'query':{'match_all':{}}})

  # res = es.search(
  #        index="lambda-index5",
  #        size=20,
  #        body={
  #            "query": {
  #                "query_string" : {
  #                   "fields": ["content"],
  #                   "query": search_term
  #                }
  #            }
  #        }
  #    )
 
  ##These are the "gets" index is mycorp, the doc_type is what I defined above in the puts and the id=*
  #res=es.get(index='mycorp',doc_type='employee',id=1)
  #print(res)  
  #res2=es.get(index='mycorp',doc_type='employee',id=2)
  #print(res2)  
  #res3=es.get(index='mycorp',doc_type='employee',id=3)
  #print(res3)  

 ##match all
  #res=es.search(index='mycorp',body={'query':{'match_all':{}}})
  #print("Got %d Hits:" % res['hits']['total']['value'])

  #res= es.search(index='mycorp',body={'query':{'match':{'first_name':'christine'}}})
  #print(res['hits']['hits'])

  # res= es.search(index='mycorp',body={
  #       'query':{
  #           'bool':{
  #               'must':[{
  #                       'match':{
  #                           'first_name':'christine'
  #                       }
  #                   }]
  #           }
  #       }
  #   })

  # res= es.search(index='mycorp',doc_type='employee',body={
  #         'query':{
  #             'match':{
  #                 "about":"play cricket"
  #             }
  #         }
  #     })
  # for hit in res['hits']['hits']:
  #     print(hit['_source']['about'])
  #     print(hit['_score'])
  #     print('**********************')


  # res= es.search(index='mycorp',doc_type='employee',body={
  #           'query':{
  #               'match_phrase':{
  #                   "about":"play cricket"
  #               }
  #           }
  #       })
  # for hit in res['hits']['hits']:
  #     print(hit['_source']['about'])
  #     print(hit['_score'])
  #     print('**********************')


  # filtered query where gt means greater than.
  # res= es.search(index='mycorp',body={
  #         'query':{
  #             'bool':{
  #                 'must':{
  #                     'match':{
  #                         'first_name':'christine'
  #                     }
  #                 },
  #                 "filter":{
  #                     "range":{
  #                         "age":{
  #                             "gt":20
  #                         }
  #                     }
  #                 }
  #             }
  #         }
  #     })

  # print(res['hits']['hits'])
  # this query works to query one or more fields and return data.
  # res= es.search(index='mycorp',doc_type='employee',body={
  # "query": {
  #   "multi_match" : {
  #     "query":    "lee christine eve",
  #     "fields": [ "first_name", "last_name" ]
  #     }
  #   }
  #   })
  # for hit in res['hits']['hits']:
  #     print(hit['_source']['about'])
  #     print(hit['_score'])
  #     print('**********************')


  #this is an example of a muliti_match search from a search box html to a response html
#   search_term = request.form['input']
#   res= es.search(index='mycorp', doc_type='employee',body={
#   "query": {
#     "multi_match" : {
#       "query":    search_term,
#       "fields": [ "first_name", "last_name" ]
#       }
#     }
#     })
#   for hit in res['hits']['hits']:
#       print(hit['_source']['about'])
#       print(hit['_score'])
#       print('**********************')




  # #Let's try to search our actual index.
  # search_term = request.form['input']
  # res= es.search(index='lambda-index5', doc_type='_doc',body={
  # "query": {
  #   "multi_match" : {
  #     "query":    search_term,
  #     "fields": ["content", "metadata" ]
  #     }
  #   }
  #   })
  # print(res)
  # print(search_term)
  # for hit in res['hits']['hits']:
  #     print(hit['_source']['about'])
  #     print(hit['_score'])
  #     print('**********************')


#saving my original query against our index.  
#print(res['bulkdata'])
        #'query' : {'match_all':{}}},
#   res = es.search(
#   index="lambda-index5",
#   size=20,
#   body={
#   "query" : {"match": {"metadata": search_term}},
#   "highlight": {
#       "fields": {"metadata": {"pre_tags": ["<b>"],"post_tags": ["</b>"]}}}})
#   res['ST']=search_term
#   #print(res)
#  # print(search_term)
#   for hit in res['hits']['hits']:
#      hit['good_summary']='….'.join(hit['highlight']['metadata'][1:])
#   print(res['hits']['hits'])
#  print(search_term)
  #return render_template('results.html', res=res)



# run the application
if __name__ == "__main__":  
  aapplication.run('127.0.0.1', debug=True)
