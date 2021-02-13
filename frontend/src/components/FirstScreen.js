import React from 'react';

class FirstScreen extends React.Component {
  constructor(props) {
        super(props);
        this.state = {
            flag: 0
        }
    };

    handleOnClick(event) {
        event.preventDefault();
        if(event.target.name === 'registerButton') this.setState({flag: 1});
        else if(event.target.name === 'loginButton') this.setState({flag: 2});
    }

    render() {
        if(this.flag === 1) return <Register/>
        if(this.flag === 2) return <Login/>
        return (
            <div> 
                <h1> Welcome to AI WOJ </h1>
                <p> Login to begin using. If you don't have an account, sign up. Get your NBA stories here! </p>
                <br/>
                <button name='registerButton' value={this.flag} onClick={this.handleOnClick}/>
                <button name='loginButton' value={this.flag} onClick={this.handleOnClick}/>
            </div>
        )
    }
}

export default FirstScreen;