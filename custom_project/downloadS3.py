import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import boto3
import io
from PIL import Image  
import PIL  

s3 = boto3.resource('s3', region_name='')
bucket = s3.Bucket('')
object = bucket.Object('')

file_stream = io.StringIO()
object.download_fileobj(file_stream)
# img = mpimg.imread(file_stream)
img = Image.open(file_stream)  
img.save("test.jpg") 

# fig.savefig('Sub Directory/graph.png')




