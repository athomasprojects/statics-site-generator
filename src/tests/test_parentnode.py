import unittest

from static_site_generator.htmlnode import ParentNode, LeafNode


class TestParentNode(unittest.TestCase):
    dummy_leaf = LeafNode("p", "This is a paragraph of text.")
    dummy_children = [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ]

    def test_notag(self):
        with self.assertRaises(ValueError, msg="ParentNode `tag` cannot be None"):
            ParentNode(None, children=[TestParentNode.dummy_leaf])

    def test_nochildren(self):
        with self.assertRaises(ValueError, msg="ParentNode `children` cannot be None"):
            ParentNode("!DOCTYPE", children=None)

    def test_to_html(self):
        self.assertEqual(
            ParentNode("p", TestParentNode.dummy_children).to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_nested(self):
        inner = (ParentNode("p", TestParentNode.dummy_children).to_html(),)

        self.assertEqual(
            ParentNode("title", [inner]),
            "<title><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></title>",
        )
