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
                        <p>Salary: {detailsPane.data.salary}</p>
                        <p>Location: {detailsPane.data.jobLocation}</p>
                        <p>Company: {detailsPane.data.company}</p>
                        <p>Description: {detailsPane.data.jobDescription}</p>
                        <p>Employment type: {detailsPane.data.employmentType}</p>
                        <a href={detailsPane.data.jobUrl} target="_blank" rel="noopener noreferrer">
                            Apply
                        </a>
                    </div>
                </SlidingPane>
            )}
        </>
    );
}
