# Faceshape Detection for Earrings Recommendation

This project uses facial recognition to identify the face shape of users - heart, oblong, oval, round and square. The face shape is then used to determine the right fit of earrings, as shown below.

## Setup
### Frontend
1. Change directory into frontend vite
2. Run `npm i` to install modules
3. Run `npm run dev`

### Backend
1. Run `conda create --name <env> --file requirements.txt`
2. Change directory into backend
3. Run `uvicorn backend:app --reload`

### Backend with PeekingDuck
1. Run peekingduck init to start peekingduck
2. Run peekingduck run to run peedkingduck pipeline


## User Stories
Upload a photo to the webpage and receive a classification result of what earrings is most suitable for the user's face shape.


## Features
- Image upload
- Face shape prediction from upload
    - Build ml model to detect facial features (shape)
        - Data Preparation - Data augmentation
        - Model Creation(choosing which model we are using, if dh need ownself create)
        - Model Training
        - Model Inference
- Recommend type of earrings through external link


### Training Phase
1. Load data from dataset
2. Load model from models
3. Train model on data `python train_classifier.py`
4. Use peekingduck pipeline


### Inference Phase
1. User uploads photo
2. Photo gets pushed to ML pipeline
3. ML model produces inference
4. Inference used to recommend earrings

 

**Tech Stack**
- Website (To be Hoseed on AWS)
- Frontend - React/Vite (npm)
- Backend - Python, Tensorflow