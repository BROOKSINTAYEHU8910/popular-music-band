from flask import Flask, escape
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<b> My first Flask application in action! </b>"


@app.route("/author")
def get_author():
    res = requests.get("https://openlibrary.org/search/authors.JSON?q=Brook Sintayehu")
    if res.status_code == 200:
        return {"message": res.JSON()}
    elif res.status_code == 400:
        return {"message": "sometging went wrong!"}, 404
    else:
        return {"message": "Server error!"}, 500

@app.route("/book/<isbn>")
def get_author(isbn):
    res = requests.get("https://openlibrary.org/isbn/{escape(isbn)}.JSON")
    if res.status_code == 200:
        return {"message": res.JSON()}
    elif res.status_code == 400:
        return {"message": "sometging went wrong!"}, 404

if __name__ == '__main__':
    app.run()
