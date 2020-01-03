import sys
import os
import webbrowser
import pyimgur

from config import CLIENT_ID

GOOGLE_SEARCH_URL = "https://images.google.com/searchbyimage?image_url="

for p in sys.argv[1:]:
    absolute_image_path = os.path.join(os.getcwd(), p)
    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(absolute_image_path)
    webbrowser.open_new_tab(GOOGLE_SEARCH_URL + uploaded_image.link)
