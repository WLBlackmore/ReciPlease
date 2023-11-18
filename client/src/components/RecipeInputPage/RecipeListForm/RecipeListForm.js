import React from "react";
import './RecipeListForm.css';

const RecipeListForm = (()=>{
    return (
        <body>
            <div className="container">
                <h2>Ingredient List</h2>
                <form id="ingredientForm">
                    <div id="ingredientFields">
                        <div className="ingredient-field">
                            <input type="text" name="ingredient[]" placeholder="Ingredient" required/>
                            <input type="number" name="quantity[]" placeholder="Quantity" required/>
                            <input type="unit" name="unit[]" placeholder="Unit" required/>
                            <button type="button"  id="remove">Remove</button>
                        </div>
                    </div>
                    <button type="button" id="add">Add More</button>
                    <input type="submit" value="Submit"></input>
                </form>
            </div>
        </body>
    )
})

export default RecipeListForm;