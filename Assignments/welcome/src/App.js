import React from 'react';

import './App.css';

function Shoppping_list() {
  return (
    <div>
      <h1>Welcome, Dr.Gaster</h1>
      <hr />
      <div className="Shopping_list">
        <h3 className="list-title">
          Shopping List
        </h3>
        <ul>
          <li>Item 1</li>
          <li>Item 2</li>
          <li>Item 3</li>
          <li>Item 4</li>
        </ul>
        <h3>
          Add a new item: <input type="text" name="" id="" placeholder="New Item"/>
        </h3>
      </div>
    </div>
  );
}

export default Shoppping_list;
