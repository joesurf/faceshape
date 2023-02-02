# Faceshape Detection for Spectacle Recommendation

This project uses facial recognition to identify the face shape of users - heart, oblong, oval, round and square. The face shape is then used to determine the right fit of spectacles, as shown below.

[Recommendation of glasses based on face shape]("./images/glass_frame_recommendation.jpg")


## Setup
### Frontend
1. Run npm i to install modules
2. Run npm start

### Backend
1. conda create --name <env> --file requirements.txt
2. run the main.py file

### Backend with PeekingDuck
1. Run peekingduck init to start peekingduck
2. Run peekingduck run to run peedkingduck pipeline


## Usage
Upload a photo to the webpage and receive a classification result of what face shape the user has.


## Features
- Take photo to upload
- Build ml model to detect facial features (shape)
    Data Preparation - Data augmentation
    Model Creation(choosing which model we are using, if dh need ownself create)
    Model Training
    Model Inference
- Recommend glasses frame (offer multiple options vs offer single option)

Bonus:
Recommend color


### Training Phase
1. Load data from dataset
2. Load model from models
3. Train model on data
4. Deploy on AWS Sagemaker


### Inference Phase
1. User uploads photo
2. Photo gets pushed to ML pipeline
3. ML model produces inference
4. Inference used to recommend glass
5. Display glasses

 

**Tech Stack**
- Website (Host on AWS)
- Frontend - React (npm)
- Backend - Python, Pytorch