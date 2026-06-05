import docx


def get_full_text(file_name):
    doc = docx.Document('demo.docx')
    return_list = []
    for obj in doc.paragraphs:
        return_list.append(obj.text)

    return '\n'.join(return_list)
    #return '\n\n'.join(return_list) # add double space between paragraphs

    #return return_list


print(get_full_text('demo.docx'))