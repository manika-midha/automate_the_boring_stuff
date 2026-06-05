import PyPDF2 as pf

pdf_file_obj = open('meetingminutes.pdf', 'rb')
pdf_reader = pf.PdfReader(pdf_file_obj)
print(len(pdf_reader.pages))

page1 = pdf_reader.pages[0]
print(page1.extract_text())