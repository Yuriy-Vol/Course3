import json
from config import PATH_POSTS
from post.post_class import Post


class PostDAO:

    def load_posts_data(self):

        with open(PATH_POSTS, "r", encoding="utf-8") as f:
            posts_data = json.load(f)
            posts = []
            for post in posts_data:
                posts.append(Post(
                    post["poster_name"],
                    post["poster_avatar"],
                    post["pic"],
                    post["content"],
                    post["views_count"],
                    post["likes_count"],
                    post["pk"]
                ))
        return posts

    def get_posts_all(self):
        return self.load_posts_data()

    def get_posts_by_user(self, user_name):
        posts = self.load_posts_data()
        posts_by_user = []
        for post in posts:
            if post.poster_name == user_name:
                posts_by_user.append(post)
        return posts_by_user

    def get_post_by_pk(self, pk):
        posts = self.load_posts_data()
        for post in posts:
            if post.pk == int(pk):
                return post

    def search_for_posts(self, query):
        posts = self.load_posts_data()
        posts_by_query = []
        for post in posts:
            if query in post.content:
                posts_by_query.append(post)
        return posts_by_query