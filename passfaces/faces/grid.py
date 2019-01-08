# import Image
#
# #opens an image:
# im = Image.open("old_man.jpg")
#
# #creates a new empty image, RGB mode, and size 400 by 400.
# new_im = Image.new('RGB', (400,400))
#
# #Here I resize my opened image, so it is no bigger than 100,100
# im.thumbnail((100,100))
# #Iterate through a 4 by 4 grid with 100 spacing, to place my image
# for i in xrange(0,400,100):
#     for j in xrange(0,400,100):
#         #I change brightness of the images, just to emphasise they are unique copies.
#         im=Image.eval(im,lambda x: x+(i+j)/30)
#         #paste the image at location i,j:
#         new_im.paste(im, (i,j))
#
# new_im.show()


import Tkinter as tk
from PIL import Image, ImageTk
# position coordinates of root 'upper left corner'
x = 0
y = 0

root = tk.Tk()
root.title('passfaces')
# make the root window the size of the image
root.geometry("%dx%d+%d+%d" % (w, h, x, y))

# pick an image file you have .bmp  .jpg  .gif.  .png
# load the file and covert it to a Tkinter image object
oldman = "old_man.jpg"
oldman = ImageTk.PhotoImage(Image.open(imageFile))



# get the image size
w = oldman.width()
h = oldman.height()


# root has no image argument, so use a label as a panel
panel1 = tk.Label(root, image=oldman)
panel1.pack(side='top', fill='both', expand='yes')

# put a button on the image panel to test it
button2 = tk.Button(panel1, text='button2')
button2.pack(side='top')

# save the panel's image from 'garbage collection'
panel1.image = oldman

# start the event loop
root.mainloop()