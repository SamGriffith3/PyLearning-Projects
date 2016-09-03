from pprint import pprint
import projects.jpg_walker
from projects.jpg_walker import all_pictures, all_jpgs


first_dir = input("First Directory Path: ")
second_dir = input("Second Directory Path: ")
all_pictures(first_dir)
pprint(all_jpgs)
print(len(all_jpgs))
all_pictures(second_dir)
pprint(all_jpgs)
print(len(all_jpgs))
