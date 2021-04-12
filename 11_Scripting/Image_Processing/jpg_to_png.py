import sys
import os
from PIL import Image

current_path = os.getcwd()
path = current_path + os.sep + sys.argv[1] + os.sep
directory = current_path + os.sep + sys.argv[2] + os.sep

if not os.path.exists(directory):
    os.makedirs(directory)

for filename in os.listdir(path):
    clean_name, extension = os.path.splitext(filename)
    if extension == '.jpg' or extension == '.JPG':
        img = Image.open(f'{path}{filename}')
        # added the / in case user doesn't enter it. You may want to check for this and add or remover it.
        img.save(f'{directory}/{clean_name}.png', 'png')

print('all done!')
