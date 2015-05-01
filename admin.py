from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'App python + flask - gguerra'

if __name__ == '__main__':
    app.run()
