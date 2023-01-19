import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.models as models
import torchvision.transforms as transforms

import argparse
import logging
import os
import sys
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True


from .buildModel import buildModel
from .dataloader import createDataloaders
from .train import train
from .test import test



# Configuration for Debugging andd Profiling
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))


def main(args):

    path = os.getcwd()
    args.data_dir = path + "/faceshape/FaceShapeDataset"
    args.model_dir = path + "/faceshape/models"
    args.output_dir = path + "/faceshape/output"

    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    logger.info(f"Running on Device {device}")
    logger.info(f"Hyperparameters : LR: {args.lr},  Eps: {args.eps}, Weight-decay: {args.weight_decay}, Batch Size: {args.batch_size}, Epoch: {args.epochs}")
    # logger.info(f"Data Dir Path: {args.data_dir}")
    # logger.info(f"Model Dir  Path: {args.model_dir}")
    # logger.info(f"Output Dir  Path: {args.output_dir}") 
    
    model=buildModel()
    model = model.to(device)

    train_data_loader, test_data_loader = createDataloaders(args.data_dir, args.batch_size )
    
    loss_criterion = nn.CrossEntropyLoss()
    #Using AdamW as it yieds usually better performance then Adam in most cases due to the way it uses weight decay in computations
    optimizer = optim.AdamW(model.parameters(), lr=args.lr, eps=args.eps, weight_decay = args.weight_decay)

    #Adding in the epoch to train and test/validate for the same epoch at the same time.
    for epoch_no in range(1, args.epochs +1 ):
        logger.info(f"Epoch {epoch_no} - Starting Training phase.")
        model=train(model, train_data_loader, loss_criterion, optimizer, device, epoch_no)
        logger.info(f"Epoch {epoch_no} - Starting Testing phase.")
        test(model, test_data_loader, loss_criterion, device, epoch_no)
    
    logger.info("Starting to Save the Model")
    torch.save(model.state_dict(), os.path.join(args.model_dir, 'model.pth'))
    logger.info("Completed Saving the Model")

    
if __name__=='__main__':
    parser=argparse.ArgumentParser()

    parser.add_argument(
        "--batch_size", 
        type=int, 
        default=64, 
        metavar="N", 
        help="input batch size for training (default: 64)"
    )
    parser.add_argument(
        "--epochs", 
        type=int, 
        default=5, 
        metavar="N", 
        help="number of epochs to train (default: 2)"    
    )
    parser.add_argument( 
        "--lr", 
        type=float, 
        default=0.1, 
        metavar="LR", 
        help="learning rate (default: 1.0)" 
    )
    parser.add_argument( 
        "--eps", 
        type=float, 
        default=1e-8, 
        metavar="EPS", 
        help="eps (default: 1e-8)" 
    )
    parser.add_argument( 
        "--weight_decay", 
        type=float, 
        default=1e-2, 
        metavar="WEIGHT-DECAY", 
        help="weight decay coefficient (default 1e-2)" 
    )
                        

    # parser.add_argument(
    #     '--data_dir', 
    #     type=str, 
    #     default=os.environ['SM_CHANNEL_TRAINING'])
    # parser.add_argument(
    #     '--model_dir', 
    #     type=str, 
    #     default=os.environ['SM_MODEL_DIR'])
    # parser.add_argument(
    #     '--output_dir', 
    #     type=str, 
    #     default=os.environ['SM_OUTPUT_DATA_DIR'])
    
    args=parser.parse_args()
    
    main(args)
