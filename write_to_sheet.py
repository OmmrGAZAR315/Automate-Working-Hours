from google.oauth2 import credentials
import setAccessToken
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def read_from_file(filename):
    """
    Reads data from the specified text file.
    Assumes each line in the file represents a value to be written to a cell.
    """
    with open(filename, 'r') as file:
        values = [[line.strip()] for line in file]
    return values

def write_to_sheet(spreadsheet_id, values, sheet_name='Sheet1', column='B'):
    """
    Updates the specified column of the given sheet in the spreadsheet with the given values.
    Each sublist in 'values' represents a row in the spreadsheet.
    """

    access_token = setAccessToken.access_token
    creds = credentials.Credentials(access_token)

    try:
        service = build('sheets', 'v4', credentials=creds)

        body = {
            'values': values
        }

        # Adjust the range to specify the desired sheet and column
        range_ = f'{sheet_name}!{column}:{column}'

        result = service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range=range_,
            valueInputOption='RAW',
            body=body
        ).execute()

        print(f"{result.get('updatedCells')} cells updated.")

        return result

    except HttpError as error:
        print(f"An error occurred: {error}")
        return error


