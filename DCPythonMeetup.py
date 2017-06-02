#WMATA API

import json
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen

#hex 
demo_key = "e1eee2b5677f408da40af8480a5fd5a8"

'''print("The numeric value of {} in decimal is {}",
    demo_key, int(demo_key, 16))'''

incidents_url = "https://api.wmata.com/Incidents.svc/json/ElevatorIncidents"
hdrs = {'api_key': demo_key}
req = Request(incidents_url, headers=hdrs)
result = urlopen(req)
raw_data = result.read().decode('utf-8')
data = json.loads(raw_data)
incidents = data["ElevatorIncidents"]
print(incidents)

for i in incidents:
    print(i['StationName'])
