import hashlib
import tkinter as tk
from tkinter import messagebox,ttk
from tkinter import filedialog as fd
import sys
import zlib
import os

if __name__ == '__main__':

        try:
            kod = sys.argv[1]
            konum = sys.argv[2]
            if kod=="SHA-256":
                print(hashlib.sha256(open(konum, 'rb').read()).hexdigest())
            if kod=="SHA-512":
                print(hashlib.sha512(open(konum, 'rb').read()).hexdigest())
            if kod=="SHA-1":
                print(hashlib.sha1(open(konum, 'rb').read()).hexdigest())
            if kod=="MD5":
                print(hashlib.md5(open(konum, 'rb').read()).hexdigest())
            if kod=="CRC-32":
                buffersize = 65536
                crcvalue = 0
                with open(konum, 'rb') as afile:
                    buffr = afile.read(buffersize)
                    while len(buffr) > 0:
                        crcvalue = zlib.crc32(buffr, crcvalue)
                        buffr = afile.read(buffersize)
                print(format(crcvalue & 0xFFFFFFFF, '08x'))
            exit(1)
        except  IndexError as e:
            pass





kod=""
root=tk.Tk()

l = tk.Label(root, text = "HashCalcPro v1.0")
l.config(font =("Courier", 14))
l.pack()

root.title("HashCalcPro v1.0 -Sarmsak Portable Utilities by Arsarimsak-")
root.geometry('500x100')
#pyinstallericin: auto-py-to-exe ile calistir ikonu direk roota . ile ekle ve ikon secenekden de ekle
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

iconPath = resource_path('icon.ico')
root.iconbitmap(iconPath)
#pyinstaller bitis


#root.resizable(False, False)

hashliste=['SHA-1','SHA-256','SHA-512','MD5','CRC-32']
dropdownhash=tk.ttk.Combobox(root,values=hashliste)
dropdownhash.current(1)
dropdownhash.pack()


T = tk.Text(root, height=1, borderwidth=0)
T.tag_configure("center", justify='center')

T.insert(1.0, "Please select a type from selection box.")
T.config(font =("Courier", 12))
T.tag_add("center", "1.0", "end")
T.configure(state="disabled")

T.pack()

def select_file():
    filetypes = (('All files', '*.*'), ('All files', '*.*'))
    konum = fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)
    kod=dropdownhash.get()
    if kod!="":
        if kod == "SHA-256":
            T.configure(state=tk.NORMAL)
            b=hashlib.sha256(open(konum, 'rb').read()).hexdigest()
            T.delete('1.0', tk.END)
            T.insert(1.0, b)
            T.configure(state="disabled")
            root.geometry('700x100')


        if kod == "SHA-512":
            T.configure(state=tk.NORMAL)
            b=hashlib.sha512(open(konum, 'rb').read()).hexdigest()
            T.delete('1.0', tk.END)
            T.insert(1.0, b)
            T.configure(state="disabled")
            root.geometry('850x100')

        if kod == "SHA-1":
            T.configure(state=tk.NORMAL)
            b=hashlib.sha1(open(konum, 'rb').read()).hexdigest()
            T.delete('1.0', tk.END)
            T.insert(1.0, b)
            T.configure(state="disabled")
            root.geometry('500x100')

        if kod == "MD5":
            T.configure(state=tk.NORMAL)
            b=hashlib.md5(open(konum, 'rb').read()).hexdigest()
            T.delete('1.0', tk.END)
            T.insert(1.0, b)
            T.configure(state="disabled")
            root.geometry('500x100')

        if kod == "CRC-32":
            buffersize = 65536
            crcvalue = 0
            with open(konum, 'rb') as afile:
                buffr = afile.read(buffersize)
                while len(buffr) > 0:
                    crcvalue = zlib.crc32(buffr, crcvalue)
                    buffr = afile.read(buffersize)
            T.configure(state=tk.NORMAL)
            b=format(crcvalue & 0xFFFFFFFF, '08x')
            T.delete('1.0', tk.END)
            T.insert(1.0, b)
            T.configure(state="disabled")
            root.geometry('500x100')



open_button = ttk.Button(root,text='Open a File',command=select_file)
open_button.pack(expand=True)







root.mainloop()
