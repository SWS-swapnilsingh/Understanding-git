from flask import Flask, request

app = Flask(__name__, template_folder = "templates")

@app.route('/base/<name>')
def home(name):
    return "hello from home!"

@app.route('/hello')
def hello():
    return "hello world!"

if __name__=="__main__":
    app.run()