#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import with_statement
import contextlib
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode
try:
    from  urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
import sys

def make_tiny(url):
    request_url = ('http://tinyurl.com/api-create.php?'+urlencode({'url':url}))
    with contextlib.closing(urlopen(request_url)) as res:
        return res.read().decode('utf-8')
    print 1
def main():
    urls = sys.argv[1:]
    for url in urls:
        tinyurl = make_tiny(url)
        print tinyurl

if __name__ == '__main__':
    main()

