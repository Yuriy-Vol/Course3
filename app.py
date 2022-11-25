from flask import Flask
from api.main.views import main_blueprint
from api.posts.views import posts_blueprint
from api.users.views import users_blueprint

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(posts_blueprint)
app.register_blueprint(users_blueprint)

if __name__ == "__main__":
    app.run()