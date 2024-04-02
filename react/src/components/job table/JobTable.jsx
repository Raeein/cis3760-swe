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
            <div>
                <span className="logo-wrapper">
                    <motion.h1
                        className="logo"
                        initial={{
                            y: 80,
                            opacity: 0,
                        }}
                        animate={{
                            y: 0,
                            opacity: 1,
                        }}
                        transition={{ duration: 1.2, ease: [0.33, 1, 0.68, 1] }}
                    >
                        GeoJobSearch
                    </motion.h1>
                </span>
            </div>

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
                        filter
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
