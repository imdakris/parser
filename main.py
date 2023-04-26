import requests
from apikey import API_TOKEN
data = {
    "custname": "Ruslan",
    "custtel": "0935005380",
    "custemail": "imdakris@gmail.com",
    "size": "medium",
    "topping": "bacon"
}

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Host": "httpbin.org",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-6448ff31-4d1cbae5563ca825330bbc4c"
}

variable = requests.Session()
variable.get('http://httpbin.org/form/post')
response = variable.post('http://httpbin.org/post', headers=headers, data=data, allow_redirects=True)

print(response.text)
