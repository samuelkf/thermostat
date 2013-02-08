#!/usr/bin/env python
from sht1x.Sht1x import Sht1x as SHT1x
import time, redis, os

sht1x = SHT1x(24, 23)
r = redis.StrictRedis(host='localhost', port=6379, db=0)

while True:
	curtemp = round(sht1x.read_temperature_C(), 2)
	curhum = round(sht1x.read_humidity(), 2)
	dewpoint = round(sht1x.calculate_dew_point(curtemp, curhum), 2)
	targettemp = int(r.get('targettemp'))

	r.set('curtemp', curtemp)
	r.set('curhum', curhum)
	r.set('dewpoint', dewpoint)

	if r.get('timer') == '1':
		if curtemp < targettemp:
			r.set('heat', 1)
			os.system('./switcher.py 1')
		else:
			r.set('heat', 0)
			os.system('./switcher.py 0')
	else:
		r.set('heat', 0)
	time.sleep(3)
