#!/usr/bin/env python
import redis
import mechanize
import json
import time
 
class Cosm:
 
  _url_base = "http://api.cosm.com/v2/feeds/"
  _feed_id = None
  _version = None
  _data = None
  _payload = None
  _opener = None
 
  def __init__(self, feed_id, apikey):
    self._version = "1.0.0"
    self._feed_id = feed_id
    self._opener = mechanize.build_opener()
    self._opener.addheaders = [('X-PachubeApiKey',apikey)]
    self._data = []
    self._payload = {}
 
  def addDatapoint(self,dp_id,dp_value):
    self._data.append({'id':dp_id, 'current_value':dp_value})
 
  def buildUpdate(self):
    self._payload['version'] = self._version
    self._payload['id'] = self._feed_id
    self._payload['datastreams'] = self._data
 
  def sendUpdate(self):
    url = self._url_base + self._feed_id + "?_method=put"
    try:
      self._opener.open(url,json.dumps(self._payload))
    except mechanize.HTTPError as e:
      print "An HTTP error occurred: %s " % e

r = redis.StrictRedis(host='localhost', port=6379, db=0)

c = Cosm('XXXXXX', 'XXXXXXXXXXXXXXXXXXXXXXXX')

c.addDatapoint('Temperature', r.get('curtemp'))
c.addDatapoint('Humidity', r.get('curhum'))
c.addDatapoint('Setpoint', r.get('targettemp'))
c.addDatapoint('Heat', r.get('heat'))
c.addDatapoint('Dewpoint', r.get('dewpoint'))

c.buildUpdate()
c.sendUpdate()
