from pdfminer.high_level import extract_text, extract_pages
from pdfminer.layout import LTTextBoxHorizontal

def main():
    page = 0 
    for page_layout in extract_pages("./infoPLD.pdf"):
        page += 1
        if page != 8: 
            continue
        for element in page_layout:
            print()
            print(repr(element))    
            print()

main()