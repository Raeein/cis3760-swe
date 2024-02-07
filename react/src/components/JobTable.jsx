export default function JobTable({ data }) {
    return (
        <table>
        <thead>
            <tr>
            <th>Job ID</th>
            <th>Title</th>
            <th>Salary</th>
            <th>Description</th>
            <th>Employment Type</th>
            <th>Location</th>
            </tr>
        </thead>
        <tbody>
            {data.map((job, index) => (
            <tr key={index}>
                <td>{job.id}</td>
                <td>{job.title}</td>
                <td>{job.salary}</td>
                <td>{job.description}</td>
                <td>{job.employment_type}</td>
                <td>{job.location}</td>
            </tr>
            ))}
        </tbody>
        </table>
    );
}