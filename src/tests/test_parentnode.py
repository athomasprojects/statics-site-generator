import unittest

from static_site_generator.htmlnode import ParentNode, LeafNode


class TestParentNode(unittest.TestCase):
    def test_no_tag(self):
        with self.assertRaises(ValueError, msg="ParentNode `tag` cannot be None"):
            ParentNode(None, [LeafNode("p", "This is a paragraph of text.")])

    def test_no_children(self):
        with self.assertRaises(ValueError, msg="ParentNode `children` cannot be None"):
            ParentNode("!DOCTYPE", children=None)

    def test_to_html_one_child(self):
        self.assertEqual(
            ParentNode("p", [LeafNode(None, "CHILD")]).to_html(),
            "<p>CHILD</p>",
        )

    def test_to_html_nested_parent(self):
        grandchild = LeafNode("body", "GRANDCHILD")
        child = ParentNode("p", [grandchild])
        parent = ParentNode("h2", [child])
        self.assertEqual(
            ParentNode("title", [parent]).to_html(),
            "<title><h2><p><body>GRANDCHILD</body></p></h2></title>",
        )

    def test_to_html_multiple_children(self):
        inner = ParentNode(
            "p",
            children=[
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(
            ParentNode("div", [inner]).to_html(),
            "<div><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></div>",
        )
