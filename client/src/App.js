import React, { useState, useEffect } from 'react';
import RecipeInputPage from './components/RecipeInputPage/RecipeInputPage';

function App() {
  // Managing States
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

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
    // Log the ingredients to the console (for debugging purposes)
    console.log(ingredients);
  
    try {
      // Make a POST request to the Flask backend
      const response = await fetch('http://localhost:5000/submit-form', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ ingredients }), // Make sure to send the ingredients as a JSON string
      });
  
      // Throw error if response is not okay
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
  
      // You can add logic here to handle the response if needed
      console.log('Ingredients submitted successfully');
  
    } catch (error) {
      // Handle errors if the request fails
      console.error('Error submitting ingredients:', error);
    }
  };
  

  return (
    <>
      <RecipeInputPage ingredientData={data} onFinalSubmit={postIngredients}/>
    </>
  )
}

export default App;
