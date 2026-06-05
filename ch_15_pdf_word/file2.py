import PyPDF2 as pf

pdf_file_obj = open('encrypted.pdf', 'rb')
pdf_reader = pf.PdfReader(pdf_file_obj)
pdf_reader.decrypt('rosebud')

print(pdf_reader.is_encrypted)
page1 = pdf_reader.pages[0]
print(page1.extract_text())

