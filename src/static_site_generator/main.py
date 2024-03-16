from static_site_generator.htmlnode import HtmlNode
from static_site_generator.textnode import TextNode


def main():
    text = "This is a text node"
    text_type = "bold"
    url = "https://www.boot.dev"
    props = {"href": "https://www.google.com", "target": "_blank"}
    tag = "title"
    dummy = HtmlNode("p", "dummy", props=props)
    children = [dummy] * 3

    t = TextNode(text, text_type, url)
    h = HtmlNode(tag, url, children, props=props)

    print(t)
    print(h)


if __name__ == "__main__":
    main()
