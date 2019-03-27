# Gdrive_helper
CLI based Google Drive tool that will make uploading local files easier(for me):

## to set up install using pip:
```
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib\
```
## Getting Credentials.json
You'll need to head over to 
```
https://console.developers.google.com/apis/dashboard
```
1.Enable Google Drive API 
2.Create Oauth credential
3.download and rename to credentials.json and place it in main folder

## To-do 
- implement resumable uploads(done)
- implement filters using regex for batch uploads(done)
- implement gui 
- implement folder creation
- create search function before upload to avoid redundant uploads
