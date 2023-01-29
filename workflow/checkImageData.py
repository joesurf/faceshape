from os import listdir
from PIL import Image
from os import walk


def checkImageIntegrity(path, filename):
    try:
        print(path)
        img = Image.open(path + filename) # open the image file
        img.verify() # verify that it is, in fact an image
        print("Verified:", filename)
    except (IOError, SyntaxError) as e:
        print('Bad file:', filename) # print out the names of corrupt files



# shapes = ["Square", "Heart", "Oblong", "Oval", "Round"]

# dir = "../FaceShapeDataset/training_set/"

# for shape in shapes:
    
#     for filename in listdir(dir + shape + '/'):
#         # if filename.endswith('.jpg'):
#         path = dir + shape + '/'
#         checkImageIntegrity(path, filename)

