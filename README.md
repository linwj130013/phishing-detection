# Phishing Detection

Foobar is a Python library for dealing with word pluralization.

## Setup for the Flask server
1. Open Python IDE of your choice and select the folder flask-app
2. This step is optional but recommended: Create and activate a virtualenv
3. Install the requirements:
```bash
pip3 install -r requirements.txt
```
4. Now you can run the app using:
```bash
flask run
```
5. If you see the message "Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)", it means that the app is running successfully. Leave it running fo the chrome extension to work (this is where we will place our python code in the future)

## Setup for Chrome Extension
1. Open Google Chrome, enter "chrome://extensions" in the address bar and press Enter
2. Enable Developer mode switch (located at the top right) and click on "Load Unpacked"
3. Select the folder "chrome-extension" from the directory selection window that pops up
4. This should be enough for your extension to be up and running. Whenever you load a new webpage, you will see an alert that displays the url of that webpage.