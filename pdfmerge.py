import sys
import os
from PyPDF2 import PdfFileReader, PdfFileMerger
from PDFFile import File;

def getPDFFiles():
    # return an array of constructed file objects
    # based on pdfs in current repository
    current_dir = os.getcwd()
    pdf_file_names = []
    pdf_file_names += [each for each in os.listdir(current_dir) 
        if (each.endswith('.pdf') or each.endswith('.PDF'))
    ]
    
    pdf_files = []
    for name in pdf_file_names:
        fd = open(name, 'rb')
        pdfReader = PdfFileReader(fd)
        pdf_files += File(name, pdfReader)

    return pdf_files


def printPDFList(files:File = []):
    # Prints list 
    # Generates a formatted list in the console
    pass

def getFilesToConcat(indexArr:int = []):
    # returns all the requested files to concat in order
    pass

def concatPDFs(files:File = []):
    merger = PdfFileMerger()
    pass

def handleConcatFile(outputName:str, mergedFile:PdfFileMerger):
    mergedFile.write(outputName)

getPDFFiles()