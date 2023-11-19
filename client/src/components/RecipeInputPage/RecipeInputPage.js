import React, {useState, useEffect} from "react";
import RecipeListForm from "./RecipeListForm/RecipeListForm";
const RecipeInputPage = (props) => {
    const handleSubmit = (ingredients) => {
        props.onFinalSubmit(ingredients);
    }
    return (
        <RecipeListForm ingredientData={props.ingredientData} onIntSubmit={handleSubmit}/>
    )
}

export default RecipeInputPage;