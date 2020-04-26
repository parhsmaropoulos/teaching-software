import React , {Component} from 'react';
import { Form, Button, Col } from 'react-bootstrap';

class TestRegisterForm extends Component{
    state = {
        questions: []
    }

    addQuestion(){
        this.setState({questions: [...this.state.questions,""]})
    }

    render() {
        return(
            <div>
            <Form>
                <Form.Row>
                    <Form.Group as={Col} controlId="TeacherName">
                                <Form.Label>Teacher Name</Form.Label>
                                <Form.Control type="text" placeholder="Enter your name" required />
                    </Form.Group>

                    <Form.Group as={Col} controlId="TestName">
                                <Form.Label>Test Name</Form.Label>
                                <Form.Control type="text" placeholder="Enter your test name" required />
                    </Form.Group>
                </Form.Row>
                <Button onClick={(e) => this.addQuestion(e)} >Add Question</Button>
            </Form>

                {
                    this.state.questions.map((question,index)=>{
                        return (
                            <Form>
                                <Form.Row>
                                    <Form.Group as={Col} controlId="Number1">
                                                <Form.Label>Number 1</Form.Label>
                                                <Form.Control type="number" placeholder="First number" required />
                                    </Form.Group>
                                    <Form.Group as={Col} controlId="Number2">
                                                <Form.Label>Number 2</Form.Label>
                                                <Form.Control type="number" placeholder="Second number" required />
                                    </Form.Group>
                                </Form.Row>
                                <Form.Group controlId="Answer">
                                            <Form.Label>Answer</Form.Label>
                                            <Form.Control type="number" placeholder="Answer" required />
                                </Form.Group>
                            </Form>
                        )
                    })
                }
            </div>
        )
    }
}


export default TestRegisterForm;