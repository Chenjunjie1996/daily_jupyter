from flask import Flask

# 一个完整的应用
app = Flask(__name__)
@app.route('/')
def index():
    return '<h1> Hello World!</h1>'
