import React from "react";
import SlidingPane from "react-sliding-pane";
import "react-sliding-pane/dist/react-sliding-pane.css";
import majorCities from "../../cities";
import "./FilterMenu.css";
import { useState } from "react";

const employment_types = [
    "Full time",
    "Part time",
    "Internship",
    "Permanent",
    "Temporary",
    "Contract",
];

export default function FilterMenu({
    search,
    setSearch,
    handleEndpointChange,
    filterPane,
    setfilterPane,
}) {
    function handleFilterChange(value, type) {
        if (value === "") {
            handleEndpointChange("api/jobs/all");
        } else {
            type === "employment"
                ? handleEndpointChange(`api/jobs/filter/employments/${value}`)
                : handleEndpointChange(`api/jobs/filter/locations/${value}`);
        }

        setSearch((prevSearch) => {
            if (value === prevSearch) {
                handleEndpointChange("api/jobs/all");
                return "";
            } else {
                return value;
            }
        });
    }

    const [salary, setSalary] = useState({ min: 0, max: 999 });

    function handleMinSalaryChange(event) {
        const newMin = event.target.value;
        setSalary((prevSalary) => {
            if (newMin === "" && prevSalary.max === "") {
                handleEndpointChange("api/jobs/all");
                return { min: 0, max: 999 };
            } else {
                handleEndpointChange(
                    `api/jobs/filter/salaries/${newMin}&${prevSalary.max}`
                );
                return { min: newMin, max: prevSalary.max };
            }
        });
    }

    function handleMaxSalaryChange(event) {
        const newMax = event.target.value;
        console.log(newMax + "THIS IS THE NEW MAX");
        setSalary((prevSalary) => {
            if (newMax === "" && prevSalary.min === "") {
                handleEndpointChange("api/jobs/all");
                return { min: 0, max: 999 };
            } else {
                handleEndpointChange(
                    `api/jobs/filter/salaries/${prevSalary.min}&${newMax}`
                );
                return { min: prevSalary.min, max: newMax };
            }
        });
    }

    return (
        <>
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
                                        value={salary.min}
                                        onChange={handleMinSalaryChange}
                                    />
                                    <input
                                        type="text"
                                        placeholder="max"
                                        value={salary.max}
                                        onChange={handleMaxSalaryChange}
                                    />
                                </div>
                            </div>
                            <div className="employments">
                                <p>Employment Type</p>
                                <div className="employment-type-wrapper">
                                    <select
                                        value={search}
                                        onChange={(e) => handleFilterChange(e.target.value, "employment")}
                                    >
                                        <option value="">Select Employment Type</option>
                                        {employment_types.map((type) => (
                                            <option key={type} value={type}>
                                                {type}
                                            </option>
                                        ))}
                                    </select>
                                </div>
                            </div>
                            <div className="locations">
                                <p>Location</p>
                                <div className="location-wrapper">
                                    <select
                                        value={search}
                                        onChange={(e) => handleFilterChange(e.target.value, "location")}
                                    >
                                        <option value="">Select Location</option>
                                        {majorCities.major_cities.map((location) => (
                                            <option key={location} value={location}>
                                                {location}
                                            </option>
                                        ))}
                                    </select>
                                </div>
                            </div>
                        </div>
                    </div>
                </SlidingPane>
            )}
        </>
    );
}
