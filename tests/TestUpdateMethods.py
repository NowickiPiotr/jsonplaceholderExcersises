import requests
import unittest

class TestPutMethods(unittest.TestCase):
    
    def test_update_post(self):
        data = {'title':'new title','body':'update','userId':5} 
        response = requests.put('https://jsonplaceholder.typicode.com/posts/13', data)               
        print(response.text)
        self.assertTrue(response.ok)

    def test_post_contains_correct_title_after_updating(self):
        data = {'title':'new title','body':'update','userId':5} 
        response = requests.put('https://jsonplaceholder.typicode.com/posts/13', data)     
        jsonOutput = response.json()          
        print(response.text)
        self.assertEqual(jsonOutput['title'],'new title')

    def test_post_contains_correct_body_after_updating_post(self):
        data = {'title':'new title','body':'update','userId':5} 
        response = requests.put('https://jsonplaceholder.typicode.com/posts/13', data)     
        jsonOutput = response.json()          
        print(response.text)
        self.assertEqual(jsonOutput['body'],'update')

    def test_post_contains_correct_userId_after_updating_post(self):
        data = {'title':'new title','body':'update','userId':5} 
        response = requests.put('https://jsonplaceholder.typicode.com/posts/13', data)     
        jsonOutput = response.json()          
        print(response.text)
        self.assertEqual(jsonOutput['userId'],'5')

if __name__ == '__main__':
    unittest.main()