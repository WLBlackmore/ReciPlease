import React, { useState } from "react";
import "./RecipeListForm.css";

const DUMMYDATA = [
  { ingredient: "Beans", unit: "mL" },
  { ingredient: "Rice", unit: "g" },
  { ingredient: "Soup", unit: "mL" },
];

const RecipeListForm = () => {
  const [ingredients, setIngredients] = useState([
    { ingredient: "", quantity: 0, unit: "" },
  ]);

  const addIngredientHandler = () => {
    setIngredients([...ingredients, { ingredient: "", quantity: 0, unit: "" }]);
  };

  const removeIngredientHandler = (index) => {
    const list = [...ingredients];
    list.splice(index, 1);
    setIngredients(list);
  };

  const handleIngredientChange = (index, event) => {
    const { name, value } = event.target;
    const newIngredients = [...ingredients];
    newIngredients[index][name] = value;

    // Update unit placeholder if the ingredient matches one in DUMMYDATA
    if (name === "ingredient") {
      const matchedIngredient = DUMMYDATA.find(
        (item) => item.ingredient === value
      );
      if (matchedIngredient) {
        newIngredients[index].unit = matchedIngredient.unit;
      } else {
        // Reset the unit if the ingredient does not match
        newIngredients[index].unit = "";
      }
    }

    setIngredients(newIngredients);
  };

  return (
    <body>
      <div className="container">
        <h2>Ingredient List</h2>
        <form id="ingredientForm">
          <div id="ingredientFields">
            {ingredients.map((ingredient, index) => (
              <div className="ingredient-field" key={index}>
                <input
                  type="text"
                  name="ingredient"
                  placeholder="Ingredient"
                  value={ingredient.ingredient}
                  list="ingredient-choice"
                  onChange={(event) => handleIngredientChange(index, event)}
                  required
                />
                <input
                  type="number"
                  name="quantity"
                  placeholder="Quantity"
                  min={0}
                  value={ingredient.quantity}
                  onChange={(event) => handleIngredientChange(index, event)}
                  required
                />
                <input
                  type="text"
                  name="unit"
                  placeholder={
                    ingredient.ingredient &&
                    DUMMYDATA.find(
                      (item) => item.ingredient === ingredient.ingredient
                    )
                      ? DUMMYDATA.find(
                          (item) => item.ingredient === ingredient.ingredient
                        ).unit
                      : "Unit"
                  }
                  value={ingredient.unit}
                  onChange={(event) => handleIngredientChange(index, event)}
                  readOnly
                />

                {ingredients.length > 1 && (
                  <button
                    type="button"
                    id="remove"
                    onClick={() => removeIngredientHandler(index)}
                  >
                    Remove
                  </button>
                )}
              </div>
            ))}
          </div>
          <button type="button" id="add" onClick={addIngredientHandler}>
            Add More
          </button>
          <input type="submit" value="Submit" />
        </form>
      </div>

      <datalist id="ingredient-choice">
        {DUMMYDATA.map((item) => (
          <option key={item.ingredient} value={item.ingredient}></option>
        ))}
      </datalist>
    </body>
  );
};

export default RecipeListForm;
