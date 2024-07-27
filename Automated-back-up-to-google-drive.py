#Automated Backup to Google Drive by Virginia Herrero

from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import os, shutil

#Paths
path_to_zip = r"C:/Users/Backup_Test_Folder"
path_to_archive_locally = r"C:/Users/Backups_Archive"

#Zip the folder to back up
def create_zip_folder(path_to_zip, folder_name):
    """"
    Function to create a zip folder. 
    Takes the path to the folder to back up (string) and the folder name (string). 
    Returns boolean: True if the zip is created, False if it is not.
    """
    try:
        shutil.make_archive(os.path.join(path_to_archive_locally, folder_name), "zip", path_to_zip)
        return True
    except FileNotFoundError as e:
        return False

#Google Drive API authentication
def google_auth():
    """
    Function to authenticate connection to google drive using the API.
    To avoid authentication every time the script is run, the credentials are saved in 'my_credentials.txt' and called from there
    to automatically authenticate the access to google drive.
    Returns: gauth and drive
    """
    gauth = GoogleAuth()
    #Try to load the saved credentials from the first OAuth approval
    gauth.LoadCredentialsFile("my_credentials.txt")
    #If the app was not authenticated, it requests authentication from google
    if gauth.credentials is None:
        #Use local default browser for authentication
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        #Refresh credentials if token is expired
        gauth.Refresh()
    else:
        #Initialize saved credentials
        gauth.Authorize()
    #Save current credentials to a text file
    gauth.SaveCredentialsFile("my_credentials.txt")
    drive = GoogleDrive(gauth)
    return gauth, drive