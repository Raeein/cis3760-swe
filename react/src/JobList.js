import jobDataTest from './test.json'
import JobTable from './JobTable.jsx'


//TODO Use for connecting Springboot api
//import axios from 'axios';

const JobList = () => {
  // const [jobData, setJobData] = useState([])
  // useEffect(() => {
  //   axios.get('/api/jobs/all')
  //     .then((response) => response.json())
  //     .then((data) => setJobData(data))
  //     .catch((error) => console.error('Error:', error))
  // }, [])

    return(
        <JobTable data = {jobDataTest} />
    )
}

export default JobList;