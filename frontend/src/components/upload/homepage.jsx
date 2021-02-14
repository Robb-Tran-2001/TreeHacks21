import React from "react";

export class Homepage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
    }
  }

  render() {
    return (
      <div className="base-container" ref={this.props.containerRef}>
        <div className="header">Hello</div>
      </div>
    );
  }
}

// import React from 'react';

// class Homepage extends React.Component {
//     constructor(props) {
//         super(props);
//         this.state = {
//             value: null,
//         };
//     }

//     render() {
//         return (
//             <h1> 
//                 Hello
//             </h1>
//         )
//     }
// }

// // export default Homepage;