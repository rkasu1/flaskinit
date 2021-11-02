from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    print (1+5)
    return "<h1>Hello, my friend!</h1>"
@app.route('/avg/<name>')
def success(name):
   return 'welcome %s' % name