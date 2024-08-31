import working_hours
import write_to_sheet

def main():
    pdf_path = input("Enter the path of the PDF file: ")
    save_path = input("Enter the path where you want to save the extracted text: ")
    spreadsheet_id = '1e39iKmA1lWhW7GpA59O7Q0z2tFkEDNhpR5PL7T9jf84'
    sheet_name = input('Enter the sheet name ')  # Replace with the actual sheet name you want to append to

    pdf_path = pdf_path.replace("\\", "/")
    save_path = save_path.replace("\\", "/")

    working_hours.extract_text_from_pdf(pdf_path, save_path)
    values = write_to_sheet.read_from_file(save_path)
    write_to_sheet.write_to_sheet(spreadsheet_id, values, sheet_name)

if __name__ == "__main__":
    main()