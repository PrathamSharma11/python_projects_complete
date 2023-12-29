import PyPDF2
a = PyPDF2.PdfFileReader('dummy.pdf')
print(a.documentInfo)