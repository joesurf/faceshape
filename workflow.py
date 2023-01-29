# Make a post request with the image key in s3 bucket
import requests

image = "heart.jpg"

url = ''
myobj = {'objectKey': image}

response = requests.post(url, json = myobj)

result = response[0]




# Read and save image data