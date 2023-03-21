from flask import Flask

app = Flask(__name__)


@app.route('/carousel')
def carousel():
    with open('carousel.html', encoding='utf-8') as html:
        return html.read()


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
