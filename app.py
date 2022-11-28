from flask import Flask
from api.main.views import main_blueprint
from api.posts.views import posts_blueprint
from api.users.views import users_blueprint
from api.search.views import search_blueprint
from api.bookmarks.views import bookmarks_blueprint, bookmarks_blueprint_add_del

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(posts_blueprint)
app.register_blueprint(users_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(bookmarks_blueprint)
app.register_blueprint(bookmarks_blueprint_add_del)

if __name__ == "__main__":
    app.run()
