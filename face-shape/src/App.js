import React, {useState} from 'react';
import logo from './logo.svg';
import './App.css';
import { Upload } from "@aws-sdk/lib-storage";
import { S3Client, S3 } from "@aws-sdk/client-s3";
import ImageUploader from 'react-images-upload';



function App() {
  const [file,setFile] = useState();
  function fileChange(e){
    var file = e.target.files[0];
    // console.log(e.target.files[0])

    const target = { Bucket:"face-shape", Key:file.name, Body:file};
    const creds = {accessKeyId: "AKIAQK6P4H6OZJOKIO4C",secretAccessKey:"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"};
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
  return (
    
    <div style={{ textAlign: 'center' }}>
        <label>Upload a picture of your face here:</label><br></br>
      <input type="file" accept="image/jpeg,image/png " id="file" onChange={fileChange}/>  
    </div>
  );
}

export default App;