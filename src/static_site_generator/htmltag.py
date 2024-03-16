from enum import Enum
from typing import Optional

from static_site_generator import util


class HtmlTag:
    class _Tag(Enum):
        DOCTYPE = "!DOCTYPE"
        A = "a"
        ABBR = "abbr"
        ADDRESS = "address"
        AREA = "area"
        ARTICLE = "article"
        ASIDE = "aside"
        AUDIO = "audio"
        B = "b"
        BASE = "base"
        BDI = "bdi"
        BDO = "bdo"
        BLOCKQUOTE = "blockquote"
        BODY = "body"
        BR = "br"
        BUTTON = "button"
        CANVAS = "canvas"
        CAPTION = "caption"
        CITE = "cite"
        CODE = "code"
        COL = "col"
        COLGROUP = "colgroup"
        DATA = "data"
        DATALIST = "datalist"
        DD = "dd"
        DEL = "del"
        DETAILS = "details"
        DFN = "dfn"
        DIALOG = "dialog"
        DIR = "dir"
        DIV = "div"
        DL = "dl"
        DT = "dt"
        EM = "em"
        EMBED = "embed"
        FIELDSET = "fieldset"
        FIGCAPTION = "figcaption"
        FIGURE = "figure"
        FONT = "font"
        FOOTER = "footer"
        FORM = "form"
        FRAME = "frame"
        FRAMESET = "frameset"
        H6 = "h6"
        HEAD = "head"
        HEADER = "header"
        HR = "hr"
        HTML = "html"
        I = "i"
        IFRAME = "iframe"
        IMG = "img"
        INPUT = "input"
        INS = "ins"
        KBD = "kbd"
        LABEL = "label"
        LEGEND = "legend"
        LI = "li"
        LINK = "link"
        MAIN = "main"
        MAP = "map"
        MARK = "mark"
        MENU = "menu"
        META = "meta"
        METER = "meter"
        NAV = "nav"
        NOFRAMES = "noframes"
        NOSCRIPT = "noscript"
        OBJECT = "object"
        OL = "ol"
        OPTGROUP = "optgroup"
        OPTION = "option"
        OUTPUT = "output"
        P = "p"
        PARAM = "param"
        PICTURE = "picture"
        PRE = "pre"
        PROGRESS = "progress"
        Q = "q"
        RP = "rp"
        RT = "rt"
        RUBY = "ruby"
        S = "s"
        SAMP = "samp"
        SCRIPT = "script"
        SECTION = "section"
        SELECT = "select"
        SMALL = "small"
        SOURCE = "source"
        SPAN = "span"
        STRIKE = "strike"
        STRONG = "strong"
        STYLE = "style"
        SUB = "sub"
        SUMMARY = "summary"
        SUP = "sup"
        SVG = "svg"
        TABLE = "table"
        TBODY = "tbody"
        TD = "td"
        TEMPLATE = "template"
        TEXTAREA = "textarea"
        TFOOT = "tfoot"
        TH = "th"
        THEAD = "thead"
        TIME = "time"
        TITLE = "title"
        TR = "tr"
        TRACK = "track"
        U = "u"
        UL = "ul"
        VAR = "var"
        VIDEO = "video"
        WBR = "wbr"
        _EMPTY = ""
        _INVALID_TAG = "INVALID_TAG"

    _tag_set = util.enum_values(_Tag)

    @classmethod
    def is_tag(cls, s: str) -> bool:
        return s in HtmlTag._tag_set

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
