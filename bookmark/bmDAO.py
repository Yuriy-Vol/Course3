import json
import logging
from config import PATH_BM
from bookmark.bm_class import Bookmarks
from post.postDAO import PostDAO

logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class BookmarksDAO:

    def load_bookmarks_data(self):

        with open(PATH_BM, "r", encoding="utf-8") as f:
            bookmark_data = json.load(f)
            bookmarks = []
            for bookmark in bookmark_data:
                bookmarks.append(Bookmarks(
                    bookmark["pk"]
                ))
        return bookmarks

    def get_dookmarks_all(self):
        return self.load_bookmarks_data()

    def get_bookmarks_list(self):
        all_bookmarks = self.load_bookmarks_data()
        all_bookmarks_list = []
        for bookmarks in all_bookmarks:
            all_bookmarks_list.append(bookmarks.pk)
        return all_bookmarks_list

    def get_all_post_by_bookmark(self):

        posts = PostDAO()
        all_posts = posts.get_posts_all()
        all_posts_by_bookmark = []
        all_bookmarks_list = self.get_bookmarks_list()
        for post in all_posts:
            if post.pk in all_bookmarks_list:
                all_posts_by_bookmark.append(post)
        return all_posts_by_bookmark

    def post_by_bookmark_pk(self, postid):
        post_by_id = PostDAO.get_post_by_pk(postid)
        all_bookmarks = self.get_bookmarks_list()
        bookmark_bool = False
        if post_by_id.pk in all_bookmarks:
            bookmark_bool = True
        return bookmark_bool

    def bookmark_add_del(self, postid):
        bookmarks = self.get_dookmarks_all()
        bookmarks_list = self.get_bookmarks_list()
        postid = int(postid)
        finall_bookmarks = []
        trigg = False
        for index, pk in zip(range(len(bookmarks_list)), bookmarks_list):
            logger.debug(f"bookmarks_list - {bookmarks}, postid - {index}")
            if postid == pk:
                trigg = True
                bookmarks.pop(index)
            else:
                finall_bookmarks.append({"pk": pk})
        if trigg is False:
            finall_bookmarks.append({"pk": postid})

        with open(PATH_BM, "w", encoding="UTF-8") as f:
            json.dump(finall_bookmarks, f, ensure_ascii=False, sort_keys=True, indent="\t")
