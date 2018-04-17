import pandas as pd
import numpy as np
from elasticsearch import Elasticsearch

import json
import requests
import os

#es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
#es.index(index='test-index', doc_type='test', id=1, body={'test': 'test'})

fn = os.path.join(os.path.dirname(__file__), 'qualshort.csv')

print("Read in the file")
print (fn)

#df = pd.read_csv('C:/vulnapp/short.csv')
df = pd.read_csv(fn)

# df is a dataframe or dataframe chunk coming from your reading logic
df['_id'] = df.index # make a fake id
df_as_json = df.to_json(orient='records', lines=True)

final_json_string = ''
for json_document in df_as_json.split('\n'):
    jdict = json.loads(json_document)
    metadata = json.dumps({'index': {'_id': jdict['_id']}})
    jdict.pop('_id')
    final_json_string += metadata + '\n' + json.dumps(jdict) + '\n'

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post('http://elasticsearch:9200/my_indexqual/my_type/_bulk', data=final_json_string, headers=headers, timeout=60)
