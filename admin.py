from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'App python + flask - gguerra'

@app.route('/users')
def usuarios():
    return 'Cadastro de usuários'

if __name__ == '__main__':
    app.run()
