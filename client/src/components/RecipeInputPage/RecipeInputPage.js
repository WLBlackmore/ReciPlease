import React, {useState, useEffect} from "react";
import RecipeListForm from "./RecipeListForm/RecipeListForm";
const RecipeInputPage = (props) => {
    return (
        <RecipeListForm ingredientData={props.ingredientData}/>
    )
}

export default RecipeInputPage;