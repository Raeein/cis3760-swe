import React from "react";
import SearchBar from "./SearchBar";
import { useState } from "react";

export default function JobTable({ data }) {
  const [search, setSearch] = useState("")

  const [detailsPane, setDetailsPane] = React.useState({visible: false, data: null});



  function searchBarChange(event) {
    // console.log(event.target.value);
    setSearch(event.target.value);
  }

  return (
    <>
      <div>
          <span className="logo">GeoJobSearch</span>
      </div>

      <div>
        <pre>
          {JSON.stringify(detailsPane.data, null, 2)}
        </pre>
      </div>
        
      <div className="JobTable">
        <h1>Should be open? {detailsPane.visible ? "Yes" : "No"}</h1>
        <SearchBar onSearched={searchBarChange} />
        <div className="card-list">
          {data
            .filter((item) => {
              return search.toLowerCase() === ""
                ? item
                : item.jobTitle.toLowerCase().includes(search.toLowerCase());
            })
            .map((job) => (
              <article className="card" key={job.jobId} onClick={() => setDetailsPane({visible: true, data: job})}>
                <h1>{job.jobTitle}</h1>
                <p>Salary: {job.salary}</p>
                {/* <p>{job.description}</p> */}
                <h2>located in {job.jobLocation}</h2>
              </article>
            ))}
        </div>
      </div>
    </>
  );
}