import "./FileUpload.css";
import React, { useState } from 'react';
import { saveAs } from 'file-saver';


const FileUpload = () => {
    const [status, setStatus] = useState(false);
    const [file, setFile] = useState();

    
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

    if (status) {
        defaultBtn.addEventListener("change", function(){
            const file = this.files[0];
            setFile(file);
            if(file){
                const reader = new FileReader();
                reader.onload = function(){
                    const result = reader.result;
                    img.src = result;
                    wrapper.classList.add("active");
                }
                reader.readAsDataURL(file);

                download(file)


                // var imgFile = new File(file, {type: "image/png"});
                // FileSaver.saveAs(imgFile, "/Users/joesurf/Downloads");
            }
        });
    }

    const download = (image) => {
        var element = document.createElement("a");
        var file = new Blob(
          [
            image
          ],
          { type: "image/*" }
        );
        element.href = URL.createObjectURL(file);
        element.download = "image.jpg";
        element.click();
      };

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
