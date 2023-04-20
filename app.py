from flask import Flask

app = Flask(__name__, template_folder = "templates")

@app.route('/base/<name>')
def home(name):
    return "hello from home!"

if __name__=="__main__":
    app.run()