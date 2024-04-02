import React from "react";
import SlidingPane from "react-sliding-pane";
import "react-sliding-pane/dist/react-sliding-pane.css";
import "./JobSideBar.css";

export default function JobSidebar({ detailsPane, setDetailsPane }) {
    return (
        <>
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
                        <div className="slider-details">
                            <div className="job-info">
                                <div className="job-info-header">
                                    <h1>{detailsPane.data.jobTitle}</h1>
                                    <h3>{detailsPane.data.company}</h3>
                                    <h3>{detailsPane.data.jobLocation}</h3>
                                    <p>Salary: {detailsPane.data.salary}</p>
                                </div>
                                <div className="job-info-body">
                                    <p>
                                        Description:{" "}
                                        {detailsPane.data.jobDescription}
                                    </p>
                                    <p>
                                        This is a{" "}
                                        {detailsPane.data.employmentType}{" "}
                                        position
                                    </p>
                                </div>
                                <a
                                    href={detailsPane.data.jobUrl}
                                    target="_blank"
                                    rel="noopener noreferrer"
                                    className="apply-button"
                                >
                                    Apply
                                </a>
                            </div>
                        </div>
                    </div>
                </SlidingPane>
            )}
        </>
    );
}
