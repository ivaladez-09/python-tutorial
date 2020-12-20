import PyPDF2
import os

current_path = os.getcwd() + os.sep

template = PyPDF2.PdfFileReader(open(current_path + 'super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open(current_path + 'wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
  page = template.getPage(i)
  page.mergePage(watermark.getPage(0))
  output.addPage(page)

  with open(current_path + 'watermarked_output.pdf', 'wb') as file:
    output.write(file)
