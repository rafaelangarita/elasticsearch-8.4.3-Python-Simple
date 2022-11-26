# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os
import time
from elasticsearch import Elasticsearch
from datetime import date


ES_NODES = "http://localhost:9200"



def get_all_data(index):
    es_client = Elasticsearch(hosts=[ES_NODES])

    result = es_client.search(
        index=index,
        body={
            "query": {
                "match_all": {}
            }
        }
    )

    import json
    json_object = json.loads(json.dumps(result))

    json_formatted_str = json.dumps(json_object, indent=2)

    print(json_formatted_str)
    print(result)

#https://kb.objectrocket.com/elasticsearch/how-to-create-and-delete-elasticsearch-indexes-using-the-python-client-library#create+an+elasticsearch+index
#https://kb.objectrocket.com/elasticsearch/how-to-use-the-search-api-for-the-python-elasticsearch-client-265


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    elastic = Elasticsearch(hosts=[ES_NODES])
    if elastic.indices.exists('cars'):
        print('the index already exists')
    else:
        elastic.indices.create(index='caRrs')


    # create a document to upload
    data = [{
        'ad_id': 1053675,
        'city': 'Houston',
        'category': 'Cars',
        'date_posted': date.today(),
        'title': '2020 Chevrolet Silverado',
        'body': "This brand new vehicle is the perfect truck for you."
    }]

    # add document to index
    res = elastic.index(index='cars', doc_type="_doc", id=data[0]['ad_id'], body=data[0])

    print(res['result'])

    #get all documents from index 'cars'
    get_all_data('cars')



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
