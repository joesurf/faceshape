import io
import os
import boto3
from PIL import Image

s3 = boto3.resource('s3')

def image_from_s3(bucket, key):

    bucket = s3.Bucket(bucket)
    image = bucket.Object(key)
    img_data = image.get().get('Body').read()

    return Image.open(io.BytesIO(img_data))

image = image_from_s3("peekingduck", "heart.jpg")
image.save("heart.jpg")


# https://peekingduck.s3.amazonaws.com/heart.jpg