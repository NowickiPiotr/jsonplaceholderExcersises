import requests
import unittest

class TestDeleteMethods(unittest.TestCase):

    def test_delete_post(self):
        response = requests.delete('https://jsonplaceholder.typicode.com/posts/101')
        self.assertTrue(response.ok) 
    
    def test_object_not_available_after_deleting(self):
        response = requests.delete('https://jsonplaceholder.typicode.com/posts/101')
        self.assertFalse(response.json())

if __name__ == '__main__':
    unittest.main()