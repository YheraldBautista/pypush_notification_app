"""
Pushover App test
@author: Yherald Bautista
"""
# import modules
import http.client, urllib

# create connection
conn = http.client.HTTPSConnection("api.pushover.net:443")
file = 'resolution.txt'

#Read a file with phrases
with open(file, mode='r') as f:
    text = f.read()


# make POST request to send message
conn.request("POST", "/1/messages.json",
  urllib.parse.urlencode({
    "token": "token",
    "user": "user",
    "title": "PyPushNotification",
    "message": text,
    "url": "",
    "priority": "0" 
  }), { "Content-type": "application/x-www-form-urlencoded" })

# get response
conn.getresponse()