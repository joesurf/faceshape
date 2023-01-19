import torch
import logging
import sys



logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))


def test(model, test_loader, criterion, device, epoch_no):
    '''
    Use model to predict test data for one epoch
    '''
    logger.info(f"Epoch: {epoch_no} - Testing Model on Complete Testing Dataset")
    model.eval()
    running_loss=0
    running_corrects=0
    
    with torch.no_grad(): # No gradient calculation while testing 
        for inputs, labels in test_loader:
            inputs=inputs.to(device)
            labels=labels.to(device)
            outputs=model(inputs)
            loss=criterion(outputs, labels)
            pred = outputs.argmax(dim=1, keepdim=True)
            running_loss += loss.item() * inputs.size(0) 
            running_corrects += pred.eq(labels.view_as(pred)).sum().item() #

        total_loss = running_loss / len(test_loader.dataset)
        total_acc = running_corrects/ len(test_loader.dataset)
        logger.info( "\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n".format(
            total_loss, running_corrects, len(test_loader.dataset), 100.0 * total_acc
        ))
        
