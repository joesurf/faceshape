import "./FileUpload.css";
import React, { useState, useEffect } from 'react';
import axios from 'axios';


const FileUpload = () => {
    const [status, setStatus] = useState(false);
    const [file, setFile] = useState();
    const [upload, setUpload] = useState(false);
    const [prediction, setPrediction] = useState("");
    const [result, setResult] = useState("Finding the perfect pair of earrings for you...");
    const [link, setLink] = useState("");

    
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

        // console.log(file)

        // const jsonFile = JSON.stringify(file);
        // console.log(jsonFile);
          

        // try {
        //     const response = await axios.post(`http://localhost:8000/fileUpload/${jsonFile}/`, user);
        //     console.log("Uplooad successful!");
        //   } catch (error) {
        //     if (error.response) {
        //       console.log(error.reponse.status);
        //     } else {
        //       console.log(error.message);
        //     }
        // }

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

    const getEarringsFromFaceShape = () => {
        // Reference: https://blingvine.com/blogs/online-jewellery-blog/how-to-choose-the-best-earrings-for-you-face-shape
        if (prediction == "round") {
            setResult("A round face is complemented by long drop or dangle earrings. This design will elongate your face and make it look slimmer.")
            setLink("https://blingvine.com/blogs/online-jewellery-blog/earrings-for-round-faces");
        } else if (prediction == "heart") {
            setResult("For a heart shaped face, find a desert that is wider at the bottom than the top.")
            setLink("https://blingvine.com/blogs/online-jewellery-blog/earrings-for-heart-shaped-face");
        } else if (prediction == "oval") {
            setResult("Oval shaped faces are the luckiest of all, as any shape of earrings will work for you. Choose from any style.");
            setLink("https://blingvine.com/blogs/online-jewellery-blog/earrings-for-oval-face");
        } else if (prediction == "square") {
            setResult("Soften the edges of a square face with earrings that are medium to long with rounded edges. Oval shapes are a great go-to.");
            setLink("https://blingvine.com/blogs/online-jewellery-blog/earrings-for-square-face");
        } else if (prediction == "oblong") {
            setResult("For a triangular face, choose earrings that emphasise the width of your face. Studs, clustered earrings, short danglers, and hopps in medium to large size are a good fit for you.");
            setLink("https://blingvine.com/blogs/online-jewellery-blog/best-earrings-for-a-triangle-face-shape");
        // } else {
        //     setResult("I'm sorry, we can't find any earrings for you");
        }
    }

    useEffect(() => {
        getEarringsFromFaceShape()
    }, [prediction]);

    return (
        <div className="w-[100%] h-[100%] relative z-[5]">
            <div className="container">
                { 
                    !file && 
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
                                {/* { file.name } uploaded!{"\n"}
                                { prediction } faceshape detected! */}
                                { result }
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
                {
                    !prediction &&
                    <div>
                        <button onClick={defaultBtnActive} id="custom-btn">Choose a file</button>
                        <input id="default-btn" type="file" hidden />
                    </div>
                }
                {
                    prediction &&
                    <div>
                        <a href={link} target="_blank" rel="noopener noreferrer">
                            <button id="custom-btn">Go to recommended link</button>
                        </a>
                    </div>
                }

            </div>
        </div>
    );
}


export default FileUpload;
