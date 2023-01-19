import time
import copy
import torch
import matplotlib.pyplot as plt
import logging
import sys



device = 0 # CHANGE
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))


def train(model, train_loader, criterion, optimizer, device, epoch_no):
    '''
    Trains model on data using criterion and optimizer for one epoch
    '''
    logger.info(f"Epoch: {epoch_no} - Training Model on Complete Training Dataset" )
    model.train()
    running_loss = 0
    running_corrects = 0
    running_samples = 0
    for inputs, labels in train_loader:
        inputs = inputs.to(device)
        labels = labels.to(device)
        
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        pred = outputs.argmax(dim=1,  keepdim=True)
        
        running_loss += loss.item() * inputs.size(0) 
        running_corrects += pred.eq(labels.view_as(pred)).sum().item()
        running_samples += len(inputs) 
        
        loss.backward()
        optimizer.step()
        if running_samples % 500 == 0:
            logger.info(
                "\nTrain set:  [{}/{} ({:.0f}%)]\t Loss: {:.2f}\tAccuracy: {}/{} ({:.2f}%)".format(
                    running_samples,
                    len(train_loader.dataset),
                    100.0 * (running_samples / len(train_loader.dataset)),
                    loss.item(),
                    running_corrects,
                    running_samples,
                    100.0*(running_corrects/ running_samples)
                )
            )
    total_loss = running_loss / len(train_loader.dataset)
    total_acc = running_corrects/ len(train_loader.dataset)
    logger.info( "\nTrain set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n".format(
        total_loss, running_corrects, len(train_loader.dataset), 100.0 * total_acc
    ))   
    return model


# model, FT_losses = train_model(model_ft, criterion, optimizer_ft, exp_lr_scheduler, num_epochs=200)
# plt.figure(figsize=(10,5))
# plt.title("FRT Loss During Training")
# plt.plot(FT_losses, label="FT loss")
# plt.xlabel("iterations")
# plt.ylabel("Loss")
# plt.legend()
# plt.show()

# torch.save(model, "/model.pt")