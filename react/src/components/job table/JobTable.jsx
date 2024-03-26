import React, { useState } from "react";
import SearchBar from "../search/SearchBar";
import JobCard from "../job card/JobCard";
import FilterMenu from "../filter/FilterMenu";
import JobSidebar from "../job side bar/JobSidebar";
import "./JobTable.css";

export default function JobTable({ data, handleEndpointChange }) {
    const [search, setSearch] = useState("");

    const [detailsPane, setDetailsPane] = useState({
        visible: false,
        data: null,
    });

    const [filterPane, setfilterPane] = useState({
        visible: false,
        data: null,
    });

    return (
        <>
            <div>
                <span className="logo">GeoJobSearch</span>
            </div>

            <div className="JobTable">
                <div className="search-container">
                    <SearchBar
                        setSearch={setSearch}
                        handleEndpointChange={handleEndpointChange}
                    />
                    <button
                        className="filter-icon"
                        onClick={() =>
                            setfilterPane({ visible: true, data: null })
                        }
                    >
                        filter
                    </button>
                </div>
                <div className="card-list">
                    {Array.isArray(data) &&
                        data.map((job, index) => (
                            <JobCard
                                job={job}
                                handleDetailsPane={setDetailsPane}
                                key={index}
                            />
                        ))}
                </div>
            </div>

            <JobSidebar
                detailsPane={detailsPane}
                setDetailsPane={setDetailsPane}
            />

            <FilterMenu
                search={search}
                setSearch={setSearch}
                handleEndpointChange={handleEndpointChange}
                filterPane={filterPane}
                setfilterPane={setfilterPane}
            />
        </>
    );
}
