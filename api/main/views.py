from flask import Blueprint, render_template
from post.postDAO import PostDAO
from bookmark.bmDAO import BookmarksDAO

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")


@main_blueprint.route("/")
def index_page():
    all_posts = PostDAO()
    all_bookmarks = BookmarksDAO()
    posts = all_posts.get_posts_all()
    bookmarks_list = all_bookmarks.get_bookmarks_list()
    num_bookmarks = len(bookmarks_list)
    return render_template("index.html", posts=posts, num_bookmarks=num_bookmarks, bookmarks_list=bookmarks_list)
