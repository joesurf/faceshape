from models.inception_resnet_v1 import InceptionResnetV1
from torch import nn, optim, as_tensor
from torch.optim import lr_scheduler
import torch.nn.functional as F


from .dataloader import class_names


device = 0 # CHANGE

def buildModel():
    '''
    Add two fully connected layers to pretrained resnet model
    '''
    
    # create neural network model

    for param in model.parameters():
        param.requires_grad = False

    num_features=model.fc.in_features
    model.fc = nn.Sequential(
        nn.Linear(num_features, 256), #Adding our own fully connected layers
        nn.ReLU(inplace = True),
        nn.Linear(256, 133),
        nn.ReLU(inplace = True) # output should have 133 nodes as we have 133 classes of dog breeds
    )
    return model