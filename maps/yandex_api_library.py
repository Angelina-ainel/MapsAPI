import requests


def geocode(address):
    url = 'http://geocode-maps.yandex.ru/1.x/'
    params = {'apikey': '40d1649f-0493-4b70-98ba-98533de7710b',
              'geocode': address,
              'format': 'json'}
    response = requests.get(url, params=params)
    if not response:
        pass
    return response.json()


def get_spn_from_toponym(toponym):
    long1, lat1 = map(float, toponym['boundedBy']['Envelope']['lowerCorner'].split())
    long2, lat2 = map(float, toponym['boundedBy']['Envelope']['upperCorner'].split())
    spn = long2 - long1, lat2 - lat1
    return spn


def get_relevant_toponym(json_response):
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    return toponym


def get_coord_toponym(toponym):
    toponym_coodrinates = toponym["Point"]["pos"]
    coords = map(float, toponym_coodrinates.split(" "))
    return list(coords)


def get_static(**params):
    url = 'https://static-maps.yandex.ru/1.x/'
    response = requests.get(url, params=params)
    return response.content


def search_maps(**params):
    search_api_server = "https://search-maps.yandex.ru/v1/"
    params['apikey'] = 'dda3ddba-c9ea-4ead-9010-f43fbc15c6e3'
    params['lang'] = params.get('lang', 'ru_RU')

    response = requests.get(search_api_server, params=params)
    if not response:
        pass
    return response.json()
