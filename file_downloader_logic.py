import os
import pandas as pd
import requests

class FileDownloader:
    def __init__(self, excel_file_path, download_dir, file_type):
        self.excel_file_path = excel_file_path
        self.download_dir = download_dir
        self.file_type = file_type

    def download_files(self):
        df = pd.read_excel(self.excel_file_path)
        isbns = df['e_isbn'].tolist()

        pdf_base_url = "https://link.springer.com/content/pdf/10.1007/{}.pdf?pdf=button"
        epub_base_url = "https://link.springer.com/download/epub/10.1007/{}.epub"

        for isbn in isbns:
            if self.file_type in ["PDF", "Both"]:
                pdf_url = pdf_base_url.format(isbn)
                pdf_response = requests.get(pdf_url)
                
                if pdf_response.status_code == 200:
                    pdf_filename = os.path.join(self.download_dir, f"PDF_{isbn}.pdf")
                    with open(pdf_filename, "wb") as pdf_file:
                        pdf_file.write(pdf_response.content)
                    print(f"PDF file {pdf_filename} downloaded successfully.")
                else:
                    print(f"Error occurred while downloading the PDF file for ISBN {isbn}.")

            if self.file_type in ["EPUB", "Both"]:
                epub_url = epub_base_url.format(isbn)
                epub_response = requests.get(epub_url)
                
                if epub_response.status_code == 200:
                    epub_filename = os.path.join(self.download_dir, f"EPUB_{isbn}.epub")
                    with open(epub_filename, "wb") as epub_file:
                        epub_file.write(epub_response.content)
                    print(f"EPUB file {epub_filename} downloaded successfully.")
                else:
                    print(f"Error occurred while downloading the EPUB file for ISBN {isbn}.")
