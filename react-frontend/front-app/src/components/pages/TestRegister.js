import React,{Component} from 'react';
import { Container } from 'react-bootstrap';
import TestRegisterForm from '../forms/TestRegisterForm';

class TestRegister extends Component{
    render(){
        return(
            <Container>
                <TestRegisterForm/>
            </Container>
        )
    }
}

export default TestRegister;