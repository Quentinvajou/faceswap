import tensorflow as tf
import os
from google_images_download import google_images_download


os.listdir('src')
response = google_images_download.googleimagesdownload()
arguments = {"keywords":"keira knightley filmographie","limit":100,"print_urls":True}
paths = response.download(arguments)

print('plop')
