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
    <div className="JobTable">
      <SearchBar onSearched={searchBarChange} />
      <div className="card-list">
        {data
          .filter((item) => {
            return search.toLowerCase() === ""
              ? item
              : item.jobTitle
                  .toLowerCase()
                  .includes(search.toLocaleLowerCase());
          })
          .map((job) => (
            <article className="card" key={job.jobId}>
              <h1>{job.jobTitle}</h1>
              <p>Salary: {job.salary}</p>
              <p>{job.description}</p>
              <h2>located in {job.jobLocation}</h2>
            </article>
          ))}
      </div>
    </div>
  );
}
