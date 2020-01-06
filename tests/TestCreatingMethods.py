import requests
import unittest

class TestPostMethods(unittest.TestCase):
    
    def test_correct_response_after_adding_post_with_id_101(self):
        data = {'title':'title','body':'body content','userId':1} 
        response = requests.post('https://jsonplaceholder.typicode.com/posts', data) 
        self.assertTrue(response.ok)

    def test_it_is_possible_get_new_post(self):
        response = requests.get('https://jsonplaceholder.typicode.com/posts/'+'101')   
        print(response.json())
        self.assertTrue(response.json())

if __name__ == '__main__':
    unittest.main()