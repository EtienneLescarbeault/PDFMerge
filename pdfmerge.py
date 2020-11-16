import os
import sys
import time
from PyPDF2 import PdfFileReader, PdfFileMerger


def getPDFFiles():
    current_dir = sys.argv[1]
    pdf_file_names = []
    pdf_file_names += [each for each in os.listdir(current_dir)
                       if (each.endswith('.pdf') or each.endswith('.PDF'))]

    return pdf_file_names


def printPDFList(file_names: str = []):
    # Generates a formatted list in the console
    out = ""
    for i in range(len(file_names)):
        out += '(' + str(i+1) + ') ' + file_names[i] + "   "  # 3 spaces
        if((i + 1) % 3 == 0):
            out += "\n"
    print(out)


def getConcatFiles(index_group: int = [], file_names: str = []):
    merged_file = PdfFileMerger()
    for i in index_group:
        try:
            fd = open(file_names[i], 'rb')
            merged_file.append(PdfFileReader(fd))
        except Exception:
            print("Error: Could not open " + file_names[i])
            print("It will be ignored in the merging process. \n")
    return merged_file


def handleConcatFile(mergedFile: PdfFileMerger):
    output_name = input("Output name: \n")
    mergedFile.write(output_name + ".pdf")
    mergedFile.close()


'''
Main script
'''
files = getPDFFiles()
files_length = len(files)
if len(files) <= 0:
    print("No PDF file found! Exiting...\n")
    time.sleep(3)
    sys.exit()


printPDFList(files)

index_arr = []
valid = False
while not valid:
    index_seq = input("Sequence of files to merge\n").split()
    valid = True
    if len(index_seq) == 0:
        valid = False

    for i in index_seq:
        try:
            file_num = int(i)
            if file_num > files_length or file_num < 1:
                raise Exception()
            index_arr.append(file_num-1)
        except Exception:
            print("Invalid input: " + str(i))
            print("""     - Make sure to enter a valid number sequence separated by spaces
     - The numbers must match the file indices
            """)
            printPDFList(files)
            valid = False
            index_seq = ""
            index_arr = []


merged_doc = getConcatFiles(index_arr, files)
handleConcatFile(merged_doc)
