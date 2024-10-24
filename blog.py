from flask import Flask, render_template
from get_blogs import Blogs

app = Flask(__name__)


def get_blogs():
    my_blogs = Blogs()
    my_blogs.load_blogs()
    return my_blogs.blogs


@app.route("/blogs")
def blogs():
    my_blogs= get_blogs()
    return render_template(template_name_or_list="all_blogs.html", blogs=my_blogs)


@app.route("/blogs/<int: id>")
def blog(pk):
    my_blog = get_blogs()[pk]
    return render_template(template_name_or_list="blog.html", blog=my_blog)


if __name__ == "__main__":
    app.run(debug=True)
