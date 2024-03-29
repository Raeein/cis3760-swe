import React from "react";
import "./JobCard.css";

export default function JobCard({ job, handleDetailsPane }) {
    return (
        <article
            className="card"
            key={job.jobId}
            onClick={() => handleDetailsPane({ visible: true, data: job })}
        >
            <div className="card-header">
                <div className="header-wrapper">
                    <div className="source-logo"></div>
                    <div className="post-info">
                        <p className="post-info-title">Indeed</p>
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
                <h1>{job.jobTitle}</h1>
                <p>located in {job.jobLocation}</p>
            </div>
            <div className="card-footer"></div>
        </article>
    );
}
