import unittest

from static_site_generator.htmlnode import LeafNode


class TestHtmlNode(unittest.TestCase):
    def test_value(self):
        tag = None
        value = "We have a value."
        node = LeafNode(tag, value)
        self.assertEqual(node.value, value)

    def test_novalue(self):
        with self.assertRaises(
            ValueError, msg="`value` of a `LeafNode` cannot be None."
        ):
            LeafNode(tag=None, value=None)

    def test_tohtml(self):
        self.assertEqual(
            LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test_tohtml_noprops(self):
        self.assertEqual(
            LeafNode("p", "This is a paragraph of text.").to_html(),
            "<p>This is a paragraph of text.</p>",
        )


if __name__ == "__main__":
    unittest.main()
