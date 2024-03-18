from static_site_generator.htmlnode import HtmlNode, LeafNode, ParentNode
from static_site_generator.textnode import TextNode


def main():
    text = "This is a text node"
    text_type = "bold"
    url = "https://www.boot.dev"
    props = {"href": "https://www.google.com", "target": "_blank"}
    dummy = HtmlNode("p", "dummy", props=props)
    children = [dummy] * 3
    tag = "a"
    # t = TextNode(text, text_type, url)
    # h = HtmlNode()
    # leaf = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    dummy_leaf = LeafNode("title", "leaf")
    parent = ParentNode(
        "p",
        children=[
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )
    nested = ParentNode(
        "p",
        [dummy_leaf] + ([parent] * 3),
    )

    double_nested = ParentNode("a", [nested])
    # print(t)
    # print(leaf.to_html())
    # print(parent.to_html())
    # print(nested.to_html())
    print(double_nested.to_html())


if __name__ == "__main__":
    main()
