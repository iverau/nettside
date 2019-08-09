import requests

URL = "https://xkcd.com/353"
image_URL = "https://imgs.xkcd.com/comics/python.png"
test_URL = "https://httpbin.org/post"

payload = {'page':2, 'count':25}

r = requests.post(test_URL,data=payload)

print(r.json()['form'])