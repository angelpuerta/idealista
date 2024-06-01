import os
from pathlib import Path
import logging

from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2 import service_account

def store_drive(file_path, drive_path):
    # Load credentials from the service account key file
    credentials_path = Path(__file__).parent.parent.joinpath("config").joinpath('credentials.json')
    os_path = Path(__file__).parent.parent.joinpath(file_path)
    credentials = service_account.Credentials.from_service_account_file(str(credentials_path),
                                                                        scopes=['https://www.googleapis.com/auth/drive'])

    service = build('drive', 'v3', credentials=credentials)
    file_name = os.path.basename(file_path)

    # Create a file metadata
    file_metadata = {
        'name': file_name,
        'mimeType': 'application/vnd.google-apps.spreadsheet',
        'parents': [drive_path]
    }

    # Create a media object for the file upload
    media = MediaFileUpload(os_path, mimetype='text/tab-separated-values', resumable=True)

    # Upload the file
    file = service.files().update(body=file_metadata, media_body=media, fields='id').execute()

    logging.info(f"File uploaded successfully. File ID: {file['id']}")