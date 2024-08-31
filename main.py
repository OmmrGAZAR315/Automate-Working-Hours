import working_hours
import write_to_sheet

pdf_path = "C:/Users/omara/Downloads/Phone Link/Working Hours.pdf"
save_path = "C:/Users/omara/Downloads/Phone Link/Working Hours.txt"
spreadsheet_id = '1e39iKmA1lWhW7GpA59O7Q0z2tFkEDNhpR5PL7T9jf84'
sheet_name = 'Aug'  # Replace with the actual sheet name you want to append to

working_hours.extract_text_from_pdf(pdf_path, save_path)
values = write_to_sheet.read_from_file(save_path)
write_to_sheet.write_to_sheet(spreadsheet_id, values, sheet_name)
