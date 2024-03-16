import dataclasses
from typing import Optional

import static_site_generator.htmltag as HtmlTag
from static_site_generator.htmlattribute import HtmlAttribute
from static_site_generator import util


@dataclasses.dataclass(slots=True)
class HtmlNode:
    tag: Optional[str] = None
    value: Optional[str] = None
    children: Optional[list["HtmlNode"]] = None
    props: Optional[dict[str, str]] = None

    def __init__(self, tag, value, children, props):
        match tag:
            case None:
                self.tag = tag
            case str() if HtmlTag.is_tag(tag):
                self.tag = tag
            case _:
                raise ValueError(f"Invalid `tag`: {tag}")

        match value, children:
            case (None, None):
                raise ValueError(
                    "`value` and `children` of `HtmlNode` cannot be both be `None`."
                )
            case (str(), []):
                raise ValueError(
                    "`HtmlNode` is expected to have children; `children` cannot be an empty list."
                )
            case (None, str()):
                raise ValueError(
                    "`HtmlNode` is expected to have a value; `value` cannot be `None`."
                )
            case (str() as v, list() as c):
                self.value = v
                self.children = c

            case (_, _):
                raise ValueError(
                    "`HtmlNode` expects a `str` for `value` and a `list` for `children`."
                )

        assert isinstance(props, dict), "`HtmlNode` expects a `dict` for `props`."
        self.props = props

    def __repr__(self):
        return f"HtmlNode(\ntag : {self.tag},\nvalue : {self.value},\nchildren : {self.children},\nprops : {util.string_of_dict(self.props)})"

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self) -> str:
        """
        Returns a string of the html attributes of the node.
        """
        s = ""
        for k, v in self.props.items():
            if HtmlAttribute.is_attr(k) and k is not None:
                s += f"{k}={v} "
            else:
                s += f"{k}={HtmlAttribute._INVALID_ATTR.value}"
        return s
