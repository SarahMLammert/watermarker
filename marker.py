import PyPDF2
import sys

file = sys.argv[1]
watermark_file = sys.argv[2]

template = PyPDF2.PdfFileReader(open(file, 'rb'))
watermark = PyPDF2.PdfFileReader(open(watermark_file, 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
	page = template.getPage(i)
	page.mergePage(watermark.getPage(0))
	output.addPage(page)

	with open('watermarked_file.pdf', 'wb') as file:
		output.write(file)