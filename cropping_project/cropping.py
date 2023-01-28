from PIL import Image
import pandas as pd

#img = Image.open(r"C:\Users\MINLY-TWO\Documents\GitHub\faceshape\cropping_project\images\round_(149)_230128_171217.jpg") 
test_df = pd.read_csv(r"C:\Users\MINLY-TWO\Documents\GitHub\faceshape\cropping_project\output_280123-19-02-57.csv")
#print(test_df['filename'].size)
for i in range(0, test_df['filename'].size): 
    filename = test_df['filename'][i]
    temp_img = Image.open("{filename}".format(filename='./images/'+filename))
    left = test_df['left'][i]
    top = test_df['top'][i]
    right = test_df['right'][i]
    bottom = test_df['bottom'][i]

    img_res = temp_img.crop((left, top, right, bottom)) 
    img_res.save('./output/cropped{num}.jpg'.format(num=i+1))

