from flask import Blueprint, render_template, request
from post.postDAO import PostDAO

search_blueprint = Blueprint("search_blueprint", __name__, template_folder="templates")


@search_blueprint.route("/search/")
def search_page():
    search_arg = request.args.get("s", "").lower()
    all_posts = PostDAO()
    search_posts = all_posts.search_for_posts(search_arg)
    return render_template("search.html", search_arg=search_arg, posts=search_posts, numbers=len(search_posts))
