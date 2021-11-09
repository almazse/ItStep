from django.test import TestCase
from rest_framework.test import APITestCase, RequestsClient

TEST_DATA = {'apartaments': 3,
            'city': 'Запорожье',
            'country': 'Украина',
            'house_num': 18,
            'street': 'проспект Ленина',
            'zip_code': 69001}


class APITesting(APITestCase):

    def setUp(self) -> None:
        self.client = RequestsClient()
        self.client.post('http://127.0.0.1:8000/address/', data=TEST_DATA)

    def test_post_address(self):
        test_data = TEST_DATA.copy()
        test_data['apartaments'] = 100
        response = self.client.post("http://127.0.0.1:8000/address/", data=test_data)
        self.assertEqual(response.status_code, 201)

    def test_get_addresses(self):
        response = self.client.get("http://127.0.0.1:8000/address/")
        self.assertEqual(response.status_code, 200)

    def test_get_address(self):
        response = self.client.get('http://127.0.0.1:8000/address/1/')
        self.assertEqual(response.status_code, 200)

    def test_get_address_incorrect_id(self):
        response = self.client.get('http://127.0.0.1:8000/address/20/')
        self.assertEqual(response.status_code, 404)

    def test_put_address(self):
        test_data = TEST_DATA.copy()
        response = self.client.put("http://127.0.0.1:8000/address/1/", data=test_data)
        self.assertEqual(response.status_code, 200)

    def test_post_invalid_address(self):
        test_data = TEST_DATA.copy()
        test_data['apartaments'] = 0
        response = self.client.post('http://127.0.0.1:8000/address/', data=test_data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('apartaments field cannot be less than zero', response.json()['non_field_errors'][0])

    def test_put_invalid_address(self):
        test_data = TEST_DATA.copy()
        test_data['apartaments'] = 0
        response = self.client.put('http://127.0.0.1:8000/address/1/', data=test_data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('apartaments field cannot be less than zero', response.json()['non_field_errors'][0])

    def test_post_invalid_country(self):
        test_data = TEST_DATA.copy()
        test_data['country'] = "Ukr"
        response = self.client.post("http://127.0.0.1:8000/address/", data=test_data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('The country field Can not be shorter than 3 characters', response.json()['non_field_errors'][0])

    def test_put_invalid_country(self):
        test_data = TEST_DATA.copy()
        test_data['country'] = "Ukr"
        response = self.client.put('http://127.0.0.1:8000/address/1/', data=test_data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('The country field Can not be shorter than 3 characters', response.json()['non_field_errors'][0])

    def test_post_invalid_city(self):
        test_data = TEST_DATA.copy()
        test_data['city'] = "Зап"
        response = self.client.post("http://127.0.0.1:8000/address/", data=test_data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('The city field Can not be shorter than 3 characters', response.json()['non_field_errors'][0])

    def test_put_invalid_city(self):
        test_data = TEST_DATA.copy()
        test_data['city'] = "Зап"
        response = self.client.put('http://127.0.0.1:8000/address/1/', data=test_data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('The city field Can not be shorter than 3 characters', response.json()['non_field_errors'][0])

    def test_post_invalid_house_num(self):
        test_data = TEST_DATA.copy()
        test_data['house_num'] = 0
        response = self.client.post('http://127.0.0.1:8000/address/', data=test_data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('house_num field cannot be less than zero', response.json()['non_field_errors'][0])

    def test_put_invalid_house_num(self):
        test_data = TEST_DATA.copy()
        test_data['house_num'] = 0
        response = self.client.put('http://127.0.0.1:8000/address/1/', data=test_data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('house_num field cannot be less than zero', response.json()['non_field_errors'][0])

    def test_post_invalid_zip_code(self):
        test_data = TEST_DATA.copy()
        test_data['zip_code'] = 6900
        response = self.client.post("http://127.0.0.1:8000/address/", data=test_data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('The zip_code field Must be a five-digit number', response.json()['non_field_errors'][0])

    def test_put_invalid_zip_code(self):
        test_data = TEST_DATA.copy()
        test_data['zip_code'] = 6900
        response = self.client.put('http://127.0.0.1:8000/address/1/', data=test_data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('The zip_code field Must be a five-digit number', response.json()['non_field_errors'][0])

    def test_post_invalid_street(self):
        test_data = TEST_DATA.copy()
        test_data['street'] = "Пархомова"
        response = self.client.post("http://127.0.0.1:8000/address/", data=test_data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('The street field must contain: (улица|проспект|бульвар|переулок)'
                      , response.json()['non_field_errors'][0])

    def test_put_invalid_street(self):
        test_data = TEST_DATA.copy()
        test_data['street'] = "Пархомова"
        response = self.client.put('http://127.0.0.1:8000/address/1/', data=test_data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('The street field must contain: (улица|проспект|бульвар|переулок)'
                      , response.json()['non_field_errors'][0])

    def test_delete_address(self):
        response = self.client.delete("http://127.0.0.1:8000/address/1/")
        self.assertEqual(response.status_code, 204)
