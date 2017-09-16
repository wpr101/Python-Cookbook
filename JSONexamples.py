import json

data = {
    'name' : 'ACME',
    'key' : 'value',
    'shares' : 100,
    'price' : 542.23
}

json_str = json.dumps(data)
data = json.loads(json_str)


#with open('CFTs/RDS_MySQL_With_Read_Replica.template', 'w') as f:
    #json.dump(data, f)

with open('CFTs/LAMP_Multi_AZ.template', 'r') as f:
    data = json.load(f)

with open('out.dat', 'w') as f:
    json.dump(data,f, sort_keys=True, indent=4, separators=(',', ': '))
