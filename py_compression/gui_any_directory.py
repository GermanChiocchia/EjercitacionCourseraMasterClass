import tkinter as tk
from compress_module import compress,decompress
from tkinter import filedialog

def open_file():
    filename = filedialog.askopenfilename(initialdir='/',title='Select a file')
    return filename

def compression(i,o):
    compress(i,o)

def decompression(i,o):
    decompress(i,o)

window = tk.Tk()
window.title('Compression engine')
window.geometry('600x400')

compress_button = tk.Button(window,text='Compress now',command=lambda:compression(open_file(),'py_compression\Compressed1.txt'))
compress_button.grid(row=2,column=1)

decompress_button = tk.Button(window,text='Decompress now',command=lambda:decompression(open_file(),'py_compression\Decompressed1.txt'))
decompress_button.grid(row=5,column=1)

window.mainloop()