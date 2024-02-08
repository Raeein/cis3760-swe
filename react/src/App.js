import React from 'react';
import { useState, useEffect } from 'react'
import './App.css';
import JobTable from './components/JobTable.jsx'

export default function App(){

  const [jobData, setJobData] = useState([])
  useEffect(() => {
    fetch('/api/jobs/all')
      .then((response) => response.json())
      .then((data) => setJobData(data))
      .catch((error) => console.error('Error:', error))
  }, [])

  console.log(jobData);


  return (
    <div className="App">
      <JobTable data = {jobData} />
    </div>
  );
}