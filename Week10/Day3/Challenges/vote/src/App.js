import React, { useState } from 'react';
import './App.css';

function App() {
  const [languages, setLanguages] = useState([
    { name: 'Php', votes: 0 },
    { name: 'Python', votes: 0 },
    { name: 'JavaScript', votes: 0 },
    { name: 'Java', votes: 0 },
  ]);

  const handleVote = (languageName) => {
    const index = languages.findIndex((language) => language.name === languageName);
    const newLanguages = [...languages];
    newLanguages[index].votes += 1;
    setLanguages(newLanguages);
  };

  const handleReset = (languageName) => {
    const index = languages.findIndex((language) => language.name === languageName);
    const newLanguages = [...languages];
    newLanguages[index].votes = 0;
    setLanguages(newLanguages);
  };

  return (
    <div className='App'>
      <h1>Vote for your favorite language</h1>
      <ul>
        {languages.map((language, index) => (
          <li key={index}>
            <span className="vote-count">{language.votes}</span>
            <span className="language-name">{language.name}</span>
            <span>
              <button onClick={() => handleVote(language.name)} style={{ backgroundColor: "#ccc" }}>Vote</button>
              <button onClick={() => handleReset(language.name)} style={{ backgroundColor: "#ccc" }}>Reset</button>
            </span>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
