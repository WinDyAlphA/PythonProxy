import threading
import queue
import requests

q = queue.Queue()
valid_proxies = []


with open('proxy/proxy.txt', 'r') as f:
    proxies = f.read().split('\n')
    for p in proxies:
        q.put(p)
        print(p)


def check_proxy():
    global q
    # continue
    while not q.empty():
        proxy = q.get()
        try:
            r = requests.get('https://books.toscrape.com/',
                             proxies={'http': proxy, 'https': proxy})
        except:
            continue
        if r.status_code == 200:
            valid_proxies.append(proxy)
            print(proxy)


for i in range(100):
    t = threading.Thread(target=check_proxy)
    t.start()
    print("tested")
