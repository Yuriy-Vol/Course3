from flask import Blueprint, render_template
from post.postDAO import PostDAO

users_blueprint = Blueprint("users_blueprint", __name__, template_folder="templates")


@users_blueprint.route("/users/<username>")
def users_page(username):
    all_posts = PostDAO()
    users_posts = all_posts.get_posts_by_user(username)
    return render_template("user-feed.html", posts=users_posts)