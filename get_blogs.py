from requests import get


class Blogs:
    def __init__(self):
        self.blog_url = "https://api.npoint.io/3fef3756e6f6d6acd52c"
        self.blogs = {}

    def load_blogs(self):
        response = get(url=self.blog_url)
        result = response.json()
        self.blogs = {blog["id"]: [blog["title"], blog["subtitle"], blog["body"]] for blog in result}
        print(self.blogs)


if __name__ == "__main__":
    blogs = Blogs()
    blogs.load_blogs()
