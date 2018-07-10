#!/usr/bin/env python3

# copyright ted timmons, @tedder42, 2018, with MIT license:
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import requests
import json
import os

apikey = os.environ['SPRINTLY_API_KEY']
user = os.environ['SPRINTLY_API_USER']

def get(url, params=None):
  ret = requests.get('https://sprint.ly/{}'.format(url), auth=(user, apikey), params=params )
  return ret.json()

products = get('api/products.json')
#print(json.dumps(products, indent=2))

for prod in products:
  #print('fetching {}'.format(prod['name']))
  #prod['id']
  items = get('api/products/{}/items.json'.format(prod['id']), params={'status':'someday,backlog,in-progress,completed,accepted', 'limit':500, 'children':True} )
  #print(json.dumps(items, indent=2))

  for item in items:
    item['_comments'] = get('api/products/{}/items/{}/comments.json'.format(prod['id'], item['number']))
  prod['_items'] = items


print(json.dumps(products, indent=2))
