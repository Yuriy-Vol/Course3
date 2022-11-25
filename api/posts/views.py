from flask import Blueprint, render_template
from post.postDAO import PostDAO

posts_blueprint = Blueprint("posts_blueprint", __name__, template_folder="templates")


@posts_blueprint.route("/posts/<postid>")
def post_page(postid):
    all_posts = PostDAO()
    post = all_posts.get_post_by_pk(postid)

    return render_template("post.html", post=post)
