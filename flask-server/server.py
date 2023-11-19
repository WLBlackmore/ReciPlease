from flask import Flask, jsonify, request
from flask_cors import CORS
# Ensure that the following import works:
from py.Datastream import getJSONStringFromTypeUnit
from py.RecipeHandling import RecipeHandler
import os

print("Starting the server...")

app = Flask(__name__)
CORS(app)

@app.route('/submit-form', methods=['POST'])
def handleFormSubmission():
    data = (request.json)
    ingredients_data = data['ingredients']
    processed_data = [(item['ingredient'], item['quantity']) for item in ingredients_data]
    dir_path = os.path.dirname(os.path.realpath(__file__))
    csv_file_path = os.path.join(dir_path, 'py\\Grocery Items Dataset - Sheet1.csv')  # Update to your file's relative location
    handler = RecipeHandler(csv_file_path)
    products = handler.getMinimumProductsForRecipe(processed_data)
    print(products)
    return jsonify({'status': 'success', 'message': 'Form data received'})
    

@app.route('/test')
def test():
    try:
        # Make sure this function returns a Python dict or list, not a JSON string.
        data = getJSONStringFromTypeUnit("flask-server/py/FoodTypes.csv")
        return jsonify(data)
    except Exception as e:
        print(f"An error occurred: {e}")
        # Return a proper error message if something goes wrong.
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == "__main__":
    print("Running in __main__")
    # Remove debug=True for production.
    app.run(debug=True)
