from PyPDF2 import PdfWriter, PdfReader

def collatePages(pdfs):
    readers = [PdfReader(pdf) for pdf in pdfs]
    writer = PdfWriter()
    [writer.add_page(reader.pages[0].rotate(90)) for reader in readers]
    with open("output.pdf", "wb") as fp:
        writer.write(fp)

collatePages(['FIRST.pdf', 'SECOND.pdf', 'THIRD.pdf', 'FOURTH.pdf'])