#!/usr/bin/env python3
# This scripts will share information about network beetween 2 map
# It require requests, you can install it using pip: pip3 install requests

# First DB
u1 = "https://www.fc00.org/"
# Second DB
u2 = "https://hyperboria-map.cwo.fi/"

# Graph Url
ug = "static/graph.json"
# Post Graph
up = "sendGraph"

email = "your@email.here"

from requests import get, post
from json import dumps, loads
from sys import exit

def transform(l):
    l = loads(l)
    lt = {"nodes": [], "edges": []}
    for i in l["nodes"]:
        lt["nodes"].append({"ip": i["id"], "version": i["version"]})
    for i in l["edges"]:
        lt["edges"].append({"a": i["sourceID"], "b": i["targetID"]})
    return dumps(lt)

try:
    print(post(u1 + up, data={"data": transform(get(u2 + ug).text), "mail": email, "version": 2}).text)
except:
    pass
try:
    print(post(u2 + up, data={"data": transform(get(u1 + ug).text), "mail": email, "version": 2}).text)
except:
    pass

exit(1)
