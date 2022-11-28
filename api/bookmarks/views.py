from flask import Blueprint, render_template, redirect
from bookmark.bmDAO import BookmarksDAO

bookmarks_blueprint = Blueprint("bookmarks_blueprint", __name__, template_folder="templates")
bookmarks_blueprint_add_del = Blueprint("bookmarks_blueprint_add_del", __name__, template_folder="templates")


@bookmarks_blueprint.route("/bookmarks/")
def bookmarks_page():
    bookmarks_posts = BookmarksDAO()
    all_bookmarks_posts = bookmarks_posts.get_all_post_by_bookmark()
    bookmarks_list = bookmarks_posts.get_bookmarks_list()
    num_bookmarks = len(bookmarks_list)
    return render_template("bookmarks.html", posts=all_bookmarks_posts, num_bookmarks=num_bookmarks,
                           bookmarks_list=bookmarks_list)


@bookmarks_blueprint_add_del.route("/bookmarks/adddel/<postid>")
def bookmarks_page(postid):
    bookmarks_posts = BookmarksDAO()
    bookmarks_posts.bookmark_add_del(postid)
    return redirect('/', code=302)
