import React from "react";
import { useState, useEffect } from "react";
import "./App.css";
import JobTable from "./components/job table/JobTable.jsx";
import JobMap from "./components/map/JobMap.jsx";
import NavBar from "./components/navbar/NavBar.jsx";

// import fakejobs from "./test.json";

export default function App() {
    const [jobData, setJobData] = useState([]);
    const [endpoint, setEndpoint] = useState("/api/jobs/all");
    const [location, setLocation] = useState("Milton, ON");

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
    console.log(location);

    return (
        <div className="container">
            <NavBar />
            <JobTable
                data={jobData}
                handleEndpointChange={handleEndpointChange}
                setLocation={setLocation}
            />
            <JobMap location={location} />
        </div>
    );
}
