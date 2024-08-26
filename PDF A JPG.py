import tkinter as tk
from tkinter import filedialog
from pdf2image import convert_from_path

def select_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        images = convert_from_path(file_path)
        for i in range(len(images)):
            images[i].save(f'{output_dir}/output{i}.jpg', 'JPEG')

def select_output_dir():
    global output_dir
    output_dir = filedialog.askdirectory()

root = tk.Tk()
output_dir = ''

select_pdf_button = tk.Button(root, text="Seleccionar PDF", command=select_pdf)
select_pdf_button.pack()

select_output_dir_button = tk.Button(root, text="Seleccionar carpeta de salida", command=select_output_dir)
select_output_dir_button.pack()

root.mainloop()
