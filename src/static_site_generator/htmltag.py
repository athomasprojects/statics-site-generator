from enum import Enum
from typing import Optional

from static_site_generator import util


class HtmlTag:
    class _Tag(Enum):
        ABBR = "abbr"
        ACRONYM = "acronym"
        ADDRESS = "address"
        ARTICLE = "article"
        ASIDE = "aside"
        BDO = "bdo"
        BIG = "big"
        BLOCKQUOTE = "blockquote"
        BOLD = "b"
        BUTTON = "button"
        CANVAS = "canvas"
        CITE = "cite"
        CODE = "code"
        DD = "dd"
        DFN = "dfn"
        DIV = "div"
        DL = "dl"
        DT = "dt"
        EMPHASIZE = "em"
        FIELDSET = "fieldset"
        FIGCAPTION = "figcaption"
        FIGURE = "figure"
        FOOTER = "footer"
        FORM = "form"
        H1 = "h1"
        H6 = "h6"
        HEADER = "header"
        HR = "hr"
        IMG = "img"
        INPUT = "input"
        ITAG = "i"
        KBD = "kbd"
        LABEL = "label"
        LI = "li"
        LINEBREAK = "br"
        LINK = "a"
        MAIN = "main"
        MAP = "map"
        NAV = "nav"
        NOSCRIPT = "noscript"
        OBJECT = "object"
        OL = "ol"
        OUTPUT = "output"
        PARA = "p"
        PRE = "pre"
        QUOTE = "q"
        SAMP = "samp"
        SCRIPT = "script"
        SECTION = "section"
        SELECT = "select"
        SMALL = "small"
        SPAN = "span"
        STRONG = "strong"
        SUBSCRIPT = "sub"
        SUPERSCRIPT = "sup"
        TABLE = "table"
        TELETYPE = "tt"
        TEXTAREA = "textarea"
        TFOOT = "tfoot"
        TIME = "time"
        UL = "ul"
        VAR = "var"
        VIDEO = "video"
        _INVALID_TAG = "INVALID_TAG"

    _tag_set = util.enum_values(_Tag)

    @classmethod
    def is_tag(cls, s: str) -> bool:
        s in HtmlTag._tag_set

    @classmethod
    def fmt_tag(cls, tag: str) -> Optional[tuple[str, str]]:
        """
        Opening and closing html tags for `tag`.

        Parameters
        ----------
        tag : string representing an html tag.

        Returns
        ----------
        (opening, closing) : opening and closing html tags for a given tag.
        """
        if cls.is_tag(tag):
            return f"<{tag}>", f"</{tag}>"
        else:
            return None
