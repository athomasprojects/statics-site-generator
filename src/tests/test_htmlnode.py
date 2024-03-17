import unittest

from static_site_generator.htmlnode import HtmlNode


class TestHtmlNode(unittest.TestCase):
    def test_tag(self):
        tag = "title"
        node = HtmlNode(tag)
        self.assertEqual(node.tag, tag)

    def test_tag_invalid(self):
        tag = "yo_wtf_is_this"
        with self.assertRaises(ValueError, msg=f"Invalid `tag`: {tag}"):
            HtmlNode(tag)

    def test_value(self):
        value = "Ocaml my caml"
        node = HtmlNode(value=value)
        self.assertEqual(node.value, value)

    def test_value_invalid(self):
        value = 69420
        node = HtmlNode(value=value)
        self.assertEqual(node.value, str(value))

    def test_children_empty(self):
        node = HtmlNode()
        self.assertEqual(node.children, None)

    def test_children(self):
        value = "Ocaml my caml"
        dummies = [HtmlNode(value=value)] * 3
        node = HtmlNode(value=value, children=dummies)
        self.assertEqual(node.children, dummies)

    def test_props(self):
        props = {"href": "https://www.google.com"}
        node = HtmlNode(props=props)
        self.assertEqual(node.props, props)

    def test_htmlnode_empty(self):
        node = HtmlNode()
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_htmlnode_init(self):
        tag = "!DOCTYPE"
        value = """Just a some stuff....
                YO OCAML RULES
            >>>>>>
        """
        children = [HtmlNode()] * 3
        props = {"href": "https://www.ocaml.org", "target": "_blank", "id": "my_id"}
        node = HtmlNode(tag, value, children, props)
        self.assertEqual(node.tag, tag)
        self.assertEqual(node.value, value)
        self.assertEqual(node.children, children)
        self.assertEqual(node.props, props)


if __name__ == "__main__":
    unittest.main()
