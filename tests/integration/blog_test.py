from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_post_in_blog(self):
        b = Blog('Test', 'Test Author')
        b.create_post('Test Post', 'Test content')

        self.assertEqual(len(b.posts), 1)
        self.assertEqual(b.posts[0].title, 'Test Post')
        self.assertEqual(b.posts[0].content, 'Test content')

    def test_json_multiple_posts(self):
        b = Blog('Test', 'Test Author')
        b.create_post('Test Title', 'Test')

        expected = {
            'title': 'Test',
            'author': 'Test Author',
            'posts': [{
                'title': 'Test Title',
                'content': 'Test'
            }]
        }

        self.assertDictEqual(b.json(), expected)

        b2 = Blog('My Days', 'Julie')
        b2.create_post('Test', 'Another post')
        b2.create_post('Test 2', 'Revenge of the post')

        expected2 = {
            'title':
            'My Days',
            'author':
            'Julie',
            'posts': [
                {
                    'title': 'Test',
                    'content': 'Another post'
                },
                {
                    'title': 'Test 2',
                    'content': 'Revenge of the post'
                },
            ]
        }

        self.assertDictEqual(b2.json(), expected2)
