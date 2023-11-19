import React, { useEffect } from 'react';
import './GroceryOutputPage.css'; // Assuming you have a CSS file with the styles

const GroceryOutputPage = (props) => {
   return (
    <body>
    <div className="container">
        <h2>My Shopping List</h2>
        <table>
            <thead>
                <tr>
                    <th>Product Name</th>
                    <th>Quality</th>
                    <th>Price</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Product 1</td>
                    <td>3</td>
                    <td>$5.00</td>
                </tr>
                <tr>
                    <td>Product 2</td>
                    <td>2</td>
                    <td>$7.50</td>
                </tr>
                <tr>
                    <td>Product 3</td>
                    <td>5</td>
                    <td>$3.20</td>
                </tr>
                <tr>
                <td colSpan="2" style={{ textAlign: 'right' }}><strong>Total:</strong></td>
                    <td><strong>$[Total Price]</strong></td>
                </tr>
            </tbody>
        </table>
    </div>
    </body>
    );
};

export default GroceryOutputPage;
