import React, { useState, useEffect } from "react";
import SearchBar from "./SearchBar";
import majorCities from "../cities";
import { useNavigate, useParams } from "react-router-dom";
import SlidingPane from "react-sliding-pane";
import "react-sliding-pane/dist/react-sliding-pane.css";

export default function JobTable({ data }) {
    const [search, setSearch] = useState("");
    const [salary, setSalary] = useState({ min: 0, max: 200000 });
    const [detailsPane, setDetailsPane] = useState({
        visible: false,
        data: null,
    });
    const [filterPane, setfilterPane] = useState({
        visible: false,
        data: null,
    });

    const { keyword } = useParams(); 

    const navigate = useNavigate();

    useEffect(() => {
        if (keyword) {
            setSearch(keyword);
        }
    }, [keyword]);

    function searchBarChange(event) {
        setSearch(event.target.value);
        navigate(`/search/${event.target.value}`);
    }

    function handleMinSalaryChange(event) {
        setSalary({ min: parseInt(event.target.value), max: salary.max });
    }

    function handleMaxSalaryChange(event) {
        setSalary({ min: salary.min, max: parseInt(event.target.value) });
    }

    function handleJobCardClick(job, index) {
        console.log(job);
        setDetailsPane({ visible: true, data: job });
        navigate(`/api/jobs/get/${index}`);
    }

    function handleEmployTypeChange(value, url) {
        if (value === search) {
            setSearch("");
            navigate("/jobs/all");
        } else {
            setSearch(value);
            navigate(`/${url}/${value}`);
        }
    }

    function handleFilterclick() {
        setfilterPane({ visible: true, data: null });
        navigate("/filter");
    }

    // useEffect(() => {
    //     navigate("/jobs/all");
    // }, []);

    //create an array of objects or strings that stores every unique location in data.jobLocation in it
    //then map over that array to create a list of checkboxes

    const employment_types = [
        "Full time",
        "Part time",
        "internship",
        "permanent",
        "temporary",
        "contract",
    ];

    // const jobLocation = data.map((job) => job.jobLocation);
    // const uniquejobLocation = [...new Set(jobLocation)];
    // console.log(uniquejobLocation);

    // console.log("TYPE IS" + employType);

    // console.log(salary);
    // console.log(data);

    return (
        <>
            <div>
                <span className="logo">GeoJobSearch</span>
            </div>

            <div className="JobTable">
                <div className="search-container">
                    <SearchBar onSearched={searchBarChange} />
                    <button className="filter-icon" onClick={handleFilterclick}>
                        filter
                    </button>
                </div>
                <div className="card-list">
                    {data
                        .filter((item) => {
                            return (
                                search.toLowerCase() === "" ||
                                item.jobTitle
                                    .toLowerCase()
                                    .includes(search.toLowerCase()) ||
                                item.jobLocation
                                    .toLowerCase()
                                    .includes(search.toLowerCase()) ||
                                item.employmentType
                                    .toLowerCase()
                                    .includes(search.toLowerCase())
                            );
                        })
                        .map((job, index) => (
                            <article
                                className="card"
                                key={job.jobId}
                                onClick={() => handleJobCardClick(job, index)}
                            >
                                <h1>{job.jobTitle}</h1>
                                <p>Salary: {job.salary}</p>
                                <p>Company: {job.company}</p>
                                <p>located in {job.jobLocation}</p>
                            </article>
                        ))}
                </div>
            </div>

            {detailsPane.visible && (
                <SlidingPane
                    isOpen={detailsPane.visible}
                    title={detailsPane.data.jobTitle}
                    onRequestClose={() =>
                        setDetailsPane({ visible: false, data: null })
                    }
                    from="left"
                    width="30%"
                    overlayClassName="overlay"
                    className="slider"
                >
                    <div className="slider-details">
                        <p>Salary: {detailsPane.data.salary}</p>
                        <p>Location: {detailsPane.data.jobLocation}</p>
                        <p>Company: {detailsPane.data.company}</p>
                        <p>Description: {detailsPane.data.jobDescription}</p>
                        <p>
                            Employment type: {detailsPane.data.employmentType}
                        </p>
                        {/* <p>{detailsPane.data}</p> */}
                    </div>
                </SlidingPane>
            )}

            {filterPane.visible && (
                <SlidingPane
                    isOpen={filterPane.visible}
                    title="Filter Options"
                    onRequestClose={() =>
                        setfilterPane({ visible: false, data: null })
                    }
                    from="left"
                    width="30%"
                    overlayClassName="overlay"
                    className="slider"
                >
                    <div className="slider-details">
                        <div className="filters-wrapper">
                            <div className="salary-wrapper">
                                <p>Salary</p>
                                <div className="values-wrapper">
                                    <input
                                        type="text"
                                        placeholder="min"
                                        onChange={handleMinSalaryChange}
                                    />
                                    <input
                                        type="text"
                                        placeholder="max"
                                        onChange={handleMaxSalaryChange}
                                    />
                                </div>
                            </div>
                            <div className="employment-wrapper">
                                <p>Employment Type</p>
                                <div className="employment-type-wrapper">
                                    {employment_types.map((type) => (
                                        <label htmlFor={type} key={type}>
                                            <input
                                                type="checkbox"
                                                id={type}
                                                name={type}
                                                value={type}
                                                checked={search.includes(type)}
                                                onChange={() =>
                                                    handleEmployTypeChange(
                                                        type,
                                                        "employment"
                                                    )
                                                }
                                            />
                                            {type}
                                        </label>
                                    ))}
                                </div>
                            </div>
                            <div className="locations">
                                <p>Location</p>
                                <div className="location-wrapper">
                                    {majorCities.major_cities.map(
                                        (location) => (
                                            <label key={location}>
                                                <input
                                                    type="checkbox"
                                                    onChange={() =>
                                                        handleEmployTypeChange(
                                                            location,
                                                            "location"
                                                        )
                                                    }
                                                    checked={search.includes(
                                                        location
                                                    )}
                                                ></input>
                                                {location}
                                            </label>
                                        )
                                    )}
                                </div>
                            </div>
                        </div>
                    </div>
                </SlidingPane>
            )}
        </>
    );
}
