import React, { useState, useEffect } from 'react';
import Card from 'react-bootstrap/Card';
import Navbar from 'react-bootstrap/Navbar';
import Container from 'react-bootstrap/Container';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import Row from 'react-bootstrap/Row';
import Stack from 'react-bootstrap/Stack';
import Modal from 'react-bootstrap/Modal';
import Alert from 'react-bootstrap/Alert';


const HomePage = () => {
    const [notes, setNotes] = useState([]);
    const [newNote, setNewNote] = useState('');
    const [showEdit, setShowEdit] = useState(false);
    const [noteToEdit, setNoteToEdit] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(false);
    const [errorMessage, setErrorMessage] = useState(null);

    useEffect(() => {
        fetchAllNotes();
    }, [])


    const status = (res) => {
        if (!res.ok) {
            throw new Error('Something Went Wrong');
        }
        return res;
    }

    const fetchAllNotes = () => {
        setLoading(true);
        fetch('/api/notes/all')
            .then(status)
            .then(res => res.json())
            .then(data => {
                setNotes(data);
                setLoading(false);
            }).catch(error => {
                setErrorMessage(error.message);
                setError(true);
            });
    }

    const addNewNote = () => {
        fetch('/api/notes/add', {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                text: newNote
            })
        })
        .then(status)
        .then(res => {
            console.log(res);
            setNewNote('');
            fetchAllNotes();
        }).catch(error => {
            setErrorMessage(error.message);
            setError(true);
        });
    }

    const deleteNote = (id) => {
        fetch(`/api/notes/delete/${id}`, {
            method: 'DELETE'
        })
        .then(status)
        .then(res => {
            console.log(res);
            fetchAllNotes();
        }).catch(error => {
            setErrorMessage(error.message);
            setError(true);
        });
    }

    const triggerEditModal = (note) => {
        setNoteToEdit(note);
        setShowEdit(true);
    }

    const editClose = () => {
        setShowEdit(false);
    }

    const editNote = (note) => {
        fetch('/api/notes/update', {
            method: 'PUT',
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(note)
        })
        .then(status)
        .then(res => {
            console.log(res);
            fetchAllNotes();
        }).catch(error => {
            setErrorMessage(error.message);
            setError(true);
        });
    }

    return(
        <div>
            <Navbar className="bg-body-tertiary">
                <Container>
                    <Navbar.Brand>Notes</Navbar.Brand>
                </Container>
            </Navbar>
            <Container>
                {error ? 
                    <div>
                        <Alert variant='danger' onClose={() => setError(false)} dismissible>
                            {errorMessage}
                        </Alert>
                        <br/>
                    </div>
                    :
                    <div></div>
                }
                <Row>
                    <h2>New Note</h2>
                </Row>
                <Row>
                    <Stack direction="horizontal" gap={3}>
                        <Form.Control as="textarea" rows={3} placeholder="Note..." value={newNote} onChange={(e) => setNewNote(e.target.value)}/>
                        <Button onClick={() => addNewNote()}>Add Note</Button>
                    </Stack>
                </Row>
                <br />
                <Row>
                    <h2>Note List</h2>
                </Row>
                {loading ? 
                    <div>Loading...</div>
                    : 
                    notes.length === 0? 
                        <div>List is empty..</div>
                        :
                        <Row>
                            <Stack gap={2}>
                                {notes.map(note => {
                                    return (
                                        <Card key={note.id} bg="dark" text='white'>
                                            <Card.Body>
                                                <Stack direction="horizontal" gap={1}>
                                                    <div className="p-2">{note.text}</div>
                                                    <div className="p-2 ms-auto"><Button variant='danger' onClick={() => deleteNote(note.id)}>Delete</Button></div>
                                                    <div className="p-2"><Button onClick={() => triggerEditModal(note)}>Edit</Button></div>
                                                </Stack>
                                            </Card.Body>
                                        </Card>
                                    );
                                })}
                            </Stack>
                        </Row>
                }
            </Container>
            {EditModal(noteToEdit, showEdit, editClose, editNote)}
            
        </div>
    )
}

const EditModal = (note, show, onClose, onSave) => {
    const [noteText, setNoteText] = useState();
    useEffect(() => {
        if (note) {
            setNoteText(note.text);
        }
    }, [note]);
    return(
        <Modal
            show={show}
            onHide={onClose}
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
            <Button variant="secondary" onClick={onClose}>
                Close
            </Button>
            <Button 
                variant="primary" 
                onClick={() => onSave(
                    {
                        ...note,
                        text: noteText
                    }
                )}>
                    Save
            </Button>
            </Modal.Footer>
        </Modal>
    )
    
}

export default HomePage;