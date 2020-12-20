import PyPDF2
import os

current_path = os.getcwd()

if __name__ == '__main__':
    with open(current_path + os.sep + 'dummy.pdf', 'rb') as file:  # Its important to read the PDF as binary
        reader = PyPDF2.PdfFileReader(file)
        print(reader.numPages)
        print(reader.getPage(0))

        page = reader.getPage(0)
        rotated_page = page.rotateCounterClockwise(90)
        with open(current_path + os.sep + 'tilt.pdf', 'wb') as new_file:
            writer = PyPDF2.PdfFileWriter()
            writer.addPage(rotated_page)
            writer.write(new_file)
