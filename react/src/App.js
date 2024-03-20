import React from "react";
import { useState, useEffect } from "react";
import "./App.css";
import JobTable from "./components/JobTable.jsx";
// import fakejobs from "./test.json";

export default function App() {
    const [jobData, setJobData] = useState([]);
    const [endpoint, setEndpoint] = useState("/api/jobs/all");

    function handleEndpointChange(value) {
        setEndpoint(value);
    }

    useEffect(() => {
        console.log("ENDPOINT UPDATED TO " + endpoint); // Logging updated endpoint value
        fetch(endpoint)
            .then((response) => response.json())
            .then((data) => setJobData(data))
            .catch((error) => console.error("Error:", error));
    }, [endpoint]);

    // console log the infomration in the json file as a string
    console.log(jobData);

    return (
        <div className="container">
            <JobTable
                data={jobData}
                handleEndpointChange={handleEndpointChange}
            />
            <div className="map">
                <h1>MAP</h1>
                <p>(in progress not currently functional)</p>
            </div>
        </div>
    );
}
