import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        html1 = HTMLNode("p", "bla bla bla bla", [], {"href": "www.google.com"})
        html2 = HTMLNode("p", "bla bla bla bla", [], {"href": "www.google.com"})
        self.assertEqual(html1, html2)
    
    def test_self_types(self):
        html1 = HTMLNode("p", "bla bla bla bla", [], {"href": "www.google.com"})
        self.assertTrue( type(html1.tag) == str and
            type(html1.value) == str and
            type(html1.children) == list and
            type(html1.props) == dict)
    
    def test_attribute_empty(self):
        html1 = HTMLNode("p", "bla bla bla bla", [], {"href": "www.google.com"})
        html2 = HTMLNode("p", "bla bla bla bla", [html1], {"href": "www.google.com"})
        self.assertNotEqual(html1,html2)