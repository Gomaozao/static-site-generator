class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag # string
        self.value = value # string
        self.children = children # list of HTMLNodes
        self.props = props # dict containing html attributes as keys and their values as values

    def __eq__(self, other):
        return (self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props)

    def to_html(self):
        raise NotImplementedError("to_html not implemented")

    def props_to_html(self):
        whole_string = ""
        for key in self.props:
            whole_string += key + "=" + "\"" + self.props[key] + "\"" + " "
        return " " + whole_string

    def __repr__(self):
        return f"HTMLNode('{self.tag}', '{self.value}', {self.value}, {self.props})"
    
html1 = HTMLNode("p", "bla bla bla bla", [], {"href": "www.google.com", "img": "awdeawed.jpg", "batman": "aweawo.corinthians"})
print(html1.props_to_html())
