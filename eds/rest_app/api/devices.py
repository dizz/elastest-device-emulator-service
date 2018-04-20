import datetime
import requests
#import re
import simplejson
from base64 import b64decode
from connexion import NoContent

# raw_data = requests.get("http://localhost:8000/onem2m/MemsIPE/sensor_data/x/latest/" + "http://localhost:8000/onem2m/MemsIPE/sensor_data/y/latest/" )
# #print raw_data
# array = raw_data.content
# print array
# final_data = simplejson.loads(str(array))
# print final_data
# devices = b64decode(final_data["m2m:cin"]["con"])
# print devices

# Replace with the correct URL
url1 = "http://localhost:8000/onem2m/MemsIPE/sensor_data/x/latest/"
url2 = "http://localhost:8000/onem2m/MemsIPE/sensor_data/y/latest/"
url3 = "http://localhost:8000/onem2m/MemsIPE/sensor_data/z/latest/"

url = {url1, url2, url3}

res = [requests.get(i) for i in url]
d = [j.content for j in res]

dic = [simplejson.loads(q) for q in d]

raw_data = [m["m2m:cin"]["con"]for m in dic]

data = [de.encode("utf-8") for de in raw_data]

devices =[b64decode(pa) for pa in data]
print devices




def post(servicename):
    count = len(devices)
    print(count)
    servicename['id'] = count + 1
    servicename['registered'] = datetime.datetime.now()
    devices[servicename['device']] = servicename
    return servicename, 201
    print servicename

def put(id, servicename):
    id = str(id)
    if devices.get(id) is None:
        return NoContent, 404
    devices[id] = servicename

    return devices[id]


def delete(id):
    id = str(id)
    if devices.get(id) is None:
        return NoContent, 404
    del devices[id]
    return NoContent, 204


def get(id, servicename):
    id = str(id)
    if devices.get(id) is None:
        return NoContent, 404
    devices[id] = servicename
    return devices[id]
    print devices[id]

def search():
    # NOTE: we need to wrap it with list for Python 3 as dict_values is not JSON serializable
    return devices
    print devices
