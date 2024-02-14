import React, { useState } from "react";
import SearchBar from "./SearchBar";
import SlidingPane from "react-sliding-pane";
import "react-sliding-pane/dist/react-sliding-pane.css";

export default function JobTable({ data }) {
  const [search, setSearch] = useState("");
  const [detailsPane, setDetailsPane] = useState({ visible: false, data: null });

  function searchBarChange(event) {
    setSearch(event.target.value);
  }

  return (
    <>
      <div>
        <span className="logo">GeoJobSearch</span>
      </div>

      <div className="JobTable">
        <SearchBar onSearched={searchBarChange} />
        <div className="card-list">
          {data
            .filter((item) => {
              return (
                search.toLowerCase() === "" ||
                item.jobTitle.toLowerCase().includes(search.toLowerCase())
              );
            })
            .map((job) => (
              <article
                className="card"
                key={job.jobId}
                onClick={() => setDetailsPane({ visible: true, data: job })}
              >
                <h1>{job.jobTitle}</h1>
                <p>Salary: {job.salary}</p>
                <h2>located in {job.jobLocation}</h2>
              </article>
            ))}
        </div>
      </div>

      {detailsPane.visible && (
        <SlidingPane
          isOpen={detailsPane.visible}
          title={detailsPane.data.jobTitle}
          onRequestClose={() => setDetailsPane({ visible: false, data: null })}
          from="left"  
          width="30%"
        >
          <div>
            <h3>Job Details</h3>
            <p>Salary: {detailsPane.data.salary}</p>
            <p>Location: {detailsPane.data.jobLocation}</p>
            <p>Description: {detailsPane.data.description}</p>
          </div>
        </SlidingPane>
      )}
    </>
  );
}