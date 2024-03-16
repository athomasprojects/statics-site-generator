from enum import Enum

from static_site_generator import util
from typing import Optional


class HtmlAttribute(object):
    class _Attrbute(Enum):
        ACCEPT = "accept"
        ACCEPT_CHARSET = "accept-charset"
        ACCESSKEY = "accesskey"
        ACTION = "action"
        ALIGN = "align"
        ALLOW = "allow"
        ALT = "alt"
        AS = "as"
        ASYNC = "async"
        AUTOCAPITALIZE = "autocapitalize"
        AUTOCOMPLETE = "autocomplete"
        AUTOPLAY = "autoplay"
        BACKGROUND = "background"
        BGCOLOR = "bgcolor"
        BORDER = "border"
        CAPTURE = "capture"
        CHARSET = "charset"
        CHECKED = "checked"
        CITE = "cite"
        CLASS = "class"
        COLOR = "color"
        COLS = "cols"
        COLSPAN = "colspan"
        CONTENT = "content"
        CONTENTEDITABLE = "contenteditable"
        CONTROLS = "controls"
        COORDS = "coords"
        CROSSORIGIN = "crossorigin"
        CSP = "csp"
        DATA = "data"
        DATA_STAR = "data-*"
        DATETIME = "datetime"
        DECODING = "decoding"
        DEFAULT = "default"
        DEFER = "defer"
        DIR = "dir"
        DIRNAME = "dirname"
        DISABLED = "disabled"
        DOWNLOAD = "download"
        DRAGGABLE = "draggable"
        ENCTYPE = "enctype"
        ENTERKEYHINT = "enterkeyhint"
        FOR = "for"
        FORM = "form"
        FORMACTION = "formaction"
        FORMENCTYPE = "formenctype"
        FORMMETHOD = "formmethod"
        FORMNOVALIDATE = "formnovalidate"
        FORMTARGET = "formtarget"
        HEADERS = "headers"
        HEIGHT = "height"
        HIDDEN = "hidden"
        HIGH = "high"
        HREF = "href"
        HREFLANG = "hreflang"
        HTTP_EQUIV = "http-equiv"
        ID = "id"
        INTEGRITY = "integrity"
        INTRINSICSIZE = "intrinsicsize"
        INPUTMODE = "inputmode"
        ISMAP = "ismap"
        ITEMPROP = "itemprop"
        KIND = "kind"
        LABEL = "label"
        LANG = "lang"
        LANGUAGE = "language"
        LOADING = "loading"
        LIST = "list"
        LOOP = "loop"
        LOW = "low"
        MANIFEST = "manifest"
        MAX = "max"
        MAXLENGTH = "maxlength"
        MINLENGTH = "minlength"
        MEDIA = "media"
        METHOD = "method"
        MIN = "min"
        MULTIPLE = "multiple"
        MUTED = "muted"
        NAME = "name"
        NOVALIDATE = "novalidate"
        OPEN = "open"
        OPTIMUM = "optimum"
        PATTERN = "pattern"
        PING = "ping"
        PLACEHOLDER = "placeholder"
        PLAYSINLINE = "playsinline"
        POSTER = "poster"
        PRELOAD = "preload"
        READONLY = "readonly"
        REFERRERPOLICY = "referrerpolicy"
        REL = "rel"
        REQUIRED = "required"
        REVERSED = "reversed"
        ROLE = "role"
        ROWS = "rows"
        ROWSPAN = "rowspan"
        SANDBOX = "sandbox"
        SCOPE = "scope"
        SCOPED = "scoped"
        SELECTED = "selected"
        SHAPE = "shape"
        SIZE = "size"
        SIZES = "sizes"
        SLOT = "slot"
        SPAN = "span"
        SPELLCHECK = "spellcheck"
        SRC = "src"
        SRCDOC = "srcdoc"
        SRCLANG = "srclang"
        SRCSET = "srcset"
        START = "start"
        STEP = "step"
        STYLE = "style"
        SUMMARY = "summary"
        TABINDEX = "tabindex"
        TARGET = "target"
        TITLE = "title"
        TRANSLATE = "translate"
        TYPE = "type"
        USEMAP = "usemap"
        VALUE = "value"
        WIDTH = "width"
        WRAP = "wrap"
        _INVALID_ATTR = "INVALID_ATTRIBUTE"

    _attr_set = util.enum_values(_Attrbute)

    @classmethod
    def is_attr(cls, s: str) -> bool:
        return s in cls._attr_set

    @classmethod
    def fmt_attr(cls, key: str, value: str) -> Optional[str]:
        """
        Html attribute string for `attr`.

        Parameters
        ----------
        key : html attribute
        value : attribute value

        Returns
        ----------
        attr : html attribute string if `key` is not a valid html attribute, otherwise `None`
        """
        if cls.is_attr(key):
            attr = f"{key}={value} "
        else:
            attr = None
        return attr
