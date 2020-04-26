import React, {Component} from 'react';
import {Container} from 'react-bootstrap'
import LogInForm from '../forms/LogInForm';


class LogIn extends Component{
    render() {
        return(
            <Container>
                <LogInForm/>
            </Container>
        );
    }
}

export default LogIn;