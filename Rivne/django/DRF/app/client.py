import requests
from pprint import pprint as pp


def post():
    data = {'apartaments': 0,
            'city': 'Киев',
            'country': 'Ukraine',
            'house_num': 1,
            'street': 'Киевская',
            'zip_code': 88000}
    response = requests.post("http://127.0.0.1:8000/address/", data=data)
    print(response.json(), response.status_code)


def get():
    response = requests.get("http://127.0.0.1:8000/address/")
    pp(response.json())


def put():
    data = {
            'apartaments': 10,
            'city': 'Kyiv',
            'country': "Ukra",
            'house_num': 1,
            'street': 'Киевская',
            'zip_code': 88000}
    response = requests.put("http://127.0.0.1:8000/address/1/", data=data)
    print(response.json(), response.status_code)


def delete():
    response = requests.delete("http://127.0.0.1:8000/address/6/")
    print(response.status_code)

if __name__ == '__main__':
    # pass
    # post()
    # get()
    put()
    # delete()
