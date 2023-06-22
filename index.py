from flask import Flask, request
import firebase_admin
from firebase_admin import credentials, db

# Use a service account
cred = credentials.Certificate('./serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://polar-city-332413-default-rtdb.firebaseio.com'
})

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    
    # Get a reference to the database
    ref = db.reference('webhook_data')

    # Push data to the database
    ref.push(data)
    
    return 'OK', 200

if __name__ == '__main__':
    app.run(port=5000)