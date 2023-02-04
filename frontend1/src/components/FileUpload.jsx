import "./FileUpload.css";
import React, { useState } from 'react';
import axios from 'axios';


const FileUpload = () => {
    const [status, setStatus] = useState(false);
    const [file, setFile] = useState();
    const [upload, setUpload] = useState(false);
    const [prediction, setPrediction] = useState("")

    
    const wrapper = document.querySelector(".wrapper");
    const fileName = document.querySelector(".file-name");
    const defaultBtn = document.querySelector("#default-btn");
    const customBtn = document.querySelector("#custom-btn");
    const cancelBtn = document.querySelector("#cancel-btn i");
    const img = document.querySelector("img");
    let regExp = /[0-9a-zA-Z\^\&\'\@\{\}\[\]\,\$\=\!\-\#\(\)\.\%\+\~\_ ]+$/;
    
    function defaultBtnActive(){
        const defaultBtn = document.querySelector("#default-btn");

        defaultBtn.click();

        setStatus(true);
    }

    if (status && !prediction) {
        defaultBtn.addEventListener("change", function(){
            const file = this.files[0];
            setFile(file);
            if(file){
                // const reader = new FileReader();
                // reader.onload = function(){
                //     const result = reader.result;
                //     img.src = result;
                //     wrapper.classList.add("active");
                // }
                // reader.readAsDataURL(file);

                predict(file);
                setUpload(true);
                // FileSaver.saveAs(imgFile, "/Users/joesurf/Downloads");
            }
        });
    }

    const predict = async (file) => {
        let user = {
            Id: 78912,
            Customer: "Jason Sweet",
            Quantity: 1
          };

        try {
            const response = await axios.post(`http://localhost:8000/infer/${file.name}/`, user);
            console.log("Request successful!");
            console.log(response.data)
            setPrediction(response.data["prediction"])

          } catch (error) {
            if (error.response) {
              console.log(error.reponse.status);
            } else {
              console.log(error.message);
            }
        }
    }


    return (
        <div className="w-[100%] h-[100%] relative z-[5]">
            <div className="container">
                { !file && 
                <div className="wrapper">
                    <div className="image">
                        <img src={file} alt="" />
                    </div>
                    <div className="content">
                        <div className="icon">
                            <i className="fas fa-cloud-upload-alt"></i>
                        </div>
                        <div className="text">
                            No file chosen, yet!
                        </div>
                    </div>
                </div>
                }
                {
                    upload && 
                    <div className="wrapper">
                        {/* <div className="image">
                            <img src={file} alt="" />
                        </div> */}
                        <div className="content">
                            <div className="icon">
                                <i className="fas fa-cloud-upload-alt"></i>
                            </div>
                            <div className="text">
                                { prediction } faceshape detected!
                                Finding earrings for you...
                            </div>
                        </div>
                        <div id="cancel-btn">
                            <i className="fas fa-times"></i>
                        </div>
                        <div className="file-name">
                            File name here
                        </div>
                    </div>
                }
                <button onClick={defaultBtnActive} id="custom-btn">Choose a file</button>
                <input id="default-btn" type="file" hidden />
            </div>
        </div>
    );
}


export default FileUpload;
