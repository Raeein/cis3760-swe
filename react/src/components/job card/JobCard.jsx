import React from "react";
import "./JobCard.css";
import indeedLogo from "../../assets/indeed.svg";
import canadaJobBankLogo from "../../assets/canadaBank.svg";

export default function JobCard({ job, handleDetailsPane, setLocation }) {
    const randomLogo =
        Math.floor(Math.random() * 2) === 0 ? indeedLogo : canadaJobBankLogo;

    const applied = Math.floor(Math.random() * 40) + 10;
    const applicants = Math.floor(Math.random() * 20) + 50;
    const percentage = Math.floor((applied / applicants) * 100);

    function handleClicked(location) {
        setLocation(location);
        handleDetailsPane({ visible: true, data: job });
    }

    return (
        <article
            className="card"
            key={job.jobId}
            onClick={() => handleClicked(job.jobLocation)}
        >
            <div className="card-header">
                <div className="header-wrapper">
                    <div className="source-logo">
                        <img src={randomLogo} alt="Source Logo" />
                    </div>
                    <div className="post-info">
                        <p className="post-info-title">
                            {randomLogo === indeedLogo
                                ? "Indeed"
                                : "Canadian Job Bank"}
                        </p>
                        <p className="post-info-posted">
                            Posted {Math.floor(Math.random() * 30) + 1} days ago
                        </p>
                    </div>
                    <div className="apply">
                        {" "}
                        <p>Apply</p>{" "}
                    </div>
                </div>
            </div>
            <div className="card-body">
                <h1>
                    {job.jobTitle.length > 20
                        ? job.jobTitle.substring(0, 20) + "..."
                        : job.jobTitle}
                </h1>

                <p>
                    located in{" "}
                    {job.jobLocation.length > 15
                        ? job.jobLocation.substring(0, 20) + "..."
                        : job.jobLocation}
                </p>
            </div>
            <div className="card-footer">
                <div className="progress-bar">
                    <div
                        className="filled-progress"
                        style={{ width: `${percentage}% ` }}
                    ></div>
                </div>
                <p>
                    <span>{applied} applied</span> of {applicants}
                </p>
            </div>
        </article>
    );
}
