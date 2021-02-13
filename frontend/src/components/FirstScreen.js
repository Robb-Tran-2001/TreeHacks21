import React from 'react';
import Register from './Register';
import Login from './Login';

class FirstScreen extends React.Component {
  constructor(props) {
        super(props);
        this.state = {
            flag: 0
        }
        this.handleOnClick = this.handleOnClick.bind(this)
    };

    handleOnClick(event) {
        event.preventDefault();
        if(event.target.name === 'registerButton') this.setState({flag: 1});
        else if(event.target.name === 'loginButton') this.setState({flag: 2});
    }

    render() {
        if(this.state.flag === 1) return <Register/>;
        if(this.state.flag === 2) return <Login/>;
        return (
            <div> 
                <h1> Welcome to AI WOJ </h1>
                <p> Login to begin using. If you don't have an account, sign up. Get your NBA stories here! </p>
                <br/>
                <button className='button' name='registerButton' value={this.state.flag} onClick={this.handleOnClick}/>
                <button className='button' name='loginButton' value={this.state.flag} onClick={this.handleOnClick}/>
            </div>
        )
    }
}

export default FirstScreen;