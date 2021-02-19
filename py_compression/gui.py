import tkinter as tk
from compress_module import compress,decompress

def compression(i,o):
    compress(i,o)

def decompression(i,o):
    decompress(i,o)

window = tk.Tk()
window.title('Compression engine')
window.geometry('600x400')

input_entry = tk.Entry(window)
output_entry = tk.Entry(window)

input_label = tk.Label(window,text='File to be compressed')
output_label = tk.Label(window,text='Name of the compressed file')

compress_button = tk.Button(window,text='Compress now',command=lambda:compression(input_entry.get(),output_entry.get()))

input_label.grid(row=0,column=0)
input_entry.grid(row=0,column=1)

output_label.grid(row=1,column=0)
output_entry.grid(row=1,column=1)
compress_button.grid(row=2,column=1)


input_de_entry = tk.Entry(window)
output_de_entry = tk.Entry(window)

input_de_label = tk.Label(window,text='File to be decompressed')
output_de_label = tk.Label(window,text='Name of the decompressed file')

decompress_button = tk.Button(window,text='Decompress now',command=lambda:decompression(input_de_entry.get(),output_de_entry.get()))

input_de_label.grid(row=3,column=0)
input_de_entry.grid(row=3,column=1)

output_de_label.grid(row=4,column=0)
output_de_entry.grid(row=4,column=1)
decompress_button.grid(row=5,column=1)

window.mainloop()