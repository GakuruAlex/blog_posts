from requests import get


class Blogs:
    def __init__(self):
        self.blog_url = "https://api.npoint.io/3fef3756e6f6d6acd52c"
        self.blogs = None

    def load_blogs(self):
        response = get(url=self.blog_url)
        self.blogs: list = response.json()

        print(self.blogs)
