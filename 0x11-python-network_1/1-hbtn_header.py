#!/usr/bin/python3
'''importing urllib.request to enable fetching data in urls'''
import urllib.request
'''importing sys module to enable command line
    arguments'''
import sys
link = sys.argv[1]
rq = urllib.request.Request(link)
if __name__ == "__main__":
    with urllib.request.urlopen(rq)as details:
        headers = details.getheaders()
        x_req = details.getheader('X-Request-Id')
        print(x_req)

