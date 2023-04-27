from PyPDF2 import PdfReader, PdfWriter

split_pages = [1, 2]

with open("./PDF/merged.pdf", "rb") as f:
    pdf_reader = PdfReader(f)
    pdf_writer = PdfWriter()
    rest_writer = PdfWriter()

    for page in range(len(pdf_reader.pages)):
        if page in split_pages:
            pdf_writer.add_page(pdf_reader.pages[page])
        else:
            rest_writer.add_page(pdf_reader.pages[page])


    with open("./splittedPDFs/selected.pdf", "wb") as f2:
        pdf_writer.write(f2)

    with open("./splittedPDFs/rest.pdf", "wb") as f2:
        rest_writer.write(f2)