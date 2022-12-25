from unittest import TestCase

from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test','Test Author')

        self.assertEqual('Test',b.title)
        self.assertEqual('Test Author',b.author)
        self.assertEqual(0,len(b.posts))
    
    def test_repr(self):
        b = Blog('Test','Test Author')
        estimated = b.__repr__()

        self.assertEqual(estimated,f'{b.title} is written by {b.author}')
    
    def test_create_post(self):
        b = Blog('Test','Test Author')
        b.create_post('Test Post','Test Content')

        self.assertEqual(b.posts[0].title,'Test Post')
    
    def test_json(self):
        b = Blog('Test','Test Author')
        estimated = {'title':b.title,'author':b.author,'posts':b.posts}
        self.assertDictEqual(b.json(),estimated)