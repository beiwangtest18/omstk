# -*- coding: utf-8 -*-
#coding=utf-8
__author__ = 'Alicia'
import unittest
import requests
import os
import json
from urllib import urlencode
from conf import *

class Test_heroes_post(unittest.TestCase):
   def setUp(self):
       self.uri = '/heroes'
       self.url = URL[env] +self.uri
       self.body = {"name": "API_POST", "skill": "Super power"}

   def tearDown(self):
       pass

   def test_heroes_post(self):
       params = {}
       urlencode(params)
       headers = {"Content-Type":"application/json"}
       resp = requests.request('POST', self.url, headers=headers, params=params, data=json.dumps(self.body))
       print resp.url
       print resp.status_code
       rj = json.loads(resp.content)
       print resp.content
       self.assertEqual(resp.status_code,200)

if __name__ == '__main__':
   unittest.main()

