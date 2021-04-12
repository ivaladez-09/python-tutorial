from PIL import Image, ImageFilter
import os

if __name__ == '__main__':

    current_file_path = os.getcwd()
    img_path = current_file_path + os.sep + 'astro.jpg'
    img = Image.open(img_path)
    print(img.size)
    img.thumbnail((400, 200))  # Modify in place the image to keep the aspect ratio
    print(img.size)
    img.save('thumbnail.png', 'png')
