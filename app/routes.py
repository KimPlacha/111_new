from flask import Flask

app = Flask(__name__)


@app.get("/about")
@app.get("/")
def index():  # sourcery skip: inline-immediately-returned-variable
    me = {
        "first_name": "Kim",  # type: ignore
        "last_name": "Placha",
        "hobbies": "Arts and Crafts",
        "is_online": True,
    }
    return me
