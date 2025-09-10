import re
import pymupdf


class PDFParser:
    def __init__(self):
        pass

    def parse_and_clean(self, file_path, normalize_whitespace=True):
        output = ""

        # load
        doc = pymupdf.open(file_path)

        # parse
        for page in doc:
            page_text = page.get_text(sort=True)

            # clean
            if normalize_whitespace:
                page_text = re.sub(r"\s+", " ", page_text)

            output += page_text
        return output
