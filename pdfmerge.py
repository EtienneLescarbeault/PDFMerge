import os
import sys
from PyPDF2 import PdfFileReader, PdfFileMerger


def getPDFFiles():
    # return an array of constructed file objects
    # based on pdfs in current repository
    current_dir = sys.argv[1]
    pdf_file_names = []
    pdf_file_names += [each for each in os.listdir(current_dir)
                       if (each.endswith('.pdf') or each.endswith('.PDF'))]

    return pdf_file_names


def printPDFList(file_names: str = []):
    # Prints list
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
            fd = open(file_names[i], 'rb')  # Add error control
            merged_file.append(PdfFileReader(fd))
        except Exception:
            print("Error: Could not open " + file_names[i])
            print("It will be ignored in the merging process. \n")
    return merged_file


def getFileIndicesInput(fileArrayLen: int):
    index_arr = []
    isValid = False
    while not isValid:
        index_seq = input("Sequence of files to merge \n").split()
        try:
            for i in index_seq:
                if i > fileArrayLen:
                    raise Exception()

                print(i)
                index_arr.append(int(i)-1)
            isValid = True
        except Exception:
            print("""Invalid input - Make sure to enter a valid
            number sequence separated by spaces\n""")
            isValid = False
    return index_arr


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
    sys.exit()


printPDFList(files)

index_arr = getFileIndicesInput(files_length)
merged_doc = getConcatFiles(index_arr, files)

handleConcatFile(merged_doc)
