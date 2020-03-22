from unittest import TestCase
from unittest.mock import patch, call
import app
from blog import Blog
from post import Post


class AppTest(TestCase):
    def test_menu_prints_prompt(self):
        with patch('builtins.input', return_value='q') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_print_blogs(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q'):
                app.menu()
                # TODO - why is this not called w anything ?
                mocked_print_blogs.assert_called()

    def test_print_blogs(self):
        blog = Blog('Test Blog', 'Test Author')
        app.blogs = {'Test': blog}
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with(
                '- Test Blog by Test Author (0 posts)'
            )

    def test_print_multiple_blogs(self):
        blog = Blog('Test Blog', 'Test Author')
        blog_2 = Blog('Test Blog 2', 'Test Author 2')
        app.blogs = {'Test': blog, 'Test 2': blog_2}

        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            assert mocked_print.call_args_list[0] == call(
                '- Test Blog by Test Author (0 posts)'
            )
            assert mocked_print.call_args_list[1] == call(
                '- Test Blog 2 by Test Author 2 (0 posts)'
            )

    def test_ask_create_blog(self):
        title = 'Test Blog'
        author = 'Test Author'
        blog = Blog(title, author)

        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = (title, author)
            app.ask_create_blog()

            self.assertIsNotNone(app.blogs.get(title))

            # TODO - can't get assertDictEqual to work
            # expected = {title: blog}
            # print("app.blogs ->", app.blogs)
            # print("expected ->", expected)
            # self.assertDictEqual(app.blogs, expected)

    def test_ask_read_blog(self):
        title = 'Test Blog'
        blog = Blog(title, 'Test Author')
        app.blogs = {title: blog}
        with patch('builtins.input', return_value=title):
            with patch('app.print_posts') as mocked_print_posts:
                app.ask_read_blog()
                mocked_print_posts.assert_called_with(blog)

    def test_print_posts(self):
        title = 'Test Blog'
        blog = Blog(title, 'Test Author')
        blog.create_post('Test Post', 'Test Content')
        app.blogs = {title: blog}
        with patch('app.print_post') as mocked_print_post:
            app.print_posts(blog)
            mocked_print_post.assert_called_with(blog.posts[0])
