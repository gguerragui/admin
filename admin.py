from flask import render_template
from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'gguerra'}
    render_template('index.html',
                    title='Home',
                    user=user)

@app.route('/users')
def usuarios():
    return 'Cadastro de usuários'

if __name__ == '__main__':
    app.run()
