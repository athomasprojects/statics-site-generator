import dataclasses
from typing import Optional


@dataclasses.dataclass(slots=True)
class TextNode:
    text: str
    text_init: str
    url: Optional[str] = None

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_init = text_type
        self.url = url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_init}, {self.url})"

    def __eq__(self, other):
        for field in dataclasses.fields(self):
            if getattr(self, field.name) != getattr(other, field.name):
                return False
        return True
