#!/usr/bin/python3
'''the urllib is used for fetching requests from http headers'''
import urllib.request
req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
if __name__ == "__main__":
with urllib.request.urlopen(req)as status:
    html = status.read()
