import sys
from PyPDF2 import PdfFileReader, PdfFileWriter
from PDFFile import File;

def getPDFFiles():
    # return an array of constructed file objects
    # based on pdfs in current repository
    pass

def printPDFList(files:File = []):
    # Print list 
    # Generate a formatted list in the console
    pass

def getFilesToConcat(indexArr:int = []):
    # returns all the requested files to concat in order
    pass

def concatPDFs(files:File = []):
    # given in which order
    pass

def handleConcatFile(finalFile: File):
    pass
