MENU_PROMPT = 'Enter "c" to create a blog, "l" to list blogs, "r" to read one, "p" to create a post, or "q" to quit'

blogs = dict()  # blog_name : blog object
from blog import Blog

# blog = Blog('Test Blog', 'Test Author')
# blog_2 = Blog('Test Blog 2', 'Test Author 2')
# blogs = {'Test': blog, 'Test 2': blog_2}

# blogs = {
#     {
#         'title': 'Test',
#         'author': 'Test Author',
#     },
#     {
#         'title': 'Test 2',
#         'author': 'Test Author 2',
#     },
# }


def menu():
    # Show user available blogs
    # Let user make a choice
    # Do something with that choice
    # Eventual wait

    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)


def print_blogs():
    # Print available blogs
    for key, blog in blogs.items():
        print(f'- {blog}')


def ask_create_blog():
    blog_title = input('What is your blog\'s title?')
    blog_author = input('What is your name?')
    new_blog = Blog(blog_title, blog_author)
    blogs[blog_title] = new_blog
    print('Thanks! You\'re blog is now created')
    pass


def ask_read_blog():
    pass


def ask_create_post():
    pass
