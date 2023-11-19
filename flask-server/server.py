from flask import Flask
from flask_cors import CORS
import Datastream.py


print("Starting the server...")

app = Flask(__name__)
CORS(app)

@app.route('/submit-form', methods=['POST'])
def handleFormSubmission():
    data = request.json
    print(data)
    return jsonify({'status': 'success', 'message': 'Form data received'})

@app.route('/test')
def test():
    return {'ingredients': ["banana", "apple", "orange"]}

if __name__ == "__main__":
    print("Running in __main__")
    app.run(debug=True)

print("Completed server.py")
