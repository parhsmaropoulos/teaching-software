import React, {Component} from 'react'
import { Container } from 'react-bootstrap'
import RegisterForm from '../forms/RegisterForm'

class Register extends Component{

    render(){
        return(
            <Container>
                <RegisterForm/>
            </Container>
        )
    }
}

export default Register;