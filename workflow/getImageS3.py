import io
import os
import boto3
from PIL import Image
from dotenv import load_dotenv


load_dotenv() 


# boto3.setup_default_session(profile_name='faceshape')
s3 = boto3.resource('s3')

def image_from_s3(bucket, key):

    bucket = s3.Bucket(bucket)
    image = bucket.Object(key)
    img_data = image.get().get('Body').read()

    return Image.open(io.BytesIO(img_data))

# image = image_from_s3("face-shape", "cat.jpg")
# image.save("cat.jpg")


# https://peekingduck.s3.amazonaws.com/heart.jpg