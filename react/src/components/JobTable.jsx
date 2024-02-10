import React from "react";
import SearchBar from "./SearchBar";
import { useState } from "react";

export default function JobTable({ data }) {
  const [search, setSearch] = useState("");

  function searchBarChange(event) {
    console.log(event.target.value);
    setSearch(event.target.value);
  }

  return (
    <div>
      <div className="SearchContainer">
        <SearchBar onSearched={searchBarChange} />
      </div>
      <table className="Jobs">
        <thead>
          <tr>
            <th>Job ID</th>
            <th>Title</th>
            <th>Salary</th>
            {/* <th>Description</th>
                <th>Employment Type</th> */}
            <th>Location</th>
          </tr>
        </thead>
        <tbody>
          {data
            .filter((item) => {
              return search.toLowerCase() === ""
                ? item
                : item.jobTitle
                    .toLowerCase()
                    .includes(search.toLocaleLowerCase());
            })
            .map((job, index) => (
              <tr key={index}>
                <td>{job.jobId}</td>
                <td>{job.jobTitle}</td>
                <td>{job.salary}</td>
                <td>{job.jobLocation}</td>
              </tr>
            ))}
        </tbody>
      </table>
    </div>
  );
}
