blogs = dict()  # blog_name : blog object

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


def print_blogs():
    # Print available blogs
    for key, blog in blogs.items():
        print(f'- {blog}')


print_blogs()
