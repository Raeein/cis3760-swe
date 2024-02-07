import React from 'react';
import { useState, useEffect } from 'react'
import './App.css';
import JobTable from './components/JobTable.jsx'
import jobDataTest from './test.json'

function App() {

  const [jobData, setJobData] = useState([])
  useEffect(() => {
    fetch('http://localhost:8080/api/jobs/all')
      .then((response) => response.json())
      .then((data) => setJobData(data))
      .catch((error) => console.error('Error:', error))
  }, [])

  console.log(jobData);


  return (
    <div className="App">
      <JobTable data = {jobDataTest} />
    </div>
  );
}

export default App;