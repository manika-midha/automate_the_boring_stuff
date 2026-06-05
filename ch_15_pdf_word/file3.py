import PyPDF2 as pf

pdf_file1 = open('meetingminutes.pdf', 'rb')
pdf_file2 = open('meetingminutes2.pdf', 'rb')

pdf_reader1 = pf.PdfReader(pdf_file1)
pdf_reader2 = pf.PdfReader(pdf_file2)

pdf_writer = pf.PdfWriter()

# get page 1 from file 1
page1_obj = pdf_reader1.pages[0]

# get page 2 from file 2
page2_obj = pdf_reader2.pages[1]

# add both pages to new pdf
pdf_writer.add_page(page1_obj)
pdf_writer.add_page(page2_obj)

pdf_op_file = open('combined_pdf_file.pdf', 'wb')
pdf_writer.write(pdf_op_file)

pdf_op_file.close()
pdf_file1.close()
pdf_file2.close()

