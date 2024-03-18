from static_site_generator.htmlnode import HtmlNode, LeafNode, ParentNode
from static_site_generator.textnode import TextNode


def main():
    text = "This is a text node"
    text_type = "text"
    url = "https://www.boot.dev"
    props = {"href": "https://www.google.com", "target": "_blank"}
    node = TextNode(text, text_type)
    node = node.to_html_node()
    print(node.to_html())


if __name__ == "__main__":
    main()
