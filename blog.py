from flask import Flask, render_template
from get_blogs import Blogs

app = Flask(__name__)


@app.route("/blogs")
def blogs():
    my_blogs = Blogs()
    my_blogs.load_blogs()
    return render_template(template_name_or_list="all_blogs.html", blogs=my_blogs.blogs)


if __name__ == "__main__":
    app.run(debug=True)
