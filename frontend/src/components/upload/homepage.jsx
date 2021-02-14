import axios from "axios";
import React from "react";
import Table from '@material-ui/core/Table';
import logoImg from "../../cover.png";
import cloudImg from "../../cloud.png";


export class Homepage extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
        //   username: '',
        //   password: '',
            submit: 0,
            selectedFile: null,
            matches: []
        }
        // this.handleOnClick = this.handleOnClick.bind(this);
        // this.handleOnChangerequest.POST['image'] = this.handleOnChange.bind(this);
    }

    // on file select
    onFileChange = event => {
        this.setState({ selectedFile: event.target.files[0] });
    };

    // on file upload
    onFileUpload = () => {
        this.setState({matches: []})
        const formData = new FormData();

        formData.append(
            "image",
            this.state.selectedFile,
            this.state.selectedFile.name
        );

        console.log(this.state.selectedFile);

        axios.post('http://localhost:8000/api/upload', formData)
    };

    // on file upload
    onSearch = () => {
        const formData = new FormData();

        formData.append(
            "image",
            this.state.selectedFile,
            this.state.selectedFile.name
        );

        console.log(this.state.selectedFile);
        axios.post('http://localhost:8000/api/images', formData)
          .then((response, data) => {
            if(response.status === 204) {
              console.log("No matches")
            } else if(response.status === 201) {
              console.log(response)
              this.setState({matches: response.data})
            } else if(response.status == 400) {
              alert("BAD REQUEST")
            }
          })
          .catch((err) => {
            console.log('error', err)
          })
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
      <div>
        <div className="base-container" ref={this.props.containerRef}>
          <div className="content">
            <div className="image">
              <img src={logoImg} />
            </div>
            <div className="header">Where the truth matters.</div>

            <div className="image">
              <img src={cloudImg} />
            </div>

          </div>
          <div className="footer">
            <input type="file" onChange={this.onFileChange} />
            <button className="btn" onClick={this.onFileUpload}>
                Upload
            </button>
          </div>
          <div className="footer">
            <button className="btn" onClick={this.onSearch}>
                Search
            </button>
          </div>
        </div>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        {this.state.matches.length !== 0 && 
        <Table bordered>
          <thead>
            <tr>
              <th>#</th>
                <th>Hash</th>
                <th>Timestamp</th>
                <th>Exact Match</th>
            </tr>
          </thead>
          <tbody>
            {this.state.matches.map((match, index) => (
            <tr>
                <th scope="Row">{index + 1}</th>
                <td>{match.hash}</td>
                <td>{match.timestamp}</td>
                <td>{String(match.div_check)}</td>
            </tr>
            ))}
          </tbody>
        </Table>
        }
      </div>
        
        )
      }
}