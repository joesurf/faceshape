from os import listdir
from PIL import Image
    
for filename in listdir('./custom_data/validation/square'):
    # if filename.endswith('.jpg'):
    try:
        img = Image.open('./custom_data/validation/square/'+filename) # open the image file
        img.verify() # verify that it is, in fact an image
        print("Verified:", filename)
    except (IOError, SyntaxError) as e:
        print('Bad file:', filename) # print out the names of corrupt files
