import React from "react";
import "./JobCard.css";

export default function JobCard({ job, handleDetailsPane }) {
    return (
        <article
            className="card"
            key={job.jobId}
            onClick={() => handleDetailsPane({ visible: true, data: job })}
        >
            <h1>{job.jobTitle}</h1>
            <p>Salary: {job.salary}</p>
            <p>Company: {job.company}</p>
            <p>located in {job.jobLocation}</p>
        </article>
    );
}
