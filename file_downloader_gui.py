import tkinter as tk
from tkinter import filedialog, messagebox
from file_downloader_logic import FileDownloader

class FileDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Downloader")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Select Excel file:").pack()
        self.excel_file_path_entry = tk.Entry(self.root, width=50)
        self.excel_file_path_entry.pack()
        tk.Button(self.root, text="Browse", command=self.browse_excel_file).pack()

        tk.Label(self.root, text="Select Download Directory:").pack()
        self.download_dir_entry = tk.Entry(self.root, width=50)
        self.download_dir_entry.pack()
        tk.Button(self.root, text="Browse", command=self.browse_download_dir).pack()

        tk.Label(self.root, text="Select File Type:").pack()
        self.file_type_var = tk.StringVar()
        self.file_type_var.set("Both")
        tk.Radiobutton(self.root, text="PDF only", variable=self.file_type_var, value="PDF").pack(anchor="w")
        tk.Radiobutton(self.root, text="EPUB only", variable=self.file_type_var, value="EPUB").pack(anchor="w")
        tk.Radiobutton(self.root, text="Both PDF and EPUB", variable=self.file_type_var, value="Both").pack(anchor="w")

        tk.Button(self.root, text="Download Files", command=self.download_files).pack()

    def browse_excel_file(self):
        excel_file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
        if excel_file_path:
            self.excel_file_path_entry.delete(0, tk.END)
            self.excel_file_path_entry.insert(0, excel_file_path)

    def browse_download_dir(self):
        download_dir = filedialog.askdirectory(title="Select Download Directory")
        if download_dir:
            self.download_dir_entry.delete(0, tk.END)
            self.download_dir_entry.insert(0, download_dir)

    def download_files(self):
        excel_file_path = self.excel_file_path_entry.get()
        download_dir = self.download_dir_entry.get()
        file_type = self.file_type_var.get()

        if not excel_file_path:
            messagebox.showerror("Error", "Please select the Excel file.")
            return
        if not download_dir:
            messagebox.showerror("Error", "Please select the Download Directory.")
            return

        downloader = FileDownloader(excel_file_path, download_dir, file_type)
        downloader.download_files()

if __name__ == "__main__":
    root = tk.Tk()
    app = FileDownloaderApp(root)
    root.mainloop()
gggg