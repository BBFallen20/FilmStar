import React, {useState} from "react";
import {Button, Col, Form, Row} from "react-bootstrap";
import axios from "axios";


export const LoginPage = () => {
    const [email, setEmail] = useState('');
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [token, setToken] = useState('')
    const loginSubmitHandler = function (event) {
        event.preventDefault()
        let postData = {'email': email, 'username': username, 'password': password}
        axios.post('http://127.0.0.1:8000/api/profiles/login/', postData).then(response=>{
            setToken(response.data.key)
        })
    }
    const emailChangeHandler = function (event) {
        setEmail(event.target.value)
    }
    const passwordChangeHandler = function (event) {
        setPassword(event.target.value)
    }
    const usernameChangeHandler = function (event) {
        setUsername(event.target.value)
    }
    return (
        <>
            <Row>
                <Col md={4}>
                </Col>
                <Col md={4}>
                    <Form>
                        <h4 className="text-center mt-3">Login</h4>
                        <Form.Group className="mb-3 text-center" controlId="formBasicEmail">
                            <Form.Control type="email" placeholder="Enter email" onChange={emailChangeHandler}/>
                            <Form.Text className="text-muted">
                                We'll never share your email with anyone else.
                            </Form.Text>
                            <Form.Control type="text" placeholder="Enter username" onChange={usernameChangeHandler}/>
                        </Form.Group>
                        <Form.Group className="mb-3 text-center" controlId="formBasicPassword">
                            <Form.Control type="password" placeholder="Password" onChange={passwordChangeHandler}/>
                        </Form.Group>
                        <div className="text-center">
                            <Button variant="success" type="submit" onClick={loginSubmitHandler}>
                                Login
                            </Button>
                        </div>
                    </Form>
                </Col>
                <Col md={4}>
                </Col>
            </Row>
        </>
    )
}