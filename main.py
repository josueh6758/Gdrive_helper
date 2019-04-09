from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import auth
#im not sure why it gives me unresolved reference for mediafileupload but it still works
from apiclient.http import MediaFileUpload
import file_fetch


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive']
#creating neccesary variables
authInst = auth.auth(SCOPES)
creds = authInst.get_cred()
drive_service = build('drive', 'v3', credentials=creds)
MIMETYPES = {"zip":"application/zip","png":"image/png","jpg":"image/jpeg","pdf":"application/pdf"}

def upload_file(file_name,file_path,mimetype,folder_id=None):
    """uploads a single file to the main directory in your gdrive"""
    #if theres a folder you want to put it in do 1st else goes to main
    if folder_id:
        file_metadata = {'name': file_name,
                      'parents': [folder_id]}
    else:
        file_metadata = {'name': file_name}

    media =  MediaFileUpload(file_path,
                            mimetype=mimetype)
    try:
        file = drive_service.files().create(body=file_metadata,
                                            media_body=media,
                                            fields='name, id').execute()
        print('File ID: %s' % file.get('name'), "Id: ", file.get('id'))
    except:
        print("Uh-Oh Program did an OOPSIE and could not upload file")

def create_folder(name):
    file_metadata = {
        'name': name,
        'mimeType': 'application/vnd.google-apps.folder'
    }
    file = drive_service.files().create(body=file_metadata,
                                        fields='id').execute()
    print('Folder ID: %s' % file.get('id'))


def list_files(size):
    """takes in integer and displays N amount of files in your drive"""
    results = drive_service.files().list(
        pageSize=size, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))



def main():
    #gets all files in current directory
    files = file_fetch.list_all()
    extension = input("please input extension type, ie. pdf\n")

    results = file_fetch.retrieve_files(files,extension)
    print(files)
    print(results)

    while len(results) is not 0:
        tup = results.popitem()
        print("Uploading: ", tup[0])
        upload_file(tup[0],tup[1],MIMETYPES[extension],'1ugr4OONDtGTEHS3k2KPf8zRfpHlYiZNH')

if __name__ == '__main__':
    main()