import torchvision
from torchvision import transforms
import torch
import os
import matplotlib.pyplot as plt
import numpy as np


def createDataloaders(data, batch_size):
    '''
    Transform data from image into pixels into torch dataset and loader
    '''
    train_dataset_path = os.path.join(data, "train")
    test_dataset_path = os.path.join(data, "test")
    
    training_transform = transforms.Compose([
        transforms.RandomHorizontalFlip(p=0.5),
        transforms.RandomRotation(180),
        transforms.Resize(256),
        transforms.RandomResizedCrop((224, 224)),
        transforms.ToTensor() 
    ])
    testing_transform = transforms.Compose([
        transforms.Resize(256),
        transforms.RandomRotation(180),
        transforms.RandomResizedCrop((224, 224)),
        transforms.ToTensor()
    ])
    
    train_dataset = torchvision.datasets.ImageFolder(root=train_dataset_path, transform=training_transform)    
    test_dataset = torchvision.datasets.ImageFolder(root=test_dataset_path, transform=testing_transform)
    
    train_data_loader = torch.utils.data.DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_data_loader = torch.utils.data.DataLoader(test_dataset, batch_size=batch_size)
    
    return train_data_loader, test_data_loader



def imshow(inp, title=None):
    """Imshow for Tensor."""
    inp = inp.numpy().transpose((1, 2, 0))
    mean = np.array([0.485, 0.456, 0.406])
    std = np.array([0.229, 0.224, 0.225])
    inp = std * inp + mean
    inp = np.clip(inp, 0, 1)
    plt.imshow(inp)
    if title is not None:
        plt.title(title)
    plt.pause(0.001)  # pause a bit so that plots are updated


# Get a batch of training data
# inputs, classes = next(iter(dataloaders['train']))

# Make a grid from batch
# out = utils.make_grid(inputs)
# img = imshow(out, title=[class_names[x] for x in classes])
# plt.show()