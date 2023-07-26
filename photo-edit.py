# Import statement
from PIL import Image, ImageEnhance, ImageFilter
import os

img1=Image.open('1.jpg')

# In which extention file you want to create
    # img1.save('1.png')

#Show image
    # img1.show()

# Edited Picture Size Decleration
    # MAX_SIZE = (250,250)
    # img1.thumbnail(MAX_SIZE)
    # Save edited Picture
    # img1.save('edit.jpg')

# Change extension of all JPG files present in the directory
# for item in os.listdir():
#     if item.endswith('.jpg'):
#         img1 = Image.open(item)
#         filename,extension = os.path.splitext(item)
#         img1.save(f'{filename}.png')


# 0 : blurry 
# 1: original image 
# 2 : image with increased sharpness and >2 : More sharp Image

# Save enhanced Image
# enhancer = ImageEnhance.Sharpness(img1)
# enhancer.enhance(5).save('edit.jpg')


# ------- color enhance ---------
# 0: Pure black & white image
# 1: Original image
# 2: Color will increase

# enhancer = ImageEnhance.Color(img1)
# enhancer.enhance(2).save('edit.jpg')

# ------- Brightness change ---------
# 0: Full Black Picture
# 1: Original Picture

# enhancer = ImageEnhance.Brightness(img1)
# enhancer.enhance(1.5).save('edit.jpg')

# ------- Contrast change ---------
# enhancer = ImageEnhance.Contrast(img1)
# enhancer.enhance(1.5).save('edit.jpg')

# image blur 
# img1.filter(ImageFilter.GaussianBlur(radius=4)).save('dog1edited.jpg')