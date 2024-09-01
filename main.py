import os

import working_hours
import write_to_sheet
from convert_doc_to_pdf import export_pdf
from dotenv import load_dotenv

load_dotenv()

def main():
    docId = input("Enter the document ID: ")
    workPlacePath = input("Enter the path where you want to save the PDF and txt file: ")

    # save_path = input("Enter the path where you want to save the extracted text: ")
    sheet_name = input('Enter the sheet name ')  # Replace with the actual sheet name you want to append to

    if workPlacePath == "":
        workPlacePath = "C:/Users/omara/Downloads/Phone Link/"

    # workPlacePath = workPlacePath.replace("\\", "/").strip('"')
    # save_path = save_path.replace("\\", "/").strip('"')

    workPlacePath = export_pdf(docId, workPlacePath)
    save_path = working_hours.extract_text_from_pdf(workPlacePath)
    values = write_to_sheet.read_from_file(save_path)
    write_to_sheet.write_to_sheet(os.getenv('SPREADSHEET_ID'), values, sheet_name)


if __name__ == "__main__":
    main()