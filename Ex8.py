'''
Write a python program to manipulate pdf files using pyPDF module.
Program should merge 2 or more pdf files into 1 pdf.
'''


import os
from pypdf import PdfWriter

path = os.getcwd()
files = os.listdir(path)

merger = PdfWriter()

for pdf in files:
    if(pdf.endswith(".pdf")):
        merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()

