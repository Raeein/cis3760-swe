import React, { useState } from "react";
import { motion } from "framer-motion";
import SearchBar from "../search/SearchBar";
import JobCard from "../job card/JobCard";
import FilterMenu from "../filter/FilterMenu";
import JobSidebar from "../job side bar/JobSidebar";
import "./JobTable.css";

export default function JobTable({ data, handleEndpointChange, setLocation }) {
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
            <div className="JobTable">
                <div
                    className={
                        filterPane.visible || detailsPane.visible
                            ? "search-container-filter-opened"
                            : "search-container"
                    }
                >
                    <SearchBar
                        setSearch={setSearch}
                        handleEndpointChange={handleEndpointChange}
                    />
                    <motion.button
                        className="filter-icon"
                        onClick={() =>
                            setfilterPane({ visible: true, data: null })
                        }
                        whileHover={{ scale: 1.1 }}
                        whileTap={{
                            scale: 0.9,
                            ease: "easeInOut",
                        }}
                    >
                        Filter
                    </motion.button>
                </div>
                <div className="card-list">
                    {Array.isArray(data) &&
                        data.map((job, index) => (
                            <JobCard
                                job={job}
                                handleDetailsPane={setDetailsPane}
                                setLocation={setLocation}
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
