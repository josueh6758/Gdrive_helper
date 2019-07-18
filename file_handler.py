#this module will retrieve python files in the current directory
import os
import re
import isbn_api

DIRECTORY=''


def pdf_clean(name_list):
    """take in dictionary from ret_files() to potentially rename"""
    new_names = []

    for object in name_list:
        info_list = isbn_api.find_isbn(object)
        if len(info_list) == 0:
            print("invalid entries, skipping book")
            break
        try:
            print(os.getcwd())
            dst = info_list[0]+"-"+info_list[1]+".pdf"
            print("dst: "+dst)
            print("original: "+ object)
            print("file_location: "+name_list[object])
            print("Directory: "+DIRECTORY)
            try:
                os.rename(name_list[object], DIRECTORY+"\\"+dst)
            except:
                print("renaming didnt work")

        except:
            print("couldnt retreive book info, make sure to select right info")




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
    global DIRECTORY
    #can take in another directory if needed
    if path:
        DIRECTORY=path
        for object in os.scandir(path):
            if object.is_file():
                files.append(object.path)
        return files
    #if no input is placed then the default will be current directory
    DIRECTORY=os.getcwd()
    for object in os.scandir(os.getcwd()):
        if object.is_file():
            files.append(object.path)
    return files



