from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    return '</br>'.join('''Человечество вырастает из детства.
Человечеству мала одна планета.
Мы сделаем обитаемыми безжизненные пока планеты.
И начнем с Марса!
Присоединяйся!'''.split('\n'))


@app.route('/image_mars')
def image_mars():
    with open('image_mars.html', encoding='utf-8') as html:
        return html.read()


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
