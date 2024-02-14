import React from "react";
import { useState, useEffect } from "react";
import "./App.css";
import JobTable from "./components/JobTable.jsx";
import fakejobs from "./test.json";

export default function App() {
  const [jobData, setJobData] = useState([]);
  useEffect(() => {
    fetch("/api/jobs/all")
      .then((response) => response.json())
      .then((data) => setJobData(data))
      .catch((error) => console.error("Error:", error));
  }, []);

  // console log the infomration in the json file as a string
  console.log(jobData);

  return (
    <div className="container">
      <JobTable data={jobData} />
      <div className="map">
        <h1>MAP</h1>
      </div>
    </div>
  );
}
