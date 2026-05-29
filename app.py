import fitz

pdf = fitz.open("sample.pdf")

for page_num in range(len(pdf)):
    page = pdf[page_num]
    text = page.get_text()

    print(f"\n----- PAGE {page_num + 1} -----\n")
    print(text)

pdf.close()