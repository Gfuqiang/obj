import requests

url = 'https://www.google.com.hk/async/bgasy?ei=LvuEYZbuB43nwQOsp5KgCQ&yv=3&async=_fmt:jspb'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}
res = requests.get(url=url, headers=headers)
print(res.text)