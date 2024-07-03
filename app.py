from flask import Flask
from flask import request
from flask import jsonify
from summarizer import Summarizer


app = Flask(__name__)


@app.route('/message',  methods = ['POST'])
def api():
    data = request.json
    messages = data['messages']

    summarizer = Summarizer()
    response = summarizer.new_query(messages)

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
