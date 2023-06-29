from PyPDF2 import PdfWriter, PdfReader
import os, shutil


def collatePages(pdfs):
    readers = [PdfReader(pdf) for pdf in pdfs]
    writer = PdfWriter()
    [writer.add_page(reader.pages[0].rotate(90)) for reader in readers]
    with open("totalOutput.pdf", "wb") as fp:
        writer.write(fp)


rootDir = "./signageGeneration/signageStorage"
pages = []
for root, dirs, files in os.walk(rootDir, topdown=False):
    for name in files:
        pages.append(name[:-4])
        # print(pages)
pages.sort(key=int)
pages = [os.path.join(rootDir, f"{page}.pdf") for page in pages]
# print(pages)
collatePages(pages)
