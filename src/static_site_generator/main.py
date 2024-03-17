from static_site_generator.htmlnode import HtmlNode, LeafNode
from static_site_generator.textnode import TextNode


def main():
    text = "This is a text node"
    text_type = "bold"
    url = "https://www.boot.dev"
    props = {"href": "https://www.google.com", "target": "_blank"}
    dummy = HtmlNode("p", "dummy", props=props)
    children = [dummy] * 3
    tag = "a"
    t = TextNode(text, text_type, url)
    h = HtmlNode()
    h2 = HtmlNode(tag=tag, value=url, children=children, props=props)
    leaf = LeafNode("p", "This is a paragraph of text.")
    leaf2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    leaf3 = LeafNode("div", "Click me!")

    print(t)
    print(h)
    print(h2)
    print(leaf.to_html())
    print(leaf2.to_html())
    print(leaf3.to_html())


if __name__ == "__main__":
    main()
