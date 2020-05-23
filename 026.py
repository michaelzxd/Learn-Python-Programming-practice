#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import json
with open('example.json', 'r') as myfile:
	data = myfile.read()

obj = json.loads(data)

print("usd: " + str(obj['usd']))
print("eur: " + str(obj['eur']))
print("gbp: " + str(obj['gbp']))