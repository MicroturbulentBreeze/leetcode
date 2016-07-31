#!/usr/bin/env python
# encoding=utf-8

''' 
爬虫rethat公告
https://access.redhat.com/security/security-updates/#/security-advisories
'''

import urllib2
import time 
import datetime


start_pagenum = 0 #each page has 10 number
url = "https://api.access.redhat.com/rs/search?facet=true&facet.field=portal_severity&facet.field=portal_advisory_type&facet.mincount=1&fl=id,portal_severity,portal_product_names,portal_publication_date,portal_synopsis,view_uri,allTitle&fq=portal_advisory_type:(%22Security+Advisory%22)+AND+documentKind:(%22Errata%22)&hl=true&hl.fl=abstract&hl.simple.post=%253C%252Fmark%253E&hl.simple.pre=%253Cmark%253E&q=*:*&rows=10&sort=portal_publication_date+desc&start=10"

request=urllib2.Request(url=url)
request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36')
response=urllib2.urlopen(request,timeout=600)
response_text=response.read()
print response_text




