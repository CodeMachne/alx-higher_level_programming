#!/usr/bin/python3
'''the urllib is used for fetching requests from http headers'''
import urllib.request
if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as status:
        #print("- content: ", +html)
        html = status.read()
        #print("- type: ", + type(html))
        print("\t- content: {}".format(html))
        print("\t- type: {}".format(type(html)))
        hhtml = status.read().decode('utf-8')
        print("\t- utf8 content: {}".format(hhtml))
