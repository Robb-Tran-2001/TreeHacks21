import React from "react";
import loginImg from "../../login.svg";
import axios from 'axios';
import { Homepage } from '../upload/index';

export class Register extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      username: '',
      email: '',
      password: '',
      submit: 0
    }
    this.handleOnClick = this.handleOnClick.bind(this);
    this.handleOnChange = this.handleOnChange.bind(this);
  }

  handleOnClick(event) {
    console.log("CLICKED")
    event.preventDefault();

    var payload={
        "username":this.state.username,
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
    if(this.state.submit === 1) return <Homepage/>

    return (
      <div className="base-container" ref={this.props.containerRef}>
        <div className="header">Register</div>
        <div className="content">
          <div className="image">
            <img src={loginImg} />
          </div>
          <div className="form">
            <div className="form-group">
              <label htmlFor="username">Username</label>
              <input type="text" name="username" placeholder="username" value={this.state.email} onChange={this.handleOnChange}/>
            </div>
            <div className="form-group">
              <label htmlFor="email">Email</label>
              <input type="text" name="email" placeholder="email" value={this.state.email} onChange={this.handleOnChange}/>
            </div>
            <div className="form-group">
              <label htmlFor="password">Password</label>
              <input type="password" name="password" placeholder="password" value={this.state.password} onChange={this.handleOnChange}/>
            </div>
          </div>
        </div>
        <div className="footer">
          <button type="button" className="btn" name="submit" value={this.state.submit} onClick={this.handleOnClick}>
            Register
          </button>
        </div>
      </div>
    );
  }
}
