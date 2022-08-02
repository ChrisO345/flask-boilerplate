import os
from flask import Flask, render_template


def dir_last_updated(folder):
    return str(max(os.path.getmtime(os.path.join(root_path, f))
                   for root_path, dirs, files in os.walk(folder)
                   for f in files))


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    # set the app route (127.0.0.1:5000/hello/)
    @app.route('/hello/')
    def hello():
        return render_template("index.html", title="Hello, World!",
                               last_updated=dir_last_updated('flaskr/static'))
    return app
