all_jpgs = [] # define the list of all_jpgs

suffix = (".jpg",".jpeg")  # define a tuple of image types
def all_pictures(): # define a function to recursively search through Pictures folder on C drive
    import os  # imports os components
    for root, dirs, files in os.walk('C:\\Users\\Sam\\Pictures'):  # recursively searches for jpg images
             for item in files:
                 if item.lower().endswith(suffix)== True:  # searches for suffix through jpgs
                    os.path.join(root, item)  #joins
                    all_jpgs.append(item)  # appends image location to list
             else:
                continue

all_pictures()

print(all_jpgs)  # prints list of image locations
print(all_jpgs.count(suffix))  # prints number of images found
