import os
import sys
from PyPDF2 import PdfFileReader, PdfFileMerger

def getPDFFiles():
    # return an array of constructed file objects
    # based on pdfs in current repository
    current_dir = sys.argv[1]
    pdf_file_names = []
    pdf_file_names += [each for each in os.listdir(current_dir) 
        if (each.endswith('.pdf') or each.endswith('.PDF'))
    ]

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

def getConcatFiles(index_group:int=[], file_names:str=[]):
    # returns all the requested files to concat in order
    merged_file = PdfFileMerger()
    for i in index_group:
        fd = open(file_names[i], 'rb') # Add error control
        merged_file.append(PdfFileReader(fd))

    return merged_file


def handleConcatFile(outputName:str, mergedFile:PdfFileMerger):
    mergedFile.write(outputName)

# Main script
print(sys.argv[1])
files = getPDFFiles()
printPDFList(files)
index_seq = input("Sequence of files to merge \n").split()
# Add error control (NaN, bad number...)
index_arr = [int(i)-1 for i in index_seq]
merged_doc = getConcatFiles(index_arr, files)
output_name = input("Output name: \n")
merged_doc.write(output_name+".pdf")
merged_doc.close()
