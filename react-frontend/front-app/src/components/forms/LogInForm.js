import React,{ Component } from "react";
import { Form, Button } from "react-bootstrap";

class LogInForm extends Component{
    render() {
        return(
                <Form>
                    <Form.Group controlId="Email">
                        <Form.Label>Email Address</Form.Label>
                        <Form.Control type="email" placeholder="Enter email" />
                        <Form.Text className="text-muted">
                            We'll never shar your email with anyone!
                        </Form.Text>
                    </Form.Group>

                    <Form.Group controlId="Password" >
                        <Form.Label>Passowrd</Form.Label>
                        <Form.Control type="password" placeholder="Password" />
                    </Form.Group>

                    <Button variant="primary" type="submit">
                        Log In!
                    </Button>
                </Form>
        );
    }
}

export default LogInForm;