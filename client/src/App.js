import './App.css';
import React, { useState } from 'react';
import logo from './logo.png';
import axios from 'axios';
import Result from './components/Result';
import Button from '@material-ui/core/Button';

function App() {

  const incrementLength = 5
  const [searchTerm, setSearchTerm] = useState(null)
  const [results, setResults] = useState([])
  const [showResults, setShowResults] = useState([])
  const [length, setLength] = useState(incrementLength)

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(searchTerm)
    let url = "http://localhost:8000/api/search?search="
    axios.get(url + searchTerm)
    .then((response) => {
      setResults(response.data);
      setShowResults(response.data.slice(0, incrementLength))
    })
    setLength(2 * incrementLength)
  }

  const handleChange = (e) => {
    setShowResults([]);
    setSearchTerm(e.target.value);
  }

  const loadMore = () => {
    setLength(length + incrementLength)
    setShowResults(results.slice(0, length))
  }


  return (
    <div className="App">
      <img className="logo" alt="logo" src={logo}/>
      <form onSubmit={handleSubmit}>
        <input placeholder="Search" type="text" className="search" value={searchTerm} onChange={handleChange}/>
      </form>
      <div className="additional-info">
      {(showResults.length != 0)?<p className="results">{results.length} results</p>:null}
      </div>
      <div align="center">
        {showResults.map(result => Result(result))}
        {(showResults.length != 0 && results.length != showResults.length) ? <Button className="load-more" variant="contained" onClick={loadMore}>Load More</Button> : null}
      </div>
    </div>
  );
}

export default App;
