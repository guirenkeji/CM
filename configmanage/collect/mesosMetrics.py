import pycurl
import StringIO
import urllib2 
import json
mesosMetricslist = urllib2.urlopen('http://20.26.17.133:5050/metrics/snapshot').read()
print  type(mesosMetricslist)
# print json.dump(mesosMetricslist)
# b = StringIO()
# c = pycurl.Curl()
# c.setopt(c.URL, 'http://20.26.17.133:5050/metrics/snapshot')
# c.setopt(c.WEITEDATA,b)
# c.perform()
# boby = b.getvalue()
