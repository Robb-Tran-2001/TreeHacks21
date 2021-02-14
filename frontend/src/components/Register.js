import React from 'react';
import axios from 'axios';
import Home from './Home';

class Register extends React.Component {
  constructor(props) {
        super(props);
        this.state = {
            fname: '',
            lname: '',
            email: '',
            password: '',
            submit: 0
        }
        this.handleOnClick = this.handleOnClick.bind(this);
        this.handleOnChange = this.handleOnChange.bind(this);
    };

    handleOnClick(event) {
        event.preventDefault();
        var payload={
            "fname": this.state.fname,
            "lname":this.state.lname,
            "email":this.state.email,
            "password":this.state.password
        }

        axios.post('http://localhost:5000/user/signup', payload)
            .then( (response)=> {
                console.log(response);
                if(response.status === 200){
                    this.setState({submit: 1});
                }
                else if(response.status === 409) {
                    alert("User already exists")
                    this.setState({success: 2})
                }
            })
            .catch(function (error) {
                console.log("What's wrong: ", error);
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
                    <input name="fname" value={this.state.fname} type="text" placeholder="First name" onChange={this.handleOnChange}/>
                    <input name="lname" value={this.state.lname} type="text" placeholder="Last name" onChange={this.handleOnChange}/>
                    <input name="email" value={this.state.email} type="text" placeholder="Email" onChange={this.handleOnChange}/>
                    <input name="password" value={this.state.password} type="password" placeholder="Password" onChange={this.handleOnChange}/>
                </form>
                <button className='button' name="submit" value={this.state.submit} onClick={this.handleOnClick}/>
            </div>
        )
    }
}

export default Register;