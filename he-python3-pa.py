import os
import requests
from bs4 import BeautifulSoup
import urllib.request

PAGE_URL_LIST = []
BASE_PAGE_URL = 'https://www.doutula.com/article/list/?page='
for x in range(3,5):
    url = BASE_PAGE_URL + str(x)
    PAGE_URL_LIST.append(url)

for page_url in PAGE_URL_LIST:
    response = requests.get(page_url)
    soup = BeautifulSoup(response.content,'lxml')
    img_list = soup.find_all('img', attrs={'class':'lazy image_dtb img-responsive'})
    for img in img_list:
        src = img['data-original']
        if not src.startswith('http'):
            src = 'http:' + src
        filename = src.split(' ').pop()
        print('filename {0}'.format(filename))
        path = os.path.join("D:\image", filename.split('/').pop())
        print('path', path)
        urllib.request.urlretrieve(filename, path)


