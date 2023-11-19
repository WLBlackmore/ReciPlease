import React, { useState, useEffect } from 'react';
import RecipeInputPage from './components/RecipeInputPage/RecipeInputPage';
import GroceryOutputPage from './components/GroceryOutputPage/GroceryOutputPage';

function App() {
  // Managing States
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [page, setPage] = useState(0);

  // Fetching Data
  useEffect(() => {
    const fetchData = async () => {
      try {
        // Set loading to true
        setLoading(true);

        const response = await fetch('http://localhost:5000/test');

        // Throw error if response is not okay
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        // Parse the JSON data
        const data = await response.json();

        // Set the data in state
        setData(data);
      } catch (error) { // Make sure to catch the error object
        setError(error);
      } finally {
        // Updates loading state
        setLoading(false);
      }
    };
    // Calls the method when the component is rendered
    fetchData();
    // Empty dependencies --> only runs once
  }, []);

  // if (loading) {
  //   return <h1>Loading...</h1>;
  // }

  // if (error) {
  //   return <h1>Error: {error.message}</h1>;
  // }

  // return (
  //   <div>
  //     <ul>
  //       {data.ingredients && data.ingredients.map((ingredient, index) => (
  //         <li key={index}>{ingredient}</li>
  //       ))}
  //     </ul>
  //   </div>
  // );

  const postIngredients = async (ingredients) => {
    console.log(ingredients);
    
    try {
      // Make a POST request to submit ingredients
      const postResponse = await fetch('http://localhost:5000/submit-form', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ ingredients }),
      });
    
      if (!postResponse.ok) {
        throw new Error(`HTTP error! status: ${postResponse.status}`);
      }
  
      console.log('Ingredients submitted successfully');
    
      // After successful POST, fetch the generated list
      const listResponse = await fetch('http://localhost:5000/generate-list');
    
      if (!listResponse.ok) {
        throw new Error(`HTTP error! status: ${listResponse.status}`);
      }
      
      // Assuming the response is a JSON object
      const generatedList = await listResponse.json();
      
      // Here you can set the state with the generated list
      // For example:
      // setGeneratedList(generatedList);
  
      console.log('Generated list fetched successfully');
      console.log(generatedList)
    
    } catch (error) {
      console.error('Error:', error);
    }
  
    setPage(1);
  };
  
  
  if (page===0){
    return(
      <RecipeInputPage ingredientData={data} onFinalSubmit={postIngredients}/>
    )
  }
 
  if (page===1){
    return (
      <GroceryOutputPage/>
    )
  }
}

export default App;
