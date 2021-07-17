import os

from flask import Flask


def createApp():
    app = Flask(__name__)
    
    from app.views.dashboard import dashBoard
    app.register_blueprint(dashBoard)

    return app