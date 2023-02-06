import React, { useState } from 'react';
import './App.css';
import Result from './components/Result.js';
import { Upload } from "@aws-sdk/lib-storage";
import { S3Client } from "@aws-sdk/client-s3";


function App() {
  const [file,setFile] = useState();
  function fileChange(e){
    var file = e.target.files[0];
    // console.log(e.target.files[0])

    const target = { Bucket:"face-shape", Key:file.name, Body:file};
    const creds = {accessKeyId: process.env.REACT_APP_AWS_ACCESS_KEY,secretAccessKey: process.env.REACT_APP_AWS_SECRET_KEY};
    try {
      const parallelUploads3 = new Upload({
        client: new S3Client({region:"ap-southeast-1",credentials:creds}),
        leavePartsOnError: false, // optional manually handle dropped parts
        params: target,
      });

      parallelUploads3.on("httpUploadProgress", (progress) => {
        console.log(progress);
      });

      parallelUploads3.done();
    } catch (e) {
      console.log(e);
    }

  }

  // const [specs, setSpecs] = useState([])

  const specs = ['rectangle', 'browline', 'oval', 'aviators', 'geometric', 'wrap']

  // useEffect(() => {
  //   fetch("/results").then(
  //     res => res.json()
  //   ).then(
  //     specs => {
  //       setSpecs(specs)
  //       console.log(specs)
  //     }
  //   )
  // })

  const list = []

  specs.forEach((spec) => {
    list.push(<Result type={spec}></Result>)
  })

  var faceShape = "FIND FACESHAPE FUNCTION"
  return (
    
    <div style={{ textAlign: 'center' }}>
        <label>Upload a picture of your face here:</label><br></br>
      <input type="file" accept="image/jpeg,image/png " id="file" onChange={fileChange}/> 


      <header className="App-header">
        <p>
          Your face shape is {faceShape}.
          <br /> The frames recommended for your face shape are...
          {list}
        </p>
      </header>
    </div>
    );
}
export default App;

