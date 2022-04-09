import json
from pathlib import Path
from typing import Union

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

    def test_tag(self, test_data_filepath: Union[str, Path]):
        """
        Basic test to assert elements availability and position.
        """
        assert self.doc.page_count == 1
        page = [page for page in self.doc.pages()][0]
        with open(test_data_filepath, 'rb') as file:
            test_data = json.loads(file.read())
        for element in test_data:
            name = element['name']
            x0min, x0max = element['x0']
            x1min, x1max = element['x1']
            y0min, y0max = element['y0']
            y1min, y1max = element['y1']
            areas = page.search_for(name)
            assert areas
            area = areas[0]
            assert x0min < area.x0 < x0max, f'Assertion error in "{name}".x0: {x0min} < {area.x0} < {x0max}'
            assert x1min < area.x1 < x1max, f'Assertion error in "{name}".x1: {x1min} < {area.x1} < {x1max}'
            assert y0min < area.y0 < y0max, f'Assertion error in "{name}".y0: {y0min} < {area.y0} < {y0max}'
            assert y1min < area.y1 < y1max, f'Assertion error in "{name}".y1: {y1min} < {area.y1} < {y1max}'


if __name__ == "__main__":
    tag_parser = TagParser('sample.pdf')
    tag_data = tag_parser.get_tag_data()
    print(tag_data)
    tag_parser.test_tag('test_data.json')
