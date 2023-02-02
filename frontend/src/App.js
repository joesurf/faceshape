import React, { useState, useEffect } from 'react';

import './App.css';
import Result from './components/Result';

function App() {
  const [specs, setSpecs] = useState([])

  useEffect(() => {
    fetch("/results").then(
      res => res.json()
    ).then(
      specs => {
        setSpecs(specs)
        console.log(specs)
      }
    )
  })

  const list = []

  specs.forEach((spec) => {
    list.push(<Result type={spec}></Result>)
  })

  var faceShape = "FIND FACESHAPE FUNCTION"

  return (
    <div className="App">
      <header className="App-header">
        <p>
          Your face shape is {faceShape}.
          <br /> The frames recommended for your face shape are...
          {list}
        </p>
      </header>
    </div>
  );
}

export default App;
