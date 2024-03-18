import dataclasses
from typing import Optional
from enum import Enum
from static_site_generator import util
from static_site_generator.htmlnode import LeafNode


class TextType:
    class _Type(Enum):
        TEXT = "text"
        BOLD = "bold"
        ITALIC = "italic"
        CODE = "code"
        LINK = "link"
        IMAGE = "image"

    _text_type_set = util.enum_values(_Type)

    @classmethod
    def is_valid_text_type(cls, text_type: str) -> bool:
        return text_type in cls._text_type_set

    def __str__(self):
        return self.value


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


def to_html_node(text_node) -> LeafNode:
    if TextType.is_valid_text_type(text_node.text_type):
        match text_node.text_type:
            case TextType._Type.TEXT.value:
                leaf = LeafNode(None, text_node.text)
            case TextType._Type.BOLD.value:
                leaf = LeafNode("b", text_node.text)
            case TextType._Type.ITALIC.value:
                leaf = LeafNode("i", text_node.text)
            case TextType._Type.CODE.value:
                leaf = LeafNode("code", text_node.text)
            case TextType._Type.LINK.value:
                leaf = LeafNode("a", text_node.text, props={"href": text_node.url})
            case TextType._Type.IMAGE.value:
                leaf = LeafNode(
                    "img", "", props={"src": text_node.url, "alt": text_node.text}
                )
        return leaf
    else:
        raise ValueError(f"Invalid `text_type`: {text_node.text_type}")
