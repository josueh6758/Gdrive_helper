#this will try to fetch book info based on ISBN
from bs4 import BeautifulSoup
import requests
from googlesearch import search
import re

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
        print("Error with retrieving book info")
        results.append('N/A')
    return results

def find_isbn(file_name):
    query = file_name
    #first part get links from google search using book names
    hits = []
    for link in search(query, tld='com', lang='en', num=10, start=0, stop=10, pause=2.0):
        hits.append(link)
    print(hits)
    #filter that using regex and get only amazon links
    regs = '(.*)amazon.com(.*)'
    r = re.compile(regs, re.IGNORECASE)
    results = list(filter(r.match,hits))
    #isbns are at the end of the link just get that
    lookups = {}
    for name in results:
        temp = ""
        for char in "".join(reversed(name)):
            if char== "/": break
            temp += char
        temp = "".join(reversed(temp))
        lookups[temp] = get_info(temp)
    print(lookups)

find_isbn('introduction to automata')
