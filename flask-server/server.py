from flask import Flask
from flask_cors import CORS

print("Starting the server...")

app = Flask(__name__)
CORS(app)
@app.route('/test')
def test():
    return {'ingredients': ["banana", "apple", "orange"]}

if __name__ == "__main__":
    print("Running in __main__")
    app.run(debug=True)

print("Completed server.py")
