class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self):
        def handle_plural():
            return "s" if len(self.posts) != 1 else ""

        return f'{self.title} by {self.author} ({len(self.posts)} post{handle_plural()})'

    def create_post(self, title, content):
        pass

    def json(self):
        return {
            'title': self.title,
            'author': self.author,
            'posts': self.posts,
            }
