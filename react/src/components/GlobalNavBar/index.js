import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';
import Container from 'react-bootstrap/Container';
const GlobalNavBar = (props) => {
    return <div>
        <Navbar className="bg-body-tertiary">
            <Container>
                <Navbar.Brand>Notes App</Navbar.Brand>

                <div>
                    {props.pageName}
                </div>
            </Container>
        </Navbar>
    </div>
}

export default GlobalNavBar;