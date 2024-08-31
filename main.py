import PyPDF2
import re

# Load the PDF file
pdf_path = "C:/Users/omara/Downloads/Phone Link/Working Hours.pdf"  # Replace with the actual path to your PDF file
pdf_file = open(pdf_path, 'rb')

# Create a PDF reader object
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Extract text from each page
extracted_text = ""
for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]
    extracted_text += page.extract_text()

# Close the PDF file
pdf_file.close()

# Regular expression to match durations like "8:30H", "9:00H", and "8H"
duration_pattern = r'\b\d{1,2}(:\d{2})?H\b'

# Extract all occurrences of the duration pattern
durations = re.findall(duration_pattern, extracted_text)

# Print the extracted durations
if durations:
    print("Extracted Durations:")
    for duration in durations:
        print(duration)
else:
    print("No durations found.")
