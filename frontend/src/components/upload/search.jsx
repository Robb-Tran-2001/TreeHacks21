import axios from "axios";
import React from "react";
import logoImg from "../../cover.png";


export class Search extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
        //   username: '',
        //   password: '',
            submit: 0,
            selectedFile: null
        }
        // this.handleOnClick = this.handleOnClick.bind(this);
        // this.handleOnChange = this.handleOnChange.bind(this);
    }

    // on file select
    onFileChange = event => {
        this.setState({ selectedFile: event.target.files[0] });
    };

    // on file upload
    onFileUpload = () => {
        const formData = new FormData();

        formData.append(
            "myFile",
            this.state.selectedFile,
            this.state.selectedFile.name
        );

        console.log(this.state.selectedFile);

        axios.post('http://localhost:8000/user/upload', formData)
    };

    // display file data after upload
    fileData = () => {
        if (this.state.selectedFile) {
            return (
                <div>
                    <h2>File Details</h2>
                    <p>File Name: {this.state.selectedFile.name}</p>
                    <p>File Type: {this.state.selectedFile.type}</p>
                    <p>Last Modified: {" "}{this.state.selectedFile.lastModifiedDate.toDateString()}</p>
                </div>
            )
        }
    }

    render() {
      return (
        <div className="base-container" ref={this.props.containerRef}>
          <div className="content">
            <div className="image">
              <img src={logoImg} />
            </div>
            <div className="header">Where the truth matters.</div>

          </div>
          <div className="footer">
            <input type="file" onChange={this.onFileChange} />
            <button className="btn" onClick={this.onFileUpload}>
                Search
            </button>
          </div>
        </div>
      );
  }
}