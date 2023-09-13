import React, { Component } from 'react';
import './Exercise3.css';

const style_header = {
  color: "white",
  backgroundColor: "DodgerBlue",
  padding: "10px",
  fontFamily: "Arial",
};

class Exercise extends Component {
  render() {
    return (
      <div>
        <h1 style={style_header}>Exercise 3</h1>
        <p className="para">This is a paragraph.</p>
        <a href="https://www.google.com">Google</a>
        <form>
          <input type="text" placeholder="Enter text" />
        </form>
        <img src="https://via.placeholder.com/150" alt="Placeholder" />
        <ul>
          <li>Item 1</li>
          <li>Item 2</li>
          <li>Item 3</li>
        </ul>
      </div>
    );
  }
}

export default Exercise;
