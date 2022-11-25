from flask import Blueprint, render_template
from post.postDAO import PostDAO

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")


@main_blueprint.route("/")
def index_page():
    all_posts = PostDAO()
    posts = all_posts.get_posts_all()
    return render_template("index.html", posts=posts)
