from google.oauth2 import credentials
import setAccessToken
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# ... (rest of your imports and the create function remain the same)

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
    Writes the given values to the specified column of the given sheet in the spreadsheet.
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

        result = service.spreadsheets().values().append(
            spreadsheetId=spreadsheet_id,
            range=range_,
            valueInputOption='RAW',
            insertDataOption='INSERT_ROWS',
            body=body
        ).execute()

        print(f"{result.get('updates').get('updatedCells')} cells appended.")
        return result

    except HttpError as error:
        print(f"An error occurred: {error}")
        return error

if __name__ == "__main__":
    spreadsheet_id = '1e39iKmA1lWhW7GpA59O7Q0z2tFkEDNhpR5PL7T9jf84'
    filename = 'C:/Users/omara/Downloads/Phone Link/Working Hours.txt'  # Replace with the actual path to your text file
    sheet_name = 'Aug'  # Replace with the actual sheet name you want to append to

    values = read_from_file(filename)
    write_to_sheet(spreadsheet_id, values, sheet_name)