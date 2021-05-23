from flask import Flask
from flask import request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/test', methods=['POST'])
@cross_origin()
def test():
    data = request.json
    url = data['url']
    return jsonify({"url_returned": url})


if __name__ == '__main__':
    app.run()