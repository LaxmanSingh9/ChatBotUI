from flask import Flask, request, jsonify
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    
    try:
        action = req.get('queryResult').get('action')
    except AttributeError:
        return 'json error'
    
    if action == 'input.welcome':
        res = {'fulfillmentText': 'Hello, Welcome to my Dialogflow agent!'}
    elif action == 'input.unknown':
        res = {'fulfillmentText': 'I am sorry, I did not understand that. Can you please repeat?'}
    else:
        res = {'fulfillmentText': 'This is a response from webhook.'}
    
    return jsonify(res)

if __name__ == '__main__':
    app.run()