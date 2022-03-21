import requests
import time
import webbrowser


def localtime():
    res = time.asctime(time.localtime(time.time()))
    return res


urls = []
htmls = []
for url in urls:
    htmls.append(requests.get(url))
for html in htmls:
    html.encoding = html.apparent_encoding
htmls_prev = htmls
while True:
    htmls = []
    for url in urls:
        htmls.append(requests.get(url))
    for html in htmls:
        html.encoding = html.apparent_encoding
    for i in range(0, len(htmls)):
        html = htmls[i]
        html_prev = htmls_prev[i]
        url = urls[i]
        if html.text != html_prev.text:
            print(f"{localtime()}网页有更新！url={url}")
            webbrowser.open(url)
    print(localtime())
    htmls_prev = htmls
    time.sleep(60)
