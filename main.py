import fitz


class TagParser:

    def __init__(self, filepath: str):
        self.doc = fitz.open(filepath)

    def get_tag_data(self) -> dict[str, str]:
        """
        Return parsed data from the tag.
        """
        page = [page for page in self.doc.pages()][0]
        texts = list(filter(bool, [item[4].rstrip() for item in page.get_text_blocks()]))[1:]
        values = []
        for text in texts:
            for value in text.split('\n'):
                values.append(value)

        return {k.strip(): v.strip() for k, v in [value.split(':') for value in values]}


if __name__ == "__main__":
    tag_parser = TagParser('sample.pdf')
    tag_data = tag_parser.get_tag_data()
    print(tag_data)
