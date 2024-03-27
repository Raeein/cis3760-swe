import React from "react";
import "./SearchBar.css";

export default function SearchBar({ setSearch, handleEndpointChange }) {
    function searchBarChange(event) {
        setSearch(event.target.value);
        handleEndpointChange(`api/jobs/searches/${event.target.value}`);
        if (event.target.value === "") {
            handleEndpointChange("api/jobs/all");
        }
    }
    return (
        <input
            className="search-bar"
            type="text"
            placeholder="search for a job..."
            onChange={searchBarChange}
        />
    );
}
