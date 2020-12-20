from PIL import Image, ImageFilter
import os

if __name__ == '__main__':

    current_file_path = os.getcwd()
    img_path = current_file_path + os.sep + 'pokedex' + os.sep + 'pikachu.jpg'
    img = Image.open(img_path)

    filtered_img = img.filter(ImageFilter.BLUR)
    filtered_img.save('pokedex/pikachu_blur.png', 'png')

    filtered_img = img.convert('L')
    filtered_img.save('pokedex/pikachu_gray.png', 'png')

    crooked = filtered_img.rotate(180)
    crooked.show()  # Creates and shows the image. If it is not saved, open a temp file

    resize = filtered_img.resize((300, 300))  # It only accepts a tuple
    resize.show()

    box = (100, 100, 400, 400)
    region = filtered_img.crop(box)
    region.show()

