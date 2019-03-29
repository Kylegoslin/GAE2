# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import logging

import webapp2
import urllib2
import datetime

from google.appengine.ext import ndb


class Product(ndb.Model):
    productId = ndb.StringProperty()
    productName = ndb.StringProperty()

    
    
    
class ViewAll(webapp2.RequestHandler):
    def get(self):
        output = ''

        res = Product.query()
        for row in res:
            output = output + '' + row.productName + '---'+row.productId + '<br>'
        
        self.response.out.write(output)
        
    
class Insert(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write("<b>Inserting...!</b>")
        # insert record
        p = Product(productId='1', productName='bacon')
        p.put()
    
    
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write("<b>hello!</b>")
        
            
            
            
            
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/insert', Insert),
    ('/view', ViewAll),
    
], debug=True)
