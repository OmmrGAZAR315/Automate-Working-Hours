import os.path

import PyPDF2
import re


def extract_text_from_pdf(pdf_path):
    # Load the PDF file
    pdf_file = open(pdf_path, 'rb')

    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Extract text from each page
    extracted_text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        extracted_text += page.extract_text() + "\n"

    # Close the PDF file
    pdf_file.close()

    # Correct the regex to capture the full match
    full_durations = re.findall(r'\b\d{1,2}:\d{2}H\b|\b\d{1,2}H\b', extracted_text)

    # Print the extracted durations
    if full_durations:
        print("Extracted Durations:")
        for index, duration in enumerate(full_durations):
            print(f"Index: {index + 1}, Duration: {duration}")
    else:
        print("No durations found.")

    save_path = os.path.join(os.path.dirname(pdf_path), os.path.basename(pdf_path) + '.txt')
    # Save the extracted text to a text file
    with open(save_path, 'w') as file:
        file.write("\n".join(['Working Hours'] + full_durations))
    print(f"Extracted text saved to: {save_path}")
    return save_path
