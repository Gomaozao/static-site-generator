import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", "bold", "https://www.boot.dev")
        node2 = TextNode("This is a text node", "bold", "https://www.boot.dev")
        self.assertEqual(node1, node2)

    def test_self_types(self):
        node1 = TextNode("This is a text node", "bold", "https://www.boot.dev")
        self.assertTrue(type(node1.text) == str and type(node1.text_type) == str and type(node1.url) == str)
    
    def test_two_types(self):
        node1 = TextNode("This is a text node", "bold")
        node2 = TextNode(3123, None)
        self.assertNotEqual(node1, node2)

    def test_url_none(self):
        node1 = TextNode("This is a text node", "bold", None)
        node2 = TextNode("This is a text node", "bold", "https://www.boot.dev")
        self.assertNotEqual(node1, node2)
    
    def test_dif_url(self):
        node1 = TextNode("This is a text node", "bold", "https://www.boot.dev")
        node2 = TextNode("This is a text node", "bold", "https://www.google.com")
        self.assertNotEqual(node1,node2)

    def test_text_type_property(self):
        node1 = TextNode("This is a text node", "italic", "https://www.boot.dev")
        node2 = TextNode("This is a text node", "bold", "https://www.boot.dev")
        self.assertNotEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()