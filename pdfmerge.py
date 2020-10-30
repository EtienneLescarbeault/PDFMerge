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
    
    """pdf_files:File = []
    for name in pdf_file_names:
        fd = open(name, 'rb')
        pdfReader = PdfFileReader(fd)
        pdf_files.append(File(name, pdfReader))

    return pdf_files"""
    return pdf_file_names


def printPDFList(file_names:str = []):
    # Prints list 
    # Generates a formatted list in the console
    out = ""
    for i in range(len(file_names)):
        out += '('+ str(i+1) + ') ' + file_names[i] + "   " # 3 spaces
        if((i+1)%3 == 0):
            out += "\n"
    print(out)

def getFilesToConcat(index_group:int=[], file_names:str=[]):
    # returns all the requested files to concat in order
    pdf_readers = []
    for i in index_group:
        fd = open(file_names[i]) # Add error control
        pdf_readers.append(PdfFileReader(fd))

    return pdf_readers

def concatPDFs(files = []):
    merger = PdfFileMerger()
    pass

def handleConcatFile(outputName:str, mergedFile:PdfFileMerger):
    mergedFile.write(outputName)

# Main script
files = getPDFFiles()
printPDFList(files)
index_seq = input("Sequence of files to merge \n").split()

# Add error control (NaN, bad number...)
index_arr = [int(i-1) for i in index_seq]

file_data = getFilesToConcat(index_arr, files)

