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

    def __init__(
        self,
        tag: Optional[str] = None,
        value: Optional[str] = None,
        children: Optional[list["HtmlNode"]] = None,
        props: Optional[str] = None,
    ):
        if tag is not None:
            if not isinstance(tag, str):
                tag = str(tag)
            if not HtmlTag.is_tag(tag):
                raise ValueError(f"Invalid `tag`: {tag}")

        if value is not None:
            if not isinstance(value, str):
                value = str(value)

        if props is not None:
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

        if self.children is None:
            child_str = f"{children_repr}"
        else:
            child_str = f"[{children_repr}]"

        if self.props is None:
            props_str = f"{props_repr}"
        else:
            props_str = f"{{{props_repr}}}"

        node_repr = (
            f"{indent}HtmlNode(\n"
            f"{indent}  tag : '{self.tag}',\n"
            f"{indent}  value : '{self.value}',\n"
            f"{indent}  children : {child_str},\n"
            f"{indent}  props : {props_str}\n"
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
        if self.props is not None:
            for k, v in self.props.items():
                if HtmlAttribute.is_attr(k) and k is not None:
                    s += f' {k}="{v}"'
                else:
                    s += f"{k}={HtmlAttribute._INVALID_ATTR.value}"
        return s


class LeafNode(HtmlNode):
    tag: Optional[str]
    value: Optional[str]
    props: Optional[dict[str, str]] = None

    def __init__(
        self,
        tag: Optional[str],
        value: Optional[str],
        props: Optional[dict[str, str]] = None,
    ):
        if value is None:
            raise ValueError("`value` of a `LeafNode` cannot be None.")

        super().__init__(tag, value, children=None, props=props)

    def to_html(self) -> str:
        if self.tag is None:
            return self.value
        else:
            opening, closing = HtmlTag.fmt_tag(self.tag)
            return f"{opening}{self.props_to_html()}{HtmlTag._Tag._CLOSING_ANGLE_BRKT.value}{self.value}{closing}"
