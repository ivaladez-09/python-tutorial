import PyPDF2
import os
import sys


current_path = os.getcwd()
inputs = sys.argv[1:]  # Skip first one (file name)


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(current_path + os.sep + 'super.pdf')


pdf_combiner(inputs)
