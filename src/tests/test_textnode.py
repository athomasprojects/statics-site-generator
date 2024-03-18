import unittest

from static_site_generator.textnode import TextNode, LeafNode, to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is another node", "text")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", "bold")
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, None)")

    def test_text_to_html_node(self):
        text = "This is a text node"
        text_type = "text"
        t = to_html_node(TextNode(text, text_type))
        self.assertEqual(t.to_html(), LeafNode(None, text).to_html())

    def test_bold_to_html_node(self):
        text = "This is bold text"
        text_type = "bold"
        t = to_html_node(TextNode(text, text_type))
        self.assertEqual(t.to_html(), LeafNode("b", text).to_html())

    def test_code_to_html_node(self):
        text = """
        foo = 69;
        bar = 420;
        baz = 696969;
        """
        text_type = "code"
        t = to_html_node(TextNode(text, text_type))
        self.assertEqual(t.to_html(), LeafNode(text_type, text).to_html())

    def test_link_to_html_node(self):
        text = "anchor text"
        text_type = "link"
        url = "https://www.google.com"
        t = to_html_node(TextNode(text, text_type, url))
        self.assertEqual(
            t.to_html(), LeafNode("a", text, props={"href": url}).to_html()
        )

    def test_img_to_html_node(self):
        text = "alt text"
        text_type = "image"
        url = "https://www.google.com"
        t = to_html_node(TextNode(text, text_type, url))
        self.assertEqual(
            t.to_html(),
            LeafNode("img", "", props={"src": url, "alt": text}).to_html(),
        )


if __name__ == "__main__":
    unittest.main()
