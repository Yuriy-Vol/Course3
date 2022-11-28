from flask import Blueprint, render_template
from post.postDAO import PostDAO
from comments.commentsDAO import CommentsDAO

posts_blueprint = Blueprint("posts_blueprint", __name__, template_folder="templates")


@posts_blueprint.route("/posts/<postid>")
def post_page(postid):
    all_posts = PostDAO()
    all_comments = CommentsDAO()
    post = all_posts.get_post_by_pk(postid)
    comments = all_comments.get_comments_by_postsid(postid)
    return render_template("post.html", post=post, comments=comments, numbers=len(comments))
