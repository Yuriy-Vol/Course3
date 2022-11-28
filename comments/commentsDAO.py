import json
from config import PATH_COMMENTS
from comments.comments_class import Comments


class CommentsDAO:

    def load_comments_data(self):

        with open(PATH_COMMENTS, "r", encoding="utf-8") as f:
            comments_data = json.load(f)
            comments = []
            for comment in comments_data:
                comments.append(Comments(
                    comment["post_id"],
                    comment["commenter_name"],
                    comment["comment"],
                    comment["pk"]
                ))
        return comments


    def get_comments_all(self):
        return self.load_comments_data()


    def get_comments_by_postsid(self, postid):
        all_comments = self.load_comments_data()
        comments = []
        for comment in all_comments:
            if str(comment.post_id) == postid:
                comments.append(comment)
        return comments