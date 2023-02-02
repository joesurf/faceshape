from torch import nn, optim, as_tensor
from torch.optim import lr_scheduler
import torch.nn.functional as F
from facenet_pytorch import InceptionResnetV1
import torchvision.models as models
from pprint import pprint


def buildModel():
    '''
    Add two fully connected layers to pretrained resnet model
    '''
    #model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
    # model = InceptionResnetV1(pretrained='vggface2').eval()
    model = models.vgg16(weights=models.VGG16_Weights.DEFAULT)

    num_classes = 5

    for param in model.parameters():
        param.requires_grad = False

    num_features = model.classifier[6].in_features
    model.classifier._modules['6'] = nn.Sequential(
        nn.Linear(num_features, 256), #Adding our own fully connected layers
        nn.ReLU(inplace = True),
        nn.Linear(256, num_classes),
        nn.ReLU(inplace = True) 
    )

    # num_features=model.fc.in_features
    # model.fc = nn.Sequential(
    #     nn.Linear(num_features, 256), #Adding our own fully connected layers
    #     nn.ReLU(inplace = True),
    #     nn.Linear(256, num_classes),
    #     nn.ReLU(inplace = True) 
    # )
    return model