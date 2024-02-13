import React from "react";
import SearchBar from "./SearchBar";
import { useState } from "react";

import { motion, AnimatePresence } from "framer-motion";

export default function JobTable({ data }) {
  const [search, setSearch] = useState("")

  const testHandler = (param) => {
    alert(`You clicked a card! ${param}`);
  }

  function searchBarChange(event) {
    // console.log(event.target.value);
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
              : item.jobTitle.toLowerCase().includes(search.toLowerCase());
          })
          .map((job) => (
            <article className="card" key={job.jobId} onClick={() => testHandler(job.jobTitle)}>
              <h1>{job.jobTitle}</h1>
              <p>Salary: {job.salary}</p>
              {/* <p>{job.description}</p> */}
              <h2>located in {job.jobLocation}</h2>
            </article>
          ))}
      </div>
    </div>
  );
}