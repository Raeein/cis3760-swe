import Alert from 'react-bootstrap/Alert';
const ErrorAlert = (props) => {
    return <div>
        <Alert variant='danger' onClose={props.onClose} dismissible>
            {props.errorMessage}
        </Alert>
    </div>
}

export default ErrorAlert;