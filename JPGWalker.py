import os  # imports os components
all_jpgs = [] # define the list of all_jpgs

suffix = (".jpg",".jpeg")  # define a tuple of image types
def all_pictures(directory): # define a function to recursively search through directory that is called
    for root, dirs, files in os.walk(directory):  # recursively searches for jpg images
             for item in files:
                 if item.lower().endswith(suffix)== True:  # searches for suffix through jpgs
                    all_jpgs.append(os.path.join(root, item))  # appends image location to list



all_pictures('C:\\Users\\Sam\\Pictures')  # call directory here
print(all_jpgs)  # prints list of image locations
print(len(all_jpgs)) # prints number of images found
