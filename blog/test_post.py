from unittest import TestCase

from post import Post


class PostTest(TestCase):
    def test_create_post(self):
        p = Post('Test','Test Content')
        
        self.assertEqual('Test',p.title)
        self.assertEqual('Test Content',p.content)
    
    def test_json_format(self):
        p = Post('Test','Test Content')
        res = p.json()
        expected = {'title':'Test','content':'Test Content'}
        self.assertEqual('Test',res['title'])
        self.assertEqual('Test Content',res['content'])
        self.assertDictEqual(expected,res)