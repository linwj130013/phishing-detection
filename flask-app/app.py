from flask import Flask
from flask import request, jsonify
from flask_cors import CORS, cross_origin
from sklearn.metrics import accuracy_score

from Url import Url
import pandas as pd

from sklearn import tree

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/phishing_detector', methods=['POST'])
@cross_origin()
def phishing_detector():
    global classifier
    data = request.json
    url = data['url']
    is_phishing_website = -1

    try:
        url_features = Url(url)
        li = []
        for col in data_cols:
            if col != "phishing":
                li.append(str(url_features.__dict__[col]))

        is_phishing_website = str(classifier.predict([li])[0])
    except Exception as e:
        print(e)

    return jsonify({"is_phishing_website": is_phishing_website})


with app.app_context():

    def drop_redundant_cols(data):
        data.drop("url_google_index", 1, inplace=True)
        data.drop('domain_google_index', 1, inplace=True)
        data.drop('domain_spf', 1, inplace=True)
        data.drop('ttl_hostname', 1, inplace=True)
        data.drop('qty_tld_url', 1, inplace=True)
        data.drop('domain_in_ip', 1, inplace=True)
        data.drop('qty_vowels_domain', 1, inplace=True)
        data.drop('server_client_domain', 1, inplace=True)
        data.drop('tld_present_params', 1, inplace=True)
        data.drop('email_in_url', 1, inplace=True)

    def load_data():
        data = pd.read_csv("dataset_full.csv")
        print(len(data.columns))
        drop_redundant_cols(data)
        print(len(data.columns))

        inputs = data[data.columns.drop("phishing")]
        outputs = data["phishing"]

        training_inputs = inputs
        training_outputs = outputs
        testing_inputs = []
        testing_outputs = []

        # training_inputs = inputs[:60000]
        # training_outputs = outputs[:60000]
        # testing_inputs = inputs[60000:]
        # testing_outputs = outputs[60000:]

        return data.columns, training_inputs, training_outputs, testing_inputs, testing_outputs


    data_cols, train_inputs, train_outputs, test_inputs, test_outputs = load_data()

    classifier = tree.DecisionTreeClassifier()
    classifier.fit(train_inputs, train_outputs)
    predictions = classifier.predict(test_inputs)
    accuracy = 100.0 * accuracy_score(test_outputs, predictions)
    print("Accuracy: " + str(accuracy))

if __name__ == '__main__':
    app.run()
