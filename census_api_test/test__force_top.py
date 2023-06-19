import unittest
import requests


class ToyCensusAPITestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_count_by_gender_with_top(self):
        action_type = 'CountByGender'
        users = [
            {'gender': 'male'},
            {'gender': 'female'},
            {'gender': 'other'}
        ]
        top_value = 2  # Set the desired value for top

        payload = {
            'actionType': action_type,
            'users': users,
            'top': top_value
        }

        response = requests.post('https://census-toy.nceng.net/prod/toy-census', json=payload)

        self.assertEqual(response.status_code, 200, 'API request failed')

        results = response.json()
        self.assertIsInstance(results, list, 'Response data is not a list')

        self.assertEqual(len(results), top_value, 'Number of results does not match')

    def test_count_by_gender_without_top(self):
        action_type = 'CountByGender'
        users = [
            {'gender': 'male'},
            {'gender': 'female'},
            {'gender': 'other'}
        ]

        payload = {
            'actionType': action_type,
            'users': users
        }

        response = requests.post('https://census-toy.nceng.net/prod/toy-census', json=payload)

        self.assertEqual(response.status_code, 200, 'API request failed')

        results = response.json()
        self.assertIsInstance(results, list, 'Response data is not a list')

        self.assertEqual(len(results), len(users), 'Number of results does not match')

    def test_count_by_country_with_top(self):
        action_type = 'CountByCountry'
        users = [
            {'country': 'USA'},
            {'country': 'Canada'},
            {'country': 'USA'},
            {'country': 'Mexico'}
        ]
        top_value = 2  # Set the desired value for top

        payload = {
            'actionType': action_type,
            'users': users,
            'top': top_value
        }

        response = requests.post('https://census-toy.nceng.net/prod/toy-census', json=payload)

        self.assertEqual(response.status_code, 200, 'API request failed')

        results = response.json()
        self.assertIsInstance(results, list, 'Response data is not a list')

        self.assertEqual(len(results), top_value, 'Number of results does not match')

    def test_count_by_country_without_top(self):
        action_type = 'CountByCountry'
        users = [
            {'country': 'USA'},
            {'country': 'Canada'},
            {'country': 'USA'},
            {'country': 'Mexico'}
        ]

        payload = {
            'actionType': action_type,
            'users': users
        }

        response = requests.post('https://census-toy.nceng.net/prod/toy-census', json=payload)

        self.assertEqual(response.status_code, 200, 'API request failed')

        results = response.json()
        self.assertIsInstance(results, list, 'Response data is not a list')

        self.assertEqual(len(results), len(users), 'Number of results does not match')

if __name__ == '__main__':
    unittest.main()


    def test_count_password_complexity(self):
        action_type = 'CountPasswordComplexity'
        users = [
            {'password': 'Password123'},
            {'password': 'abc123!@#'},
            {'password': 'TestPassword'},
            {'password': 'WeakPass'}
        ]
        top_value = 2  # Set the desired value for top

        payload = {
            'actionType': action_type,
            'users': users,
            'top': top_value
        }

        response = requests.post('https://census-toy.nceng.net/prod/toy-census', json=payload)

        self.assertEqual(response.status_code, 200, 'API request failed')

        results = response.json()
        self.assertIsInstance(results, list, 'Response data is not a list')

        # Verify the number of returned results based on the top value
        if top_value > 0:
            self.assertEqual(len(results), top_value, 'Number of results does not match the top value')
        else:
            self.assertEqual(len(results), len(users), 'Number of results does not match')

        for result in results:
            password = result['password']
            complexity = result['complexity']

            self.assertGreaterEqual(len(password), 8, 'Password does not meet minimum length requirement')

            self.assertTrue(any(c.isupper() for c in password), 'Password does not contain an uppercase letter')

            self.assertTrue(any(c.islower() for c in password), 'Password does not contain a lowercase letter')

            self.assertTrue(any(c.isdigit() for c in password), 'Password does not contain a digit')

            special_chars = '!@#$%^&*()'
            self.assertTrue(any(c in special_chars for c in password), 'Password does not contain a special character')


    def test_count_password_complexity_without_top(self):
        action_type = 'CountPasswordComplexity'
        users = [
            {'password': 'Password123'},
            {'password': 'abc123!@#'},
            {'password': 'TestPassword'},
            {'password': 'WeakPass'}
        ]

        payload = {
            'actionType': action_type,
            'users': users
        }

        response = requests.post('https://census-toy.nceng.net/prod/toy-census', json=payload)

        self.assertEqual(response.status_code, 200, 'API request failed')

        results = response.json()
        self.assertIsInstance(results, list, 'Response data is not a list')

        self.assertEqual(len(results), len(users), 'Number of results does not match')

        for result in results:
            password = result['password']
            complexity = result['complexity']

            self.assertGreaterEqual(len(password), 8, 'Password does not meet minimum length requirement')

            self.assertTrue(any(c.isupper() for c in password), 'Password does not contain an uppercase letter')

            self.assertTrue(any(c.islower() for c in password), 'Password does not contain a lowercase letter')

            self.assertTrue(any(c.isdigit() for c in password), 'Password does not contain a digit')

            special_chars = '!@#$%^&*()'
            self.assertTrue(any(c in special_chars for c in password), 'Password does not contain a special character')




