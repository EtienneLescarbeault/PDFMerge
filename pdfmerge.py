import sys
import os
from PyPDF2 import PdfFileReader as pfr, PdfFileWriter as pfw
from PDFFile import File;

def getPDFFiles():
    # return an array of constructed file objects
    # based on pdfs in current repository
    current_dir = os.getcwd()
    pdf_files = []
    pdf_files += [each for each in os.listdir(current_dir) 
        if (each.endswith('.pdf') or each.endswith('.PDF'))
    ]
    print(pdf_files)



def printPDFList(files:File = []):
    # Prints list 
    # Generates a formatted list in the console
    pass

def getFilesToConcat(indexArr:int = []):
    # returns all the requested files to concat in order
    pass

def concatPDFs(files:File = []):
    pass

def handleConcatFile(finalFile: File):
    pass

getPDFFiles()