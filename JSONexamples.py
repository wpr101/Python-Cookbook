# -*- coding: utf-8 -*-
import json
from json.encoder import JSONEncoder
from json.decoder import JSONDecoder

class person:
    def __init__(self, name):
        self.name = name

william = person('william')
a = {}
a['item'] = a


data = {
    'name' : 'ACME',
    'key' : 'value',
    'shares' : {'rampage':'jackson', 'mike':'perry' },
    'price' : 542.23,
    'data' : [1,2,3],
    'epic' : False,
    #william: True,
    'utfdata': float("inf")
}

#json_str = json.dumps(data)
#print(json_str)
#acme_data = json.loads(json_str)
#print(acme_data)
#print(json.dumps(data2))


#with open('CFTs/RDS_MySQL_With_Read_Replica.template', 'w') as f:
    #json.dump(data, f)

#with open('CFTs/LAMP_Multi_AZ.template', 'r') as f:
    #data = json.load(f)

def example_default(self, o):
    try:
        iterable = iter(o)
    except TypeError:
        pass
    else:
        return list(iterable)
    # Let the base class default method raise the TypeError
    return JSONEncoder.default(self, o)

with open('out.dat', 'w') as f:
    # skipkeys, True means skipping keys which are non standard types
    # ensure_ascii, False will write char literal, True will write escaped chars for it
    # check_circular, True raises value error if circle, False goes to recursion limit
    # allow_nan, True float("inf") will become Infinity, while False is ValueError
    # cls, specify the encoder, None defaults to JSONEncoder
    # indent, None has no newlines, indent is number of spaces on newlines for elements
    # separators, item, key. Most compact is (',', ':')
    json.dump(data, f, indent=4)
    #json.dump(data,f, skipkeys=False sort_keys=True, indent=4, separators=(',', ': '))

'''
s = '{"name": "ACME", "shares": 50, "price": 490.1}'

class JSONObject:
    def __init__(self, d):
        self.__dict__ = d

data = json.loads(s, object_hook=JSONObject)
#print(data.name)
#print(data)




val = JSONEncoder().encode({"foo": ["bar", "baz"]})
#print(val)
'''

