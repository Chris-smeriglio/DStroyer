import os
import pathlib

input1 = input("Directory to search:")
print(input1)
directory = pathlib.Path(input1)

filesToDelete = list(directory.glob("*.DS_Store"))
print(filesToDelete)
for file in filesToDelete:
    print("deleting file: %s" % file)
    os.remove(file)
print("done")
