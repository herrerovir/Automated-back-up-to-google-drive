#Automated Backup to Google Drive by Virginia Herrero

from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

#Set up authentification with Google Drive API
gauth = GoogleAuth()
#Try to load the saved credentials from the first 0Auth approval
gauth.LoadCredentialsFile("my_credentials.txt")
#If the app was not authentificated, ask Google for authentification
if gauth.credentials is None:
    #Use local default browser for authentification
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    #Refresh credentials if token is expired
    gauth.Refresh()
else:
    #Initialize saved credentials
    gauth.Authorize()
#Save current credentials to a text file
gauth.SaveCredentialsFile("my_credentials.txt")
#Authorize drive
drive = GoogleDrive(gauth)
