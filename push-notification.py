import http.client, urllib

conn = http.client.HTTPSConnection("api.pushover.net:443")
file = 'resolution.txt'

with open(file, mode='r') as f:
    text = f.read()

conn.request("POST", "/1/messages.json",
  urllib.parse.urlencode({
    "token": "abc123",
    "user": "user123",
    "message": text,
  }), { "Content-type": "application/x-www-form-urlencoded" })
conn.getresponse()