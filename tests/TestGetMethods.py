import requests
import unittest

class TestGetMethods(unittest.TestCase):
    
    def test_get_comments_from_post_13(self):
        response = requests.get('https://jsonplaceholder.typicode.com/comments?postId=13')
        print(response.text)
        self.assertTrue(response.ok)
 
    def test_get_first_comment_from_post_13(self):
        response = requests.get('https://jsonplaceholder.typicode.com/comments?postId=13&id=61')
        print(response.text)
        self.assertTrue(response.ok)

    def test_post_number_13_contains_5_comments(self):
        response = requests.get('https://jsonplaceholder.typicode.com/comments?postId=13')
        jsonOutput = response.json()
        self.assertEqual(len(jsonOutput),5)

    def test_comment_postId_is_not_empty(self):
        response = requests.get('https://jsonplaceholder.typicode.com/comments?postId=13&id=61')
        jsonOutput = response.json()
        self.assertIsNotNone(jsonOutput[0]['postId'])

    def test_comment_name_is_not_empty(self):
        response = requests.get('https://jsonplaceholder.typicode.com/comments?postId=13&id=61')
        jsonOutput = response.json()
        self.assertIsNotNone(jsonOutput[0]['name'])

    def test_comment_email_is_not_empty(self):
        response = requests.get('https://jsonplaceholder.typicode.com/comments?postId=13&id=61')
        jsonOutput = response.json()
        self.assertIsNotNone(jsonOutput[0]['email'])
       
    def test_comment_body_is_not_empty(self):
        response = requests.get('https://jsonplaceholder.typicode.com/comments?postId=13&id=61')
        jsonOutput = response.json()
        self.assertIsNotNone(jsonOutput[0]['body'])



if __name__ == '__main__':
    unittest.main()
