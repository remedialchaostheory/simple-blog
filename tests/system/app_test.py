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

    def test_menu_calls_print_blogs_before_menu_prompt(self):
        with patch('builtins.input', return_value='q'):
            with patch('app.print_blogs') as mocked_print_blogs:
                app.menu()
                # TODO - why is this not called w anything ?
                mocked_print_blogs.assert_called()

    def test_menu_calls_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            blog_title = 'Test Blog'
            mocked_input.side_effect = ('c', blog_title, 'Test Author', 'q')
            app.menu()
            self.assertIsNotNone(app.blogs[blog_title])

    def test_menu_calls_print_blogs(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('l', 'q')
            with patch('app.print_blogs') as mocked_print_blogs:
                app.menu()
                mocked_print_blogs.assert_called()

    def test_menu_calls_ask_read_blog(self):
        blog_title = 'Test Blog'
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('r', blog_title, 'q')
            app.menu()
            self.assertIsNotNone(app.blogs[blog_title])

        with patch('builtins.input') as mocked_input:
            with patch('app.ask_read_blog') as mocked_ask_read_blog:
                mocked_input.side_effect = ('r', blog_title, 'q')
                app.menu()
                mocked_ask_read_blog.assert_called()

    def test_menu_calls_ask_create_post(self):
        with patch('builtins.input') as mocked_input:
            blog_title = 'Test Blog'
            mocked_input.side_effect = (
                'p', blog_title, 'Test Post', 'Test Content', 'q'
            )
            app.menu()
            blog = app.blogs[blog_title]
            self.assertGreater(len(blog.posts), 0)

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

    def test_print_post(self):
        post = Post('Test Title', 'Test Content')
        with patch('builtins.print') as mocked_print_post:
            app.print_post(post)
            mocked_print_post.assert_called_with(
                app.POST_TEMPLATE.format(post.title, post.content)
            )

    def test_ask_create_post(self):
        blog_title = 'Test Blog'
        blog = Blog(blog_title, 'Test Author')
        post_title = 'Test Post'
        post_content = 'Test Content'

        blog.create_post(post_title, post_content)
        app.blogs = {blog_title: blog}

        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = (blog_title, post_title, post_content)
            app.ask_create_post()
            self.assertEqual(blog.posts[0].title, post_title)
            self.assertEqual(blog.posts[0].content, post_content)
