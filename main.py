import sys
import webbrowser
import os
import pyimgur

from config import CLIENT_ID

absolute_image_path = os.path.join(os.getcwd(), sys.argv[1])
im = pyimgur.Imgur(CLIENT_ID)
uploaded_image = im.upload_image(absolute_image_path)
webbrowser.open_new_tab("https://images.google.com/searchbyimage?image_url=" + uploaded_image.link)
