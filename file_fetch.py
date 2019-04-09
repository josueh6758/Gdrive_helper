#this module will retrieve python files in the current directory
import os
import re
path2 = os.getcwd()
#print(path2)




def retrieve_files(name_list,extension):
    """takes in list of file names and returns dictionary containing matches with paths"""
    paths = {}
    regex_s = "(.*)."+extension
    r = re.compile(regex_s, re.IGNORECASE)
    filtered = list(filter(r.match, name_list))
    if len(filtered) == 0:
        print("no objects found of type: ",extension)
        return paths

    for name in filtered:
        temp = ""
        for char in "".join(reversed(name)):
            if char== "\\": break
            temp += char
        temp = "".join(reversed(temp))
        paths[temp] = name
    return paths

def list_all(path = None):
    """
    fetches all local files and returns a list of all paths.
    Used for additional methods in the module
    """
    files = []
    #can take in another directory if needed
    if path:
        for object in os.scandir(path):
            if object.is_file():
                files.append(object.path)
        return files
    #if no input is placed then the default will be current directory
    for object in os.scandir(path2):
        if object.is_file():
            files.append(object.path)
    return files

#cleaned = retrieve_files(files,"zip")
#print(cleaned)
