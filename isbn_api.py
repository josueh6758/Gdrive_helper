#this will try to fetch book info based on ISBN

import requests

def get_info(isbn):
    """outputs both title and first author in a list"""
    results = []
    try:
        jfile = requests.get('https://www.googleapis.com/books/v1/volumes?q=isbn:'+isbn)
        jfile = jfile.json()
    except:
        print("couldnt reach the host")
        exit()
    try:
        results.append(jfile['items'][0]['volumeInfo']['title'])
        results.append(jfile['items'][0]['volumeInfo']['authors'][0])
    except KeyError as keyerr:
        print("Error with retrieving book title")
    return results
