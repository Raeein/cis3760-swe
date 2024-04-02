import React from "react";
import SlidingPane from "react-sliding-pane";
import "react-sliding-pane/dist/react-sliding-pane.css";
import "./JobSideBar.css";
import money from "../../assets/money.svg";
import pin from "../../assets/pin.svg";

export default function JobSidebar({ detailsPane, setDetailsPane }) {
    return (
        <>
            {detailsPane.visible && (
                <SlidingPane
                    isOpen={detailsPane.visible}
                    title={detailsPane.data.jobTitle + " information"}
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
                                    <div className="job-info-location">
                                        <div className="pin-logo">
                                            <img src={pin} alt="Pin Logo" />
                                        </div>
                                        <p>{detailsPane.data.jobLocation}</p>
                                    </div>
                                    <div className="pay">
                                        <div className="money-logo">
                                            <img src={money} alt="money Logo" />
                                        </div>
                                        <p>
                                            {detailsPane.data.salary !== "Salary not given" ? (
                                                <>
                                                    {detailsPane.data.salary}/hour -{" "}
                                                </>
                                            ) : (
                                                "Salary not given - "
                                            )}

                                            {
                                                detailsPane.data.employmentType
                                            }{" "}
                                            position
                                        </p>
                                    </div>
                                </div>
                                <div className="job-info-body">
                                    <p>{detailsPane.data.jobDescription}</p>
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
