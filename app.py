from flask import Flask, request


# Init a Flask app instance
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    username = request.args.get('user')
    return 'Hello ' + username + '!\n'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=7777)
