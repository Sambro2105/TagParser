# Тестовое задание для ERP.AERO

main.py contains class `TagParser`.

Method `get_tag_data` return a dict with data from the tag.

Method `test_tag` contains a basic logic for asserting availability and position for elements inside.

## Usage

```python
import TagParser

# initialize parser
tag_parser = TagParser('sample.pdf')

# get data from the tag
tag_data = tag_parser.get_tag_data()

# run basic tests, configurable through a json file
tag_parser.test_tag('test_data.json')
```

You can test the functionality by simply running the command:

`python main.py`