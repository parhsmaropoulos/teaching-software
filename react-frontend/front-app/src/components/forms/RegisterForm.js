import React,{ Component } from "react";
import { Form, Button, Col } from "react-bootstrap";

class RegisterForm extends Component{
    render() {
        return(
            // first_name
            //  last_name
            //  username
            //  password
            //  age
            //   email
                <Form>
                    <Form.Row>

                        <Form.Group as={Col} controlId="Name">
                            <Form.Label>First Name</Form.Label>
                            <Form.Control type="text" placeholder="Enter your name" required />
                            
                        </Form.Group>
                        <Form.Group as={Col} controlId="Surname">
                            <Form.Label>Last Name</Form.Label>
                            <Form.Control type="text" placeholder="Enter your last name" required />
                        </Form.Group>
                    </Form.Row>
                    <Form.Row>
                        <Form.Group as={Col} controlId="Username">
                            <Form.Label>Username</Form.Label>
                            <Form.Control type="teaxt" placeholder="Username" required/>
                        </Form.Group>
                        <Form.Group as={Col} controlId="Password">
                            <Form.Label>Password</Form.Label>
                            <Form.Control type="passowrd" placeholder="Your Password" required/>
                        </Form.Group>
                    </Form.Row>
                    <Form.Group controlId="Email">
                        <Form.Label>Email Address</Form.Label>
                        <Form.Control type="email" placeholder="Enter email" />
                        <Form.Text className="text-muted">
                            We'll never share your email with anyone!
                        </Form.Text>
                    </Form.Group>
                    <Form.Group controlId="Age" >
                        <Form.Label>Age</Form.Label>
                        <Form.Control as="select" custom>
                            <option>6</option>
                            <option>7</option>
                            <option>8</option>
                            <option>9</option>
                            <option>10</option>
                            <option>12</option>
                            <option>12</option>
                        </Form.Control>
                    </Form.Group>

                    <Button variant="primary" type="submit">
                        Register
                    </Button>
                </Form>
        );
    }
}

export default RegisterForm;