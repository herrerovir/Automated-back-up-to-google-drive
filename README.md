# Automated Backup to Google Drive with API
![GitHub top language](https://img.shields.io/github/languages/top/herrerovir/Automated-back-up-to-google-drive) ![GitHub License](https://img.shields.io/github/license/herrerovir/Automated-back-up-to-google-drive)

Backing up data is an important part of data management. Backups protect against any inconvenience that may occur, such as human error, malware, hardware failures and other threats. Often, backups are performed manually and are a complex and time-consuming task, so an automated backup is a great solution to keep all your data protected without much trouble.

This automated backup to Google Drive will help you keep all your data protected and safely stored in Google Drive and locally on your own computer. 

This script written in Python will create a zip folder of the folder you want to backup. The new zip folder will be stored locally in your computer and renamed to “Backup” plus the date and timestamp. Once the script has access to Google Drive, it will upload the zip folder to the designated folder in your Google Drive. The program will search Google Drive for other backup files with timestamps earlier than the exact time of the backup and delete them. 

The program is scheduled to perform the backup on a weekly basis.

The code and JSON file named "client_secrets.json" must be kept in the same directory to grant access to Google Drive. Do not share the json file with your credentials with anyone.

## Dependencies:
Python 3

A Google account with access to Google Drive

Libraries used: pydrive, os, shutil, datetime, schedule

## How to run the script:
* Clone or download the repository to your local machine
* Set up your Google Drive API
    - Log in to your Google Cloud Platform Console
    - Create a new project
    - Enable Google Drive API for that project
    - Add OAuth ID to the new project
* Obtain OAuth credentials
    - Click on the "Credentials" tab
    - Click on "Create credencials" and later "OAuth client ID"
    - Select "Desktop app" as the application type
    - Click "Create"
    - A screen pops up with your client ID and secret
    - Download the JSON file and store it in your local project folder with the name "client_secrets.json"
    - IMPORTANT: Do not share this json file with anyone
* Set the correct path to the folder you want to back up
    - Path_to_zip: path to the folder that you want to back up
    - Path_to_archive_locally: path where you want to back up said folder in your local machine
* In the function "upload_backup", replace the folder id with your own folder id from Google Drive
* Replace the same folder id from your Google Drive in the function "remove_old_backups"
* Set the name of the folder you want to back up in the function "main" under "folder_name"
* Set the day and hour you want to back up your files weekly 
* Run the Automated-back-up-to-google-drive.py file in a Python environment
* The first time you run the script, a browser window will open up to authorize the application to access Google Drive. Log in with your google account and authorize access. 
* The script will create a text file named "my_credentials.txt" where your credentials will be stored to automatically authenticate you and authorize access to Google Drive.
* Voilá! You have set up a weekly backup of your files to google drive without any effort!

## License:
This project is licensed under the MIT License. See the [LICENSE](LICENSE)  file for details
