import React from 'react';
import Car from './Components/Car';

const carInfo = {name: "Ford", model: "Mustang"};

function App() {
  return (
    <div>
      <Car carInfo={carInfo} />
    </div>
  );
}

export default App;
