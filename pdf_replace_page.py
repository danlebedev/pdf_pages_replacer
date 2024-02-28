from PyPDF2 import PdfReader, PdfWriter

input_pdf = input("Изменяемый файл: ")
pdf_reader = PdfReader(input_pdf)
pdf_writer = PdfWriter()

data = {}
while True:
    try:
        page = (int(input("Номер страницы: ")))
        file = (input("Заменить на: "))
    except:
        break
    else:
        data[page] = file

if data:
    for page in pdf_reader.pages:
        if (pg_num := pdf_reader.get_page_number(page) + 1) in data.keys():
            pdf_writer.add_page(PdfReader(data[pg_num]).pages[0])
        else:
            pdf_writer.add_page(page)

    output_pdf = "modified_document.pdf"
    with open(output_pdf, "wb") as output:
        pdf_writer.write(output)
else:
    print("Изменения не были применены.")
input()