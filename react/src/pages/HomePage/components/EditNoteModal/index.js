import React, { useState, useEffect } from 'react';
import Modal from 'react-bootstrap/Modal';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
const EditNoteModal = (props) => {
    const [noteText, setNoteText] = useState();
    useEffect(() => {
        if (props.note) {
            setNoteText(props.note.text);
        }
    }, [props.note]);
    
    return(
        <Modal
            show={props.show}
            onHide={props.onClose}
            backdrop="static"
            keyboard={false}
        >
            <Modal.Header closeButton>
            <Modal.Title>Edit Note</Modal.Title>
            </Modal.Header>
            <Modal.Body>
                <Form.Control as="textarea" rows={3} value={noteText} onChange={(e) => setNoteText(e.target.value)}/>
            </Modal.Body>
            <Modal.Footer>
            <Button variant="secondary" onClick={props.onClose}>
                Close
            </Button>
            <Button 
                variant="primary" 
                onClick={() => props.onSave(
                    {
                        ...props.note,
                        text: noteText
                    }
                )}>
                    Save
            </Button>
            </Modal.Footer>
        </Modal>
    )
    
}

export default EditNoteModal;