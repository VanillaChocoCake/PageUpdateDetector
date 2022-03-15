import requests
import time
import webbrowser


def localtime():
    res = time.asctime(time.localtime(time.time()))
    print(res)


url = input("url:")
html = requests.get(url)
html.encoding = html.apparent_encoding
html_prev = html
while True:
    html = requests.get(url)
    html.encoding = html.apparent_encoding
    if html.text != html_prev.text:
        print(f"网页有更新！{localtime()}")
        webbrowser.open(url)
        time.sleep(600)
    else:
        html_prev = html
        localtime()
        time.sleep(60)
