#Automated Backup to Google Drive by Virginia Herrero

from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import os, shutil
from datetime import datetime

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

#Upload folder to google drive
def upload_backup(drive, path_to_zip, folder_name):
    """
    Function to upload the backup folder to google drive.
    Takes: access to drive, path to the folder to back up (string), the name of the folder (string).
    Returns: None
    """
    #Create a google drive file instance
    f = drive.CreateFile({"parents":[{"id": "1VpQA5BL2GxKs4jbrRk8GtF60MHIkJneA"}]})
    f["title"] = folder_name
    #Set the path to the zip file
    f.SetContentFile(os.path.join(path_to_zip, folder_name)) 
    #Upload the zip file
    f.Upload() 
    #Set f to none because of a vulnerability found in PyDrive
    f = None

def main():
    """
    Function to control the back up process.
    * Set backup folder name with: Backup + date and time
    * If the zip folder is not created, state why and stop the program
    * Get access to google drive
    * Upload zip file to google drive
    """
    #Set machine date and time
    now = datetime.now()
    #Set backup folder name
    folder_name = "Backup " + now.strftime(r"%d/%m/%Y %H:%M:%S").replace("/", "-").replace(":", " ")
    #If zip creation fails, raise exception and stop the program
    if not create_zip_folder(path_to_zip, folder_name):
        raise Exception ("There was an error creating the zip file")
    #Google Drive authentication
    gauth, drive = google_auth()
    #Upload zip file to google drive
    upload_backup(drive, path_to_archive_locally, folder_name+".zip")


if __name__ == "__main__":
    main()