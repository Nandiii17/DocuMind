import fitz


def extract_text(pdf_path):

    pdf = fitz.open(pdf_path)

    pages = []

    for page_num, page in enumerate(pdf):

        text = page.get_text()

        # Stop before References section
        if (
            "References" in text
            and len(text) > 1000
        ):
            break

        pages.append(
            {
                "page": page_num + 1,
                "text": text
            }
        )

    pdf.close()

    return pages