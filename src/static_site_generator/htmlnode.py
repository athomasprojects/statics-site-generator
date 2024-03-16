import dataclasses
from typing import Optional

from static_site_generator.htmltag import HtmlTag
from static_site_generator.htmlattribute import HtmlAttribute


@dataclasses.dataclass(slots=True)
class HtmlNode:
    tag: Optional[str]
    value: Optional[str]
    children: Optional[list["HtmlNode"]]
    props: Optional[dict[str, str]]

    def __init__(self, tag=None, value=None, children=None, props=None):
        if tag is None:
            tag = ""
        elif not isinstance(tag, str):
            tag = str(tag)
        if not HtmlTag.is_tag(tag):
            raise ValueError(f"Invalid `tag`: {tag}")

        if value is None:
            value = ""
        elif not isinstance(value, str):
            value = str(value)

        if children is None:
            children = []

        if props is None:
            props = {}
        else:
            assert isinstance(props, dict), "`HtmlNode` expects a `dict` for `props`."

        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self, level=0) -> str:
        indent = "  " * level
        children_repr = ""
        if self.children:  # Simplified the condition
            children_repr = ",\n".join(
                child.__repr__(level + 1) for child in self.children
            )
            children_repr = f",\n{children_repr}"
        props_repr = (
            ", ".join(f"'{key}': '{value}'" for key, value in self.props.items())
            if self.props
            else ""
        )
        node_repr = (
            f"{indent}HtmlNode(\n"
            f"{indent}  tag : '{self.tag}',\n"
            f"{indent}  value : '{self.value}',\n"
            f"{indent}  children : [{children_repr}],\n"
            f"{indent}  props : {{{props_repr}}}"
            f"\n{indent})"
        )
        return node_repr

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
