import requests

with open('proxy/valid_proxy.txt', 'r') as f:
    proxies = f.read().split('\n')

site_to_check = ['https://books.toscrape.com/',
                 'https://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html', 'https://books.toscrape.com/catalogue/category/books/fantasy_19/index.html', 'https://books.toscrape.com/catalogue/category/books/classics_6/index.html', 'https://books.toscrape.com/catalogue/category/books/womens-fiction_9/index.html']

counter = 0


def rechercherTitre(str):
    lines = str.split('\n')
    for line in lines:
        if line.contains('title'):
            print(line)


for site in site_to_check:
    try:
        print('proxy : {proxy}'.format(proxy=proxies[counter]))
        res = requests.get(
            site, proxies={'http': proxies[counter], 'https': proxies[counter]})
        print(res.status_code)
        print(res.text)

    except:
        print('failed for : {proxy}'.format(proxy=proxies[counter]))
    finally:
        counter += 1
