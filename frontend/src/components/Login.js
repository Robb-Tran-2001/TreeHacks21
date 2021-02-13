import React from 'react';
import axios from 'axios';
import Home from './Home';

class Login extends React.Component {
  constructor(props) {
        super(props);
        this.state = {
            email: '',
            password: '',
            submit: 0
        }
        this.handleOnClick = this.handleOnClick.bind(this);
        this.handleOnChange = this.handleOnChange.bind(this);
    };

    handleOnClick(event) {
        console.log("CLICKED")
        event.preventDefault();

        var payload={
            "email":this.state.email,
            "password":this.state.password
        }

        axios.post('http://localhost:5000/user/login', payload)
            .then( (response)=> {
                console.log(response);
                if(response.status === 200){
                    this.setState({submit: 1});
                }
                else if(response.status === 401) {
                    alert("Bad credentials")
                    console.log("Bad credentials")
                }
            })
            .catch(function (error) {
                console.log(error);
            });
    }

    handleOnChange(event) {
        event.preventDefault();
        const name = event.target.name;
        const value = event.target.value;
        this.setState({[name]: value});
    }

    render() {
        if(this.state.submit === 1) return <Home/>
        return (
            <div> 
                <form id="info">
                    <input name="email" value={this.state.email} type="text" placeholder="Email" onChange={this.handleOnChange}/>
                    <input name="password" value={this.state.password} type="password" placeholder="Password" onChange={this.handleOnChange}/>
                </form>
                <button className='button' name="submit" value={this.state.submit} onClick={this.handleOnClick}/>
            </div>
        )
    }
}

export default Login;