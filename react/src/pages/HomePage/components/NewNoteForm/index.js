import Stack from 'react-bootstrap/Stack';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import Row from 'react-bootstrap/Row';
const NewNoteForm = (props) => {
    return <div>
        <Row>
            <h2>New Note</h2>
        </Row>
        <Row>
        <Stack direction="horizontal" gap={3}>
            <Form.Control as="textarea" rows={3} placeholder="Note..." value={props.value} onChange={(e) => props.onChange(e.target.value)}/>
            <Button onClick={() => props.onSubmit()}>Add Note</Button>
        </Stack>
        </Row>
    </div>
}

export default NewNoteForm;