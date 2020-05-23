#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import json
import urllib

obj = json.loads('{"gold": 1271,"silver": 1284,"platinum": 1270}')
print(obj['gold'])

url = "https://api.gdax.com/products/BTC-EUR/ticker"
data = urllib.urlopen(url).read().decode()
obj = json.loads(data)

print('$ ' + obj['price'])
print('$ ' + obj['volume'])