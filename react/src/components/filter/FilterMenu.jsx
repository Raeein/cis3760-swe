import React from "react";
import SlidingPane from "react-sliding-pane";
import "react-sliding-pane/dist/react-sliding-pane.css";
import majorCities from "../../cities";
import "./FilterMenu.css";

const employment_types = [
    "Full time",
    "Part time",
    "internship",
    "permanent",
    "temporary",
    "contract",
];

export default function FilterMenu({
    search,
    setSearch,
    handleEndpointChange,
    filterPane,
    setfilterPane,
}) {
    function handleEmployTypeChange(value) {
        handleEndpointChange(`api/jobs/filter/employments/${value}`);
        setSearch((prevSearch) => {
            if (value === prevSearch) {
                handleEndpointChange("api/jobs/all");
                return "";
            } else {
                return value;
            }
        });
    }

    function handleLocationChange(value) {
        handleEndpointChange(`api/jobs/filter/locations/${value}`);
        setSearch((prevSearch) => {
            if (value === prevSearch) {
                handleEndpointChange("api/jobs/all");
                return "";
            } else {
                return value;
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
                            {/* <div className="salary-wrapper">
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
                    </div> */}
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
                                                    handleEmployTypeChange(type)
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
                                                        handleLocationChange(
                                                            location
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
