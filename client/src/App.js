import React, { useState } from 'react';
import logo from './logo.png';
import ytlogo from './yt-logo.png';
import axios from 'axios';
import Result from './components/Result';
import Button from '@material-ui/core/Button';
import CircularProgress from '@material-ui/core/CircularProgress';
import { motion } from "framer-motion"
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {

  const incrementLength = 6
  const [searchTerm, setSearchTerm] = useState(null)
  const [results, setResults] = useState([])
  const [showResults, setShowResults] = useState([])
  const [length, setLength] = useState(incrementLength)
  const [searchAttempt, setSearchAttempt] = useState(false)
  const [loading, setLoading] = useState(false);

  //const MAIN_URL = "http://localhost:8000"
  const MAIN_URL = "https://waveform-server.herokuapp.com"

  const handleSubmit = (e) => {
    setLoading(true)
    e.preventDefault();
    let url = MAIN_URL + "/api/search?search="
    axios.get(url + searchTerm)
    .then((response) => {
      setLoading(false);
      if(response.data.length > 0){
        setSearchAttempt(false)
        setResults(response.data);
        setShowResults(response.data.slice(0, incrementLength))
      }
      else{
        setSearchAttempt(true)
        setResults([])
      }
    })
    setLength(2 * incrementLength)
  }

  const handleLucky = (e) => {
    setLoading(true)
    e.preventDefault();
    let url = MAIN_URL + "/api/lucky?search="
    axios.get(url + searchTerm)
    .then((response) => {
      setLoading(false);
      if(response.data){
        setSearchAttempt(false)
        setResults([response.data])
        setShowResults([response.data]);
      }
      else {
        setSearchAttempt(true)
        setResults([])
      }
    })
  }

  const handleChange = (e) => {
    setShowResults([]);
    setSearchTerm(e.target.value);
    setSearchAttempt(false)
  }

  const loadMore = () => {
    setLength(length + incrementLength)
    setShowResults(results.slice(0, length))
  }

  const variants = {
    empty: { y: '15vh' },
    filled: { y: 0 }
  }

  return (
    <div className="App">
      <motion.div
      className="header"
        initial={{y: '100vh'}}
        animate={showResults.length ? "filled" : "empty"}
        variants={variants}>
        <img className="logo" alt="logo" src={logo}/>
        <form onSubmit={handleSubmit}>
          <input placeholder="Search" type="text" className="search" value={searchTerm} onChange={handleChange}/>
          <br />
          <Button className="wvbtn" variant="light" onClick={handleSubmit}> Waveform Search</Button>
          <Button className="wvbtn" variant="light" onClick={handleLucky}> I'm Feeling Lucky</Button>
        </form>
        <div className="additional-info">
          {showResults.length !== 0 || searchAttempt?
          <div>
            <p className="results">{results.length} results</p>
            </div>:<p className="trademark">Made by <a className="name" href="https://www.youtube.com/aphrx"><img className="yt-icon" src={ytlogo}/>Aphrx</a></p>}
          
        </div>
        {loading?<CircularProgress className="loading-results" color="white"/>:null}
      </motion.div>
      
      <div align="center">
        {showResults.map(result => Result(result))}
        {(showResults.length !== 0 && results.length !== showResults.length) ? <Button className="load-more" variant="contained" onClick={loadMore}>Load More</Button> : null}
      </div>
    </div>
  );
}

export default App;
