#!/usr/bin/python3
import urllib.request
with urllib.request.Request('https://alx-intranet.hbtn.io/status')as status:
    html = status.read()
