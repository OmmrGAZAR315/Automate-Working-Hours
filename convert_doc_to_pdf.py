import io
import os

from google.oauth2 import credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload

import setAccessToken


def export_pdf(real_file_id, output_dir):
    """Download a Document file in PDF format.

    Args:
        real_file_id (str): File ID of any Google Workspace document.
        output_dir (str): Directory where the PDF will be saved.

    Returns:
        str: Path to the downloaded PDF file.
    """
    creds = credentials.Credentials(setAccessToken.access_token)

    try:
        # create drive api client
        service = build("drive", "v3", credentials=creds)

        # pylint: disable=maybe-no-member
        request = service.files().export_media(
            fileId=real_file_id, mimeType="application/pdf"
        )
        file = io.BytesIO()
        downloader = MediaIoBaseDownload(file, request)
        done = False
        while not done:
            status, done = downloader.next_chunk()
            print(f"Download {int(status.progress() * 100)}%.")

        # Save the file to the output directory
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        file_path = os.path.join(output_dir, f"{real_file_id}.pdf")
        with open(file_path, "wb") as f:
            f.write(file.getvalue())

    except HttpError as error:
        print(f"An error occurred: {error}")
        return None

    return file_path
