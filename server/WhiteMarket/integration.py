import urllib.request, json, requests
def scrapitems(url):
    json_response = json.loads(urllib.request.urlopen("https://es.wallapop.com/rest/wall?"+url).read().decode())
    for item in json_response['items']:

        product = {}
        product['title'] = item['title']
        product['price'] = item['salePrice']
        product['description'] = item['description']
        product['category'] = "Other"
        product['state'] = 2
        for index, image in enumerate(item['images']):
            product["img"+str(index)] = image['mediumURL']

        print('------------------')
        print(product)

        r = requests.post("http://localhost:8000/api/products/", headers={'Authorization': 'JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcmlnX2lhdCI6MTUyNjIxMDE4MywiZXhwIjoxNTI3MzUyODI0LCJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Im9zY2xsd2ViQGdtYWlsLmNvbSIsImVtYWlsIjoib3NjbGx3ZWJAZ21haWwuY29tIn0.nH0Bu564nX6gZiNfxOCnGtDHPoHqXYyC9_77zTBKUAw'},data=product)
        if r.status_code != 201:
            print('error')
    scrapitems(json_response['searchNextPage'])

scrapitems("itemsCount=36&start=36&bumpCollectionType=0&densityType=20&step=0&resultsPerPage=18&latitude=40.4167635&longitude=-3.7038088")

