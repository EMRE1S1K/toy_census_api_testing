import unittest
import requests


class ToyCensusAPITestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_count_by_country(self):
        action_type = 'CountByCountry'
        payload = {
            'actionType': action_type,
            'users': []
        }

        response = requests.post('https://census-toy.nceng.net/prod/toy-census', json=payload)

        self.assertEqual(response.status_code, 200, 'API request failed')

        json_response = response.json()
        self.assertIsInstance(json_response, list, 'Response data is not a list')

        results = json_response
        users = []
        for result in results:
            country = result['name']
            count = result['value']
            users.append({'country': country, 'count': count})
        payload['users'] = users

        counts = [result['value'] for result in results]
        sorted_counts = sorted(counts, reverse=True)
        self.assertEqual(counts, sorted_counts, 'Country counts are not in descending order')

    def test_count_by_gender(self):
        payload = {
            'actionType': 'CountByGender',
            'users': [
                {'gender': 'male'},
                {'gender': 'female'},
                {'gender': 'other'}
            ]
        }

        response = requests.post('https://census-toy.nceng.net/prod/toy-census', json=payload)

        self.assertEqual(response.status_code, 200, 'API request failed')

        results = response.json()
        counts = [result['value'] for result in results]
        sorted_counts = sorted(counts, reverse=True)
        self.assertEqual(counts, sorted_counts, 'Gender counts are not in descending order')
        self.assertIsInstance(results, list, 'Response data is not a list')

        self.assertEqual(len(results), 3, 'Number of genders does not match')

        self.assertGreaterEqual(results[0]['value'], results[1]['value'], 'Genders are not ordered correctly')

    def test_count_password_comp(self):
        action_type = 'CountPasswordComplexity'
        users = [
            {'password': 'Abcdef123'},  # Complexity value: 0
            {'password': 'Abcdef123!'},  # Complexity value: 1
            {'password': 'Abcdef123!!'},  # Complexity value: 2
            {'password': 'Abcdef123!!!'},  # Complexity value: 3
            {'password': 'abc'},
            {'password': 123}
        ]

        payload = {
            'actionType': action_type,
            'users': users
        }

        response = requests.post('https://census-toy.nceng.net/prod/toy-census', json=payload)

        self.assertEqual(response.status_code, 200, 'API request failed')

        results = response.json()
        self.assertIsInstance(results, list, 'Response data is not a list')

        complexities = [result['value'] for result in results]
        sorted_complexities = sorted(complexities, reverse=True)
        self.assertEqual(complexities, sorted_complexities, 'Password complexities are not in descending order')

        self.assertEqual(len(results), len(users), 'Number of passwords does not match')

        self.assertGreaterEqual(results[0]['value'], results[1]['value'], 'Passwords are not ordered correctly')


if __name__ == '__main__':
    unittest.main()
