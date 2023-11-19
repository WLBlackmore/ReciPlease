import React, { useState } from 'react';
import './GroceryOutputPage.css'; 

const GroceryOutputPage = (props) => {
    const processedData = props.processedData;
    // Initialize strikethrough state for each row
    const [strikethroughs, setStrikethroughs] = useState(new Array(processedData.length).fill(false));

    // Function to toggle strikethrough
    const toggleStrikethrough = index => {
        const newStrikethroughs = [...strikethroughs];
        newStrikethroughs[index] = !newStrikethroughs[index];
        setStrikethroughs(newStrikethroughs);
    };

    // Calculate the total price
    const totalPrice = processedData.reduce(
        (acc, item) => acc + item.number * item.price,
        0
    );

    return (
        <body>
            <div className="container">
                <h2>My Shopping List</h2>
                <table>
                    <thead>
                        <tr>
                            <th>Product Name</th>
                            <th>Quantity</th>
                            <th>Price</th>
                        </tr>
                    </thead>
                    <tbody>
                        {processedData.map((item, index) => (
                            <tr 
                                key={index} 
                                onClick={() => toggleStrikethrough(index)}
                                style={{ textDecoration: strikethroughs[index] ? 'line-through' : 'none' }}
                            >
                                <td>{item.product}</td>
                                <td>{item.number}</td>
                                <td>${item.price.toFixed(2)}</td>
                            </tr>
                        ))}
                        <tr>
                            <td colSpan="2" style={{ textAlign: 'right' }}><strong>Total:</strong></td>
                            <td><strong>${totalPrice.toFixed(2)}</strong></td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </body>
    );
};

export default GroceryOutputPage;
