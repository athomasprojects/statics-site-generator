import dataclasses
from typing import Optional


@dataclasses.dataclass(slots=True)
class TextNode:
    text: str
    text_type: str
    url: Optional[str] = None

    def __init__(self, text, text_type, url=None):
        assert isinstance(text, str), "`text` must be a string."
        self.text = text

        assert isinstance(text_type, str), "`text_type` must be a string."
        self.text_type = text_type

        if url is not None:
            assert isinstance(url, str), "`url` must be a string or None."
        self.url = url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

    def __eq__(self, other):
        for field in dataclasses.fields(self):
            if getattr(self, field.name) != getattr(other, field.name):
                return False
        return True
