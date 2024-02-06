from PIL import Image

# Testing - can open preset images
img = Image.open("geek.jpg")
# Need to save as thumbnail to keep aspect ratio
# If size is larger though, have to use resize - thumbnail won't work
img.thumbnail((400,400))
img.save('new_img.jpg')
#img.show()