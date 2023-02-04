import requests
import cv2


file = 'josh.jpg'

url = f'http://localhost:8000/infer/{file}'
myobj = {'somekey': 'somevalue'}

x = requests.post(url, json = myobj)

print(x.text)