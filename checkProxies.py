import threading
import queue
import requests

q = queue.Queue()
valid_proxies = []

with open('proxies.txt', 'r') as f:
    proxies = f.read().split('\n')
    for p in proxies:
        q.put(p)




def check_proxy():
    global q
    # continue
    while not q.empty():
        proxy = q.get()
        try:
            r = requests.get('http://ipinfo.org/json', proxies={'http': proxy,'https':proxy})
            
        except:
            continue
        