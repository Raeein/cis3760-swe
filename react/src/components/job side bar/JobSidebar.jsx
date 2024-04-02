import React from "react";
import SlidingPane from "react-sliding-pane";
import "react-sliding-pane/dist/react-sliding-pane.css";

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
                        <div className="job-info">
                            <div className="job-info-header">
                                <p>Company: {detailsPane.data.company}</p>
                                <p>Location: {detailsPane.data.jobLocation}</p>
                                <p>Salary: {detailsPane.data.salary}</p>
                            </div>
                            <p>
                                Description: {detailsPane.data.jobDescription}
                            </p>
                            <p>
                                This is a {detailsPane.data.employmentType}{" "}
                                position
                            </p>
                        </div>
                    </div>
                </SlidingPane>
            )}
        </>
    );
}
